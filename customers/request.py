CUSTOMERS = [
    {
      "email": "susanmichellewiens@gmail.com",
      "password": "kennels",
      "name": "susan wiens",
      "id": 1
    },
    {
      "email": "susanmichellewiens@gmail.com",
      "password": "kennels",
      "name": "kelly wiens",
      "id": 2
    },
    {
      "email": "susanmichellewiens@gmail.com",
      "password": "kennels",
      "name": "karla wiens",
      "id": 3
    },
    {
      "email": "susanmichellewiens@gmail.com",
      "password": "kennels",
      "name": "benjamin wiens",
      "id": 4
    }
]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None

    for customer in CUSTOMERS:
        
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer