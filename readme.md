# Neo4j Sample Graph Creator

This Python script connects to a Neo4j database and creates a sample graph with nodes and relationships. It uses the `neo4j` Python driver and `dotenv` for environment variable management.

## Features

- Creates `Person` nodes with attributes like `name` and `age`.
- Creates `Product` nodes with attributes like `name` and `price`.
- Establishes `BOUGHT` relationships between `Person` and `Product` nodes.
- Cleans up existing nodes and relationships before creating the sample graph.

## Prerequisites

- Python 3.7 or higher
- A running Neo4j database instance
- Installed Python packages: `neo4j`, `python-dotenv`

## Installation

1. Clone this repository or copy the script to your local machine.
2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project directory with the following content:

   ```plain text
   NEO4J_URI=bolt://<your-neo4j-host>
   NEO4J_USERNAME=<your-username>
   NEO4J_PASSWORD=<your-password>
   NEO4J_DATABASE=<your-database-name>
   ```  

## Usage

1. Update the `.env` file with your Neo4j connection details.
2. Run the script:

   ```sh
   python main.py
   ```

3. The script will create a sample graph in your Neo4j database and print a success message.

## Sample Data

### Nodes

- Persons:
  - Alice (28 years old)
  - Bob (32 years old)
  - Carol (41 years old)
- Products:
  - Laptop ($1200)
  - Smartphone ($800)
  - Headphones ($150)
- Relationships
  - Alice bought a Laptop and Headphones.
  - Bob bought a Smartphone.
  - Carol bought Headphones.
