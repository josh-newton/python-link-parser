#!/usr/bin/python
import mechanize
from BeautifulSoup import BeautifulSoup
import argparse

def printLinks(url):
	browser = mechanize.Browser()
	page = browser.open(url)
	html = page.read()
	
	try:
		soup = BeautifulSoup(html)
		links = soup.findAll(name='a')
		for link in links:
			if link.has_key('href'):
				print link['href']
	except:
		pass

def main():
	parser = argparse.ArgumentParser('%prog -u <target-url>')
	parser.add_argument('-u', dest='tgtUrl', help='specify target url')
	args = parser.parse_args()
	url = args.tgtUrl
	if url == None:
		print parser.usage
		exit(0)
	else:
		printLinks(url)

if __name__ == '__main__':
	main()