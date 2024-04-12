import requests

def get_amiibo_data(name=None):
    base_url = "https://www.amiiboapi.com/api/amiibo/"
    url = base_url
    if name:
        url += f"?name={name}"
    
    response = requests.get(url)
    
    if response.ok:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")

def main():
    # Example usage
    amiibo_name = input("Enter the name of the Amiibo (leave blank to see all): ")
    amiibo_data = get_amiibo_data(amiibo_name)
    
    if amiibo_data:
        print("Amiibo Data:")
        print(amiibo_data)
    else:
        print("No data found for the provided Amiibo name.")

if __name__ == "__main__":
    main()
