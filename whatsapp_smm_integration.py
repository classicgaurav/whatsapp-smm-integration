import requests

def send_order(service_id, quantity, link):
    api_key = 'your_api_key'
    url = 'https://smmsocialmedia.in/api/v2'
    payload = {
        'key': api_key,
        'action': 'add',
        'service': service_id,
        'quantity': quantity,
        'link': link
    }
    response = requests.post(url, data=payload)
    return response.json()

# Example usage
service_id = 1  # Replace with actual service ID
quantity = 100  # Number of likes, followers, etc.
link = 'https://instagram.com/yourprofile'
result = send_order(service_id, quantity, link)
print(result)
