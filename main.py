from sanic import Sanic
from sanic.response import json

app = Sanic()


@app.route("/api")
async def test(request):
    return json({"hello": "world"})
