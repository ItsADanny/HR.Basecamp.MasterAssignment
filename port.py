import sqlite3
from shipment import Shipment

class Port:

    def __init__(self, id: str, code: int, name: str, city: str, province: str, country: str) -> None:
        self.id = id
        self.code = code
        self.name = name
        self.city = city
        self.province = province
        self.country = country

    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__, ", ".join([f"{key}={value!s}" for key, value in self.__dict__.items()]))

    def get_shipments(self) -> tuple:
        # Create an empty tuple to which we will use to add all the shipment instances
        # Connect to the database
        db_conn = sqlite3.connect("shipments.db")
        # Prepare the select query
        query = "SELECT * FROM shipments WHERE origin = ? OR destination = ?"
        # Execute the query and get the cursor
        cur = db_conn.execute(query, [self.id, self.id])
        # Loop through the results and create Shipment instances with the data and
        for row in cur:
