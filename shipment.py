from datetime import date
from vessel import Vessel
from port import Port
from shipmentapp import db_get_portinfo, db_get_vesselinfo

class Shipment:

    def __init__(self, id: str, date: date, cargo_weight: int, distance_naut: float, duration_hours: float, average_speed: float, origin: str, destination: str, vessel: int) -> None:
        self.id = id
        self.date = date
        self.cargo_weight = cargo_weight
        self.distance_naut = distance_naut
        self.duration_hours = duration_hours
        self.average_speed = average_speed
        self.origin = origin
        self.destination = destination
        self.vessel = vessel

    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__, ", ".join([f"{key}={value!s}" for key, value in self.__dict__.items()]))

    def get_ports(self) -> {str: Port, str: Port}:
        # Retrieve the ID of the Origin and Destination of the shipment
        id_origin = self.origin
        id_destination = self.destination

        # Get the information from the database about the origin port
        port_origin = db_get_portinfo()
        # Get the information from the database about the destination port
        port_destination = db_get_portinfo()

        # Return the results
        return {id_origin: port_origin, id_destination: port_destination}

    def get_vessel(self) -> Vessel:
        return db_get_vesselinfo(self.id)

    def calculate_fuel_costs(self, price_per_liter: float, vessel: Vessel) -> float:
        # TODO: Implement the required steps for this function
        pass

    def convert_speed(self, to_format: str) -> float:
        # TODO: Implement the required steps for this function
        pass

    def convert_distance(self, to_format: str) -> str:
        # TODO: Implement the required steps for this function
        pass
