import sqlite3
import json
from models import Customer

CUSTOMERS = [
    {
      "email": "susanmichellewiens@gmail.com",
      "password": "kennels",
      "name": "susan wiens",
      "id": 1,
      "status": "waiting"
    },
    {
      "email": "susanmichellewiens@gmail.com",
      "password": "kennels",
      "name": "kelly wiens",
      "id": 2,
      "status": "waiting"
    },
    {
      "email": "susanmichellewiens@gmail.com",
      "password": "kennels",
      "name": "karla wiens",
      "id": 3,
      "status": "waiting"
    },
    {
      "email": "susanmichellewiens@gmail.com",
      "password": "kennels",
      "name": "benjamin wiens",
      "id": 4,
      "status": "waiting"
    }
]

def get_all_customers():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.email,
            c.password,
            c.name
        FROM customer c
        """)

        # Initialize an empty list to hold all animal representations
        customer_list = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            customer = Customer(row['id'], row['email'], row['password'],
                            row['name'])

            customer_list.append(customer.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(customer_list)

def get_single_customer(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            c.id,
            c.email,
            c.password,
            c.name
        FROM customer c
        WHERE c.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        customer = Customer(data['id'],data['email'],data['password'],
                            data['name'])

        return json.dumps(customer.__dict__)

def create_customer(customer):
    # Get the id value of the last animal in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    customer["id"] = new_id

    # Add the animal dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer


def delete_customer(id):
    # Initial -1 value for animal index, in case one isn't found
    customer_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the animal. Store the current index.
            customer_index = index

    # If the animal was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the animal. Update the value.
            CUSTOMERS[index] = new_customer
            break