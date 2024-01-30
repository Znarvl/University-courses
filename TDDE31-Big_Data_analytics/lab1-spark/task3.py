from pyspark import SparkContext

def max_temperature(a,b):
    if a >=b:
        return a
    else:
        return b

def min_temperature(a,b):
    if a <=b:
        return a
    else:
        return b

sc = SparkContext(appName = "task3")
temperature_file = sc.textFile("BDA/input/temperature-readings.csv")

#102170; 2013-11-01 ;06:00:00 ;6.8; G
# 0, station, 1 date, 2 time, 3 air temp, 4 quality

lines = temperature_file.map(lambda line: line.split(";"))

#key: , Station, year, month,    value: temperature
year_temperature = lines.map(lambda x: ((x[0], x[1]) , (float(x[3]))))
#day_temperature = year_temperature.reduceByKey(lambda x, y: (max(x[0], y[0]), min(x[0], y[0])))
day_temperature_max = year_temperature.reduceByKey(max)
day_temperature_min = year_temperature.reduceByKey(min)
day_teperature_combined= day_temperature_min.join(day_temperature_max)
day_temperature = day_teperature_combined.map(lambda x: ((x[0][0], x[0][1][0:4], x[0][1][5:7]), (x[1][0] + x[1][1], 1)))
month_temperature = day_temperature.reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))

month_temperature = month_temperature.filter(lambda x: int(x[0][1]) >= 1960 and int(x[0][1]) <= 2014)

result = month_temperature.map(lambda x: ((x[0]), float(x[1][0]/(x[1][1]*2))))

result.saveAsTextFile("BDA/output")

# takeOrdered(n, [ordering])	Return the first n elements of the RDD using either their natural order or a custom comparator.

# for all days
#   sort
#   get min temp for day, get max temp for day
# for all accumulated days
#   for all max and all min / divide by days in that month = month avg
