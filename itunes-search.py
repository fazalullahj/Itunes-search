import json
# Make sure you have installed requests using --> pip install requests
import requests
print("""                    Itunes Browser      
Using this program, you can search for tracks in the Itunes...""")
artist= input("What do you want to search? ")
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+artist)


o = response.json()

for result in o["results"]:
    print("-->",result["trackName"])
