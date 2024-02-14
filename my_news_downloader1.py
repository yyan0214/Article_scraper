from urllib.request import urlopen, Request
import os
import re

# Specify the path to BeautifulSoup module
import sys
sys.path.append('/Users/py/miniconda3/envs/Project1/lib/python3.12/site-packages')

from bs4 import BeautifulSoup

# Function to download content from a given URL

def download_article(url):
    try:
        # Set user agent to avoid bot detection
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        # Open URL and read content
        with urlopen(req) as response:
            html = response.read()
        # Parse the HTML content of the page
        soup = BeautifulSoup(html, 'html.parser')
        # Find the main content of the article based on specific HTML elements
        article_content = soup.find_all('section', {'class': 'sc-4e574cd-0 bhtqwj'}) 
        if article_content:
            # Extract text from the article content
            article_text = '\n'.join(section.get_text(separator='\n') for section in article_content)
            # Remove underlines
            #cleaned_text = re.sub(r'(?<=[a-zA-Z0-9])_(?=[a-zA-Z0-9])', '', article_text)
            return article_text.strip()  # Strip leading/trailing whitespace
        else:
            return "No article content found."
    except Exception as e:
        return f"Error occurred: {str(e)}"
    
# Function to read URLs from a text file and download the articles
def download_articles_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            urls = file.readlines()
            for idx, url in enumerate(urls):
                url = url.strip()
                print(f"Downloading article from URL: {url}")
                # Download article content
                article_content = download_article(url)
                print("Article content:", article_content)  # Print article content for debugging
                # Write content to a file
                with open(f'article_{idx+1}.txt', 'w') as article_file:
                    article_file.write(article_content)
                print(f"Article {idx+1} saved to file.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")


if __name__ == "__main__":
    # Path to the text file containing URLs
    file_path = "urls.txt"
    # Download articles from URLs in the file
    download_articles_from_file(file_path)
