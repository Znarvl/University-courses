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

sc = SparkContext(appName = "task1")
temperature_file = sc.textFile("BDA/input/temperature-readings.csv")
lines = temperature_file.map(lambda line: line.split(";"))
year_temperature = lines.map(lambda x: (x[1][0:4], float(x[3])))
year_temperature = year_temperature.filter(lambda x: int(x[0]) >= 1950 and int(x[0]) <= 2014)

max_temperatures = year_temperature.reduceByKey(max_temperature)
max_temperatures_sorted = max_temperatures.sortBy(ascending = False, keyfunc = lambda k: k[1])

min_temperatures = year_temperature.reduceByKey(min_temperature)
min_temperatures_sorted = min_temperatures.sortBy(ascending = False, keyfunc = lambda k: k[1])

temps = max_temperatures_sorted.join(min_temperatures_sorted)
temps = temps.sortBy(ascending = False, keyfunc = lambda k: k[1][0])

temps.saveAsTextFile("BDA/output")