# Twitter-Sentiment-Analysis-Chatbot
Developed a real-time Twitter Sentiment Analysis Chatbot using NLP and ML to classify tweets as positive, negative, or neutral. Integrated advanced models for high accuracy, enabling businesses to monitor brand sentiment and make data-driven decisions. Used Python, APIs, Pandas, and data visualization tools.


User Manual: Twitter Sentiment Analysis Chatbot


1. Introduction

This document serves as a user manual for the Twitter Sentiment Analysis Chatbot project. The application is a web-based tool that uses a pre-trained machine learning model to predict the sentiment (positive or negative) of a given text, such as a tweet. The user interface is built using the Streamlit framework, providing an easy-to-use experience to analyze sentiment with a confidence score.

2. Features

Text Input: A text area to type or paste a tweet or any other text.
Sentiment Prediction: Analyzes the input text and classifies its sentiment as either "Positive" or "Negative."
Confidence Score: Displays a confidence percentage for the sentiment prediction, indicating how certain the model is about its classification.

3. Prerequisites

To run this project, you must have Python installed on your system. It is also recommended to use an Integrated Development Environment (IDE) like VS Code with the Python extension to manage your project files and use the integrated terminal.

4. Getting Started: Installation & Setup

The following steps will guide you through setting up and running the project in your local environment.
Open the Project Folder in VS Code: Launch VS Code and open the folder containing all the project files (main_nlp_file.py, sentiment_model.h5, tokenizer.pickle, etc.).
Open the Terminal: In VS Code, navigate to the top menu and select Terminal > New Terminal. This will open a command-line interface.
Install Required Libraries: In the terminal, run the following command to install all the necessary Python libraries:        Bash
                pip install streamlit tensorflow nltk 
Download NLTK Data: The application requires specific data from the NLTK library. Run the following commands in the terminal to download it: 
Bash  python -m nltk.downloader stopwords    python -m nltk.downloader wordnet   You only need to do this once.




5. How to Use the Application

Once the setup is complete, you can run the Streamlit application.
Launch the Application: In the VS Code terminal, execute the following command
                     Bash streamlit run main_nlp_file.py  
Access the Web App: After running the command, your default web browser will automatically open to a new page displaying the "Twitter Sentiment Analysis Chatbot." If it doesn't open automatically, you can copy and paste the provided local URL (e.g., http://localhost:8501) into your browser.
Enter Text: In the text box on the web page, type or paste the text you want to analyze.
Analyze Sentiment: Click the Analyze Sentiment button. The application will process the text and display the predicted sentiment and the confidence score directly below the button.
