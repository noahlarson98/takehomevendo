from flask import Flask, jsonify, request, Response
import json

coins = 0
drinks = [5, 5, 5] # 3 different beverages, 5 each

app = Flask(__name__)

@app.route('/', methods=['PUT', 'DELETE'])
def baseuri():
    global coins
    if request.method == 'PUT':
        requestbody = request.get_json()
        coins_accepted = 0

        print(requestbody)
        if requestbody == {"coin": 1}: # Only accept one coin at a time
            coins += 1
            coins_accepted = 1
        
        # If the body is anything else, no coins have been accepted.
        return Response(headers={'X-Coins': coins_accepted}, status= 204, content_type='application/json')
    
    if request.method == 'DELETE':
        coins_returned = coins
        coins = 0
        return Response(headers={'X-Coins': coins_returned}, status= 204, content_type='application/json')

@app.route('/inventory', methods=['GET'])
def getInventory():
    return jsonify(drinks) # Easy way to return int array

@app.route('/inventory/<int:id>', methods = ['GET', 'PUT'])
def inventory(id):
    global coins
    if request.method == 'GET':
        return jsonify(drinks[id])
    
    if request.method == 'PUT':
        if drinks[id] <= 0: # Drink is sold out
            return Response(headers={'X-Coins': coins}, status=404, content_type='application/json') # Error 404: Drink not found
        if coins < 2:
            return Response(headers={'X-Coins': coins}, status=403, content_type='application/json') # Not enough coins
        
        returned_coins = coins
        coins = 0 # Upon transaction completion, any unused quarters must be dispensed back to the customer
        drinks[id] = drinks[id] - 1
        json_response = json.dumps({"quantity": 1}) # {number of items vended}... It should only be one, at least at a time... Unless it means total... And would that mean total of all transactions or just for that particular type?
        return Response(json_response, headers={'X-Coins': returned_coins, 'X-Inventory-Remaining': drinks[id]}, status= 200)


if __name__ == '__main__':
    app.run()