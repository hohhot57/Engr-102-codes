num_items = 7
my_string = ""    # empty string

if num_items > 3:
   my_string = my_string + 'a'
elif num_items < 10:
   my_string = my_string + 'c'
else:
   my_string = my_string + 'm'

print((my_string + 'd'), end = '!')
