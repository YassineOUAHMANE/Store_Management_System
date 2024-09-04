import mysql.connector

class Unit_dao:
 def __init__(self):
        self.connection = mysql.connector.connect(
            user='root',
            password='root',
            host='localhost',
            database='store_management',
            port='3306'
            )
 def getUOM(self):
     cursor = self.connection.cursor()
     query = 'select * from units'
     cursor.execute(query)
     response = []
     for (uom_id,uom_name) in cursor:
         response.append(
              {
                  'uom_id': uom_id,
                  'uom_name' : uom_name
              }
         ) 
     return response    
           
        



if __name__ == "__main__":
    Unit = Unit_dao()
    print(Unit.get_units())

