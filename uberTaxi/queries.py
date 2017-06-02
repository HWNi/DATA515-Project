SELECT COUNT(*) FROM [dbo].[apr_time] WHERE [day] = ??
SELECT COUNT(*) FROM [dbo].[apr_time] WHERE [day] = ?? and [hour] = ??
SELECT COUNT(*) FROM [dbo].[apr_time] WHERE [hour] = ?? 
SELECT COUNT(*) FROM [dbo].[apr_time] WHERE [minute] = ?? 
SELECT COUNT(*) FROM [dbo].[apr_time] WHERE [day] = ?? and [hour] = ?? and [minute] = ?? group by [neighborhood]

#SELECT COUNT(*) FROM [dbo].[apr_time] WHERE [month] = ??


def count_by_query(month,hour):
	'''
	month: the corresponding table name. i.e. apr
	day: int
	hour: int
	minute: int
	'''
	prepare_statement = "SELECT count(*) as count, [neighborhood] FROM [dbo].[" + month + "_time] WHERE [hour] = " 
	+ str(hour) + "group by [neighborhood]"
	cursor.execute(prepare_statement)
	rows = cursor.fetchone()
	#lat_list = []
	#lon_list = []
	neighborhood_list = []
	count_list = []
	for row in rows:
		#lat_list.append(row.LAT)
		#lon_list.append(row.LON)
		neighborhood.append(row.neighborhood)
		count_list.append(row.count)

	dics = {}
	keys = [i for i in neighborhood_list]


	for key in keys:
		dics[i] = count_list[i]

	return dics