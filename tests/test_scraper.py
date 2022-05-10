import pytest
from scraper import get_citations_needed_count, get_citations_needed_report
from scraper import GetError

def test_get_citations_needed_count():
  actual = get_citations_needed_count("https://en.wikipedia.org/wiki/Cryptography")
  expected = 3
  assert actual == expected

def test_get_citations_needed_count_GET_error():
  with pytest.raises(GetError):
    actual = get_citations_needed_count("this isnt a url")

def test_get_citations_needed_report():
  actual = get_citations_needed_report("https://en.wikipedia.org/wiki/Cryptography")
  expected = ['The Diffie–Hellman and RSA algorithms, in addition to being the first publicly known examples of high-quality public-key algorithms, have been among the most widely used. Other asymmetric-key algorithms include the Cramer–Shoup cryptosystem, ElGamal encryption, and various elliptic curve techniques.[citation needed]\n', 'Cryptography has long been of interest to intelligence gathering and law enforcement agencies.[8] Secret communications may be criminal or even treasonous[citation needed]. Because of its facilitation of privacy, and the diminution of privacy attendant on its prohibition, cryptography is also of considerable interest to civil rights supporters. Accordingly, there has been a history of controversial legal issues surrounding cryptography, especially since the advent of inexpensive computers has made widespread access to high-quality cryptography possible.\n', 'In 1996, thirty-nine countries signed the Wassenaar Arrangement, an arms control treaty that deals with the export of arms and "dual-use" technologies such as cryptography. The treaty stipulated that the use of cryptography with short key-lengths (56-bit for symmetric encryption, 512-bit for RSA) would no longer be export-controlled.[68] Cryptography exports from the US became less strictly regulated as a consequence of a major relaxation in 2000;[69] there are no longer very many restrictions on key sizes in US-exported mass-market software. Since this relaxation in US export restrictions, and because most personal computers connected to the Internet include US-sourced web browsers such as Firefox or Internet Explorer, almost every Internet user worldwide has potential access to quality cryptography via their browsers (e.g., via Transport Layer Security). The Mozilla Thunderbird and Microsoft Outlook E-mail client programs similarly can transmit and receive emails via TLS, and can send and receive email encrypted with S/MIME. Many Internet users don\'t realize that their basic application software contains such extensive cryptosystems. These browsers and email programs are so ubiquitous that even governments whose intent is to regulate civilian use of cryptography generally don\'t find it practical to do much to control distribution or use of cryptography of this quality, so even when such laws are in force, actual enforcement is often effectively impossible.[citation needed]\n']
  assert actual == expected
  
def test__get_citations_needed_report_inproper_link():
  with pytest.raises(GetError):
    get_citations_needed_report("this isn't a link")