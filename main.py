from dotenv import load_dotenv
from neo4j import GraphDatabase, basic_auth  

import os

load_dotenv()

# Configure Auth Details
uri = os.getenv("NEO4J_URI")
username = os.getenv('NEO4J_USERNAME')
password = os.getenv('NEO4J_PASSWORD')
database = os.getenv("neo4j")

people = [  
    {"name": "Alice", "age": 28},  
    {"name": "Bob", "age": 32},  
    {"name": "Carol", "age": 41},  
]  

products = [  
    {"name": "Laptop", "price": 1200},  
    {"name": "Smartphone", "price": 800},  
    {"name": "Headphones", "price": 150},  
]  

purchases = [  
    ("Alice", "Laptop"),  
    ("Bob", "Smartphone"),  
    ("Carol", "Headphones"),  
    ("Alice", "Headphones"),  
]  

# to create the nodes and relationships  
def create_graph(tx):  

    tx.run("MATCH (n) DETACH DELETE n")  
    
    for person in people:  
        tx.run("MERGE (:Person {name: $name, age: $age})",  
               name=person["name"], age=person["age"])  
    
    for product in products:  
        tx.run("MERGE (:Product {name: $name, price: $price})",  
               name=product["name"], price=product["price"])  
    
    for person_name, product_name in purchases:  
        tx.run(  
            """  
            MATCH (person:Person {name: $person_name})  
            MATCH (product:Product {name: $product_name})  
            MERGE (person)-[:BOUGHT]->(product)  
            """,  
            person_name=person_name, product_name=product_name  
        )  

# Main function  
def main():  
    driver = GraphDatabase.driver(uri, auth=basic_auth(username, password), database=database)  
    with driver.session() as session:  
        session.execute_write(create_graph)  
    print("Sample graph has been successfully created.")  
    driver.close()  

if __name__ == "__main__":  
    main()  