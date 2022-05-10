import requests
from bs4 import BeautifulSoup

# https://en.wikipedia.org/wiki/Cryptography
def get_citations_needed_count(url_string):
  '''
  accepts a url in string format and outputs the number of html elements with the title: "Wikipedia:Citation needed" aka it returns the number of citations needed. 
  '''
  try:
    page = requests.get(url_string)
    soup = BeautifulSoup(page.content, "html.parser")
    citation_needed_list = soup(title="Wikipedia:Citation needed")
    num_needed_citations = len(citation_needed_list)
    return num_needed_citations
  except:
    raise GetError("Issue with GETing link")


def get_citations_needed_report(url_string):
  '''
  Takes a url string as an argument and returns a list of the paragraphs tags that contain an anchor tag that has a title of "Wikipedia:Citation needed"
  '''
  try:
    page = requests.get(url_string)
    soup = BeautifulSoup(page.content, "html.parser")
    citations_needed_list = soup(title="Wikipedia:Citation needed")

    p_tag_list = [a_tag.find_parent('p').text for a_tag in citations_needed_list]
    
    return p_tag_list
    
  except:
    raise GetError("Issue with GETing link")


class GetError(Exception):
  pass
