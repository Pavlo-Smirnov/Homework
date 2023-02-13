# the first formatting method
name = 'Pasha'
day = 'Saturday'
print (f'Good day {name}! {day} is a perfect day to learn some python.')

# the second formatting method
s = 'Good day {}! {} is a perfect day to learn some python.'
print (s.format (name,day))

# the third formatting method

print ('Good day {0}! {1} is a perfect day to learn some python.'.format (name, day))
print ('Good day %s! %s is a perfect day to learn some python.' % (name, day))