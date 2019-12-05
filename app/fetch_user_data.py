import requests
import jsonpath
import json

url = 'https://reqres.in/api/users?page=2'

def get_users():

    # Send request
    response = requests.get(url)
    assert response.status_code == 200
    print(f'STATUS: {response.status_code}')

    # print body
    parsed = json.loads(response.content)
    print(json.dumps(parsed, indent=4, sort_keys=True))

    # print header
    # print(response.headers)

def fetch_response_headers():
    # Send request
    response = requests.get(url)
    
    # print header
    print(response.headers)
    print(f"Date: {response.headers.get('Date')}")
    print(f"Server: {response.headers.get('Server')}")


def fetch_cookies():
    # Send request
    response = requests.get(url)
    
    # print header
    print(response.headers)
    print(f"Cookies: {response.cookies}")

def fetch_encoding():
    # Send request
    response = requests.get(url)
    
    # print header
    print(response.headers)
    print(f"Enconding: {response.encoding}")

def fetch_elapsed_time():
    # Send request
    response = requests.get(url)
    
    # print header
    print(response.headers)
    print(f"Enconding: {response.elapsed}")

def validate_response_body_using_jsonpath():
    # Send request
    response = requests.get(url)

    json_response = json.loads(response.text)
    # print(f'json_response = {json_response}')
    # print(json.dumps(json_response, indent=4, sort_keys=True))

    #Json path
    pages = jsonpath.jsonpath(json_response, 'total_pages')
    assert pages[0] == 2
    print(pages[0])
    data = jsonpath.jsonpath(json_response, 'data')
    print(f'data = {data[0]}')
    print(f'email = {data[0][0]["email"]}')

    #Fetch firstnames and last names
    for user in data[0]:
        print(f'{user["first_name"]} {user["last_name"]} ({user["email"]})')

if __name__ == '__main__':
    # get_users()
    # fetch_response_headers()
    # fetch_cookies()
    # fetch_encoding()
    # fetch_elapsed_time()
    validate_response_body_using_jsonpath()