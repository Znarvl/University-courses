from pyspark import SparkContext


sc = SparkContext(appName = "task2")
temperature_file = sc.textFile("BDA/input/temperature-readings.csv")

#102170; 2013-11-01 ;06:00:00 ;6.8; G
# 0, station, 1 date, 2 time, 3 air temp, 4 quality

lines = temperature_file.map(lambda line: line.split(";"))
#key: Station, year, month, value: temperature
year_temperature = lines.map(lambda x: ((x[0], x[1][0:4], x[1][5:7]) , float(x[3])))


#filter out year and above 10 degrees
year_temperature = year_temperature.filter(lambda x: int(x[0][1]) >= 1950 and int(x[0][1]) <= 2014 and float(x[1]) >= 10)



#first part commented
#month = year_temperature.map(lambda x: ((x[0][1], x[0][2]), 1))
#count_month = month.reduceByKey(lambda x,y: x + y )

#get stations
#Already got above 10 degrees so now look at distinct stations

#Key: Year, months, #value: stations (distinct)
stations = year_temperature.map(lambda x : ((x[0][1], x[0][2]), x[0][0])).distinct()

#key: year month, value: 1
stations = stations.map(lambda x: ((x[0]), 1))
stations = stations.reduceByKey(lambda x,y: x + y )


stations.saveAsTextFile("BDA/output")



# (y1, mx, T1)
# (y1, mx, T2)
# y1, my, T3
# y1, my, T4
# ...
# => y1, mx, 2