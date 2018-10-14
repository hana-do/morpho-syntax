import requests
import nltk
from word_info import *

from bs4 import BeautifulSoup

# credentials
url_base = 'http://www.oed.com.ezproxy.mnsu.edu/'
url_login = 'https://login.ezproxy.mnsu.edu/login'
url_home = 'http://ezproxy.mnsu.edu/login?url=http://www.oed.com'
payload = {'user': '', 'pass': ''}

# initialize text
text = WordInfo('We stopped on an edgeless plateau that stretched to nothing on all sides')
tagged_text = text.get_tagged_text()

with requests.Session() as s:
  # get past login page
  s.get(url_login)
  r = s.post(url_home, data=payload)
  # print(r.text)

  # query each word
  for t in tagged_text:
    # get search result page
    url_word = "http://www.oed.com.ezproxy.mnsu.edu/search?searchType=dictionary&q=" + 'friend' + "&_searchBtn=Search" #t[0]
    r_word = s.post(url_word, data=payload)

    # create bs object
    bs_word = BeautifulSoup(r_word.text, 'html.parser')

    # get oed part of speech
    pos_oed = get_oed_pos('NOUN') #t[1]

    # check if many results
    hasManyResult = str(bs_word.find(id='entryPrevNextNav')) == ('None')

    # retain results of matched pos
    links = []
    if hasManyResult:
      bs_res = bs_word.find_all('span', class_="word")
      for r in bs_res:
        r_ps = r.find_all('span', class_="ps")

        # get links to results
        if str(r_ps).find(pos_oed) != -1:
          link = url_base + r.a['href']
          links.append(link)
    else:
      links.append(url_word)

    # reload result page
    for link in links:
      if link != url_word:
        r_word = s.post(link, data=payload)
        bs_word = BeautifulSoup(r_word.text, 'html.parser')

      print(link)
      print(bs_word)

      # get origin
      # origin =

    break
