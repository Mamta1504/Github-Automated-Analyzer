import requests
import openai
import radon.metrics
import re
from github import Github

import os
from secret_key.api_key import OPENAI_SECRET_KEY
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Set the OpenAI API key in the environment variable.
os.environ["OPENAI_API_KEY"] = OPENAI_SECRET_KEY

def calculate_complexity_with_gpt(code):
    prompt = PromptTemplate(
        input_variables=['code'], 
        template="Calculate the complexity of the given code and return the complexity in a float value without any explanation.")
    langchain = OpenAI(temperature=0.8)
    chain = LLMChain(llm=langchain, prompt=prompt, verbose=True)
    return chain.run(code)


def fetch_github_repositories(github_url):
    # Initialize variables to store the most complex repository
    most_complex_repo = None
    most_complex_score = -1

    try:
        # Parse the username from the GitHub URL
        username = github_url.split('/')[-1]

        # Initialize the GitHub API client
        g = Github()

        # Get the user object
        user = g.get_user(username)

        # Fetch all repositories for the user
        repositories = user.get_repos()

        # Find the most complex repository based on your criteria (e.g., stars, forks, size, etc.)
        for repo in repositories:
            complex_score = repo.stargazers_count + repo.forks_count
            if complex_score > most_complex_score:
                most_complex_repo = repo
                most_complex_score = complex_score

        if most_complex_repo:
            return most_complex_repo.full_name, most_complex_repo.html_url
        else:
            return None, None

    except Exception as e:
        print("Error:", e)
        return None, None