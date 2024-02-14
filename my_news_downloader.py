from bs4 import BeautifulSoup
import requests
from newspaper import Article
import re

def download_article(url):
    try:
        response = requests.get(url)
        html_content = response.text
        
        article = Article(url)
        article.set_html(html_content)
        article.parse()
        
        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find the last paragraph element that contains the desired class
        last_paragraph = soup.find_all('section', {'class': 'sc-4e574cd-0 bhtqwj'})[-1]
          
        if last_paragraph:
            # Extract text from the article content
            last_paragraph_text = last_paragraph.get_text().strip()
            cleaned_text = re.sub(r'(?<=[a-zA-Z0-9])_(?=[a-zA-Z0-9])', '', last_paragraph_text)
            article_text = article.text.strip() + '\n' + cleaned_text.strip()

        return article_text
    
    except Exception as e:
        return f"Error occurred: {str(e)}"
    
# Function to read URLs from a text file and download the articles
def download_articles_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            urls = file.readlines()
            for index, url in enumerate(urls):
                url = url.strip()
                print(f"Downloading article from URL: {url}")
                # Download article content
                article_content = download_article(url)
                print("Article content:", article_content)  # Print article content for debugging
                # Write content to a file
                with open(f'article_{index+1}.txt', 'w') as article_file:
                    article_file.write(article_content)
                print(f"Article {index+1} saved to file.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")


if __name__ == "__main__":
    # Path to the text file containing URLs
    file_path = "urls.txt"
    # Download articles from URLs in the file
    download_articles_from_file(file_path)
