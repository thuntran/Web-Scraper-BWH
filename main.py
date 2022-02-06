# Import necessary modules
from os import link
from urllib.request import Request, urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
from csv import writer

# Function to append the info of an internship to the end of 
# the CSV file
def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, "a+", newline="") as write_obj:
        # Create a writer object from CSV module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the CSV file
        csv_writer.writerow(list_of_elem)


# Ask user for input (link to indeed.com job posting)
print("Web Scraping Tool for Internships on indeed.com")
url = input("Please input your indeed.com link: ")
my_url  = Request(url)

# Openup connection and grab the page being parsed in
uClient = uReq(my_url)

# Save the page to a variable because it's a simple HTML file 
# to prevent crashing
page_html = uClient.read()

# Close the website that was scraped
uClient.close()

# Parse the HTML to create a BeautifulSoup object
page_soup = soup(page_html, "html.parser")

# Grab each job card on the job posting and put in a job_containers array
job_containers = page_soup.findAll("a", {"class" : re.compile(r'job_')})

# Open the CSV file
filename = "jobs.csv"
f = open(filename, "a") # Append to the end of the file,
                        # instead of overwriting

# Iterate through each job in the jobs container
for job_container in job_containers:
    # Get the title container 
    # For indeed.com, title can be accessed through the h2 tag with
    # the jobTitle class
    title_container = job_container.findAll("h2", {"class":"jobTitle"})

    # Get the company container 
    # For indeed.com, company name can be accessed through the div tag 
    # with a number of classes specified below
    # NOTE: Company name and location are tagged under the same div,
    # so this also returns the location of the job
    company_container = job_container.findAll("div", {"class":"heading6 company_location tapItem-gutter companyInfo"})
    # Get the link container via href
    link_container = job_container["href"]
    
    # Convert the job title into a string (text)
    job_title = title_container[0].text
    # If the job title starts with the substring "new",
    # rewrite that job title in a nicer format
    if job_title[0:3] == "new":
        job_title = "New: " + job_title[3:] 

    # Convert the company name into a string (text)
    company_name = company_container[0].text
    
    # Convert the link to the job posting into a string
    link_url = f"http://indeed.com{link_container}"

    # Create a posting in the CSV file with job title, company name ( + location),
    # and link to the job posting
    posting = [0] * 3 
    posting[0] = (job_title)
    posting[1]= (company_name)
    posting[2] = (link_url)

    # Append the job posting to the end of the CSV file
    append_list_as_row(filename, posting)
    print("Scraping Site Successful, Go to your excel sheet to view your new csv file!")

# Close the CSV file
f.close()