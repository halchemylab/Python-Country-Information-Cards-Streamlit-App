import requests

response = requests.get("https://www.timeapi.io/api/Time/current/zone?timeZone=Asia/Taipei")

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)
