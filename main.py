# importing the modules created
from extract_repo import extract_top_n_repos
from extract_committees import extract_top_m_committees
import sys

if __name__=='__main__':
    # getting the values from command line arguments
    org_name = sys.argv[1]
    n = int(sys.argv[2])
    m = int(sys.argv[3])
    # calling the respective modules
    repos = extract_top_n_repos(org_name,n)
    extract_top_m_committees(repos,org_name,m)
