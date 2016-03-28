# Script to convert estimate in weeks to points. Useful for converting initial sizing exercises into points.

try:
	weeks = float(raw_input('Enter the number of estimated weeks: '))
	point_value = float(raw_input('How many points can a developer complete in a day? '))

# calculate number of points per week
	week_points = point_value * 5

# convert weeks into points based on capacity
	points = weeks * week_points

#	print weeks, point_value, week_points

	print '\nThat works out to ' + str(points) + ' points\n'

except:
	print 'Error. Please enter a valid numeral.'
	
