from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def get_json_products():
    with open('products.json') as file:
        return json.load(file)


def get_csv_products():
    data = []
    with open('products.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return data


def get_sql_products():
    try:
        connection = sqlite3.connect('products.db')
        connection.row_factory = sqlite3.Row
        cur = connection.cursor()

        cur.execute("SELECT id, name, category, price FROM Products")
        rows = cur.fetchall()

        connection.close()
        return [dict(r) for r in rows]

    except sqlite3.Error:
        return None


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
def list_items():
    with open('items.json') as file:
        content = json.load(file)

    return render_template('items.html', items=content.get("items", []))


@app.route('/products')
def list_products():
    src = request.args.get('source')
    pid = request.args.get('id')

    if src not in ["json", "csv", "sql"]:
        return render_template('product_display.html', error="Wrong source")

    if src == "json":
        products = get_json_products()
    elif src == "csv":
        products = get_csv_products()
    else:
        products = get_sql_products()
        if products is None:
            return render_template('product_display.html', error="Database error")

    if pid:
        try:
            pid = int(pid)
        except ValueError:
            return render_template('product_display.html', error="Product not found")

        products = [p for p in products if p["id"] == pid]

        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)


if __name__ == "__main__":
    app.run(debug=True)
