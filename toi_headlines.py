from urllib.request import urlopen
from bs4 import BeautifulSoup
final_news = []
code_box = urlopen('http://timesofindia.indiatimes.com/home/headlines').read()
soup = BeautifulSoup(code_box, 'html.parser')
top_headlines = soup.find_all("ul", { "class" : "content" }, limit=2)
for lines in top_headlines:
	ww  = lines.find_all("li")
	for lines in ww:
		print(lines.get_text())
		print("\n")
