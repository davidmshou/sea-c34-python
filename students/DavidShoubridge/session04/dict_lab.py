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


my_numbers = list(range(0, 16))
my_letters = list("ABCDEFGHIJKLMNOP")
print(my_numbers)
print(my_letters)

combined_dict = dict(zip(my_numbers, my_letters))

print(combined_dict)


dict_update = dict(new_dictionary)  # Copy original list.


for key, value in dict_update.items():  # Value == number of 'a's in value
    number_a = 0
    if "a" in value:
        number_a += 1
        dict_update[key] = number_a

print dict_update
