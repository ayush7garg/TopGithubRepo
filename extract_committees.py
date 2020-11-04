# Importing the required libraries
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# setting the webdriver as we are dealing with dynamic websites
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)
# repos is the list of top n repositories extracted
def extract_top_m_committees(repos,org_name,m):
    for repo in repos:
        # generating the url for the repo from its name and its organization's name
        url = "https://github.com/"+org_name+"/"+repo[0]+"/graphs/contributors"
        commits = []
        driver.get(url)
        # waiting for 2 seconds to ensure that the page is fully loaded
        time.sleep(2)
        # parsing the webpage
        page = driver.page_source
        soup = BeautifulSoup(page, 'html.parser')
        # scraping the list of all contributors
        user_list = soup.find_all('a',attrs={'class':'text-normal','data-hovercard-type':'user'})
        for user in user_list:
            # extracting the name of the contributor
            user_name = user.get_text().strip()
            # extracting the number of commits for the above contributor
            user_commits = soup.find('a',attrs={'href':'https://github.com/'+org_name+"/"+repo[0]+"/commits?author="+user_name})
            if user_commits is not None:
                user_commits = user_commits.get_text().strip()
                user_commits = user_commits.split(' ')[0]
                user_commits = int(''.join(user_commits.split(',')))
            else:
                user_commits = 0
            commits.append([user_name,user_commits])
        # sorting the list 'commits' based on the number of commits of each contributor
        commits = sorted(commits,key=lambda i:i[1],reverse=True)
        # picking the top m contributors
        commits = commits[:m]
        # printing out the details of each of the top m contributors
        for commit in commits:
            print('Org:',org_name,' Repo_name:',repo[0],' User:',commit[0],' Commits:',commit[1])
