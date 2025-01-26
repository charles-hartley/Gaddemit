#defining a main function which will be called to run the program
def main():
    #collect an expression from the user
    expression = input("What expression do yo have in mind? ")
    #using the split() method
    parting = expression.split()
    #converting x & y to float
    x = float(parting[0])
    y = parting[1]
    z = float(parting[2])

    result = calculate_expression(x, y, z)
    print_result(result)

#creating a function to perform the logical calculation
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
        else: #assumption if z == 0
            return "Don't you know Math?"
    else: #incase user inputs the wrong operator
        return "Error: Invalid Operator"

#creating a function to check if its an integer or a float
def print_result(result):
    if isinstance(result, (int, float)):
        format_result = f"{result:.1f}"
        print(format_result)
    else: #if not an int or float then to output the error results from calculate_expression
        print(result)

main()