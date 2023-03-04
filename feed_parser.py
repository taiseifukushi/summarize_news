import feedparser
import pdb # pdb.set_trace()

def list_extract_url(url):
  parsed_feed = feedparser.parse(url)
  return [entry.link for entry in parsed_feed.entries]
