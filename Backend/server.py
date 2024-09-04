from flask import Flask, request, jsonify
import Product_dao
import Unit_dao
import Orders_dao
import json

app = Flask(__name__)

@app.route('/getProducts',methods = ['GET'])
def Get_Products():
    Product = Product_dao.ProductDAO()
    response = jsonify(Product.get_all_products())
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/deleteProduct',methods=['POST'])
def delete_product():
    Product =  Product_dao.ProductDAO()
    return_id = Product.delete_product(request.form['product_id'])
    response = jsonify({
        'Product_id':return_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/getUOM',methods = ['GET'])
def getUOM():
    Unit = Unit_dao.Unit_dao()
    response = jsonify(Unit.getUOM())
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
      
@app.route('/insertProduct',methods = ['POST'])
def insertProduct():
    Product = Product_dao.ProductDAO()
    request_payload = json.loads(request.form['data'])
    product_id = Product.insert_new_product(request_payload)
    response = jsonify({
        'Product_id':product_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/editname', methods=['POST'])
def editname():
    product = Product_dao.ProductDAO()
    product.edit_product_name(request.form['product_id'], request.form['name'])
    response = jsonify({"status": "success"})
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
    

@app.route('/editunit', methods=['POST'])
def edituom():
    product = Product_dao.ProductDAO()
    product.edit_product_Unit(request.form['product_id'], request.form['uom'])
    response = jsonify({"status": "success"})
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/editprice', methods=['POST'])
def editprice():
    product = Product_dao.ProductDAO()
    product.edit_product_Price(request.form['product_id'], request.form['price'])
    response = jsonify({"status": "success"})
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/insertOrder',methods = ['POST'])
def insertOrder():
    Order = Orders_dao.Orders_dao()
    request_payload = json.loads(request.form['data'])
    order_id = Order.insert_orders(request_payload)
    response = jsonify({
        'order_id':order_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response



if __name__ == "__main__":
    print("Starting Python Flask Server for store-management system")
    app.run(port=5000)