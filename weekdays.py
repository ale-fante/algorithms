

def getWeekDay(weekday, daysoff):
	weekdays = {
		"1" : "Sunday",
		"2" : "Monday",
		"3" : "Tuesday",
		"4" : "Wednesday",
		"5" : "Thursday",
		"6" : "Friday",
		"7" : "Saturday"
	}

	day = weekdays[weekday]
	length_of_stay = int(daysoff)

	total_nights = 0
	for d in weekdays:
		print(d)

week_day = raw_input("On what day of the week will your vacation start? ")
nights_out = raw_input("How many days will you take off? ")
getWeekDay(week_day, nights_out)