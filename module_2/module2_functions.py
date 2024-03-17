# Module2: URLReader
# Input: File path containing URLs of articles to download
# Output: Text files containing downloaded article content
# SOLID Principle Used: Single Responsibility Principle (SRP)
# Benefit: The ArticleDownloader class has a single responsibility of reading urls and extracting article content, making it easier to maintain and understand.

from module_1.module1_functions import ArticleDownloader


class URLReader:
    def __init__(self):
        pass

    def download_articles_from_file(self,file_path):
        try:
            with open(file_path, 'r') as file:
                urls = file.readlines()
                for index, url in enumerate(urls):
                    url = url.strip()
                    print(f"Downloading article from URL: {url}")
                    # Download article content
                    article_downloader = ArticleDownloader()
                    article_content = article_downloader.get_article(url)
                    #article_content = download_article(url)
                    print("Article content:", article_content)  # Print article content for debugging
                    # Write content to a file
                    with open(f'article_{index+1}.txt', 'w') as article_file:
                        article_file.write(article_content)
                    print(f"Article {index+1} saved to file.")
        except Exception as e:
            print(f"Error occurred: {str(e)}")
