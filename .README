# Setting Up in your Environment
Create a local .venv and .env file to install project dependencies
- Install the following to the local virtual environment:
        - Flask
        - ebaysdk
        - python-dotenv
        - gunicorn (Optional)
- Create a local .env file to define the `PORT` that you will run that application on.
# Contract
## GET /search?card_name
Returns top ten card listings from eBay based on list price.
- Query Params
card_name (required), string
For more information on forming argument view documenation on
https://developer.ebay.com/api-docs/user-guides/static/finding-user-guide/finding-searching-by-keywords.html
- Code: 200
```
{
    code: 200,
    content: [
        "id": int,
        "listingType": string,
        "listingURL": string,
        "price": float,
        "title": string,
        "listingDetails": array[
            object{bidCount: int}(optional),
            object{watchCount: int}(optional),
            object{butItNowPrice: float}(optional)
        ]
    ]
```
- Error responses:
    - Code: 404
    - Content: `{"Error": "Card not found"}
