# ScrapeAnything App

ScrapeAnything is a Streamlit-based web application that allows users to scrape content from websites and parse it using the Gemini AI API. This app provides an easy-to-use interface for extracting and organizing information from web pages.

![Mockup of the app](/assets/mockup.png)

We are using [Cline](https://github.com/cline/cline) with Claude 3.5 Sonnet (previoulsy Claude-dev) to build this app in minutes. Here is the prompt:
```shell
Please create streamlit app based on the attached image to scrape information from inputed url, then parse the content using the Gemini AI API. Return the final result in the table format based on parse command input based on step 1. 
Use python, streamlit and gemini API to run this task
```

![Screenshot](/assets/Screenshot.png)


## Tech Stack

- Python 3.10+
- Streamlit
- BeautifulSoup4
- Requests
- Google Generative AI (Gemini API)
- python-dotenv

## Step-by-Step Guide

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```
   pip install streamlit requests beautifulsoup4 google-generativeai pandas python-dotenv
   ```

4. **Set up the environment variables:**
   Create a `.env` file in the project root and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

5. **Run the Streamlit app:**
   ```
   streamlit run app.py
   ```

6. **Use the app:**
   - Open your web browser and go to `http://localhost:8501`
   - Enter a URL in the "Enter url" field and click "Start scraping"
   - Describe what you want to extract from the scraped content
   - Click "Parse content" to see the results

## Limitations

- This app currently only works with static HTML content as it uses the `requests` library for fetching web pages. It may not work correctly with websites that rely heavily on JavaScript to render content.

## Enhancing the App for Dynamic Content

To scrape dynamic or JavaScript-based websites, you can enhance the app using libraries such as:

1. **Selenium**: A powerful tool for controlling web browsers through programs and automating web interactions.
   ```
   pip install selenium
   ```

2. **Playwright**: A newer alternative to Selenium, which supports multiple browsers and has a more modern API.
   ```
   pip install playwright
   ```

3. **Scrapy**: A comprehensive web scraping framework that can handle JavaScript rendering with additional middleware.
   ```
   pip install scrapy
   ```

4. **Puppeteer**: A Node.js library for controlling headless Chrome or Chromium, which can be used with Python through `pyppeteer`.
   ```
   pip install pyppeteer
   ```

5. **requests-html**: An extension of the requests library with JavaScript support.
   ```
   pip install requests-html
   ```

To implement these enhancements, you would need to modify the `scrape_website` function in `app.py` to use one of these libraries instead of `requests`. Each library has its own method for rendering JavaScript and capturing the resulting HTML content.

Remember that using these tools may require additional setup, such as installing browser drivers or configuring headless browser options.
