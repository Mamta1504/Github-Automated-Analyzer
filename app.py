import streamlit as st
from fetch_file import fetch_github_repositories

# Function to handle user input
def user_input():
    """
    Display a title and text input field for the GitHub user's URL.
    
    Returns:
        str: The GitHub user's URL entered by the user.
    """
    st.title('Github Automated Analysis')
    github_user_url = st.text_input("Please Enter The GitHub User's URL")
    return github_user_url

# Function to display introductory information
def display_intro():
    """
    Display introductory information about the application.
    """
    # Display the large heading in one complete line
    st.markdown("<h1 style='text-align: center;'>🚀 Welcome to the GitHub Repository Analyzer! 🚀</h1>", unsafe_allow_html=True)
    
    # Add the rest of the project description written here
    st.write("Are you ready to explore the coding depths of GitHub's brightest minds?")
    st.write("Our Python-powered utility is your gateway to uncovering the most captivating, technically demanding repositories within any GitHub user's profile.")
    st.write("🔍 How does it work?")
    st.write("Just enter the GitHub user's URL in the provided textbox, hit that 'Enter' button, and let the magic begin! Our tool harnesses the power of GPT and LangChain to meticulously assess each repository, singling out the one that boasts the greatest technical prowess.")
    st.write("📊 What's in it for you?")
    st.write("Once the analysis is complete, we'll proudly present the crown jewel—the repository that stands as a testament to intricate coding artistry. It's not just about finding code; it's about discovering inspiration, learning, and connecting with the brilliant minds behind these projects.")
    st.write("🤝 Join the GitHub Community")
    st.write("Our tool isn't just about repositories; it's about building connections. Use it to strike up conversations, collaborate, and learn from the experts who create these exceptional repositories. The GitHub community is waiting for you to dive in and make your mark.")
    st.write("Ready to embark on a journey of technical discovery? Get started now and unlock the world of GitHub's most exceptional repositories!")


# Function to display the result
def display_result(github_user_url, most_complex_repository_name, most_complex_repository_link):
    """
    Display the result of the analysis.

    Args:
        github_user_url (str): The URL of the user's GitHub profile.
        most_complex_repository_name (str): The name of the most complex repository.
        most_complex_repository_link (str): The URL of the most complex repository.
    """
    if most_complex_repository_name and most_complex_repository_link:
        st.write(f"The most technically complex repository is **'{most_complex_repository_name}'**.")
        # Display "Link" as clickable text that redirects to the repository
        st.write(f"Here is the direct link to the repository: [Link]({most_complex_repository_link})")
    else:
        st.write("Ohh!!! Some Error Encountered")

# Main function
def main():
    """
    The main function that coordinates the application.
    """
    # Display introductory information
    display_intro()
    
    # Get user input
    github_user_url = user_input()

    if github_user_url:
        most_complex_repository_name, most_complex_repository_link = fetch_github_repositories(github_user_url)
        display_result(github_user_url, most_complex_repository_name, most_complex_repository_link)

if __name__ == "__main__":
    main()
