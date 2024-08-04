from os import error
from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError
from flask import Flask, request, jsonify


# need to establish the route and http server
# process json with request
# get format from member
#
# query param: card_name
# url /search
#
app = Flask(__name__)


@app.route("/search")
def handle_search():
    card = request.args.get("card_name")
    # need to get cards
    # need to constrain to top 10
    # need to determine which information to return
    # need to ensure they're pokemon cards
    # need to handle no results
    req = Finding(config_file="ebay.yaml")
    res = req.execute("findItemsAdvanced", {"keywords": card})
    print(req.response.dict())
    return f"{req.response.dict()}"

    # try:
    # api = Finding(config_file="ebay.yaml")
    # response = api.execute("findItemsAdvanced", {"keywords": "Python"})
    # res_dict = response[0]
    # print(res_dict)
    # except ConnectionError as e:
    # print(e)
    # print(e.response.dict())
