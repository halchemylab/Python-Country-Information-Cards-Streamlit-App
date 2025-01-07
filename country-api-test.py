import requests

response = requests.get('https://restcountries.eu/rest/v3/all')
response = requests.get("https://restcountries.com/v3/name/taiwan")

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)