import requests

api_address='http://api.openweathermap.org/data/2.5/weather?appid=49e0d6f14bca2e847b9ecf42bcd25f29&q=bangalore'
json_data = requests.get(url).json()
format_add = json_data['weather'][0]['description']
return(format_add)

