def main():
    #Call the function "print_square" with size 3 to print a 3 by 3 square of "#"
    print_square(3)

def print_square(size):
    #Outer loop: Iterate through each row of the square
    for i in range(size):
        #print("#" * size)
        #Inner loop: Iterate through each column in the current row
        for j in range(size):
            #Print "#" without a newline (end="" prevents line breaks)
            print("#", end="")
        #print a newline after completing one row
        print()

#Call the "main" function to start the program
main()