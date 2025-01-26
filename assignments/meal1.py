#we start by defining a main() function
def main():
    #user's input collection
    time = input("What's the time? ").strip()
    #using the convert function to get the returned value
    time_hours = convert(time)
    
    #Determine and print the meal time
    if 7 <= time_hours <= 8:
        print("breakfast time")
    elif 12 <= time_hours <= 13:
        print("Lunch time")
    elif 18 <= time_hours <= 19:
        print("Dinner time")
    
#convert function
def convert(time):
    # Handling 12-hour format
    time_in_am = "a.m" in time.lower()
    time_in_pm = "p.m" in time.lower()

    # Removing any a.m or p.m using the string replace and strip method
    time = time.lower().replace("a.m", "").replace("p.m", "").strip()

    # Split the time into hours and minutes
    hours, minutes = map(int, time.split(":"))

    # Convert 12-hour format to 24-hour format
    if time_in_am and hours == 12:
        hours = 0
    if time_in_pm and hours != 12:
        hours += 12

    # Convert hours + minutes / 60 to float
    return hours + (minutes / 60)


if __name__ == "__main__":
    main()