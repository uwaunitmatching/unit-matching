Requires BeautifulSoup Python Package ("pip install beautifulSoup" as root in BASH)

Scrapes world university rankings: Times, Shanghai and QS

1. The template for the scraping is derived from Mitchell's script for scraping the University List.
2. Credit goes to him for the initial scraping code.
3. Inherited by Matt, credit to Hidir for Times ranking which is the base for Shanghai
4. Modifications were done to make the script work with a single website.
5. Link up to the database is missing.
6. loadrankingstodb.py does not connect to a database correctly.
7. scrape_txt.py works differently to Times and Shanghai
	7.1. It reads a text file which is given to the code through command line
	7.2. This text file should be the information from the QS ranking website (ctrl-A, ctrl-C, ctrl-V into a text file)
	7.3. Does not currently work with the other two rankings as planned