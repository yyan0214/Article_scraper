# Article Downloader

The Article Downloader is a Python script designed to extract article content from various websites and save it to text files. It utilizes web scraping techniques with the BeautifulSoup library to parse HTML content and the Newspaper library to extract article text. This software is useful for individuals who want to save articles for offline reading or analysis.

## Features

- Extract article content from supported websites.
- Save the extracted article content to text files for offline use.
- Handle variations in HTML structure to ensure robust extraction.

## Supported Websites

The script currently supports downloading articles from the following websites:

- BBC


## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/article-downloader.git
    ```

2. Navigate to the project directory:

    ```bash
    cd article-downloader
    ```

3. Initialize the conda environment with the provided `requirements.yml` file:

    ```bash
    conda env create -f requirements.yml
    ```

4. Activate the conda environment:

    ```bash
    conda activate article-downloader
    ```

## Usage

1. Create a text file containing URLs of the articles you want to download. Each URL should be on a separate line.

2. Run the `main.py` script and provide the path to the text file containing URLs as an argument:

    ```bash
    python main.py urls.txt
    ```

3. The script will download the articles from the provided URLs and save them to text files in the current directory.

## Customization

You can customize the script to support additional websites or adjust the extraction logic as needed. Simply modify the code in `main.py` and the `download_article` function in `article_downloader.py`.

## Output

The script will generate a text file for each article downloaded. Each text file will contain the extracted article content along with metadata such as the article title and publication date.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

[Your Name](https://github.com/your_username)

---

Feel free to customize the README file further to include additional information or instructions specific to your project.
