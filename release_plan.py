# get inputs for total number of points, number of days left, team size per platform
# consider adding an input for contingency

points = int(raw_input('How many points total?\n'))
due_date = int(raw_input('How many working days until the due date?\n')) # in future figure out how to calculate due date
current_team = int(raw_input('How many team members are on a platform?\n'))

# convert points to number of days per platform. On this team, 1 point is a half day and there are two platforms
platform_days = points / 4

# devs could complete the number of points inputted in these number of days
one_dev = platform_days
two_devs = platform_days/2
four_devs = platform_days/4

# Print out the number of days per platform it would take to finish the points
print('\nThat amount of points equates to ' + str(platform_days) + ' days per platform')

# Is your current team big enough?
if current_team * due_date > platform_days:
	print('You can do it with your current team size!\n')
elif current_team * due_date == platform_days:
	print("You're at full capacity. You have no more points to spend")
else:
	print("You're gonna need a bigger team!\n")
	
# How many more points or less points can current team size handle
point_day = 4 # each platform member can get 2 points done a day
team_points_daily = point_day * current_team
total_point_capacity = (team_points_daily * due_date)
print('Your current team can get ' + str(total_point_capacity) + ' points done by the due date.\n')

# Suggest adding or subtracting points based on team capacity
if total_point_capacity > points:
	print('You can add ' + str(total_point_capacity - points) + ' points to your scope\n')
elif total_point_capacity < points:
	print('You need to remove ' + str(points - total_point_capacity) + ' points from your scope\n')
else:
	print("You're at capacity. Maintain the course.\n")

# Project the impact of different team sizes
print('1 developer on each platform would take ' + str(one_dev) + ' working days to complete the work.')
print('2 developers on each platform would take ' + str(two_devs) + ' working days to complete the work.')
print('4 developers on each platform would take ' + str(four_devs) + ' working days to complete the work.\n\n')