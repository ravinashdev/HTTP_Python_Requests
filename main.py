# ---------------------------- IMPORTS ------------------------------- #
# Allows you to read the .env file
from venv import create
from wsgiref import headers

from dotenv import load_dotenv
import os
import asyncio
import httpx
import json
import datetime as dt
# ---------------------------- CONSTANTS ------------------------------- #
load_dotenv()
PIXELA_CREATE_USER_POST_REQUEST_COMPONENTS = json.loads(os.getenv("PIXELA_CREATE_USER_POST_REQUEST_COMPONENTS"))
PIXELA_CREATE_GRAPH_POST_REQUEST_COMPONENTS = json.loads(os.getenv("PIXELA_CREATE_GRAPH_POST_REQUEST_COMPONENTS"))
PIXELA_MARK_GRAPH = json.loads(os.getenv("PIXELA_MARK_GRAPH"))
today = dt.date.today().strftime("%Y-%m-%d")
print(today)
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
async def delete_data(client, url, params, payload, headers):
    response = await client.delete(url=url, params=params, json=payload, headers=headers)
    print(f"Status Code: {response.status_code}")
    return response.json()
# MAIN Function
async def pixela_maker():
    async with httpx.AsyncClient() as client:
        create_user = await post_data(client, PIXELA_CREATE_USER_POST_REQUEST_COMPONENTS["url"], PIXELA_CREATE_USER_POST_REQUEST_COMPONENTS["params"], PIXELA_CREATE_USER_POST_REQUEST_COMPONENTS["payload"], PIXELA_CREATE_USER_POST_REQUEST_COMPONENTS["headers"])
        create_graph = await post_data(client, PIXELA_CREATE_GRAPH_POST_REQUEST_COMPONENTS["url"], PIXELA_CREATE_GRAPH_POST_REQUEST_COMPONENTS["params"], PIXELA_CREATE_GRAPH_POST_REQUEST_COMPONENTS["payload"], PIXELA_CREATE_GRAPH_POST_REQUEST_COMPONENTS["headers"])
        mark_graph = await post_data(client, PIXELA_MARK_GRAPH["url"], PIXELA_MARK_GRAPH["params"], PIXELA_MARK_GRAPH["payload"], PIXELA_MARK_GRAPH["headers"] )

# ---------------------------- UI SETUP ------------------------------- #
pixela_maker = asyncio.run(pixela_maker())