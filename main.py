from extract_repo import extract_top_n_repos
from extract_committees import extract_top_m_committees
import sys

if __name__=='__main__':
    org_name = sys.argv[1]
    n = int(sys.argv[2])
    m = int(sys.argv[3])
    repos = extract_top_n_repos(org_name,n)
    extract_top_m_committees(repos,org_name,m)
