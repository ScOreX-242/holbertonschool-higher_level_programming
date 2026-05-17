from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def load_json_data():
    with open('products.json') as file:
        return json.load(file)


def load_csv_data():
    result = []
    with open('products.csv') as file:
        reader = csv.DictReader(file)
        for item in reader:
            result.append({
                "id": int(item["id"]),
                "name": item["name"],
                "category": item["category"],
                "price": float(item["price"])
            })
    return result


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/contact')
def contact_page():
    return render_template('contact.html')


@app.route('/items')
def show_items():
    with open('items.json') as file:
        content = json.load(file)

    items = content.get("items", [])
    return render_template('items.html', items=items)


@app.route('/products')
def show_products():
    source = request.args.get('source')
    pid = request.args.get('id')


    if source not in ["json", "csv"]:
        return render_template('product_display.html', error="Wrong source")

    products = load_json_data() if source == "json" else load_csv_data()

    if pid:
        try:
            pid = int(pid)
        except ValueError:
            return render_template('product_display.html', error="Product not found")

        products = list(filter(lambda p: p["id"] == pid, products))

        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)


if __name__ == "__main__":
    app.run(debug=True)
