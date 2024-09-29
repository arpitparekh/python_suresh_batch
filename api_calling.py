# pip install requests

from urllib import response
import requests

url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url)

if response.status_code==200:
  data = response.json()
  for x in data:
    print(x['title'])

else:
  print("Error")
