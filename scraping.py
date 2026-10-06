import requests
from bs4 import BeautifulSoup

url = "https://yotta.co.id/"

response = requests.get(url)

if response.status_code == 200:
    print("Success")
else:
    print("Gagal")

print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("h2")

print("Title:", title)