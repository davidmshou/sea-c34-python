from __future__ import print_function
import sys

donor_dict = {"John Doe": [10000, 5000, 30000], "Jane Johns": [25000, 10000], "Buster Bluth": [80000, 100000]}


def select_operation():
    """Request input from user.
    """
    user_input = raw_input(u"Enter: (c)reate a report, (s)end thank you, or (q)uit: ")

    if user_input.lower() == u"c":
        donor_list()
    elif user_input.lower() == u"s":
        name_prompt()
    elif user_input.lower() == u"q":
        sys.exit(u"Have a good day, sir.")
    else:
        print(u"Please select (c)reate a report or (s)end thank-you.")
        select_operation()


def donor_list():
    """Print donor list
    """
    print(donor_dict)
    select_operation()


def name_prompt():
    """Prompt user for name of donor, or list of donors.
    """
    user_input = raw_input(u"Please enter donor's name, (l)ist, or (q)uit: ")
    donor_tuple = tuple(donor_dict)

    if user_input.lower() == "l":
        print(donor_dict.keys())
        name_prompt()
    elif user_input.lower() == "q":
        sys.exit(0)
    else:
        for key in donor_tuple:
            if user_input.lower() == key.lower():
                donation_amount(user_input)
                break
            else:
                if user_input.lower() != key.lower():
                    donor_dict[user_input] = []
                    donation_amount(user_input)
                break


def donation_amount(donor):
    donation_input = raw_input(u"Enter donation amount: ")
    donation_int = int(donation_input)

    if donor in donor_dict:
        donor_dict[donor].append(donation_int)
        email_format(donor, donation_int)


def email_format(donor, amount):
    print(u"Hello, %s! Thank you for your donation of %i" % (donor, amount))

if __name__ == "__main__":
    while True:
        select_operation()
