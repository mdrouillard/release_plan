# get inputs for total number of points, number of days left, team size per platform

points = int(raw_input('How many points total?\n'))
points_per_platform = points/2
print "Okay, that's " + str(points_per_platform) + ' points for each platform\n'
due_date = int(raw_input('How many working days until the due date?\n')) # in future figure out how to calculate due date
current_team = int(raw_input('How many team members are on a platform?\n'))
dev_speed = int(raw_input('How many points can a dev get done in a day?\n'))

# convert points to number of days per platform. 
platform_days = points_per_platform / dev_speed

# devs could complete the number of points inputted in these number of days
one_dev = platform_days
two_devs = platform_days/2
three_devs = platform_days/3
four_devs = platform_days/4

# Print out the number of days per platform it would take to finish the points
print('\nThat amount of points equates to ' + str(platform_days/current_team) + ' days per platform')


# How many more points or less points can current team size handle per platform
team_points_daily = dev_speed * current_team
total_point_capacity = (team_points_daily * due_date)
print('Your current team can get ' + str(total_point_capacity) + ' points per platform done by the due date.\n')

# Is your current team big enough? 
if total_point_capacity > points_per_platform :
	print('You can do it with your current team size!\n')
elif total_point_capacity == points_per_platform:
	print("You're at full capacity. You have no more points to spend\n")
else:
	print("You're gonna need a bigger team!\n")

# Suggest adding or subtracting points based on team capacity per platform
if total_point_capacity > points_per_platform:
	print('You can add ' + str(total_point_capacity - points_per_platform) + ' points per platform to your scope\n')
elif total_point_capacity < points_per_platform:
	print('You need to remove ' + str(points_per_platform - total_point_capacity) + ' points per platform from your scope\n')
else:
	print("Careful, you're cutting it close. Keep an eye on scope.\n")

# Project the impact of different team sizes
print('One developer on each platform would take ' + str(one_dev) + ' working days to complete the work or ' + str(float(one_dev)/5) + ' weeks.') 
print('Two developers on each platform would take ' + str(two_devs) + ' working days to complete the work or ' + str(float(two_devs)/5) + ' weeks.')
print('Three developers on each platform would take ' + str(three_devs) + ' working days to complete the work or ' + str(float(three_devs)/5) + ' weeks.')
print('Four developers on each platform would take ' + str(four_devs) + ' working days to complete the work or ' + str(float(four_devs)/5) + ' weeks.\n\n')

