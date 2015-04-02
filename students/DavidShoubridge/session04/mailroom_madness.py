from __future__ import print_function
import numpy
import sys

donor_dict = {
    "John Doe": [10000.00, 5000.00, 30000.00], "Jane Johns": [25000.00, 10000.00],
    "Buster Bluth": [80000.00, 100000.00]
}


def safe_input(user_prompt):
    try:
        user_input = raw_input(user_prompt)
    except(KeyboardInterrupt, EOFError):
        return "None"
    else:
        return user_input


def select_operation():
    """Request input from user, which will either create a report or send a \
    thank-you.
    """
    user_input = safe_input(u"Enter: (C)reate a report, (S)end thank you, or (Q)uit: ")

    if user_input.lower() == u"c" or user_input.lower() == u"create a report":
        donor_list()
    elif user_input.lower() == u"s" or user_input.lower() == u"send thank you":
        name_prompt()
    elif user_input.lower() == u"q" or user_input.lower() == u"quit":
        sys.exit(u"Have a good day, sir.")
    else:
        print(u"Please select (c)reate a report or (s)end thank-you.")
        select_operation()


def donor_list():
    """Sorts donor list and sorts by total donation."""
    donors = []

    for donor, value in donor_dict.items():
        total = sum(value)
        average = numpy.mean(value)
        number_of_donations = len(value)
        donors.append(
            [
                donor, number_of_donations,
                total, average
            ]
        )
    donors.sort(key=lambda x: x[3], reverse=True)

    print(
        "{:15s} {:15s} {:15s} {:15s}\n".format(
            "Name", "Total Donations", "Donation Sum",
            "Av. Donation"
        )
    )
    for i in donors:
        print(
            "{:15s} {:<15d} {:<15,.2f} {:<15,.2f}".format(
                i[0], i[1], i[2], i[3]
            )
        )
    print("\n\n")

    select_operation()


def name_prompt():
    """
    Prompt user for name of donor, or list of donors.
    """
    user_input = safe_input(
        u"Please enter Donor's name, (L)ist, (M)ain menu, or (Q)uit: "
    )
    #donor_tuple = tuple(donor_dict)
    #print(donor_tuple)
    if user_input.lower() == u"l" or user_input.lower() == u"list":
        print(donor_dict.keys())
        name_prompt()
    elif user_input.lower() == u"q" or user_input.lower() == u"quit":
        sys.exit(0)
    elif user_input.lower() == u"m" or user_input.lower() == u"main menu":
        select_operation()
    else:
        for key in donor_tuple:
            if user_input.lower() == key.lower():
                print("Donor in database")
                donation_amount(user_input)
                break
            else:
                if user_input.lower() != key.lower():
                    print("Donor not in database")
                    donor_dict[user_input] = []
                    donation_amount(user_input)
                break


def donation_amount(donor):
    """
    Prompt user for donation amount, then adds it to donors 'file'.
    """
    donation_input = safe_input(u"Enter donation amount: ")

    try:
        donation_input = float(donation_input)
    except (TypeError, ValueError):
        print("Only numbers are valid, returning to menu.")
        name_prompt()
    else:
        if donor in donor_dict:
            donor_dict[donor].append(donation_input)
            email_format(donor, donation_input)


def email_format(donor, amount):
    """
    Creates thank you email based on donor name and amount given previously.
    """
    print(u"Hello, %s! Thank you for your donation of %f" % (donor, amount))

if __name__ == "__main__":
    print(
        " __  __        __  __           _                     \n"
        "|  \/  |      |  \/  |         | |                    \n"
        "| \  / |______| \  / | __ _  __| |_ __   ___  ___ ___ \n"
        "| |\/| |______| |\/| |/ _` |/ _` | '_ \ / _ \/ __/ __|\n"
        "| |  | |      | |  | | (_| | (_| | | | |  __/\__ \__ \ \n"
        "|_|  |_|      |_|  |_|\__,_|\__,_|_| |_|\___||___/___/\n"
        "                                                      \n"
    )

    while True:
        select_operation()
