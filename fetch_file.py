import os
from github import Github
from secret_key.api_key import OPENAI_SECRET_KEY  # Store API keys securely

# Set the OpenAI API key in the environment variable.
os.environ["OPENAI_API_KEY"] = OPENAI_SECRET_KEY

def fetch_github_repositories(github_url):
    """
    Fetches the most technically complex repository from a GitHub user's profile.

    Args:
        github_url (str): The URL of the GitHub user's profile.

    Returns:
        tuple: A tuple containing the name and URL of the most complex repository.
    """
    try:
        username = extract_username(github_url)
        repositories = get_user_repositories(username)
        
        if repositories:
            most_complex_repo = find_most_complex_repository(repositories)
            return most_complex_repo
        else:
            return None, None

    except Exception as e:
        print("Error:", e)
        return None, None

def extract_username(github_url):
    """
    Extracts the username from a GitHub URL.

    Args:
        github_url (str): The URL of the GitHub user's profile.

    Returns:
        str: The extracted username.
    """
    # Parse the username from the GitHub URL
    return github_url.split('/')[-1]

def get_user_repositories(username):
    """
    Gets the list of repositories for a GitHub user.

    Args:
        username (str): The GitHub username.

    Returns:
        list: A list of repository objects.
    """
    g = Github()
    user = g.get_user(username)
    return list(user.get_repos())

def calculate_complexity(repo):
    """
    Calculates the complexity of a repository based on custom criteria.

    Args:
        repo (Repository): A GitHub repository object.

    Returns:
        int: The calculated complexity score.
    """
    # Define a function to calculate the complexity of a repository (customize as needed)
    return repo.stargazers_count + repo.forks_count

def find_most_complex_repository(repositories):
    """
    Finds the most complex repository from a list of repositories.

    Args:
        repositories (list): A list of repository objects.

    Returns:
        tuple: A tuple containing the name and URL of the most complex repository.
    """
    most_complex_repo = None
    most_complex_score = -1

    for repo in repositories:
        complexity = calculate_complexity(repo)
        if complexity > most_complex_score:
            most_complex_score = complexity
            most_complex_repo = (repo.full_name, repo.html_url)

    return most_complex_repo

if __name__ == "__main__":
    github_url = "https://github.com/username"  # Replace with the GitHub URL you want to analyze
    most_complex_repository = fetch_github_repositories(github_url)

    if most_complex_repository:
        print(f"The most technically complex repository is '{most_complex_repository[0]}'")
        print(f"Here is the direct link to the repository: [{most_complex_repository[0]}]({most_complex_repository[1]})")
    else:
        print("Ohh!!! Some Error Encountered")
