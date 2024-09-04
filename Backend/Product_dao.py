import mysql.connector


class ProductDAO:
    def __init__(self):
        self.connection = mysql.connector.connect(
            user='root',
            password='root',
            host='localhost',
            database='store_management',
            port='3306'
            )
    def Close_connection_database(self):
        self.connection.close()        
    def Execute_query(self,query):    
        self.cursor = self.connection.cursor()
        self.query = query
        self.cursor.execute(self.query) 
        self.connection.commit()
        self.cursor.close()
    def get_all_products(self):
        products = []
        self.cursor = self.connection.cursor()
        self.query = "select p.product_id,p.name ,u.name ,p.price_per_unit from store_management.products as p inner join store_management.units as u on p.uom_id=u.uom_id"
        self.cursor.execute(self.query)
        for (Product_id,Product_name,Uom_name,Price_per_unit) in self.cursor:
            products.append({
                'product_id': Product_id ,
                'name': Product_name,
                'uom_name': Uom_name,
                'price_per_unit': Price_per_unit,
            })
        self.cursor.close()
        return products
    
    def insert_new_product(self,product):
        cursor = self.connection.cursor()
        query = "insert into store_management.products(name,uom_id,price_per_unit) values(%s,%s,%s)"
        data = (product['product_name'],product['uom_id'],product['price_per_unit'])
        cursor.execute(query,data)
        self.connection.commit()
        return cursor.lastrowid
         
          


    def delete_product(self,product_id):
        self.cursor = self.connection.cursor()
        query = f"Delete from products where Product_id={product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def edit_product_name(self, product_id, name):
        self.cursor = self.connection.cursor()
        query = "UPDATE products SET name = %s WHERE product_id = %s"
        self.cursor.execute(query, (name, product_id))
        self.connection.commit()

    def edit_product_Unit(self, product_id, Unit_name):
        self.cursor = self.connection.cursor()
        query = "UPDATE products SET uom_id = (select uom_id from units where name = %s)  WHERE product_id = %s"
        self.cursor.execute(query, (Unit_name, product_id))
        self.connection.commit()

    def edit_product_Price(self, product_id, Price):
        self.cursor = self.connection.cursor()
        query = "UPDATE products SET price_per_unit = %s WHERE product_id = %s"
        self.cursor.execute(query, (Price, product_id))
        self.connection.commit()

    
    


        
if __name__ == '__main__':
    product = ProductDAO()
         