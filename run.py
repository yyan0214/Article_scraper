# Input: Text file containing URLs of articles to download
# Output: Text files containing downloaded article content
# SOLID Principle Used: Dependency Inversion Principle (DIP)
# Benefit: The run module depends on abstractions (ArticleDownloader and URLReader interfaces) rather than concrete implementations, allowing for flexibility and ease of testing.


from module_1.module1_functions import ArticleDownloader
from module_2.module2_functions import URLReader

if __name__ == "__main__":
    # Example usage: Download articles from URLs in a text file
    file_path = "raw_urls.txt"

    url_reader = URLReader()
    url_reader.download_articles_from_file(file_path)


