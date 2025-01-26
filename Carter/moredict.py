import requests

#empty dictionary to hold spacecraft data
spacecraft_data = {}

#Function to fetch and update data from an external site
def update_spacecraft_craft(url):
    global spacecraft_data
    try:
        response = requests.get(url)
        #Raise exception for HTTP errors
        response.raise_for_status()

        #parse the JSON data from the response
        new_data = response.json()
        print("New data received:", new_data)

        #update the existing dictionary
        spacecraft_data.update(new_data)
        print("Updated spacecraft data:", spacecraft_data)
    
    except requests.exceptions.RequestException as e:
        print("Error fetching data:, e")
    
#Example URL of the external site (replace with the real one)
url = "https://api.example.com/spacecraft_data"

#Call the function to fetch and update
update_spacecraft_data(url)