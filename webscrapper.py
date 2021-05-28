from bs4 import BeautifulSoup
import requests

def stockScrape(ticker):
  root = 'https://finance.yahoo.com/quote/'
  url = root + ticker
  page = requests.get(url)
  soup = BeautifulSoup(page.text, 'html.parser')
  price = soup.find('span', {'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text

  print("Found stock price from yahoo finance: " + price)
  return price;


def getData(url):
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


def getText(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.text, 'html.parser')
  paragraphs = soup.find_all('p')
  text = []
  if (len(paragraphs)<3):
      text.append(paragraphs[1].get_text())
  else:
      for x in range(1, 3):
        text.append(paragraphs[x].get_text())
  newline_text=[]
  for x in text:
    new_str = x.replace('\n', '')
    newline_text.append(new_str)

  final_text = []
  for i in range(len(newline_text)):
    new_str = ''
    x=newline_text[i]
    con = 1
    while con == 1:
      try:
        first_idx = x.index('[')
        second_idx = x.index(']')
        new_str = x[:first_idx] + x[second_idx+1:]
        x=new_str
      except:
        con = 0

    final_text.append(new_str)
  text = ''
  text = text.join(final_text)
  return text


def getFitnessBrand(url):
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
name, href = getFitnessBrand("https://en.wikipedia.org/wiki/List_of_fitness_wear_brands")

def getHref(name_input, name, href):
  name_input = name_input.lower()
  idx = name.index(name_input)
  return href[idx]
