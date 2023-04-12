import requests

apikey="f620d71f81b7555db4e9344e8e465fad"
lat=12.9716
lon=77.5946


response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=12.9716&lon=77.5946&appid=f620d71f81b7555db4e9344e8e465fad")
response.raise_for_status()
data= response.json()
temp=data["main"]

print(temp["temp"])
