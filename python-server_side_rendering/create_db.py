import sqlite3


def setup_db():
    connection = sqlite3.connect('products.db')
    cur = connection.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            category TEXT,
            price REAL
        )
    """)

    cur.execute("DELETE FROM Products")

    products = [
        (1, "Smartphone", "Electronics", 599.99),
        (2, "Desk Lamp", "Home Goods", 29.99),
        (3, "Backpack", "Accessories", 49.99),
        (4, "Water Bottle", "Sports", 12.50)
    ]

    cur.executemany(
        "INSERT INTO Products (id, name, category, price) VALUES (?, ?, ?, ?)",
        products
    )

    connection.commit()
    connection.close()


if __name__ == "__main__":
    setup_db()
