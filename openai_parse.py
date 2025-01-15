import asyncio
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

template = (
    "You are tasked with summarizing the following text content: {dom_content}. "
    "Please provide a concise summary that captures the most important points. "
    "Do not include any additional information, comments, or explanations. "
    "Your summary should focus on the key points and should not include irrelevant details."
)

async def get_chatgpt_response(dom_content):
    prompt = template.format(dom_content=dom_content)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Using GPT-3.5
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )

    summary = response['choices'][0]['message']['content'].strip()

    return summary

async def summarize_with_chatgpt(dom_chunks):
    summaries = []

    tasks = []
    for chunk in dom_chunks:
        tasks.append(get_chatgpt_response(chunk))

    summaries = await asyncio.gather(*tasks)

    return "\n".join(summaries)
