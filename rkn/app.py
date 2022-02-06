import aiohttp
from fastapi import FastAPI
from starlette.responses import PlainTextResponse

app = FastAPI()
URL = "https://reestr.rublacklist.net/api/v2/ips/json/"


@app.get('/')
async def index():
    content = "Hello world"
    return PlainTextResponse(content=content)


@app.get('/rkn.rsc')
async def index():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as resp:
            print(resp.status)
            data = await resp.json()
            content = "/ip firewall address-list\n"
            for ip in data:
                if ":" not in ip:
                    content += f"add list=rkn address={ip} comment=RKN\n"
            return PlainTextResponse(content=content)
