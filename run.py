import requests
import re

while True:
    # Make a GET request
    response = requests.get("https://camo.githubusercontent.com/0616881cef9ed65daff7bc9f55a339314a439b0d972bb01b310a5464f28253c3/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d616e64686b64776d6c6e266c6162656c3d56697369746f7226636f6c6f723d306537356236267374796c653d666c6174")

    if response.status_code == 200:
        # Decode the bytes to a string
        content = response.content.decode('utf-8')

        # Use regex to find the visitor count
        match = re.search(r'<text x="55.9" y="14">(\d+)</text>', content)
        
        if match:
            visitor_count = match.group(1)
            print(f'[+] View : {visitor_count}')
        else:
            print('[-] View not added.')
    else:
        print(f'Err : {response.status_code}')