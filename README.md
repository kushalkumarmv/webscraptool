# webscraptool
 
This Python-based web scraping tool extracts product data from e-commerce websites and stores it in a MySQL database. It uses the BeautifulSoup and Requests libraries to parse HTML and handle HTTP requests.

Features
Scrapes product data such as name, price, and URL from an e-commerce website.
Stores the extracted data in a MySQL database.
Provides a simple setup for querying the stored data.

Requirements :
* Python 3.x
* Requests
* BeautifulSoup4
* mysql-connector-python
  
You can install the required libraries using pip:

* pip install requests beautifulsoup4 mysql-connector-python

Database Configuration:

Update the create_db_connection function with your MySQL database credentials (host, user, password, and database).

Scraping Logic:
Modify the scrape_ecommerce_site function to adapt to the HTML structure of the e-commerce website you are targeting. Update the CSS selectors (.product-class, .product-name-class, .product-price-class) as needed.
Running the Script:

Ensure that the URL in the main function points to the e-commerce site you want to scrape.

Run the script to start scraping and storing data:

bash
Copy code
python scraper.py
Code Overview
Database Connection:
The create_db_connection function establishes a connection to your MySQL database.

Table Creation: 
The create_table function creates a table named products in the database if it doesn't already exist.

Data Insertion:
The insert_product function inserts product details into the products table.

Scraping: 
The scrape_ecommerce_site function fetches and parses HTML content from the provided URL to extract product information.

Main Function:
The main function coordinates the database setup, data scraping, and data insertion processes.

For further customization or usage, refer to the script and adjust the parameters as needed.


