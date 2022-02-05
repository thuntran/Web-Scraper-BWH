# Import necessary modules
from os import link
from urllib.request import Request, urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
from csv import writer


def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

print("Web Scraping Tool for Internships on indeed.com")
url = input("Please input your indeed.com link: ")
my_url  = Request(url)

#Opening up connection and grabbing the page
uClient = uReq(my_url)
#Save it to a vairable cause it's a simple html file to prevent crashing
page_html = uClient.read()
#close the website you scraped
uClient.close()
# Html passing
page_soup = soup(page_html, "html.parser")
# grabs each product. Even though this is for linkedin jobs, you can parse different parts of the website
containers = page_soup.findAll("a", {"class" : re.compile(r'job_')})


filename = "jobs.csv"
f = open(filename, "a")

for container in containers:
    title_container = container.findAll("h2", {"class":"jobTitle"})
    company_container = container.findAll("div", {"class":"heading6 company_location tapItem-gutter companyInfo"})
    link_container = container["href"]
    listt = [0]*3
    job_title = title_container[0].text
    if job_title[0:3] == "new":
        job_title = "New: " + job_title[3:]
    
    


    company_name = company_container[0].text

   
    link_url = f"http://indeed.com{link_container}"
    listt[0] = (job_title)
    listt[1]=(company_name)
    listt[2] = (link_url)
    append_list_as_row(filename, listt)


f.close()































# for link in page_soup.find_all('a', {"class":"tapItem fs-unmask result job_"}, href = True):
#     print('href: ', link['href'])
#     # display the actual urls
#     print(link.get('href'))
# print(containers)
# print(len(containers))

# <a id="job_0e690b44e989ceaf" data-mobtk="1fr3sk2bdt5b5800" data-jk="0e690b44e989ceaf" data-hiring-event="false" target="_blank" data-hide-spinner="true" rel="nofollow" 
# class="tapItem fs-unmask result resultWithShelf sponTapItem desktop vjs-highlight" href="/rc/clk?jk=0e690b44e989ceaf&amp;fccid=216eb700022de6f6&amp;vjs=3"><div class="slider_container"><div class="slider_list"><div class="slider_item"><div class="job_seen_beacon"><table class="jobCard_mainContent big6_visualChanges" cellpadding="0" cellspacing="0" role="presentation"><tbody><tr><td class="resultContent"><div class="heading4 color-text-primary singleLineTitle tapItem-gutter"><h2 class="jobTitle jobTitle-newJob"><div class="new topLeft holisticNewBlue desktop"><span class="label">new</span></div><span title="Software Engineer (Intern)">Software Engineer (Intern)</span></h2></div><div class="heading6 company_location tapItem-gutter companyInfo"><span class="companyName"><a data-tn-element="companyName" class="turnstileLink companyOverviewLink" target="_blank" href="/cmp/Hewlett-Packard-Enterprise?from=SERP&amp;campaignid=serp-linkcompanyname&amp;fromjk=0e690b44e989ceaf&amp;jcid=c95831c31635f73c" rel="noopener">Hewlett Packard Enterprise</a></span><span class="ratingsDisplay withRatingLink"><a data-tn-variant="cmplinktst2" class="ratingLink" target="_blank" href="/cmp/Hewlett-Packard-Enterprise/reviews" title="Hewlett Packard Enterprise reviews" aria-label="Company rating 3.8 out of 5 stars" rel="noopener"><span class="ratingNumber" aria-label="3.8 of stars rating" role="img"><span aria-hidden="true">3.8</span><svg width="12" height="12" role="presentation" class="starIcon" aria-hidden="true" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M8 12.8709L12.4542 15.5593C12.7807 15.7563 13.1835 15.4636 13.0968 15.0922L11.9148 10.0254L15.8505 6.61581C16.1388 6.36608 15.9847 5.89257 15.6047 5.86033L10.423 5.42072L8.39696 0.640342C8.24839 0.289808 7.7516 0.289808 7.60303 0.640341L5.57696 5.42072L0.395297 5.86033C0.015274 5.89257 -0.13882 6.36608 0.149443 6.61581L4.0852 10.0254L2.90318 15.0922C2.81653 15.4636 3.21932 15.7563 3.54584 15.5593L8 12.8709Z" fill="#767676"></path></svg></span></a></span><div class="companyLocation">Durham, NC<span class="more_loc_container"><a rel="nofollow" class="more_loc" href="/addlLoc/redirect?tk=1fr3sk2bdt5b5800&amp;jk=0e690b44e989ceaf&amp;dest=%2Fjobs%3Fq%3Dsoftware%2Bengineer%2Bintern%26l%3DUnited%2BStates%26grpKey%3D8gcGdG5mdGNsuA%252F7msIKqhAlCglub3JtdGl0bGUaGHNvZnR3YXJlIGVuZ2luZWVyIGludGVybg%253D%253D" aria-label="Same Software Engineer (Intern) job in 3 other locations">+3 locations</a></span></div></div><div class="heading6 tapItem-gutter metadataContainer noJEMChips salaryOnly"><div class="metadata estimated-salary-container"><span class="estimated-salary"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 16 13" role="presentation" aria-hidden="true" aria-label="Estimated $44.7K to $56.5K a year"><defs></defs><path fill="#595959" fill-rule="evenodd" d="M2.45168 6.10292c-.30177-.125-.62509-.18964-.95168-.1903V4.08678c.32693-.00053.6506-.06518.95267-.1903.30331-.12564.57891-.30979.81105-.54193.23215-.23215.4163-.50775.54194-.81106.12524-.30237.18989-.62638.19029-.95365H9.0902c0 .3283.06466.65339.1903.9567.12564.30331.30978.57891.54193.81106.23217.23215.50777.41629.81107.54193.3032.12558.6281.19024.9562.1903v1.83556c-.3242.00155-.6451.06616-.9448.19028-.3033.12563-.5789.30978-.81102.54193-.23215.23214-.4163.50774-.54193.81106-.12332.2977-.18789.61638-.19024.93849H3.99496c-.00071-.32645-.06535-.64961-.19029-.95124-.12564-.30332-.30979-.57891-.54193-.81106-.23215-.23215-.50775-.4163-.81106-.54193zM0 .589843C0 .313701.223858.0898438.5.0898438h12.0897c.2762 0 .5.2238572.5.5000002V9.40715c0 .27614-.2238.5-.5.5H.5c-.276143 0-.5-.22386-.5-.5V.589843zM6.54427 6.99849c1.10457 0 2-.89543 2-2s-.89543-2-2-2-2 .89543-2 2 .89543 2 2 2zm8.05523-2.69917v7.10958H2.75977c-.27615 0-.5.2238-.5.5v.5c0 .2761.22385.5.5.5H15.422c.4419 0 .6775-.2211.6775-.6629V4.29932c0-.27615-.2239-.5-.5-.5h-.5c-.2761 0-.5.22385-.5.5z" clip-rule="evenodd"></path></svg><span>Estimated $44.7K – $56.5K a year</span><button type="button" aria-label="About Indeed's estimated salaries" aria-haspopup="true" class="estimated-salary-legal-disclaimer-button"><img class="estimated-salary-legal-disclaimer-icon" src="https://c03.s3.indeed.com/mosaic-provider-jobcards/dist/images/src/components/JobMetaData/EstimatedSalary/QuestionCircle-7293f3.svg" alt="" aria-hidden="true"></button></span></div><div class="metadata"><div class="attribute_snippet"><svg width="14" height="13" viewBox="0 0 14 13" fill="none" role="presentation" xmlns="http://www.w3.org/2000/svg" aria-label="Job type" aria-hidden="true"><path fill="#595959" fill-rule="evenodd" d="M4.50226.5c-.27614 0-.5.223858-.5.5v2.1H.5c-.276142 0-.5.22386-.5.5v1.9h14V3.6c0-.27614-.2239-.5-.5-.5h-3.4977V1c0-.276142-.22389-.5-.50004-.5h-5Zm4.19962 2.6H5.30344V1.8h3.39844v1.3Z" clip-rule="evenodd"></path><path fill="#595959" d="M5.70117 6.80005H0v5.20005c0 .2761.223857.5.5.5h13c.2761 0 .5-.2239.5-.5V6.80005H8.30117v.80322c0 .27614-.22386.5-.5.5h-1.6c-.27614 0-.5-.22386-.5-.5v-.80322Z"></path></svg>Internship</div></div></div><div class="heading6 error-text tapItem-gutter"></div></td></tr></tbody></table><table class="jobCardShelfContainer big6_visualChanges" role="presentation"><tbody><tr class="jobCardShelf"></tr><tr class="underShelfFooter"><td><div class="heading6 tapItem-gutter result-footer"><div class="job-snippet"><ul style="list-style-type:circle;margin-top: 0px;margin-bottom: 0px;padding-left:20px;"> 
#  <li>University students enrolled in a Masters advanced degree program who are working in a technical or non-technical internship role at the company during their…</li>
# </ul></div><span class="date"><span class="visually-hidden">Posted</span>Today</span></div></td></tr></tbody></table><div aria-live="polite"></div></div></div><div class="slider_sub_item"></div></div></div><div class="kebabMenu"><button aria-label="Job Actions" aria-haspopup="true" aria-expanded="false" class="kebabMenu-button"><svg width="24" height="24" role="presentation" aria-hidden="true" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 7C13.1 7 14 6.1 14 5C14 3.9 13.1 3 12 3C10.9 3 10 3.9 10 5C10 6.1 10.9 7 12 7ZM12 10C10.9 10 10 10.9 10 12C10 13.1 10.9 14 12 14C13.1 14 14 13.1 14 12C14 10.9 13.1 10 12 10ZM12 17C10.9 17 10 17.9 10 19C10 20.1 10.9 21 12 21C13.1 21 14 20.1 14 19C14 17.9 13.1 17 12 17Z" fill="#2d2d2d"></path></svg></button></div></a>
# <h2 class="t-24 t-bold">2022 Intern - Software Development Engineer</h2>
# <div id="ember610" class="">
#           <a data-control-id="80bxjyf0CjFzqxftP/ZzCw==" tabindex="0" href="/jobs/view/2906712760/?eBP=JYMBII_JOBS_HOME_ORGANIC&amp;recommendedFlavor=SCHOOL_RECRUIT&amp;refId=sDnsupEP2rLM0n32RuZAHw%3D%3D&amp;trackingId=80bxjyf0CjFzqxftP%2FZzCw%3D%3D&amp;trk=flagship3_jobs_discovery_jymbii" id="ember611" class="disabled ember-view job-card-container__link job-card-list__title">
#             2022 Intern - Software Development Engineer
#           </a>
      
# </div>

# filename = "jobs.csv"
# f = open(filename, "w")
# # headers = "Role, Company Name, Skills, Link To Site\n"


# for container in containers:
# 	#Grabbing using their div tag the brand name, the title of the product and the specific na,e
# 	brand = container.img["title"]
# 	title_container = container.findAll("a", {"class":"item-title"})
# 	product_name = title_container[0].text
# 	# shipping container returned an empty array
# 	# shipping_container = container.findAll("li", {"class":"price-ship"})
# 	#shipping =  shipping_container[0].text.strip()
# 	print("brand: " + brand)
# 	# print("title_container: " + title_container)
# 	print("product_name: " + product_name)
#     # f.write()
# 	f.write(brand + "," +product_name.replace(",", "|")+ "\n")
# f.close()