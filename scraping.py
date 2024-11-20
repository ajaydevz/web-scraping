import requests
from bs4 import BeautifulSoup


url = "https://infopark.in/companies/job-search"
response = requests.get(url, verify=False)
print(response.text)

key_word = ["python","Python"]
output_file = open("jobs.txt","w")

# create instance of BeautifulSoup
soup = BeautifulSoup(response.text, 'lxml')
jobs = soup.find_all("div",{"class":"row company-list joblist"})
# print(jobs)


for job in jobs:
    title_element = job.find("a")
    title = title_element.text
    link = title_element["href"]
    company_name = job.find("div",{"class":"jobs-comp-name"}).text
    job_date = job.find("div",{"class":"job-date"}).text
    # print(title,'>>>',company_name,'>>>',job_date)
    
    if any( word in title for word in key_word):
        # print(title,'--',company_name,'--',job_date)
        output_file.write(title+" "+company_name+" "+job_date+"\n"+link+"\n\n")




