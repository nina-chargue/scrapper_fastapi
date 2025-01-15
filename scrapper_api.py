from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
from scrapping_logic import extract_body_content, clean_body_content, split_dom_content
from openai_parse import summarize_with_chatgpt 

app = FastAPI()

class WebsiteRequest(BaseModel):
    url: str

class WebsiteTextInfo(BaseModel):
    body: List[str]

async def fetch_website_data(url: str) -> dict:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)

            if response.status_code != 200:
                raise HTTPException(status_code=404, detail="Website not found")
            
            body_content = extract_body_content(response.text)
            if body_content:
                body_content = clean_body_content(body_content)
                body_content = split_dom_content(body_content)
                data = {"body": body_content}
            else:
                data = {"body": ["No body content found"]}

            return data

    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@app.post("/extract-info/")
async def extract_info(request: WebsiteRequest):
    data = await fetch_website_data(request.url)

    parsed_data = await summarize_with_chatgpt(data['body'])
    
    return {"parsed_data": parsed_data}
