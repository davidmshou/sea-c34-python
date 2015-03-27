"""
Step 1
"""
new_dictionary = {"name": "Michael", "city": "Seattle", "cake": "Chocolate"}

print(new_dictionary)

del new_dictionary["cake"]

print(new_dictionary)

new_dictionary["fruit"] = "Mango"

print(new_dictionary)

for key in new_dictionary.iterkeys():
    print key

for value in new_dictionary.itervalues():
    print value

#print(new_dictionary.get("cake"))
print("cake" in new_dictionary)

for value in new_dictionary.values():
    if value == "Mango":
        print("We've got %s's." % (value))

"""
Step 2
"""

my_numbers = list(range(0, 16))
my_letters = list("ABCDEFGHIJKLMNOP")
print(my_numbers)
print(my_letters)

combined_dict = dict(zip(my_numbers, my_letters))

print(combined_dict)

"""
Step 3
"""

dict_update = dict(new_dictionary)  # Copy original list.


for key, value in dict_update.items():  # Value == number of 'a's in value
    number_a = 0
    if "a" in value:
        number_a += 1
        dict_update[key] = number_a

print dict_update

"""
Step 4
"""

s2 = set(range(0, 21))

tuple_2 = tuple(s2)
for number in tuple_2:
    if number % 2 != 0:
        s2.remove(number)

print(s2)


s3 = set(range(0, 21))

tuple_3 = tuple(s3)

for number in tuple_3:
    if number % 3 != 0:
        s3.remove(number)

print(s3)


s4 = set(range(0, 21))

tuple_4 = tuple(s4)

for number in tuple_4:
    if number % 4 != 0:
        s4.remove(number)

print(s4)

print(s3.issubset(s2))

print(s4.issubset(s2))

"""
Step 5
"""


