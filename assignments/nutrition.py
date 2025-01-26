def fruit_dicts(item):
#creating a fruit dict with keys as fruits and values as calories
    fruits = {
    "Apple": 130,
    "Avocado": 50,
    "Banana": 110,
    "Cantaloupe": 50,
    "Grapefruit": 60,
    "Grapes": 90,
    "Honeydew Melon": 50,
    "Kiwifruit": 90,
    "Lemon": 15,
    "Lime": 20,
    "Nectarine": 60,
    "Orange": 80,
    "Peach": 60,
    "Pear": 100,
    "Pineapple": 50,
    "Plums": 70,
    "Strawberries": 50,
    "Sweet Cherries": 100,
    "Tangerine": 50,
    "Watermelon": 80
    }
    if item in fruits:
        return f"Calories: {fruits[item]}"
    return ""

def main():
    #prompt user for input
    item = input("Item: ").strip()

    #if fruit_dicts(item):
        #print(fruit_dicts(item))
    
    
    result = fruit_dicts(item)

    if result:
        print(result)
main()