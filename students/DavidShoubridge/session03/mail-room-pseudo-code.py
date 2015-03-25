def select_operation(prompt):
    """Request input from user with a prompt, and return the result.
    """
    prompt("Type 'create a report' or 'send thank-you'")
    if user_input == "create a report":
        donor_list()
    else:
        name_prompt()


def donor_list():
    print(donors_dictionary)
    select_operation()


def name_prompt(prompt):
    prompt("Enter donor's name or type 'list' for a list of donors: ")
    if user_input == "list":
        print(donor_name_list_)
        name_prompt()
    elif user_input == <donor name not on list>:
        donor_name_list.append(user_input)
        donation_amount(user_input)
    else:
        donation_amount(user_input)

donation = []


def donation_amount(user_input):
    prompt("Please enter donation amount for %s." % (user_input))
    donation.append(amount_entered)
    donors_dictionary.append(donation)
    email_format()


def email_format(donor, amount):
    print("Hello %s! Thank you for your donation of %s." % (donor, amount))

