# ---------------------------- IMPORTS ------------------------------- #
# Allows you to read the .env file
from wsgiref import headers

from dotenv import load_dotenv
import os
import asyncio
import httpx
# ---------------------------- CONSTANTS ------------------------------- #
# load_dotenv()
# ---------------------------- GLOBAL VARIABLES ------------------------------- #

# ---------------------------- FUNCTIONS ------------------------------- #
# GET Request
async def get_data(client, url, params, payload, headers):
    # 'params' works exactly like the standard requests library
    response = await client.get(url=url, params=params, json=payload, headers=headers)
    print(f"Status Code: {response.status_code}")
    return response.json()
# POST Request
async def post_data(client, url, params, payload, headers):
    response = await client.post(url=url, params=params, json=payload, headers=headers)
    print(f"Status Code: {response.status_code}")
    return response.json()
# PUT Request
async def put_data(client, url, params, payload, headers):
    response = await client.put(url=url, params=params, json=payload, headers=headers)
    print(f"Status Code: {response.status_code}")
    return response.json()
# POST Request
async def delete_data(client, url, params, payload, header):
    response = await client.delete(url=url, params=params, json=payload, headers=headers)
    print(f"Status Code: {response.status_code}")
    return response.json()
# MAIN Function
async def main():
    urls_with_params_payload_headers = [
        (url, params, payload, headers),
        (url, params, payload, headers)
    ]
    async with httpx.AsyncClient() as client:
        tasks = [get_data(client, url, params, json, headers) for url, params, json, headers in urls_with_params_payload_headers ]
        # Execute all calls concurrently
        try:
            results = await asyncio.gather(*tasks)
        except Exception as e:
            print(e)
        return results
# ---------------------------- UI SETUP ------------------------------- #
