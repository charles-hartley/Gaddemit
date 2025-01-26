#define the main function
def main():
    """
    ask for user input and we call convert_to_snakecase(snake_case)
    to print the result
    """
    snake_case = input("camelCase: ").strip()
    result = convert_to_snakecase(snake_case)
    print(result)


def convert_to_snakecase(snake_case):
    """
    defining a function to handle the conversion to snake_case
    """
    result = []
    for letter in snake_case:
        if letter.isupper():
            result.append("_" + letter.lower())
        else:
            result.append(letter)
    result ="".join(result)
    return result
    
main()


