from flask import jsonify, request

from app import app

PRODUCTS: list[dict] = []


@app.get("/products")
def products():
    page = max(int(request.args.get("page", 1)), 1)
    return jsonify(PRODUCTS[(page - 1) * 20 : page * 20])
