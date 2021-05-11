from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

def get_fitness_brand(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.text, 'html.parser')
  # list_elem = soup.find_all('li')
  # print(list_elem)
  list_elem = soup.find(id='mw-content-text')
  a = list_elem.find_all('a')
  a= a[:190]
  href = []
  name = []
  for link in a:
    name.append(link.get_text().lower())
    # print(link)
    href.append("https://en.wikipedia.org"+link.get('href'))
  return name, href
# name, href = get_fitness_brand("https://en.wikipedia.org/wiki/List_of_fitness_wear_brands")

def get_href(name_input, name, href):
  name_input = name_input.lower()
  idx = name.index(name_input)
  return href[idx]
# get_href("Nike", name, href)

def get_data(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.text, 'html.parser')
  table = soup.table
  info = table.find_all('tr')
  info.pop(0)
  info.pop(len(info)-1)
  text_list = []
  for x in info:
    text_list.append(x.get_text())
  text = '|'
  text= text.join(text_list)
  print(text)

####################
#FLASK####
######################
app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name')
    brand, href = get_fitness_brand("https://en.wikipedia.org/wiki/List_of_fitness_wear_brands")
    get_href(name, brand, href)
    info = get_data(href)
    return jsonify(data = info)

if __name__ == "__main__":
    app.run(debug=True)


