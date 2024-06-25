import requests
from bs4 import BeautifulSoup

def fetch_webpages(urls):
    for url in urls:
        response = requests.get(url)
        yield response.text

def extract_paragraphs(pages):
    for page in pages:
        soup = BeautifulSoup(page,'html.parser')
        title = soup.title.string if soup.title else "No Title Found"
        paragraphs = soup.find_all('p')  
        content = "\n".join([p.get_text() for p in paragraphs])
        yield title, content

def save_to_file(filename , title_and_contents):
    with  open(filename , 'w', encoding='utf-8') as file :
        for title,content in title_and_contents:
            file.write(f"Title : {title}\n")
            file.write(f"Contents : \n{content}\n")
            file.write("\n" + "="*80 + "\n\n")


urls =['https://en.wikipedia.org/wiki/Oswald_(TV_series)']  
webpages =fetch_webpages(urls)
title_and_contents = extract_paragraphs(webpages)
save_to_file('saved_paragraph.txt',title_and_contents) 

print("Content extracted and saved to 'extracted_paragraphs.txt'")         