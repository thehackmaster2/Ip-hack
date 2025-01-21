import requests

def trace_ip(ip_address):
    try:
        url = f"http://ip-api.com/json/{ip_address}"
        response = requests.get(url)
        data = response.json()
        
        if data['status'] == 'success':
            print(f"IP Address: {data['query']}")
            print(f"Country: {data['country']}")
            print(f"Region: {data['regionName']}")
            print(f"City: {data['city']}")
            print(f"ZIP: {data['zip']}")
            print(f"Latitude: {data['lat']}")
            print(f"Longitude: {data['lon']}")
            print(f"ISP: {data['isp']}")
            print(f"Organization: {data['org']}")
        else:
            print("IP address not found or invalid.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ip = input("Enter IP address to trace: ")
    trace_ip(ip)