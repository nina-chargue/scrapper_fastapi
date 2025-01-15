# Website Content Extractor and Summarizer API

This project provides a web scraping and summarization API that extracts and summarizes content from websites. Users can input a URL, and the API will return a concise summary of the website's content, without needing to specify what to extract.

## Features
- Scrapes website content using **BeautifulSoup** to extract the body text.
- Cleans and processes HTML to extract only the relevant content.
- Summarizes extracted content using **OpenAI's GPT model** (currently using **GPT-3.5-turbo**).
- Fast, efficient API built with **FastAPI**.
- Asynchronous web requests handled by **httpx** for speed and scalability.

## Technologies Used
- **Python**: Backend programming language.
- **FastAPI**: Framework for building the web API.
- **BeautifulSoup**: Library for HTML parsing and content extraction.
- **OpenAI GPT**: Language model for text generation and summarization.
- **httpx**: Asynchronous HTTP client for fetching web content.
- **Uvicorn**: ASGI server to run the FastAPI application.

## How It Works
1. **User Input**: Users provide a URL of the website they wish to summarize.
2. **Web Scraping**: The website content is fetched using `httpx` and parsed using **BeautifulSoup**.
3. **Content Cleaning**: The raw HTML content is cleaned to remove any unnecessary elements, retaining only the main body of text.
4. **Summarization**: The cleaned text is sent to **GPT-3.5-turbo** for summarization. The model processes the entire website content and generates a concise summary.
5. **Return Response**: The API returns the summary of the website's content.

### New Features:
- No need for users to provide a specific description of the content. The API will automatically summarize the entire website based on the content it retrieves.
- The response is a general summary of the website, making it more user-friendly and easier to use.

## API Endpoint
- **POST** `/extract-info/`: Extract and summarize content from a given website.

### Request Example:
The request now only requires a URL of the website to summarize:

```json
{
  "url": "https://gocartours.com/blog/brief-history-madrid/"
}
