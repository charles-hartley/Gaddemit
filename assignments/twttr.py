#creating a main function.
def main():
    """
    collect user's input and clean it with .strip().lower()
    call for the ommit_vowels function
    print the output
    """
    tweet = input("Input: ").strip()
    out_put = ommit_vowels(tweet)
    print(f"Output: {out_put}")


def ommit_vowels(tweet):
    """
    collect the return strings
    using a for loop to iterate the tweet
    condition to check 
    """
    result = ""
    vowels = ["a", "e", "i", "o", "u"]
    for char in tweet:
        if char.lower() not in vowels:           
             result += char

    return(result)

main()