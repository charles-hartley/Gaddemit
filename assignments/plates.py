MAX_CHARACTERS = 6
MIN_CHARACTERS = 2

def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    """
    check the length of the plate for comparison and return False if the condition ain't met.
    check the first two chars are letters(.isalpha()).
    check for punctuations, periods and spaces
    """

    if not (MIN_CHARACTERS <= len(plate) <= MAX_CHARACTERS):
            return False
    
    if not plate[:2].isalpha():
            return False
    
    #if any(char in string.punctuation + string.whitespace for char in plate):
    if not plate.isalnum():
        return False
    
    """
    Flag to track if a number has been found
    loop through each character in plate
    check if the char is a digit
    check if first digit is a 0 and not number found then return False
    return false if there is a letter in the rest of chars
    """

    num_found = False
    for char in plate:
        if char.isdigit():
            #if not num_found:
            if char == "0" and not num_found:
                return False
            num_found = True
        elif num_found:
            return False
    
    #return True if all conditions are met
    return True

if __name__ == "__main__":
    main()