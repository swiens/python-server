EMPLOYEES = [
    {
      "id": 1,
      "name": "Jeremy Bakker",
      "locationId": 2
    },
    {
      "id": 2,
      "name": "Greg Bakker",
      "locationId": 2
    },
    {
      "id": 3,
      "name": "Carole Bakker",
      "locationId": 1
    },
    {
      "id": 4,
      "name": "Sarah Bakker",
      "locationId": 1
    },
    {
      "name": "Joshua Wiens",
      "locationId": 1,
      "animalId": 1,
      "id": 5
    }
]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
        
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee