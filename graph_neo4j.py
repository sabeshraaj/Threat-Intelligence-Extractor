# while using google colab just run the below commented line and then run the code
# !pip install neo4j
from neo4j import GraphDatabase

class Neo4jConnector:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def run_query(self, query, parameters=None):
        with self.driver.session() as session:
            return session.run(query, parameters)

neo4j = Neo4jConnector("neo4j_uri", "neo4j_username", "neo4j_password") # update your neo4j account credentials

def construct_query(parameters):
    query_parts = []

    # Create Threat Actors (modified to handle multiple actors)
    if "threat_actors" in parameters:
        query_parts.append("UNWIND $threat_actors AS actor_name MERGE (actor:ThreatActor {name: actor_name})")

    # Add IoCs (IP Addresses and Domains)
    if "IoCs" in parameters:
        if "ipv4s" in parameters["IoCs"]:
            query_parts.append("WITH actor UNWIND $IoCs.ipv4s AS ip MERGE (ioc:IPAddress {address: ip}) MERGE (actor)-[:ASSOCIATED_WITH]->(ioc)")

        if "domains" in parameters["IoCs"]:
            query_parts.append("WITH actor UNWIND $IoCs.domains AS domain MERGE (dom:Domain {name: domain}) MERGE (actor)-[:ASSOCIATED_WITH]->(dom)")

    # Add TTPs (Tactics and Techniques)
    if "ttps" in parameters:
        if "Tactics" in parameters["ttps"]:
            query_parts.append("WITH actor UNWIND $ttps.Tactics AS tactic_array UNWIND tactic_array AS tactic_name MERGE (t:Tactic {name: tactic_name}) MERGE (actor)-[:USES_TACTIC]->(t)")

        if "Techniques" in parameters["ttps"]:
            query_parts.append("WITH actor UNWIND $ttps.Techniques AS technique_array UNWIND technique_array AS technique_name MERGE (tech:Technique {name: technique_name}) MERGE (actor)-[:USES_TECHNIQUE]->(tech)")

    # Add Malware
    if "malware" in parameters:
        query_parts.append("WITH actor UNWIND $malware AS malware_data MERGE (m:Malware {name: malware_data.Name}) MERGE (actor)-[:DEPLOYS]->(m)")

    # Add Targeted Entities
    if "targeted_entities" in parameters:
        query_parts.append("WITH actor UNWIND $targeted_entities AS entity MERGE (target:TargetEntity {name: entity}) MERGE (actor)-[:TARGETS]->(target)")

    # Combine all parts into one query
    if query_parts:
        query = "\n".join(query_parts)
        return query
    else:
        raise ValueError("No valid parameters provided to construct query")

# Complete Parameters with all values -> change it with the parameters which you have extracted from your pdf's
Parameters = {}

query = construct_query(Parameters)
neo4j.run_query(query, Parameters)

# Debug: Print the constructed query
print("Constructed Query:\n", query)
