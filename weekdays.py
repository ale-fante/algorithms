

def getWeekDay(weekday, daysoff):
	weekdays = {
		"0" : "Sunday",
		"1" : "Monday",
		"2" : "Tuesday",
		"3" : "Wednesday",
		"4" : "Thursday",
		"5" : "Friday",
		"6" : "Saturday"
	}

	day = weekdays[weekday]
	length_of_stay = int(daysoff)

	come_back_length = int(weekday) + length_of_stay
	come_back_day = weekdays[str(come_back_length)]

	days_off_list = []
	for d in range(come_back_length + 1):
		if d < 6:
			days_off_list.append(d)
			last_day_off = days_off_list[-1]

			continue
		elif d > 6:
			"WTF"

	print("You will be leaving on " + day)
	print("If you take " + str(length_of_stay) + 
		" day(s) off. Then you will come back on a " + str(weekdays[str(last_day_off)]))


week_day = raw_input("On what day of the week will your vacation start? ")
nights_out = raw_input("How many days will you take off? ")
getWeekDay(week_day, nights_out)