import requests
import re
from concurrent.futures import ThreadPoolExecutor

def fetch_and_extract(url):
    response = requests.get(url)
    if response.status_code == 200:
        match = re.search(r'<text x="59\.4" y="\d+"[^>]*>(\d+)</text>', response.content.decode('utf-8'))
        if match:
            return match.group(1)
        else:
            return "Number not found."
    else:
        return f'Err: {response.status_code}'

def main():
    url = "https://camo.githubusercontent.com/0616881cef9ed65daff7bc9f55a339314a439b0d972bb01b310a5464f28253c3/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d616e64686b64776d6c6e266c6162656c3d56697369746f7226636f6c6f723d306537356236267374796c653d666c6174"
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(fetch_and_extract, url) for _ in range(10)]
        
        for future in futures:
            result = future.result()
            print(result)

if __name__ == "__main__":
    main()
