SELECT COUNT(*) FROM [dbo].[apr_time] WHERE [day] = ??
SELECT COUNT(*) FROM [dbo].[apr_time] WHERE [day] = ?? and [hour] = ??
SELECT COUNT(*) FROM [dbo].[apr_time] WHERE [hour] = ?? 
SELECT COUNT(*) FROM [dbo].[apr_time] WHERE [minute] = ?? 
SELECT COUNT(*) FROM [dbo].[apr_time] WHERE [day] = ?? and [hour] = ?? and [minute] = ?? group by [neighborhood]

#SELECT COUNT(*) FROM [dbo].[apr_time] WHERE [month] = ??


def count_by_query(month,day,hour,minute):
	'''
	month: the corresponding table name. i.e. apr
	day: int
	hour: int
	minute: int
	'''
	prepare_statement = "SELECT distinct [lat], [lon], [neighborhood] FROM [dbo].[" + month + "_time] WHERE [day] = "+ str(day) + "and [hour] = " 
	+ str(hour) + "and [minute] =" + str(minute) + "group by [neighborhood]"
	cursor.execute(prepare_statement)
	rows = cursor.fetchone()
	lat_list = []
	lon_list = []
	neighborhood_list = []
	for row in rows:
		lat_list.append(row.LAT)
		lon_list.append(row.LON)
		neighborhood.append(row.neighborhood)

	dics1 = {}
	keys1 = [i for i in neighborhood_list]
	dics2 = {}
	keys2 = ["Lat","Lon"]

	for 
	for key in keys1:


