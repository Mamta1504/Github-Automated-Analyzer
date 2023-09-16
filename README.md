# Mercor Challenge - Github Automated Analyzer

## Project Overview
The goal of this project is to create a Python-based tool that harnesses the capabilities of GPT and LangChain to analyze GitHub repositories. Its primary objective is to identify the most technically complex and challenging repository within a specified user's GitHub profile. The tool accepts a GitHub user's URL as input and conducts a comprehensive assessment of each repository, taking into account factors such as code structure, complexity, and other pertinent metrics.

## Prerequisites
Before using the tool, ensure that the following components are installed:

* Python 3.x
* Pip package manager

## How It Operates
1. **User Input:** The tool prompts the user to enter a GitHub user's URL.
2. **Fetching Repositories:**  It retrieves all repositories from the provided GitHub user's profile by utilizing the GitHub API.
3. **Assessing Complexity:** For each repository, the tool employs GPT and LangChain to evaluate its technical complexity and level of challenge.
4. **Identification of the Most Challenging:** Following the evaluation of all repositories, the tool selects the repository with the highest complexity score as the most technically challenging.
6. **Output:** The tool presents the name of the most challenging repository, along with a direct link to it on GitHub.
## Installation
To get started, clone this repository to your local machine. Afterward, install the necessary dependencies by executing the following command:<br/>
Install the required dependencies by running the following command:
'
```
pip install -r requirements.txt
```

## Dependencies
The tool relies on several key dependencies, including:


* Python 3.9 
* Streamlit
* PyGitHub
* GPT (OpenAI GPT-3 or later version)
* LangChain

### Usage
Run the application using the following command:
```
streamlit run app.py
```
Within the web interface, input the GitHub user's profile URL and click "Enter." The tool will process the information and display the most technically challenging repository from the user's profile.

Sample link - "https://github.com/{username}"