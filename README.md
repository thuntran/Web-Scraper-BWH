# Web Scraper (for Black Wings Hack 2022)
***Our program is a web scraper tool that scrapes the users' prefered job posting from [indeed.com](https://www.indeed.com/).***

# Programs Functionality
We utilized the [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/) package to parse the HTML data from that site. Subsequently, we developed a Python program that manipulates the data in the html to return the job title, company name and link to the specific job posting.
These data are then moved to a CSV file of the users choosing.
Our program's process was eased by utilizing Git and GitHub to commit, push, and pull to merge our different codes.

Consequently, we've been able to ease the process of job-searching for college students by creating a working program that creates a CSV file of job postings and their attributes without the grueling process of searching from different pages on [indeed](https://www.indeed.com/).

# How to Run The Program
1. Download the latest version of Visual Studio Code depending on your device(***Mac/Linux/Windows***). The proper documentation and guide can be found here: https://code.visualstudio.com/download
3. Download Python for your device here: https://www.python.org/downloads/
4. Open your command line on Windows (terminal on Mac/Linux) by searching on your start page and type `python --version ` to ensure Python has been installed properly. If you run into errors, check the help guide at the end of this README for extra help.
4. Download the Python extension via VSCode which is found on the extensions menu of VSCode.
5. To ensure everything is installed properly, copy this code `print('hello world')` and press the run button or `Ctrl+Shift+B` to run the program.
6. Open your command line or terminal on your computer and type `pip install bs4`. BeautifulSoup is a Python package that allows for pulling data out of HTML and XML files.
7. On your command line or terminal, at your current working directory, copy the following text to clone the project `git clone https://github.com/thuntran/Web-Scraper-BWH.git`. A folder named `Web-Scraper-BWH` folder should be created at the current directory on your local computer.
9. Run the program with this folder and add an indeed HTML link to get any job posting you want.
10. Yayyy, congratulations! You now have a cool CSV file of great internships/jobs.
11. <strong>NOTE: You can only use an indeed.com link and no other as the program is set up for indeed only. </strong>
12. To understand the program better, here's a demo video:

# Installing packages for the Web Scraper program
1. Python installation guide: https://realpython.com/installing-python/ and https://docs.microsoft.com/en-us/visualstudio/python/installing-python-support-in-visual-studio?view=vs-2022
2. VSCode installation guide: https://code.visualstudio.com/docs/setup/setup-overview
3. BeautifulSoup installation guide: https://www.tutorialspoint.com/beautiful_soup/beautiful_soup_installation.htm
4. Any further errors: https://stackoverflow.com/ and of course YouTube videos :)

<strong>Proudly developed by Abi, Ella and Thu for Black Wings Hack 2022</strong>
