from fastapi import FastAPI
from requests import get
from starlette.responses import PlainTextResponse

app = FastAPI()
URL = "https://reestr.rublacklist.net/api/v2/ips/json/"


@app.get('/')
async def index():
    content = "Hello world"
    return PlainTextResponse(content=content)


@app.get('/rkn.rsc')
async def index():
    response = get(URL)
    data = response.json()
    content = "/ip firewall address-list\n"
    for ip in data:
        content += f"add list=rkn address={ip} comment=RKN\n"
    return PlainTextResponse(content=content)
