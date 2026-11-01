from flask import jsonify

from app import app

PRODUCTS: list[dict] = []


@app.get("/products")
def products():
    return jsonify(PRODUCTS)
