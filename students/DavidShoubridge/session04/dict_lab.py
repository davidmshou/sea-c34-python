"""
Step 1
"""
new_dictionary = {"name": "Michael", "city": "Seaattle", "cake": "Chocolate"}

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
my_letters = []

for num in my_numbers:
    my_letters.append(hex(my_numbers[num]))

print(my_numbers)
print(my_letters)

combined_dict = dict(zip(my_numbers, my_letters))

print(combined_dict)

"""
Step 3
"""

dict_update = dict(new_dictionary)  # Copy original list.
dictionary_2 = list(dict_update.values())
number_a = []

for x in dictionary_2:
    number_a.append(x.count('a'))

dictionary_3 = dict(zip(dictionary_2, number_a))
print(dictionary_3)

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

monty = set("Python")

monty.add("i")
print(monty)

let_it_go = frozenset("marathon")
print(let_it_go)

print monty.union(let_it_go)
print monty.intersection(let_it_go)
