from pyspark import SparkContext
from pyspark.sql import SQLContext, Row
from pyspark.sql import functions as F

sc = SparkContext(appName = "task5")

def sum(a, b):
    return a + b
stations_file = sc.textFile("BDA/input/stations-Ostergotland.csv")
precipitation_file = sc.textFile("BDA/input/precipitation-readings.csv")


stations = stations_file.map(lambda line: line.split(";"))
stations = stations.map(lambda x: x[0]).collect()

precipitation = precipitation_file.map(lambda line: line.split(";"))

# key: station, year, month value: precipitation
precipitation = precipitation.map(lambda x: ((x[0], x[1][0:4], x[1][5:7]) , (float(x[3]))))


#Get precipitation from only ostgota stations
ostergotland_stations = precipitation.filter(lambda x: x[0][0] in stations)

#find between 1993 and 2016
ostergotland_stations = ostergotland_stations.filter(lambda x: int(x[0][1]) >= 1993 and int(x[0][1]) <=2016)



#sum each station year month
ostergotland_stations = ostergotland_stations.reduceByKey(lambda x,y: x + y)

#key: year, month value: monthly precipiations and 1 to count length
ostergotland_stations = ostergotland_stations.map(lambda x: ((x[0][1], x[0][2]), (x[1], 1)))

#sum each month of year and many stations there are
#((u'1998', u'12'), (356.3000000000001, 6))
ostergotland_stations = ostergotland_stations.reduceByKey(lambda x,y: (x[0] + y[0], x[1] + y[1]))

#key: Year month, value: total precipitation divided by amount of months
result = ostergotland_stations.map(lambda x: ((x[0]), float(x[1][0]/x[1][1])))
result.saveAsTextFile("BDA/output")
