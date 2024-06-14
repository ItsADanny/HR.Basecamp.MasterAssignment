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
        shipment = Shipment(db_shipment_id, db_shipment_date, db_shipment_cargo_weight, db_shipment_distance_naut,
                            db_shipment_duration_hours, db_shipment_average_speed, db_shipment_origin,
                            db_shipment_destination, db_shipment_vessel)

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
        tuple_results = (vessel_longest, vessel_shortest)

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
        tuple_results = (vessel_widest, vessel_smallest)

        # Close the database connection
        db_conn.close()

        # Return the results
        return tuple_results

    # Which vessels have the most shipments -> tuple[Vessel, ...]
    def vessels_with_the_most_shipments(self) -> tuple[Vessel, ...]:
        # Create an empty dict in which we will count the number of shipments for a certain vessel
        dict_vessel_stats = dict()

        # Create an empty list in which we will store the results that will be turned into a tuple
        list_results = list()

        # Connect to the database
        db_conn = sqlite3.connect('shipments.db')

        # Prepare a query for getting the vessel for all the shipments from the database
        shipments_query = "SELECT vessel FROM shipments"

        # Execute the query and get the results
        results_shipments_query = db_conn.execute(shipments_query)

        # Iterate through all the results and check if the vessel already exists in the dict.
        # If it does, then add 1 to the vessels counter
        # Else create it and start it at 1
        for vessel in results_shipments_query:
            if vessel[0] not in dict_vessel_stats:
                dict_vessel_stats[vessel[0]] = 1
            else:
                dict_vessel_stats[vessel[0]] += 1

        # After we made our dict with the number, we are going to organize them according to which ship
        # has the highest number of shipments
        organized_dict_vessel_stats = dict(sorted(dict_vessel_stats.items(), key=lambda x: x[1]))

        # Now we prepare a query for getting all the information of the vessel from our database
        vessel_query = "SELECT * FROM vessels WHERE imo = ?"

        # Now we iterate through our dict and get the information of the vessel
        for vessel in organized_dict_vessel_stats.items:
            # Execute the query and get the results
            vessel_result = db_conn.execute(vessel_query, [vessel]).fetchone()

            # Retrieve all the results from our query and put them in the associated variables
            imo_vessel_db = vessel_result[0]
            mmsi_vessel_db = vessel_result[1]
            name_vessel_db = vessel_result[2]
            country_vessel_db = vessel_result[3]
            type_vessel_db = vessel_result[4]
            build_vessel_db = vessel_result[5]
            gross_vessel_db = vessel_result[6]
            netto_vessel_db = vessel_result[7]
            length_vessel_db = vessel_result[8]
            beam_vessel_db = vessel_result[9]

            # Create a Vessel class instance with the just retrieved information
            vessel = Vessel(imo_vessel_db, mmsi_vessel_db, name_vessel_db, country_vessel_db, type_vessel_db,
                            build_vessel_db, gross_vessel_db, netto_vessel_db, length_vessel_db, beam_vessel_db)

            # Append the instance to our results' list
            list_results.append(vessel)

        # Close the connection to the database
        db_conn.close()

        # Turn the list into a tuple
        tuple_results = tuple(list_results)

        # Return the tuple
        return tuple_results

    # Which ports have the most shipments -> tuple[Port, ...]
    def ports_with_most_shipments(self) -> tuple[Port, ...]:
        # Create an empty dict in which we will count the number of shipments for a certain port
        dict_port_stats = dict()

        # Create an empty list in which we will store the results that will be turned into a tuple
        list_results = list()

        # Connect to the database
        db_conn = sqlite3.connect('shipments.db')

        # Prepare a query for getting the origin for all the shipments from the database
        origin_query = "SELECT origin FROM shipments"

        # Execute the query and get the results
        results_origin_query = db_conn.execute(origin_query)

        # Iterate through all the results and check if the vessel already exists in the dict.
        # If it does, then add 1 to the vessels counter
        # Else create it and start it at 1
        for port in results_origin_query:
            if port[0] not in dict_port_stats:
                dict_port_stats[port[0]] = 1
            else:
                dict_port_stats[port[0]] += 1

        # After we did the query for the origin, now we must do one for the destination

        # Prepare a query for getting the destination for all the shipments from the database
        destination_query = "SELECT destination FROM shipments"

        # Execute the query and get the results
        results_destination_query = db_conn.execute(destination_query)

        # Iterate through all the results and check if the vessel already exists in the dict.
        # If it does, then add 1 to the vessels counter
        # Else create it and start it at 1
        for port in results_destination_query:
            if port[0] not in dict_port_stats:
                dict_port_stats[port[0]] = 1
            else:
                dict_port_stats[port[0]] += 1

        # After we made our dict with the number, we are going to organize them according to which ship
        # has the highest number of shipments
        organized_dict_port_stats = dict(sorted(dict_port_stats.items(), key=lambda x: x[1]))

        # Now we prepare a query for getting all the information of the vessel from our database
        port_query = "SELECT * FROM ports WHERE id = ?"

        # Now we iterate through our dict and get the information of the vessel
        for port in organized_dict_port_stats.items:
            # Execute the query and get the results
            port_result = db_conn.execute(port_query, [port]).fetchone()

            # Retrieve all the results from our query and put them in the associated variables
            id_port_db = port_result[0]
            code_port_db = port_result[1]
            name_port_db = port_result[2]
            city_port_db = port_result[3]
            province_port_db = port_result[4]
            country_port_db = port_result[5]

            # Create a Vessel class instance with the just retrieved information
            port = Port(id_port_db, code_port_db, name_port_db, city_port_db, province_port_db, country_port_db)

            # Append the instance to our results' list
            list_results.append(port)

        # Close the connection to the database
        db_conn.close()

        # Turn the list into a tuple
        tuple_results = tuple(list_results)

        # Return the tuple
        return tuple_results

    # Which ports (origin) had the first shipment? -> tuple[Port, ...]:
    # Which ports (origin) had the first shipment of a specific vessel type?  -> tuple[Port, ...]:
    def ports_with_first_shipment(self, vessel_type: str = None) -> tuple[Port, ...]:
        # Predefine a list variable which we will later turn into a tuple
        list_results = list()

        # Make a connection to the database
        db_conn = sqlite3.connect('shipments.db')

        # Check to see if there is a vessel type given
        if vessel_type is None:
            # Prepare the query
            query = ("SELECT p.id, p.code, p.name, p.city, p.province, p.country FROM shipments s JOIN ports p ON "
                     "s.origin = p.id JOIN vessels v ON s.vessel = v.imo ORDER BY s.date LIMIT 1")
            # Execute the query and retrieve the results
            results_query = db_conn.execute(query)
        else:
            # Prepare the query
            query = ("SELECT p.id, p.code, p.name, p.city, p.province, p.country FROM shipments s JOIN ports p ON "
                     "s.origin = p.id JOIN vessels v ON s.vessel = v.imo WHERE v.type = ? ORDER BY s.date LIMIT 1")
            # Execute the query and retrieve the results
            results_query = db_conn.execute(query, [vessel_type])

        # Use the results to make Port class instances
        for port in results_query:
            # Get the data and put it in the associated variable
            id_port_db = port[0]
            code_port_db = port[1]
            name_port_db = port[2]
            city_port_db = port[3]
            province_port_db = port[4]
            country_port_db = port[5]

            # Create the instance
            port_instance = Port(id_port_db, code_port_db, name_port_db, city_port_db, province_port_db,
                                 country_port_db)

            # Add the instance to the list
            list_results.append(port_instance)

        # Close the connection to the database
        db_conn.close()

        # Return the results as a tuple
        return tuple(list_results)

    # Which ports (origin) had the latest shipment? -> tuple[Port, ...]:
    # Which ports (origin) had the latetst shipment of a specific vessel type? -> tuple[Port, ...]:
    def ports_with_latest_shipment(self, vessel_type: str = None) -> tuple[Port, ...]:
        # Predefine a list variable which we will later turn into a tuple
        list_results = list()

        # Make a connection to the database
        db_conn = sqlite3.connect('shipments.db')

        # Check to see if there is a vessel type given
        if vessel_type is None:
            # Prepare the query
            query = ("SELECT p.id, p.code, p.name, p.city, p.province, p.country FROM shipments s JOIN ports p ON "
                     "s.origin = p.id JOIN vessels v ON s.vessel = v.imo ORDER BY s.date DESC LIMIT 1")
            # Execute the query and retrieve the results
            results_query = db_conn.execute(query)
        else:
            # Prepare the query
            query = ("SELECT p.id, p.code, p.name, p.city, p.province, p.country FROM shipments s JOIN ports p ON "
                     "s.origin = p.id JOIN vessels v ON s.vessel = v.imo WHERE v.type = ? ORDER BY s.date DESC LIMIT 1")
            # Execute the query and retrieve the results
            results_query = db_conn.execute(query, [vessel_type])

        # Use the results to make Port class instances
        for port in results_query:
            # Get the data and put it in the associated variable
            id_port_db = port[0]
            code_port_db = port[1]
            name_port_db = port[2]
            city_port_db = port[3]
            province_port_db = port[4]
            country_port_db = port[5]

            # Create the instance
            port_instance = Port(id_port_db, code_port_db, name_port_db, city_port_db, province_port_db,
                                 country_port_db)

            # Add the instance to the list
            list_results.append(port_instance)

        # Close the connection to the database
        db_conn.close()

        # Return the results as a tuple
        return tuple(list_results)

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
