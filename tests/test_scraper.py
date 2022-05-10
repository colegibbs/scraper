import pytest
from scraper import get_citations_needed_count
from scraper import GetError

def test_get_citations_needed_count():
  actual = get_citations_needed_count("https://en.wikipedia.org/wiki/Cryptography")
  expected = 3
  assert actual == expected

def test_get_citations_needed_count_GET_error():
  with pytest.raises(GetError):
    actual = get_citations_needed_count("this isnt a url")