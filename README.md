Final resolved content

# Car Parts Finder API

## Overview

The **Car Parts Finder API** is a Flask-based RESTful API that allows users to manage and search for car parts. It supports CRUD operations (Create, Read, Update, Delete) and integrates with an SQLite database to store car parts data.

## Features

- Search for car parts by brand, model, or year.
- Add new car parts.
- Update existing car parts.
- Delete car parts.

---

## Installation

### Prerequisites

1. Python 3.8 or higher
2. pip (Python package manager)
3. SQLite (default database used)

### Setup Instructions

1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd car-parts-finder-api
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/MacOS
   .venv\Scripts\activate    # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Initialize the database:
   ```bash
   python db_setup.py
   ```
5. Run the application:
   ```bash
   python app.py
   ```
6. Open your browser and visit `http://127.0.0.1:5000`.

---

## Endpoints

### 1. **Home**

- **URL:** `/`
- **Method:** `GET`
- **Description:** Displays a welcome message.

#### Example Request

```bash
GET http://127.0.0.1:5000/
```

#### Example Response

```
Welcome to the Car Parts Finder API!
```

---

### 2. **Get Car Parts**

- **URL:** `/api/parts`
- **Method:** `GET`
- **Description:** Retrieve all car parts or filter by brand, model, or year.
- **Query Parameters:**
  - `brand` (optional)
  - `model` (optional)
  - `year` (optional)

#### Example Request

```bash
GET http://127.0.0.1:5000/api/parts?brand=Toyota&year=2022
```

#### Example Response

```json
[
  {
    "id": 1,
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2022,
    "part": "Brake Pads",
    "price": 50
  }
]
```

---

### 3. **Add a New Car Part**

- **URL:** `/api/parts`
- **Method:** `POST`
- **Description:** Add a new car part to the database.
- **Body:** JSON object with the following fields:
  - `brand` (required)
  - `model` (required)
  - `year` (required)
  - `part` (required)
  - `price` (required)

#### Example Request

```bash
POST http://127.0.0.1:5000/api/parts
Content-Type: application/json

{
    "brand": "Subaru",
    "model": "Impreza",
    "year": 2023,
    "part": "Turbocharger",
    "price": 300
}
```

#### Example Response

```json
{
  "message": "Part added successfully!"
}
```

---

### 4. **Update a Car Part**

- **URL:** `/api/parts/<int:part_id>`
- **Method:** `PUT`
- **Description:** Update an existing car part.
- **Body:** JSON object with the fields to update.

#### Example Request

```bash
PUT http://127.0.0.1:5000/api/parts/1
Content-Type: application/json

{
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2022,
    "part": "Updated Brake Pads",
    "price": 55
}
```

#### Example Response

```json
{
  "message": "Part updated successfully!"
}
```

---

### 5. **Delete a Car Part**

- **URL:** `/api/parts/<int:part_id>`
- **Method:** `DELETE`
- **Description:** Delete a car part by its ID.

#### Example Request

```bash
DELETE http://127.0.0.1:5000/api/parts/1
```

#### Example Response

```json
{
  "message": "Part deleted successfully!"
}
```

---

## Database Schema

The API uses an SQLite database with the following schema:

### **Table: parts**

| Column | Type    | Description                 |
| ------ | ------- | --------------------------- |
| id     | INTEGER | Primary key, auto-increment |
| brand  | TEXT    | Car brand                   |
| model  | TEXT    | Car model                   |
| year   | INTEGER | Manufacture year            |
| part   | TEXT    | Part name                   |
| price  | REAL    | Part price                  |

---

## Testing the API

Use **Postman** or **cURL** to test the endpoints. Refer to the examples provided in the **Endpoints** section.

---

## Future Improvements

1. Add user authentication for secure access.
2. Implement advanced search and sorting.
3. Deploy the API to a cloud service.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.





=======
# car-parts-finder-api
Final resolved content

