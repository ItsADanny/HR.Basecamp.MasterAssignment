import csv
import os
import sqlite3
import sys

from vessel import Vessel
from port import Port
from shipment import Shipment
from datetime import date


class Reporter:
    # How many vessels are there? -> int
    def total_amount_of_vessels(self) -> int:
        # Make a connection to the database
        db_conn = sqlite3.connect('shipments.db')

        # Prepare a query for execution
        query = "SELECT COUNT(*) FROM vessels"

        # Execute the query and fetch the results
        result = db_conn.execute(query).fetchone()[0]

        # Close the database connection
        db_conn.close()

        # Return the result
        return result

    # What is the longest shipment distance? -> Shipment
    def longest_shipment(self) -> Shipment:
        # Make a connection to the database
        db_conn = sqlite3.connect('shipments.db')

        # Prepare the query for execution
        query = "SELECT * FROM shipments WHERE distance_naut = (SELECT MAX(distance_naut) FROM shipments)"

        # Execute the query and fetch the result
        result = db_conn.execute(query).fetchone()

        # Split the results into their appropriate variable
        db_shipment_id = result[0]
        db_shipment_date = result[1]
        db_shipment_cargo_weight = result[2]
        db_shipment_distance_naut = result[3]
        db_shipment_duration_hours = result[4]
        db_shipment_average_speed = result[5]
        db_shipment_origin = result[6]
        db_shipment_destination = result[7]
        db_shipment_vessel = result[8]

        # Create a shipment instance
        shipment = Shipment(db_shipment_id, db_shipment_date, db_shipment_cargo_weight, db_shipment_distance_naut, db_shipment_duration_hours, db_shipment_average_speed, db_shipment_origin, db_shipment_destination, db_shipment_vessel)

        # Return the shipment instance
        return shipment

    # What is the longest and shortest vessel? -> tuple[Vessel, Vessel]
    def longest_and_shortest_vessels(self) -> tuple[Vessel, Vessel]:
        # Make a connection to the database
        db_conn = sqlite3.connect('shipments.db')

        # Prepare 2 queries for execution
        query_shortest_vessel = "SELECT * FROM vessels WHERE length = (SELECT MIN(length) FROM vessels)"
        query_longest_vessel = "SELECT * FROM vessels WHERE length = (SELECT MAX(length) FROM vessels)"

        # Execute both queries and fetch the results for both
        result_query_shortest_vessel = db_conn.execute(query_shortest_vessel).fetchone()
        result_query_longest_vessel = db_conn.execute(query_longest_vessel).fetchone()

        # Split the results into their appropriate variable (the shortest vessel)
        db_shortest_vessel_imo = result_query_shortest_vessel[0]
        db_shortest_vessel_mmsi = result_query_shortest_vessel[1]
        db_shortest_vessel_name = result_query_shortest_vessel[2]
        db_shortest_vessel_country = result_query_shortest_vessel[3]
        db_shortest_vessel_type = result_query_shortest_vessel[4]
        db_shortest_vessel_build = result_query_shortest_vessel[5]
        db_shortest_vessel_gross = result_query_shortest_vessel[6]
        db_shortest_vessel_netto = result_query_shortest_vessel[7]
        db_shortest_vessel_length = result_query_shortest_vessel[8]
        db_shortest_vessel_beam = result_query_shortest_vessel[9]

        # Create a Vessel instance for the shortest ship
        vessel_shortest = Vessel(db_shortest_vessel_imo, db_shortest_vessel_mmsi, db_shortest_vessel_name,
                                 db_shortest_vessel_country, db_shortest_vessel_type, db_shortest_vessel_build,
                                 db_shortest_vessel_gross, db_shortest_vessel_netto, db_shortest_vessel_length,
                                 db_shortest_vessel_beam)

        # Split the results into their appropriate variable (the longest vessel)
        db_longest_vessel_imo = result_query_longest_vessel[0]
        db_longest_vessel_mmsi = result_query_longest_vessel[1]
        db_longest_vessel_name = result_query_longest_vessel[2]
        db_longest_vessel_country = result_query_longest_vessel[3]
        db_longest_vessel_type = result_query_longest_vessel[4]
        db_longest_vessel_build = result_query_longest_vessel[5]
        db_longest_vessel_gross = result_query_longest_vessel[6]
        db_longest_vessel_netto = result_query_longest_vessel[7]
        db_longest_vessel_length = result_query_longest_vessel[8]
        db_longest_vessel_beam = result_query_longest_vessel[9]

        # Create a Vessel instance for the longest ship
        vessel_longest = Vessel(db_longest_vessel_imo, db_longest_vessel_mmsi, db_longest_vessel_name,
                                db_longest_vessel_country, db_longest_vessel_type, db_longest_vessel_build,
                                db_longest_vessel_gross, db_longest_vessel_netto, db_longest_vessel_length,
                                db_longest_vessel_beam)

        # Create a tuple that contains both instances
        tuple_results = (vessel_shortest, vessel_longest)

        # Close the database connection
        db_conn.close()

        # Return the results
        return tuple_results

    # What is the widest and smallest vessel? -> tuple[Vessel, Vessel]
    def widest_and_smallest_vessels(self) -> tuple[Vessel, Vessel]:
        # Make a connection to the database
        db_conn = sqlite3.connect('shipments.db')

        # Prepare 2 queries for execution
        query_smallest_vessel = "SELECT * FROM vessels WHERE beam = (SELECT MIN(beam) FROM vessels)"
        query_widest_vessel = "SELECT * FROM vessels WHERE beam = (SELECT MAX(beam) FROM vessels)"

        # Execute both queries and fetch the results for both
        result_query_smallest_vessel = db_conn.execute(query_smallest_vessel).fetchone()
        result_query_widest_vessel = db_conn.execute(query_widest_vessel).fetchone()

        # Split the results into their appropriate variable (the shortest vessel)
        db_smallest_vessel_imo = result_query_smallest_vessel[0]
        db_smallest_vessel_mmsi = result_query_smallest_vessel[1]
        db_smallest_vessel_name = result_query_smallest_vessel[2]
        db_smallest_vessel_country = result_query_smallest_vessel[3]
        db_smallest_vessel_type = result_query_smallest_vessel[4]
        db_smallest_vessel_build = result_query_smallest_vessel[5]
        db_smallest_vessel_gross = result_query_smallest_vessel[6]
        db_smallest_vessel_netto = result_query_smallest_vessel[7]
        db_smallest_vessel_length = result_query_smallest_vessel[8]
        db_smallest_vessel_beam = result_query_smallest_vessel[9]

        # Create a Vessel instance for the shortest ship
        vessel_smallest = Vessel(db_smallest_vessel_imo, db_smallest_vessel_mmsi, db_smallest_vessel_name,
                                 db_smallest_vessel_country, db_smallest_vessel_type, db_smallest_vessel_build,
                                 db_smallest_vessel_gross, db_smallest_vessel_netto, db_smallest_vessel_length,
                                 db_smallest_vessel_beam)

        # Split the results into their appropriate variable (the widest vessel)
        db_widest_vessel_imo = result_query_widest_vessel[0]
        db_widest_vessel_mmsi = result_query_widest_vessel[1]
        db_widest_vessel_name = result_query_widest_vessel[2]
        db_widest_vessel_country = result_query_widest_vessel[3]
        db_widest_vessel_type = result_query_widest_vessel[4]
        db_widest_vessel_build = result_query_widest_vessel[5]
        db_widest_vessel_gross = result_query_widest_vessel[6]
        db_widest_vessel_netto = result_query_widest_vessel[7]
        db_widest_vessel_length = result_query_widest_vessel[8]
        db_widest_vessel_beam = result_query_widest_vessel[9]

        # Create a Vessel instance for the longest ship
        vessel_widest = Vessel(db_widest_vessel_imo, db_widest_vessel_mmsi, db_widest_vessel_name,
                               db_widest_vessel_country, db_widest_vessel_type, db_widest_vessel_build,
                               db_widest_vessel_gross, db_widest_vessel_netto, db_widest_vessel_length,
                               db_widest_vessel_beam)

        # Create a tuple that contains both instances
        tuple_results = (vessel_smallest, vessel_widest)

        # Close the database connection
        db_conn.close()

        # Return the results
        return tuple_results

    # Which vessels have the most shipments -> tuple[Vessel, ...]
    def vessels_with_the_most_shipments(self) -> tuple[Vessel, ...]:
        raise NotImplemented()

    # Which ports have the most shipments -> tuple[Port, ...]
    def ports_with_most_shipments(self) -> tuple[Port, ...]:
        raise NotImplemented()

    # Which ports (origin) had the first shipment? -> tuple[Port, ...]:
    # Which ports (origin) had the first shipment of a specific vessel type?  -> tuple[Port, ...]:
    def ports_with_first_shipment(self, vessel_type: str = None) -> tuple[Port, ...]:
        raise NotImplemented()

    # Which ports (origin) had the latest shipment? -> tuple[Port, ...]:
    # Which ports (origin) had the latetst shipment of a specific vessel type? -> tuple[Port, ...]:
    def ports_with_latest_shipment(self, vessel_type: str = None) -> tuple[Port, ...]:
        raise NotImplemented()

    # Which vessels have docked port Z between period X and Y? -> tuple[Vessel, ...]
    # Based on given parameter `to_csv = True` should generate CSV file as  `Vessels docking Port Z between X and Y.csv`
    # example: `Vessels docking Port MZPOL between 2023-03-01 and 2023-06-01.csv`
    # date input always in format: YYYY-MM-DD
    # otherwise it should just return the value as tuple(Vessels, ...)
    # CSV example (this are also the headers):
    #   imo, mmsi, name, country, type, build, gross, netto, length, beam
    def vessels_that_docked_port_between(self, port: Port, start: date, end: date, to_csv: bool = False) \
            -> tuple[Vessel, ...]:
        raise NotImplemented()

    # Which ports are located in country X? ->tuple[Port, ...]
    # Based on given parameter `to_csv = True` should generate CSV file as  `Ports in country X.csv`
    # example: `Ports in country Norway.csv`
    # otherwise it should just return the value as tuple(Port, ...)
    # CSV example (this are also the headers):
    #   id, code, name, city, province, country
    def ports_in_country(self, country: str, to_csv: bool = False) -> tuple[Port, ...]:
        raise NotImplemented()

    # Which vessels are from country X? -> tuple[Vessel, ...]
    # Based on given parameter `to_csv = True` should generate CSV file as  `Vessels from country X.csv`
    # example: `Vessels from country GER.csv`
    # otherwise it should just return the value as tuple(Vessel, ...)
    # CSV example (this are also the headers):
    #   imo, mmsi, name, country, type, build, gross, netto, length, beam
    def vessels_from_country(self, country: str, to_csv: bool = False) -> tuple[Vessel, ...]:
        raise NotImplemented()
