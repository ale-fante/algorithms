"""
  Tuples items can themselves be other tuples. 
  We can improve the info about characters to hold full date of birth, not just the year 
  plus some movies and the dates they were made
"""

julia_more_info = (("Julia", "Roberts"), (8, "October", 1967),
  "Actress", ("Atlanta", "Georgia"),
  [ ("Duplicity", 2009),
    ("Notting Hill", 1999),
    ("Pretty Woman", 1990),
    ("Erin Brockovich", 2000),
    ("Eat Pray Love", 2010),
    ("Mona Lisa Smile", 2003),
    ("Ocean's Twelve", 2004)])

print(julia_more_info)

"""
  Tuple has 5 elements, but each of those in turn can be another tuple, a list, or 
  any other kind of Python value. This property is known as **HETEROGENEOUS**, 
  meaning that it can be composed of elements of different types.
"""

# Excercises

# 1) Can Tuples be passed in as arguments

def tuple_arg_test(story_details):
	title, theme, location, release_year, protagonist = story_details
	return title, theme

story_details = ("Movie_title", "Gut Feeling", "Small town USA", 2020, "sofia")
print((tuple_arg_test(story_details)))





