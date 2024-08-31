import requests
from bs4 import BeautifulSoup
import mysql.connector 

#function to establish aconnection to mysql database

def create_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kushal123",
        database="ecommerce_data"
    )
    return connection

#function to create a table in MySQL database for storing the extracted

def create_table(connection):
    cursor =connection.cursor()
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS products(
                id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),
                name VARCHAR(255),
                price VARCHAR(255),
                url TEXT
                )
            """)
    connection.commit()

    #function to insert extracted product data into the MySQL database.

def insert_product(connection,name,price,url):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO products (name,price,url) VALUES (%s,%s,%s",(name,price,url))
        connection.commit()


    #function to scrape data from e-commerce website

def scrape_ecommerce_site(url):
     try:
          response = requests.get(url)
          response.raise_for_status()
          soup = BeautifulSoup(response.text, 'html.parser')

          products=[]
          for product in soup.select('.product-class'):
              name = product.select_one('.product-name').text
              price = product.select_one('.product-price').text
              product_url = product.select_one('a')['href']
              products.append((name,price,product_url))
          return products
     except Exception as e:
          print(f"An error occurred: {e}")
          return []
     

    #Main function to run the Scraper and store data in the database
def main():
     connection = create_db_connection()
     create_table(connection)

     url=""
     products = scrape_ecommerce_site(url)

     if products:
         for name,price,products_url in products:
             insert_product(connection,name,price, products_url)
     else:
          print("no products found")
     connection.close()

if __name__ == "__main__":
     main()