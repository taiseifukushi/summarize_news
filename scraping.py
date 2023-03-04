import requests
from bs4 import BeautifulSoup
from feed_parser import list_extract_url
import pdb # pdb.set_trace()

def get_news_text(news_article_url):
  res  = requests.get(news_article_url)
  soup = BeautifulSoup(res.content, 'html.parser')
  text = soup.find("p").get_text()
  return text

def list_news_text(rss_feed_url):
  list = list_extract_url(rss_feed_url)
  return [get_news_text(url) for url in list]
