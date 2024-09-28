import requests

base_url = 'http://127.0.0.1:5000/'

def printHttpCall(operation, url, contents=None):
    print(f'[{operation}] {url}')
    if contents is not None:
        print('Contents:\n\t', contents)
    print()

def printResponse(response):
    print('Headers:')
    for header, value in response.headers.items():
        print(f'\t{header}: {value}')
    print('Response Code: ', response.status_code)
    try:
        response_body = response.json()
    except ValueError:
        response_body = ''
    print('Response Body: ', response_body)
    print()

# PUT '/'
def insertCoin():
    coin_json = {"coin": 1}
    url = base_url
    printHttpCall('PUT', url, coin_json)
    response = requests.put(url=url, json=coin_json)
    printResponse(response)

# DELETE '/'
def ejectCoins():
    url = base_url
    printHttpCall('DELETE', url)
    response = requests.delete(url=url)
    printResponse(response)

# GET '/inventory'
def checkInventory():
    url = base_url + 'inventory'
    printHttpCall('GET', url)
    response = requests.get(url=url)
    printResponse(response)

# GET '/inventory/<id>'
def checkSpecificInventory(id):
    url = f'{base_url}inventory/{id}'
    printHttpCall('GET', url)
    response = requests.get(url=url)
    printResponse(response)

# PUT '/inventory/<id>'
def buySpecificItem(id):
    url = f'{base_url}inventory/{id}'
    printHttpCall('PUT', url)
    response = requests.put(url=url)
    printResponse(response)

def selectSpecific():
    id = '-1'
    while (id > '2' or id < '0'):
        id = input('Please enter a number between 0-2: ')
    return id

def menu():
    print('Welcome to the Vend-O-Matic!')
    print('This script provides an interface to')
    while True:
        print('What would you like to do?')
        print('1. Insert a coin')
        print('2. Eject coins')
        print('3. Check inventory')
        print('4. Check specific inventory')
        print('5. Buy specific item')

        choice = input('>')

        if choice == '1':
            print()
            insertCoin()
        elif choice == '2':
            ejectCoins()
        elif choice == '3':
            checkInventory()
        elif choice == '4':
            selected = selectSpecific()
            checkSpecificInventory(selected)
        elif choice == '5':
            selected = selectSpecific()
            buySpecificItem(selected)
        else:
            print('Invalid option\n')

if __name__ == '__main__':
    menu()