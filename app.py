import streamlit as st
from fetch_file import fetch_github_repositories


def user_input():
    st.title('Github Automated Analysis')
    url = st.text_input("Please Enter The GitHub User's URL")
    return url

def main():
    st.title("Welcome to the GitHub Repository Analyzer")   
    st.write("""This Python-based utility is designed with the purpose of assisting you in identifying the most technically intricate and demanding repository within a specified GitHub user's profile. Simply input the GitHub user's URL in the provided textbox and initiate the process by clicking "Enter".""")

    st.write("""Upon submitting the URL, our tool utilizes GPT and LangChain to individually evaluate each repository, ultimately pinpointing the one that poses the greatest technical challenge.""")
             
    st.write("""Once all repositories have been analyzed, the tool will conclusively determine and present the most technically demanding repository. This offers valuable insights into the user's most intricate and advanced projects.""")
             
    st.write("""We trust that this tool will aid you in discovering exceptional repositories and establishing connections with highly skilled developers in the GitHub community.""")

    st.write("Don't hesitate—get started now! Enjoy your exploration!")


    github_url = user_input()

    if github_url:
        most_complex_repository_name, most_complex_repository_link = fetch_github_repositories(github_url)

        if most_complex_repository_name and most_complex_repository_link:
            st.write(f"The most technically complex repository from user '{github_url}' is '{most_complex_repository_name}'.\n")
            st.write(f"Here is the direct link to the repository: [{most_complex_repository_name}]({most_complex_repository_link})")
        else:
            st.write("Ohh!!! Some Error Encountered")

if __name__ == "__main__":
    main()