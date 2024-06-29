# Web Scraping Anime Data

This project demonstrates web scraping techniques using BeautifulSoup for HTML parsing, OpenPyXL for writing to Excel, Pandas for data manipulation, and SQLite for data storage. HTTP requests were handled using the Requests library.

## Introduction

This project is a hands-on example of web scraping to collect anime ranking data from a website. The data is parsed and stored in an Excel file and a SQLite database. The project showcases how to handle HTTP requests, parse HTML content, and store data in different formats using Python libraries.

## Technologies Used

- **Python**: Programming language used.
- **BeautifulSoup**: For HTML parsing.
- **Requests**: For handling HTTP requests.
- **OpenPyXL**: For writing data to Excel files.
- **Pandas**: For data manipulation and uploading to SQLite.
- **SQLite**: For storing scraped data in a relational database.
- **DBeaver**: (Optional) For managing SQLite databases.

## Setup

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Fayash30/Web_Scraper.git
    cd Web_Scraper
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - **Windows**:
      ```sh
      .\venv\Scripts\activate
      ```
    - **macOS/Linux**:
      ```sh
      source venv/bin/activate
      ```

4. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

5. **Set up the environment variable**:
    - Create a `.env` file in the project root directory and add the URL:
      ```sh
      URL=https://www.animeexample.com/top-anime
      ```

## Usage

1. **Run the main script**:
    ```sh
    python main.py
    ```

2. **Database Interaction**:
    - Open and view the SQLite database using DBeaver or any other SQLite management tool.
    - The database file `test.db` will be created in the project directory.

## Project Details

### Web Scraping with BeautifulSoup

The script scrapes anime ranking data from the specified URL. It extracts the following details:
- Rank
- Title
- Episodes
- Score

### Data Storage

The extracted data is stored in two formats:
1. **Excel**: Using OpenPyXL to write data to `Anime.xlsx`.
2. **SQLite**: Using Pandas to upload data to `test.db`.

### HTTP Requests

Handled using the Requests library to fetch HTML content from the target website.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.
