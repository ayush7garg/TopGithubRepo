# Importing the required libraries
import urllib.request
from bs4 import BeautifulSoup

def extract_top_n_repos(org_name,n):
    # generating the url for organization's github page
    org_url = "https://github.com/"+org_name+"?q=&type=source"
    url = org_url
    # dictionary for storing the repositories and the number of its forks
    repos = {}
    while True:
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        # scraping the list of organization's source repositories
        repo_list = soup.find('div',attrs={'class':'org-repos repo-list'}).find('ul').find_all('li')
        for repo in repo_list:
            #extracting the name and number of forks for each repo
            name = repo.find('a',attrs={'itemprop':'name codeRepository'}).get_text().strip()
            forks = repo.find('a',attrs={'href':'/'+org_name+'/'+name+'/network/members'})
            if forks is None:
                forks='0'
            else:
                forks = forks.get_text().strip()
            # addind the repo name and its forks to the dictionary 'repos'
            repos[name]=int(''.join(forks.split(',')))
        # check if there is next webpage for repositories as github only shows 30 repositories on one webpage
        next_page = soup.find('a',attrs={'class':'next_page'})
        if next_page is not None:
            url = next_page.get('href')
            url = "https://github.com/"+url
        else:
            break
    # sort the repositories based on the number of forks
    repos_sorted = sorted(repos.items(),key=lambda item:item[1],reverse=True)
    req_repos = repos_sorted[:n]
    return req_repos
