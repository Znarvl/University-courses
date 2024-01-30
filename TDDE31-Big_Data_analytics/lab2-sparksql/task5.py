from pyspark import SparkContext
from pyspark.sql import SQLContext, Row
from pyspark.sql import functions as F

sc = SparkContext(appName = "task5")
sqlContext = SQLContext(sc) 


#102170; 2013-11-01 ;06:00:00 ;6.8; G
# 0, station, 1 date, 2 time, 3 air temp, 4 quality
stations_file = sc.textFile("BDA/input/stations-Ostergotland.csv")
parts = stations_file.map(lambda l: l.split(";"))
stationReadings = parts.map(lambda p: Row(station=p[0], month=p[1].split("-")[1], year=int(p[1].split("-")[0]), time=p[2], temp=float(p[3]), quality=p[4] ))
schemaStationReadings = sqlContext.createDataFrame(stationReadings)
schemaStationReadings.registerTempTable("stationReadings")


#102170; 2013-11-01 ;06:00:00 ;0.5; G
# 0, station, 1 date, 2 time, 3 precipitation, 4 quality

# (stations, year, month)
# x[0][1] year x[0][2] month
precipitation_file = sc.textFile("BDA/input/precipitation-readings.csv")
parts_precip = precipitation_file.map(lambda l: l.split(";"))
precipReadings = parts_precip.map(lambda p: Row(station=p[0], month=p[1].split("-")[1], year=p[1].split("-")[0], time=p[2], precipitation=float(p[3]), quality=p[4]))
schemaPrecipReadings = sqlContext.createDataFrame(precipReadings)
schemaPrecipReadings.registerTempTable("precipReadings")

#combine both schemas togehter
schemaMergedPrecipStation = schemaPrecipReadings.join(schemaStationReadings, ['station'], 'inner')

#filter year
schemaMergedPrecipStation = schemaMergedPrecipStation.filter((schemaMergedPrecipStation['year'] >= 1993) & (schemaMergedPrecipStation['year'] <= 2016))

#sum precipitation based on the station and year and month.
schemaMergedPrecipStation = schemaMergedPrecipStation.groupBy('station', 'year','month').agg(F.sum('precipitation').alias('month_rain'))

#Take the monthly rain and avg based on year and month
schemaMergedPrecipStation = schemaMergedPrecipStation.groupBy('year','month').agg(F.avg('month_rain')).orderBy(['year','month'], ascending=False).show()