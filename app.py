from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('parts.db')
    conn.row_factory = sqlite3.Row  # Access columns by name
    return conn


@app.route('/')
def home():
    return "Welcome to the Car Parts Finder API!"


# Get all parts or filter by query parameters
@app.route('/api/parts', methods=['GET'])
def get_parts():
    brand = request.args.get('brand')
    model = request.args.get('model')
    year = request.args.get('year')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM parts WHERE 1=1"
    params = []

    if brand:
        query += " AND brand = ?"
        params.append(brand)
    if model:
        query += " AND model = ?"
        params.append(model)
    if year:
        query += " AND year = ?"
        params.append(year)

    cursor.execute(query, params)
    rows = cursor.fetchall()
    parts = [dict(row) for row in rows]

    conn.close()
    return jsonify(parts)


# Add a new car part
@app.route('/api/parts', methods=['POST'])
def add_part():
    data = request.get_json()
    brand = data.get('brand')
    model = data.get('model')
    year = data.get('year')
    part = data.get('part')
    price = data.get('price')

    if not all([brand, model, year, part, price]):
        return jsonify({"error": "All fields are required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO parts (brand, model, year, part, price) VALUES (?, ?, ?, ?, ?)",
        (brand, model, year, part, price)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Part added successfully!"}), 201


# Update an existing car part
@app.route('/api/parts/<int:part_id>', methods=['PUT'])
def update_part(part_id):
    data = request.get_json()
    brand = data.get('brand')
    model = data.get('model')
    year = data.get('year')
    part = data.get('part')
    price = data.get('price')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE parts SET brand = ?, model = ?, year = ?, part = ?, price = ? WHERE id = ?",
        (brand, model, year, part, price, part_id)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Part updated successfully!"})


# Delete a car part
@app.route('/api/parts/<int:part_id>', methods=['DELETE'])
def delete_part(part_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM parts WHERE id = ?", (part_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Part deleted successfully!"})


if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
