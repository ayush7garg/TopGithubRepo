# Importing the required libraries
import urllib.request
from bs4 import BeautifulSoup

def extract_top_m_committees(repos,org_name,m):
    for repo in repos:
        url = "https://github.com/"+org_name+"/"+repo[0]+"/graphs/contributors"
        commits = []
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        print(soup)
        user_list = soup.find('div',attrs={'class':'clearfix js-graph graph-canvas'}).find('ol',attrs={'class':'contrib-data list-style-none'})#.find_all('li')
        print(user_list)
        # for user in user_list:
        #     user_name = user.find('a',attrs={'class':'text-normal','data-hovercard-type':'user'}).get_text().strip()
        #     user_commits = user.find('a',attrs={'href':'https://github.com/'+org_name+"/"+repo[0]+"/commits?author="+user_name}).get_text().strip()
        #     commits.append([user_name,user_commits])
        # commits = sorted(commits,key=lambda i:i[1],reverse=True)
        # commits = commits[:m]
        # for commit in commits:
        #     print('Org:',org_name,' Repo_name:',repo,' User:',commit[0],' Commits:',commit[1])
