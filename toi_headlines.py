from urllib.request import urlopen
from bs4 import BeautifulSoup
final_news = []
code_box = urlopen('http://timesofindia.indiatimes.com/home/headlines').read()
soup = BeautifulSoup(code_box, 'html.parser')
top_headlines = soup.find_all("ul", { "class" : "content" }, limit=2)
#list_items = top_headlines.find_all("li")
#print(top_headlines)
"""lins = mydivs.find_all('a')"""
#children = top_headlines.findChildren()
for lines in top_headlines:
	ww  = lines.find_all("li")
	for lines in ww:
		print(lines.get_text())
		print("\n")
"""print(top_headlines)
for child in top_headlines.descendants:
	#line = child.get_text()
	print(child)
for news in top_headlines:
    line = news.get_text()
    #final_news.append(line)
    #final_news.append("NEXT")
    print(line)"""
    
#print(top_headlines)
