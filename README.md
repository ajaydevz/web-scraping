# web-scraping

A Python script to scrape job listings from Infopark and filter them based on specified keywords. The filtered job details are saved to a text file.

Features:

- Extracts job titles, company names, job posting dates, and job links.
- Filters jobs based on specified keywords.
- Saves the filtered job information to a text file (jobs.txt).

Setup Instructions

1. Prerequisites

- Python 3.x installed.
- Required Python libraries: requests, beautifulsoup4, lxml.

2. Clone the Repository

3. Run the Script


How It Works!

1. Sends an HTTP GET request to the job listings page.
2. Parses the HTML response using BeautifulSoup.
3. Searches for job details in the HTML structure.
4. Filters jobs based on keywords defined in the key_word list.
5. Writes the filtered jobs to jobs.txt.
