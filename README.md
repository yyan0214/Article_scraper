# Article Downloader

The Article Downloader is a Python script designed to extract article content from website and save it to text files. It utilizes web scraping techniques with the BeautifulSoup library to parse HTML content and the Newspaper library to extract article text. This software is useful for individuals who want to save articles for offline reading or analysis.

## Features

- Extract article content from supported websites.
- Save the extracted article content to text files for offline use.
- Handle variations in HTML structure to ensure robust extraction.

## Supported Websites

The script currently supports downloading articles from the following websites:

- BBC News


## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/article-downloader.git
    ```

2. Navigate to the project directory:

    ```bash
    cd project1
    ```

3. Initialize the conda environment with the provided `requirements.yml` file:

    ```bash
    conda env create -f requirements.yml
    ```

4. Activate the conda environment:

    ```bash
    conda activate project1
    ```

## Usage

1. Create a text file names urls.txt that containing URLs of the articles you want to download. Each URL should be on a separate line.

2. Make sure the my_news_downloader.py and urls.txt in same folder in your computer. Run the`my_news_downloader.py` like:

    ```bash
    python3 my_news_downloader.py
    ```

3. The script will download the articles from the provided URLs and save them to text files in the current directory.

## Customization

You can customize the script to support additional websites or adjust the extraction logic as needed. Simply modify the code in the `download_article` function in `my_news_downloader.py`.

## Output

The script will generate a text file for each article downloaded. Each text file will contain the extracted article content along with metadata such as the article title and author.

## Author

Yan Pang(https://github.com/yyan0214)

---

# Article_scraper
