import requests
from bs4 import BeautifulSoup


# https://en.wikipedia.org/wiki/Cryptography
def get_citations_needed_count(url_string):
  try:
    page = requests.get(url_string)
    soup = BeautifulSoup(page.content, "html.parser")
    # all_a_tags = soup('a')
    citation_needed_list = soup(title="Wikipedia:Citation needed")
    num_needed_citations = len(citation_needed_list)
    return num_needed_citations
  except:
    raise GetError("Issue with GETing link")


class GetError(Exception):
  pass