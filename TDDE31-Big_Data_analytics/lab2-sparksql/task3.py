from pyspark import SparkContext
from pyspark.sql import SQLContext, Row
from pyspark.sql import functions as F

sc = SparkContext(appName = "task3")
sqlContext = SQLContext(sc) 

#102170; 2013-11-01 ;06:00:00 ;6.8; G
# 0, station, 1 date, 2 time, 3 air temp, 4 quality

temp_file = sc.textFile("BDA/input/temperature-readings.csv")

parts = temp_file.map(lambda l: l.split(";"))

tempReadings = parts.map(lambda p: Row(station=p[0], year=p[1].split("-")[0], month=p[1].split("-")[1], day=p[1].split("-")[2], time=p[2], value=float(p[3]), quality=p[4] ))

schemaTempReadings = sqlContext.createDataFrame(tempReadings)

schemaTempReadings.registerTempTable("tempReadings")

schema_temp_year = schemaTempReadings.filter((schemaTempReadings['year'] >= '1960') & (schemaTempReadings['year'] <= '2014'))

schema_temp_max_day = schema_temp_year.groupBy('station','year','month','day').agg(F.max('value').alias('maxtemp'))
schema_temp_min_day = schema_temp_year.groupBy('station','year','month','day').agg(F.min('value').alias('mintemp'))
schema_temp_joined = schema_temp_max_day.join(schema_temp_min_day, ['station','year','month','day'], 'inner')
schema_temp_joined = schema_temp_joined.select('station','year','month', 'day', ((schema_temp_joined['maxtemp'] + schema_temp_joined['mintemp'])/2).alias('avgDay'))

month_avg = schema_temp_joined.groupBy('station', 'year', 'month').agg(F.avg('avgDay').alias('avgtemp')).orderBy('avgtemp', ascending=False).show()
