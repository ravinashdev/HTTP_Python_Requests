# ---------------------------- IMPORTS ------------------------------- #
# Allows you to read the .env file
from venv import create
from wsgiref import headers

from dotenv import load_dotenv
import os
import asyncio
import httpx
import json
# ---------------------------- CONSTANTS ------------------------------- #
load_dotenv()
PIXELA_CREATE_USER_POST_REQUEST_COMPONENTS = json.loads(os.getenv("PIXELA_CREATE_USER_POST_REQUEST_COMPONENTS"))
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
    async with httpx.AsyncClient() as client:
        create_user = post_data(client, PIXELA_CREATE_USER_POST_REQUEST_COMPONENTS["url"], PIXELA_CREATE_USER_POST_REQUEST_COMPONENTS["params"], PIXELA_CREATE_USER_POST_REQUEST_COMPONENTS["payload"], PIXELA_CREATE_USER_POST_REQUEST_COMPONENTS["headers"])

        # tasks = [create_user]
        # Execute all calls
        try:
            results = await asyncio.gather(*tasks)
        except Exception as e:
            print(e)
        return results
# ---------------------------- UI SETUP ------------------------------- #
create_user = asyncio.run(main())