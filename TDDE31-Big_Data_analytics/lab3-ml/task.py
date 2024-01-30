from __future__ import division
from math import radians, cos, sin, asin, sqrt, exp
from datetime import datetime
from pyspark import SparkContext
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.tree import RandomForest, GradientBoostedTrees

sc = SparkContext(appName="lab_kernel")

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km

# Smoothing coefficient, can be changed later
h_distance = 100 # Up to you
h_date = 15 # Up to you
h_time = 2 # Up to you

a = 58.4274 # Up to you
b = 14.826 # Up to you
date = "2013-08-12" # Up to you

# Import data files
stations = sc.textFile("BDA/input/stations.csv")
temps = sc.textFile("BDA/input/temperature-readings.csv")

# Make new maps from data files, splitting on ";"
stations_lines = stations.map(lambda line: line.split(";"))
temps_lines = temps.map(lambda line: line.split(";"))

# should broadcast stations because temp is 2GB
#key station: value: long and lat
stations_lon_lat = stations_lines.map(lambda x: (x[0], (float(x[3]), float(x[4]))))
# need to flatten to array, collectAsMap return keyvalue pairs
broadcast_stations = sc.broadcast(stations_lon_lat.collectAsMap())

#smaller sample
#key station, date, time value: , temp long and lat
temp = temps_lines.sample(False,0.1).map(lambda x: ((x[0], x[1], x[2]),  (float(x[3]), broadcast_stations.value.get(x[0]))))

# Filters out dates that are posterior to our predicted date
temp = temp.filter(lambda x: datetime(int(x[0][1][0:4]), int(x[0][1][5:7]), int(x[0][1][8:10])) < datetime(int(date[0:4]), int(date[5:7]), int(date[8:10])))

#cache temp so it will go faster to run
temp.cache()


# Gaussian function
def gaussian(distance):
    #e^(-distance^2)
    return exp(-distance**2)

# Gaussian kernels

# Kernel 1: Distance from coordinates
def distance_kernel(lon1, lat1, lon2, lat2):
    #return gaussian value based on the distance from coordinates
    return gaussian(haversine(lon1, lat1, lon2, lat2)/h_distance)

# Kernel 2: Distance measured for dates
def day_temp_kernel(date1, date2):
    # Format dates to calculate number of days between them
    date1 = datetime(int(date1[0:4]), int(date1[5:7]), int(date1[8:10]))
    date2 = datetime(int(date2[0:4]), int(date2[5:7]), int(date2[8:10]))

    # Calculate the number of days
    dist = abs(date1 - date2).days % 365

    # 364 days is equal to a one-day difference, this solves that
    if (dist > 365/2):
        dist = 365 - dist
    return gaussian(dist / h_date)

# Kernel 3: Distance measured per hour
def hour_kernel(time1, time2):
    # Format dates to be able to calculate hour difference
    time1 = datetime(2020, 1, 1, int(time1[0:2]), int(time1[3:5]), int(time1[6:8]))
    time2 = datetime(2020, 1, 1, int(time2[0:2]), int(time2[3:5]), int(time2[6:8]))
    
    # Calculate hours between two dates
    dist = abs(time1 - time2)
    hour = (dist.seconds / 3600) # Convert timedelta in seconds to hours

    # 23 hours is equal to a one-hour difference, this solves that
    if (hour > 12):
        hour = 24 - hour
    return gaussian(hour / h_time)



#convert date in smoothing coefficient to datetime
prediction_date = datetime(int(date[0:4]), int(date[5:7]), int(date[8:10]))

#Dict to all different predictions where key: time value: temp
predictions_gbt = {}
predictions_rf = {}
predictions_sum = {}
predictions_prod = {}

# Your code here
for time in ["00:00:00", "22:00:00", "20:00:00", "18:00:00", "16:00:00", "14:00:00", "12:00:00", "10:00:00", "08:00:00", "06:00:00", "04:00:00"]:
    # Extract hour we are on now to compare dates to filter out hours in the future, first two digits
    past_time = int(time[0:2])

    # Filtered temperatures on time, such as when the clock is 14, we get all available information before 14
    temp_filtered = temp.filter(lambda x: (int(x[0][2][0:2]) <= past_time))

    # Calculate weights using kernel functions to make predictions
    total = temp_filtered.map(lambda x: (distance_kernel(a , b, x[1][1][0], x[1][1][1]),
                                          day_temp_kernel(date, x[0][1]),
                                           hour_kernel(time, x[0][2]), x[1][0]))
    
    # calculate sum and product of kernels, multiply them with the temperature, and keep track of the kernel sums separately
    kernel_sum_and_prod = total.map(lambda x: ((x[0]+x[1]+x[2]), (x[0]*x[1]*x[2]), (x[0]+x[1]+x[2])*x[3], (x[0]*x[1]*x[2])*x[3]))

    
    # calculate the total sum and product of kernels and their weighted sums and products
    reduced = kernel_sum_and_prod.reduce(lambda x1, x2: (x1[0]+x2[0], x1[1]+x2[1], x1[2]+x2[2], x1[3]+x2[3]))

    # calculate the weighted sum and product, where the weight is the kernel sum or product
    predictions_sum[time] = reduced[2] / reduced[0]
    predictions_prod[time] = reduced[3] / reduced[1]

    #ML part
    #from regressor put in same data format to predict temperature
    #Make data work with ML libraries
    #Key temp value: date (year, month, day), time (first two digits), long lat
    ml_temp = temp_filtered.map(lambda x: (x[1][0], (int(x[0][1][0:4]), int(x[0][1][5:7]), int(x[0][1][8:10]), int(x[0][2][0:2]), int(x[1][1][0]), int(x[1][1][1]))))
    #create the training data by converting temp (key) and date, time, long and lat (value) to Labeled Point
    ml_train_data = ml_temp.map(lambda x: LabeledPoint(x[0], x[1]))

    # Train a random forest model
    rf = RandomForest.trainRegressor(ml_train_data, {}, numTrees = 3, maxDepth=8)
    
    # Train a ML model using gradient boosted trees
    gbt = GradientBoostedTrees.trainRegressor(ml_train_data, {}, numIterations=10, learningRate=0.2, maxDepth=8)
    
    # Reformat data to match the train data by date, time, long and lat to predict temp 
    data = [prediction_date.year, prediction_date.month, prediction_date.day, int(time[0:2]), a, b]

    # Make predictions and add the result to our dicts with key value the actual time
    predictions_rf[time] = rf.predict(data)
    predictions_gbt[time] = gbt.predict(data)

#print all values from kernels and MLlibs
print("Sum of kernel: \n")
print(predictions_sum)

print("Product of kernel functions: \n")
print(predictions_prod)

print("Random forrest predictions: \n")
print(predictions_rf)

print("Gradient Boosted Trees predictions: \n")
print(predictions_gbt)