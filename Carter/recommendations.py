def main():
    #prompt user for a level
    difficulty = input("Difficult or Casual? ")
    #check if the level entered by the user is valid
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter a valid difficulty")
        return
    
    players = input("Multiplayer or Single-player? ")
    if not (players == "Multiplayer" or players == "Single-player"):
        print("Enter a valid number of players")
        return
    #the logical part of the program
    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Poker")
    elif difficulty == "Difficult" and players == "Single-players":
        recommend("Sokoban")
    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Hearts")
    else:
        recommend("Snake")

def recommend(game):
    print("You might like", game)

main()