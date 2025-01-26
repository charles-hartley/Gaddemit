#we do define a main function which we will call later to run the program
def main():
    #collect an expression from the user
    expression = input("What expression do you have in mind? ")
    #using the split() method
    parting = expression.split()
    #we convert x & z to float
    x = float(parting[0])
    y = parting[1]
    z = float(parting[2])

    result = calculate_expression(x, y, z)
    print_result(result)

#we create a function to perform the logical calculation
def calculate_expression(x, y, z):
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        if z != 0:
            return x / z
        else: #assumption of if z == 0
            return "Don't you know Math?"
    else: #if the user inputs the wrong operator
        return "Error: Invalid Operator"

#we create a function to check if its an integer or a float
def print_result(result):
    if isinstance(result, (int, float)):
        format_result = f"{result:.1f}"
        print(format_result)
    else: #if not an int or float then to output the error results from calculate_expression function
        print(result)

main()

