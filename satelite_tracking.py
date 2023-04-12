# import requests
#
# response = requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data= response.json()["iss_position"]
# longitude=data["longitude"]
# latitude=data["latitude"]
# tup=(longitude, latitude)
# print(tup)

import requests

response= requests.get(" https://api.sunrise-sunset.org/json?lat=12.995854&log=77696350&formatted=0")
response.raise_for_status()
sunrise=(response.json()["results"]["sunrise"])
sunset=(response.json()["results"]["sunset"])
print(f"Sunrise {sunrise}\n sunset{sunset}")