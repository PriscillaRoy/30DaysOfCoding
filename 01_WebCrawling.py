import bs4
import requests



res = requests.get('https://learncodeonline.in/')

print(type(res))
# print(res.text)
soup = bs4.BeautifulSoup(res.text, 'lxml')

# all the html tags are available in select

# title = soup.select('title')
# print(title)

# print(title[0].getText())

# for i in soup.select('.mw-headline'):
#     print(i.text)
#
# for i in soup.select('#toc'):
#     print(i.text)
#
# for i in soup.select('.toctext'):
#     print(i.text)

for link in soup.find_all('a', href = True):
    if link['href'] is '#':
        continue
    
    else:
        print(link['href'])