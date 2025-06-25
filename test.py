import requests

API_KEY = "AIzaSyA-BBTlR4sr7KA5pSi71aGmwHYv2aFK6lk"
location = "33.66906910416403,-112.11321417544627"  # 注意逗号后无空格
radius = 16000  # 米
keyword = "apartment"

url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&keyword={keyword}&key={API_KEY}"

response = requests.get(url)
data = response.json()

results = data.get("results", [])

with open("apartments.txt", "w", encoding="utf-8") as f:
    for place in results:
        name = place.get("name")
        rating = place.get("rating", 0)
        address = place.get("vicinity")
        if rating >= 4:
            line = f"{name} | Rating: {rating} | Address: {address}\n"
            print(line, end="")
            f.write(line)
