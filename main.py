import os
import requests


def setup_auth_headers():
    token = os.environ.get('TOKEN')
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'Python',
        'Authorization': f"token {token}",
        'X-GitHub-Api-Version': '2022-11-28'
    }
    
    return headers

def main():
    job_id = os.environ.get('job_id')
    owner = os.environ.get('owner')
    repo = os.environ.get('repo')

    # Set up authentication headers
    headers = setup_auth_headers()
    
    url = f"https://api.github.com/repos/{owner}/{repo}/actions/jobs/{job_id}/logs"
    response = requests.get(url, headers=headers)
    print(response.text)

if __name__ == "__main__":
    main()
