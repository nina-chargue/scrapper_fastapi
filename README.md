# Website Content Extractor and Summarizer API

This project provides a web scraping and summarization API that allows users to extract specific information from websites. Users can input a URL along with a description of the content they are interested in, and the API will return a focused summary based on the provided description.

## Features
- Scrapes website content using **BeautifulSoup** to extract the body text.
- Cleans and processes HTML to extract only relevant content.
- Summarizes extracted content based on user-defined descriptions using **LLama model** via **LangChain** and **Ollama**.
- Fast, efficient API built with **FastAPI**.
- Asynchronous web requests handled by **httpx** for speed and scalability.

## Technologies Used
- **Python**: Backend programming language.
- **FastAPI**: Framework for building the web API.
- **BeautifulSoup**: Library for HTML parsing and content extraction.
- **Ollama**: Language model (LLama-based) for text generation and summarization.
- **httpx**: Asynchronous HTTP client for fetching web content.
- **LangChain**: Tool for managing prompts and integrating language models.
- **Uvicorn**: ASGI server to run the FastAPI application.

## How It Works
1. Users provide a URL and a description of the information they want to extract.
2. The website content is fetched, cleaned, and chunked into smaller parts (if necessary).
3. The **LLama model** processes the chunks to generate a summary or extract the relevant information based on the user's description.
4. The API returns a concise summary focused on the description provided.

## API Endpoint
- **POST** `/extract-info/`: Extract and summarize content from a given website based on the user's description.

### Example Request:
```json
{
  "url": "https://gocartours.com/blog/brief-history-madrid/",
  "parse_description": "Provide a summary of the main historical events discussed in the blog."
}
