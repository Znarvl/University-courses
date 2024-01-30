from pyspark import SparkContext
from pyspark.sql import SQLContext, Row
from pyspark.sql import functions as F

sc = SparkContext(appName = "lab2task1a")
sqlContext = SQLContext(sc) 

#102170; 2013-11-01 ;06:00:00 ;6.8; G
# 0, station, 1 date, 2 time, 3 air temp, 4 quality

temp_file = sc.textFile("BDA/input/temperature-readings.csv")

parts = temp_file.map(lambda l: l.split(";"))

tempReadings = parts.map(lambda p: Row(station=p[0], date=p[1], year=p[1].split("-")[0], time=p[2], value=float(p[3]), quality=p[4] ))

schemaTempReadings = sqlContext.createDataFrame(tempReadings)

schemaTempReadings.registerTempTable("tempReadings")

schema_temp_year = schemaTempReadings.filter((schemaTempReadings['year'] >= '1950') & (schemaTempReadings['year'] <= '2014'))

schema_temp_max = schema_temp_year.groupBy('year').agg(F.max('value').alias('value'))

schema_temp_max = schema_temp_max.join(schema_temp_year, ['year', 'value'], 'inner').select('year', 'station', 'value').orderBy('value', ascending=False).show()
