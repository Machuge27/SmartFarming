import requests
import json

"""
url='http://localhost:5000/receive_data'


data = {
    'moisture': 22,
    'humidity': 12,
    'temperature': 43
}

headers = {'Content-Type': 'application/json',
           'API_KEY':'5d./?7d4bhd6kjb7875783gferggv'
           }

response = requests.post(url,headers=headers,json=data)
print(response.json())
"""

"""
import requests

url = "https://real-time-web-search.p.rapidapi.com/search"

querystring = {"q":"condition to grow maize","limit":"3"}

headers = {
	"X-RapidAPI-Key": "9eaa8c7b5emsh15813134738b8c2p1495d9jsn5a973fe692fb",
	"X-RapidAPI-Host": "real-time-web-search.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

url = "https://weather-api99.p.rapidapi.com/weather"


querystring = {"city":"Machakos"}

headers = {
	"X-RapidAPI-Key": "9eaa8c7b5emsh15813134738b8c2p1495d9jsn5a973fe692fb",
	"X-RapidAPI-Host": "weather-api99.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data=response.json()
print(data['main']['humidity'],data['main']['temp']-273)
"""
import requests


def get_data(startDateTime, endDateTime):

    url = "https://visual-crossing-weather.p.rapidapi.com/history"

    querystring = {
        "startDateTime": startDateTime,
        "aggregateHours": "24",
        "location": "Nairobi,Kenya",
        "endDateTime": endDateTime,
        "unitGroup": "us",
        "dayStartTime": "8:00:00",
        "contentType": "json",
        "dayEndTime": "17:00:00",
        "shortColumnNames": "0",
    }

    headers = {
        "X-RapidAPI-Key": "d4922ba520msh996d1f90b67d759p17f01djsn8d1e735b98bc",
        "X-RapidAPI-Host": "visual-crossing-weather.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    # print(data)
    values = data["locations"]["Nairobi,Kenya"]["values"]
    data = values[0]
    temp_celsius = (data["temp"] - 32) * 5 / 9
    humidity = data["humidity"]
    print(f"temp { temp_celsius} humidity {humidity}")
    dictionary = [
        {
            "Data": {
                "Date": startDateTime,
                "Temperature": temp_celsius,
                "Humidity": humidity,
                "Location": data["locations"],
            }
        }
    ]


for k in range(1, 4):
    for j in range(1, 13):
        for i in range(1, 29):
            print(i, j)
            date = "202" + str(k) + "-0" + str(j) + "-0" + str(i) + "T00:00:00"
            end_date = "202" + str(k) + "-0" + str(j) + "-0" + str(i) + "T23:59:59"
            get_data(date, end_date)
