from pyspark import SparkContext
from pyspark.sql import SQLContext, Row
from pyspark.sql import functions as F

sc = SparkContext(appName = "task4")
sqlContext = SQLContext(sc) 



#102170; 2013-11-01 ;06:00:00 ;6.8; G
# 0, station, 1 date, 2 time, 3 air temp, 4 quality

temp_file = sc.textFile("BDA/input/temperature-readings.csv")

precipitation_file = sc.textFile("BDA/input/precipitation-readings.csv")


parts = temp_file.map(lambda l: l.split(";"))

parts_precip = precipitation_file.map(lambda l: l.split(";"))


tempReadings = parts.map(lambda p: Row(station=p[0], month=p[1].split("-")[1], year=p[1].split("-")[0],  time=p[2], temperature=float(p[3]), quality=p[4] ))

precipReadings = parts_precip.map(lambda p: Row(station=p[0],  month=p[1].split("-")[1], year=p[1].split("-")[0], yearmonthday=p[1] , time=p[2], precipitation=float(p[3]), quality=p[4] ))


schemaTempReadings = sqlContext.createDataFrame(tempReadings)
schemaPrecipReadings = sqlContext.createDataFrame(precipReadings)

schemaTempReadings.registerTempTable("tempReadings")
schemaPrecipReadings.registerTempTable("precipReadings")


## temperature max
schema_temp_max = schemaTempReadings.groupBy('station').agg(F.max('temperature').alias('temp_max'))

schema_filter_temp = schema_temp_max.filter((schema_temp_max['temp_max'] >= 25) & (schema_temp_max['temp_max'] <= 30))

## Max precipitation

schema_precip_total = schemaPrecipReadings.groupBy('station', 'yearmonthday').agg(F.sum('precipitation').alias('total_precipitation'))

schema_precip_max = schema_precip_total.groupBy('station').agg(F.max('total_precipitation').alias('max_precipitation'))

schema_filter_precip = schema_precip_max.filter((schema_precip_max['max_precipitation'] >= 100) & (schema_precip_max['max_precipitation'] <= 200))


# Join both
schema_filter_temp.join(schema_filter_precip, ['station'], 'inner').select('station', 'temp_max', 'max_precipitation').orderBy('station', ascending=False).show()

