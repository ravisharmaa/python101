import requests

api_url = 'https://monitoring.javra.com/api/dashboard'

response = requests.get(api_url)

json_response = response.json()

print(json_response)

print(response.status_code)

response.close()


