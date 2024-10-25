import requests
import re

url = input("URL : ")
while True:
    # Make a GET request
    response = requests.get(url)

    if response.status_code == 200:
        # Decode the bytes to a string
        # Use regex to find the number
        match = re.search(r'<text x="59\.4" y="\d+"[^>]*>(\d+)</text>', response.content.decode('utf-8'))

        if match:
            number = match.group(1)
            print(f"Inject OK => {number}")  # Output: 606
        else:
            print("Number not found.")
    else:
        print(f'Err : {response.status_code}')