from sanic import Sanic
from sanic.response import json

app = Sanic()


@app.route("/api")
async def test(request):
    return json({"hello": "world"})

if __name__ == "__main__":
    # disable debug messages
    app.run(host='0.0.0.0', port=8000, workers=4,
            debug=False, access_log=False)
