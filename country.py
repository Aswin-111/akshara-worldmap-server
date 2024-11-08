import requests
from countryinfo import CountryInfo

# Function to get country data and send it to the API
country_data = []
def get_and_post_country_data():
    countries = CountryInfo().all()  # Get all countries data

    for country_name in countries:
        country_info = CountryInfo(country_name)
        
        # Prepare the data structure for the API
        data = {
            "country": country_name,
            "states": country_info.provinces()  # Get the provinces/states
        }




        
       
       







    
    

    


    

        

        
        
        
        
        
        country_data.append(data)
        response = requests.post("http://192.168.10.100/api/v1/map/add-states", json=data)
        
        if response.status_code == 200:
            print(f"Successfully posted data for {country_name}")
        else:
            print(f"Failed to post data for {country_name}: {response.status_code}")

# Run the function
get_and_post_country_data()
