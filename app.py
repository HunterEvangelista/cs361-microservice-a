from ebaysdk.finding import Connection as Finding
from flask import Flask, request, Response, jsonify
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()


@app.route("/search")
def handle_search():
    card = request.args.get("card_name")
    req = Finding(config_file="ebay.yaml")

    # keywords can be separated by a space
    # see here: https://developer.ebay.com/api-docs/user-guides/static/finding-user-guide/finding-searching-by-keywords.html
    response = req.execute(
        "findItemsAdvanced",
        {"keywords": card, "categoryId": "183454", "sortOrder": "CurrentPriceHighest"},
    )
    response_dict = response.dict()
    print(response_dict)
    if response_dict["searchResult"]["_count"] == "0":
        return Response(
            "{'error':'No card found'}", status=404, mimetype="application/json"
        )

    # process cards
    cards = response_dict["searchResult"]["item"]
    return_object = {
        "code": 200,
        "content": [],
    }

    count = 0
    for pc in cards:
        return_object["content"].append(
            {
                "id": pc["itemId"],
                "title": pc["title"],
                "price": pc["sellingStatus"]["convertedCurrentPrice"]["value"],
                "listingType": pc["listingInfo"]["listingType"],
                "listingURL": pc["viewItemURL"],
                "listingDetails": [],
            }
        )

        # handle watches
        if "watchCount" in pc["listingInfo"].keys():
            return_object["content"][-1]["listingDetails"].append(
                {"watchCount": pc["listingInfo"]["watchCount"]}
            )

        # handle if there are bids
        if "bidCount" in pc["sellingStatus"].keys():
            return_object["content"][-1]["listingDetails"].append(
                {"bidCount": pc["sellingStatus"]["bidCount"]}
            )

        # handle if there is a buy it now option
        if pc["listingInfo"]["buyItNowAvailable"] == "true":
            return_object["content"][-1]["listingDetails"].append(
                {"buyItNowPrice": pc["listingInfo"]["buyItNowPrice"]["value"]}
            )

        count += 1
        if count == 10:
            break

    return jsonify(return_object)


if __name__ == "__main__":
    app.run(port=os.getenv("PORT"), debug=False)
