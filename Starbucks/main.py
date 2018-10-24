#Determine if you should visit Starbucks
import time

#ask what day it is
print("Let's find out if today is the perfect day to visit Starbucks\n\n")
time.sleep(1)

#day = input('What day is it?\n')
day = input("What day is it?\n")

# Convert short to long day
if day.lower() == 'mon':
	day = 'Monday'
elif day.lower() == 'tue' or day.lower() == 'tues':
	day = 'Tuesday'
elif day.lower() == 'wed' or day.lower() == 'weds':
	day = 'Wednesday'
elif day.lower() == 'thur' or day.lower() == 'thurs':
	day = 'Thursday'
elif day.lower() == 'fri':
	day = 'Friday'
elif day.lower() == 'sat':
	day = 'Saturday'
elif day.lower() == 'sun':
	day = 'Sunday'

#check day a decide if Starbucks should be consumed
# Is it their birthday?
if 'birthday' in day.lower():
	time.sleep(1)
	print("\nHappy Birthday, why are you even asking me if you should visit? \n\nYou get a free Starbucks today :-)")
# Day recognised?
elif 'day' in day.lower() and day.lower() != 'day':
	time.sleep(1)
	print("\nYou've told me that today is " + day[0].upper() + day[1:] + ", I've checked, and today is the perfect day to visit Starbucks")
# Easter Egg
elif day.lower() == 'day':
	time.sleep(1)
	print("\nNice try, for trying to confuse my code, reward yourself with a visit to Starbucks.")
# Anything else entered
else:
	time.sleep(1)
	print("\nThat is either not spelt correctly, or it's not a day of the week.\n\n"
		  'I suggest you go to Starbucks immediately as you need to wake up.')