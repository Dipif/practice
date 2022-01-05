from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id":1, "name" : "Espresso", "price":3000},
    {"id":2, "name" : "Americano", "price":4000},
    {"id":3, "name" : "CafeLatte", "price":5000},]
id_num = [4]

@app.route('/')
def hello_flask() :
    return "Hello Flask"

@app.route('/menus')
def get_menus() :
    return jsonify({"menus" : menus})

@app.route('/menus', methods = ['POST'])
def create_menu() :
    request_data = request.get_json()
    new_menu = {
        "id" : id_num[0],
        "name" : request_data['name'],
        "price" : request_data['price']}
    id_num[0] += 1
    menus.append(new_menu)
    return jsonify(new_menu)

@app.route('/menus/<int:idd>', methods = ['PUT'])
def update_menu(idd) :
    request_data = request.get_json()
    new_menu = {
        "id" : idd,
        "name" : request_data['name'],
        "price" : request_data['price']}
    menus[idd-1] = new_menu
    return jsonify(new_menu)

@app.route('/menus/<int:idd>', methods = ['DELETE'])
def delete_menu(idd) :
    menus.pop(idd-1)
    return jsonify({"menus" : menus})

if __name__ == '__main__' :
    app.run()