import requests
from bs4 import BeautifulSoup

url = "https://infopark.in/companies/job-search"

# Exception handling for the network request
try:
    response = requests.get(url, verify=False)
    response.raise_for_status()  # This will raise an HTTPError for bad responses (4xx, 5xx)
except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
    exit()  # Exit the script if the request fails

# Exception handling for file operations
try:
    with open("jobs.txt", "w") as output_file:  # Use 'with' to ensure file is closed after operation
        key_word = ["python", "Python"]
        
        # Create instance of BeautifulSoup
        soup = BeautifulSoup(response.text, 'lxml')
        jobs = soup.find_all("div", {"class": "row company-list joblist"})
        
        for job in jobs:
            title_element = job.find("a")
            title = title_element.text
            link = title_element["href"]
            company_name = job.find("div", {"class": "jobs-comp-name"}).text
            job_date = job.find("div", {"class": "job-date"}).text

            # Write filtered jobs to the file if title contains any of the keywords
            if any(word in title for word in key_word):
                output_file.write(f"{title} {company_name} {job_date}\n{link}\n\n")

except IOError as e:
    print(f"Error writing to file: {e}")
    exit()  # Exit if file operations fail

print("Job scraping complete. Results saved in 'jobs.txt'.")
