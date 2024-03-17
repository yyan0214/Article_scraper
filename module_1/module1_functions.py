# Module1: ArticleDownloader
# Input: single URL of the article to download
# Output: Extracted text content of the article to module2
# SOLID Principle Used: Single Responsibility Principle (SRP)
# Benefit: The ArticleDownloader class has a single responsibility of extracting article content, making it easier to maintain and understand.

from bs4 import BeautifulSoup
import requests
from newspaper import Article

class ArticleDownloader:
    def __init__(self):
        pass

    def get_article(self,url):
        try:
            response = requests.get(url)
            html_content = response.text
        
            article = Article(url)
            article.set_html(html_content)
            article.parse()
            article_text = article.text.strip()
            

            return article_text
    
        except Exception as e:
            return f"Error occurred: {str(e)}"
        