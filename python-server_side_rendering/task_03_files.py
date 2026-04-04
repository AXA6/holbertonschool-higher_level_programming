from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json_products():
    try:
        with open("products.json", "r") as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv_products():
    products = []
    try:
        with open("products.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except (FileNotFoundError, KeyError, ValueError):
        return []
    return products


@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source == "json":
        products_list = read_json_products()
    elif source == "csv":
        products_list = read_csv_products()
    else:
        return render_template(
            "product_display.html",
            error="Wrong source",
            products=[]
        )

    if product_id is not None:
        try:
            product_id = int(product_id)
            filtered_products = [
                product for product in products_list
                if int(product["id"]) == product_id
            ]

            if not filtered_products:
                return render_template(
                    "product_display.html",
                    error="Product not found",
                    products=[]
                )

            products_list = filtered_products
        except ValueError:
            return render_template(
                "product_display.html",
                error="Product not found",
                products=[]
            )

    return render_template(
        "product_display.html",
        products=products_list,
        error=None
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
