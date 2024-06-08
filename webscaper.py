import requests
from bs4 import BeautifulSoup 
#this is a lyb that helps to get http requests
URL="https://realpython.github.io/fake-jobs/"
page=requests.get(URL)
#print(page.text) getting the pages html in text format
soup=BeautifulSoup(page.content, "html.parser") #parsing html content and extracting the data i need
#print(soup)
results=soup.find(id="ResultsContainer")
#print(results.prettify())
job_elements=results.find_all("div", class_="card-content")
python_jobs = results.find_all("h2",string=lambda text:"python" in text.lower())
#print(python_jobs)
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]
for job_element in python_job_elements:
    #print(job_element, end="\n"*2)
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    links = job_element.find_all("a")
    for link in links:
        link_url=link["href"]
        print(f"Apply here:{link_url}\n")
    print(title_element.text.strip())#strip() helps to clean the text
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()