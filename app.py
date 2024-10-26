import streamlit as st
import requests
import google.generativeai as genai
from bs4 import BeautifulSoup
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def scrape_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text()
    except Exception as e:
        return str(e)

def parse_content(content, description):
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Parse the following content and create a table based on this description: {description}\n\nContent: {content}\n\nReturn the result as a markdown table."
    response = model.generate_content(prompt)
    return response.text

st.title('ScrapeAnything App')

url = st.text_input('Enter url')

if st.button('Start scraping'):
    if url:
        with st.spinner('Scraping...'):
            scraped_content = scrape_website(url)
        st.success('Scraping completed!')
        st.session_state['scraped_content'] = scraped_content
    else:
        st.error('Please enter a URL')

description = st.text_area('Describe what you want to scrape')

if st.button('Parse content'):
    if 'scraped_content' in st.session_state and description:
        with st.spinner('Parsing...'):
            parsed_content = parse_content(st.session_state['scraped_content'], description)
        st.subheader('Here is the parsed and organized content in table format')
        st.markdown(parsed_content)
    else:
        st.error('Please scrape a website and provide a description first')

if not os.getenv("GEMINI_API_KEY"):
    st.error("GEMINI_API_KEY not found in environment variables. Please check your .env file.")
