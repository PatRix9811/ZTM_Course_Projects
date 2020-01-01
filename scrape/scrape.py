import requests
from bs4 import BeautifulSoup
from pprint import pprint


def create_custom_hn(links, subtext):
	hn = []
	for idx, item in enumerate(links):
		title = item.getText()
		href = item.get('href', None)
		vote = subtext[idx].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points', ''))
			if points > 99:
				hn.append({'title': title, 'link': href, 'votes': points})
	return hn


def get_pages():
	page = 1
	hn = []
	while True:
		res = requests.get(f'https://news.ycombinator.com/news',params =b'p=%d' % page)
		soup = BeautifulSoup(res.text, 'html.parser')
		links = soup.select('.storylink')
		subtext = soup.select('.subtext')
		custom_hn = create_custom_hn(links,subtext)  
		if custom_hn in hn or page > 2:
			return hn
		else:
			hn.extend(custom_hn)
			page += 1


def main():
	hn = get_pages()
	hn.sort(key= lambda a: a['votes'], reverse = True)
	
	for item in hn:
		print(f"""
--| {item['title']} |--
~ {item['link']}
Votes: {item['votes']}

			""")



if __name__ == '__main__':
	main()
