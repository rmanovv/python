import requests
from requests.exceptions import ConnectionError

def internet_connection_test():
    print()
    url = input()
    print(f"Attempting to connect to {url} to determine internet connection status.\n")
    
    try:
        resp = requests.get(url, timeout=10)
        resp.text
        resp.status_code
        
        print(f"Connection to {url} was successful.\n")
        
        return True
    
    except ConnectionError as e:
        requests.ConnectionError
        
        print(f"Failed to connect to {url}")
        
        return False
    
    except:
        print(f"Failed with unparsed reason!\n")
        
        return False

internet_connection_test()
