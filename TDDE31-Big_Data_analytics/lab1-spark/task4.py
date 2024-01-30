from pyspark import SparkContext

def max(a,b):
    if a >=b:
        return a
    else:
        return b

def sum(a, b):
    return a + b

sc = SparkContext(appName = "task4")


#102170; 2013-11-01 ;06:00:00 ;6.8; G
# 0, station, 1 date, 2 time, 3 air temp, 4 quality
temperature_file = sc.textFile("BDA/input/temperature-readings.csv")

#102170; 2013-11-01 ;06:00:00 ;0.5; G
# 0, station, 1 date, 2 time, 3 precipitation, 4 quality

# (stations, year, month)
# x[0][1] year x[0][2] month
precipitation_file = sc.textFile("BDA/input/precipitation-readings.csv")

temperatures = temperature_file.map(lambda line: line.split(";"))
temperatures = temperatures.map(lambda x: ((x[0]), float(x[3])))
max_temp = temperatures.reduceByKey(max)
max_temp = max_temp.filter(lambda x: float(x[1]) >= 25 and float(x[1]) <= 30)



precipitation = precipitation_file.map(lambda line: line.split(";"))
precipitation = precipitation.map(lambda x: ((x[0], x[1]), float(x[3])))
precipitation = precipitation.reduceByKey(sum)
precipitation = precipitation.filter(lambda x: int(x[1]) >= 100 and int(x[1]) <= 200)
precipitation = precipitation.map(lambda x: (x[0][0], float(x[1])))


result = max_temp.join(precipitation)
result.saveAsTextFile("BDA/output")



# Output:
# Station, maxtemp, maxprecip
