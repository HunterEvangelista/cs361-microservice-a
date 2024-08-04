from os import error
from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError
from flask import Flask, request, Response


# need to establish the route and http server
# process json with request
# get format from member
#
# query param: card_name
# url /search
#
app = Flask(__name__)

counter = {}

@app.route("/search")
def handle_search():
    card = request.args.get("card_name")
    # need to get cards
    # need to constrain to top 10
    # need to determine which information to return
    # need to ensure they're pokemon cards
    # need to handle no results
    req = Finding(config_file="ebay.yaml")
    response = req.execute("findItemsAdvanced", {"keywords": card})
    resp = req.response.dict()
    if resp["searchResult"]["_count"] <= 0:
        return Response("{'a':'b'}", status=404, mimetype="application/json")
    cards = resp["searchResult"]["item"]
    for pc in cards:
        print(pc["title"])
        cat_id = pc["primaryCategory"]["categoryId"]
        if cat_id in counter:
            counter[cat_id] += 1
        else:
            counter[cat_id] = 1

    print(counter)
    return f"{cards}"
