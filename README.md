# Dataset Generator Project

## Overview

This project generates synthetic e-commerce data and saves it to a CSV file (ecommerce_data.csv). The generated data includes customer information, order details, product details, payment methods, and locations. This dataset can be used for testing, analysis, or demonstration purposes.

## Table of Contents

1. Introduction
2. Features
3. Files Included
4. Setup Instructions
5. Usage
6. Data Generation Details
7. Attribute Creation
8. Contributing

## 1. Introduction

This project aims to provide a realistic dataset for e-commerce analysis and testing. It simulates transactions with various attributes to mimic real-world scenarios.

## 2. Features

* Generates synthetic e-commerce transaction data.
* Includes details on customers, products, orders, payments, and locations.
* Saves data to a CSV file (ecommerce_data.csv).
* Uses realistic distributions for cities, payment methods, and product categories.
* Simulates annual inflation rates and promotional discounts.

## 3. Files Included

* main.py: Main script to generate the e-commerce data.
* cities_weights.json: JSON file containing cities and their weights for random selection.
* payment_met.json: JSON file containing payment methods and their weights for random selection.
* products.json: JSON file containing product information including categories, names, brands, and prices.

## 4. Setup Instructions

To set up the project, follow these steps:

1. Clone the repository:

git clone [repository-url]
cd [repository-name]

2. Install the required Python packages:

pip install pandas numpy

3. Ensure the JSON files are in the correct directory:

The script expects cities_weights.json, payment_met.json, and products.json to be located in a directory named files. Create this directory and move the JSON files into it:

mkdir files
mv cities_weights.json files/
mv payment_met.json files/
mv products.json files/

## 5. Usage

To run the data generation script, execute the following command:

python main.py

This will generate the ecommerce_data.csv file containing the synthetic data.

## 6. Data Generation Details

The main.py script generates synthetic data by:

1. Loading data from JSON files:
Products from products.json.
Payment methods from payment_met.json.
City weights from cities_weights.json.

2. Defining date range:
Generates dates between January 1, 2019, and January 1, 2025.

3. Simulating transactions:
Randomly selects dates, payment methods, cities, and customers.
Includes details for each product in the order.
Applies annual inflation rates to product prices.
Adds random promotional discounts.

4. Creating a Pandas DataFrame:
Organizes the generated data into a structured DataFrame.

5. Saving to CSV:
Saves the DataFrame to ecommerce_data.csv.

## 7. Attribute Creation

### 7.1. cities_weights.json

This file defines the cities and their weights for random selection.

* Example:

{
"Leticia": 2,
"Medellín": 10,
"Arauca": 3,
"Bogotá": 10
}

* Creation:
1. Create a new JSON file named cities_weights.json.
2. Add city names as keys and their corresponding weights as values.
3. Ensure the weights reflect the probability of each city being selected.

### 7.2. payment_met.json

This file defines the payment methods and their weights for random selection.

* Example:

{
"Tarjeta de crédito": 20,
"Tarjeta de débito": 15,
"PSE": 17
}

* Creation:
1. Create a new JSON file named payment_met.json.
2. Add payment method names as keys and their corresponding weights as values.
3. Ensure the weights reflect the probability of each payment method being selected.

### 7.3. products.json

This file defines the product categories and their details.

* Example:

[
{
"name": "DefaultName",
"scopes": [],
"apiResources": [],
"proxies": [],
"ecommerce": {
"categories": [
{
"name": "Smartphones",
"products": [
{
"id": "SP1001",
"name": "iPhone 14",
"brand": "Apple",
"price": 999.99,
"specs": {
"ram": "6GB",
"storage": "128GB",
"color": "Negro"
}
},
{
"id": "SP1002",
"name": "Galaxy S23",
"brand": "Samsung",
"price": 899.99,
"specs": {
"ram": "8GB",
"storage": "256GB",
"color": "Blanco"
}
}
]
},
{
"name": "Laptops",
"products": [
{
"id": "LP2001",
"name": "XPS 13",
"brand": "Dell",
"price": 1249.99,
"specs": {
"ram": "16GB",
"storage": "512GB SSD",
"processor": "Intel Core i7"
}
},
{
"id": "LP2002",
"name": "MacBook Air M2",
"brand": "Apple",
"price": 1299.99,
"specs": {
"ram": "8GB",
"storage": "256GB SSD",
"processor": "Apple M2"
}
}
]
}
]
}
}
]

* Creation:
1. Create a new JSON file named products.json.
2. Define the structure as shown in the format above.
3. Add categories and products with their corresponding details.
4. Ensure the structure is correctly formatted to avoid errors.

## 8. Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.