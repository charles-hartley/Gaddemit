def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi", "Bowser"]
    for i in range(len(names)):
        print(write_letter(names[i], "Princess Peach"))


def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    Dear {receiver},

    You are cordially invited to a ball at 
    Peach's Castle this evening, 7.00pm.

    Sincerely,
    {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """

main()
