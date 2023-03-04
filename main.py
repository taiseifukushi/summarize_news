import os
import openai
from scraping import list_news_text
from dotenv import load_dotenv
load_dotenv()
import pdb # pdb.set_trace()

# ==================================================
openai.api_key = os.getenv("OPENAI_API_KEY")
RSS_FEED_URL = "https://husita-h.github.io/rss_feed_builder/rss_feed.xml"

# ==================================================
# 取得したすべての記事の内容を要約する
def summarize(text_list):
  expanded_text = join_with_newline(text_list)
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"次の記事を要約してください。また記事の内容についての補足情報を加えてほしいです。:\n\n{expanded_text}",
    temperature=0.7,
    max_tokens=64,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )
  return response["choices"][0]["text"]

def join_with_newline(text_list):
  return "\n".join(text_list)

def list_text(rss_feed_url):
  return list_news_text(rss_feed_url)

def main(url):
  list = list_text(url)
  return summarize(list)

if __name__ == '__main__':
  main(RSS_FEED_URL)
