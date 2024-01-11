# Using request module
import requests

# get request using requests
# response = requests.get("https://cmlowerence.netlify.app")
# print(response.text)

# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#   'title': 'foo',
#   'body' : 'bar',
#   'userId' : 1,
# }
# headers = {
#   'Content-type': 'application/json; charset=UTF-8',
# }
# response = requests.post(url, headers=headers, json=data)
# print(response.text)

url = "https://cmlowerence.netlify.app"
r = requests.get(url)

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify()) # printing the formatted code of the site

for heading in soup.find_all("span"):
  print(heading.text)
