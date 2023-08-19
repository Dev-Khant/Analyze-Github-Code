# 🌟 GitHub Code Analysis Chrome Extension 🌟

The GitHub Code Analysis Chrome Extension is a powerful tool that allows users to easily retrieve GitHub repository URLs, analyze their code, and obtain detailed explanations for the code snippets. Powered by OpenAI's advanced language model, ChatGPT, and built on Python with a Flask backend server, this extension delivers comprehensive insights into code repositories.

It can be used for small or mid sized repository where it's hard to find proper documentation or have a Readme with less information.

### 🚨 It might take time because depends upon the OpenAI key token limit if there's an error then it will show it or else you will get the results. So sit tight and wait for results 🚨

## 🚀 Features:

- **GitHub Repo URL Retrieval :** Simply input the GitHub repository URL into the extension, and it will instantly fetch the code for analysis.

- **Code Analysis and Explanation :** The extension leverages ChatGPT's natural language processing capabilities to provide in-depth explanations for the code, making it easier for developers to understand complex logic and functionality.

- **Summarization of Explanations :** After analyzing code from different files, the extension seamlessly summarizes all explanations to give users a clear overview of the entire project.

## ⚙️ Installation and Usage:

1. `pip install -r requirements.txt`
2. Run: `python app.py`. This runs **Flask** server.
3. Install the Chrome extension by enabling developer mode and loading the unpacked extension.
4. For first time it will ask for OpenAI key so grab and paste your key.
5. Go to the desired Repository and press the button to get its summary. 

## 🧑‍💻 Technical Stuff:

- **Langchain** is used for interacting with LLMs.
- Using OpenAI's **gpt-3.5-turbo** as LLM.
- Used **pygithub** for traversing through github repo.
- **Flask** is used for backend server. Deployed on [pythonanywhere](https://www.pythonanywhere.com/) (thanks for free hosting for some time 😊)
