# do print() to see the results
# these are the variables for a formatted string:
first_name = "bob"
last_name = "smith"
full_name = f"Hi my name is {first_name} {last_name}"
name_with_something = f"{full_name}. I have a boring name."

# string methods. btw python is case sensitive meaning that X != x or A != a:
# len() counts the amount of elements in an object including spaces
string = '123456'
count = (len(string))
# .upper and .lower change the characters to uppercase or lowercase
course = 'Python For Newbies'
uppercase = (course.upper())
lowercase = (course.lower())

# .find finds the index of an element in an object
list1 = '123456'
finder = list1.find('1')
# .replace replaces elements
replacer = list1.replace('1', 'replacement')
# the in keyword checks if an element is inside an object. the results are boolean
list_for_in = "my favorite food is pizza"
in_word = 'my' in list_for_in
# title() converts the first character of a word within a string to uppercase
title_without_upper = 'python course for idiots'
title_with_upper = title_without_upper.title()

# recap:
# len() counts the amount of elements in a string
# .upper and .lower change the characters of a string to uppercase or lowercase
# .title changes every first character of each word into uppercase
# .replace replaces an element in a string
# the keyword "in" checks if there is a object in a string with True or False.





