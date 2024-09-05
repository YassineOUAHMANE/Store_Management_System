import mysql.connector
import datetime
class Orders_dao:
    def __init__(self):
        self.connection = mysql.connector.connect(
            user='root',
            password='root',
            host='localhost',
            database='store_management',
            port='3306'
            )
    def insert_orders(self,order):
        cursor = self.connection.cursor()
        query = 'insert into orders (customer_name,datetime,total) values (%s,%s,%s)'
        order_data = (order['customer_name'],datetime.datetime.now(),order['grand_total'])
        cursor.execute(query,order_data)
        order_id = cursor.lastrowid
        order_details_data = []
        order_details_query = ('insert into order_details (order_id,product_id,quantity,total_price) values (%s,%s,%s,%s)')
        for order_details_record in order['order_details']: 
              order_details_data.append([
                  order_id,
                  int(order_details_record['product_id']),
                  float(order_details_record['quantity']),
                  float(order_details_record['total_price'])
              ])
        cursor.executemany(order_details_query,order_details_data)      
        self.connection.commit()
        return order_id

    def get_all_orders(self):
        cursor = self.connection.cursor()
        query = 'select * from orders'
        cursor.execute(query)
        response = []
        for (order_id,customer_name,datetime,total) in cursor:
            response.append({
                'order_id':order_id,
                'customer_name':customer_name,
                'datetime':datetime,
                'total':total

            })
        return response    








if __name__=='__main__':
    order = Orders_dao()
    print(order.insert_orders({
        'customer_name':'simo',
        'grand_total':'140000',
        'order_details':[{
            'product_id':1,
            'quantity':2,
            'total_price':140000
        }]
    }))        

