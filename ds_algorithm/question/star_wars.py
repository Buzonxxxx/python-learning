import requests

base_url = 'https://swapi.py4e.com/api/'

# Function to get species in film-6
def get_species():
    try:
        response = requests.get(base_url + 'films/6')
        response.raise_for_status()
        species = response.json()['species']
        print(f'There are {len(species)} species that appear in film-6 (Revenge of the Sith)')
    except requests.exceptions.RequestException as error:
        print('Error:', error)

# Function to list all films sorted by episode_id
def list_all_films():
    try:
        response = requests.get(base_url + 'films/')
        response.raise_for_status()
        films = response.json()['results']
        sorted_films = sorted(films, key=lambda film: film['episode_id'])
        for film in sorted_films:
            print(f"The No.{film['episode_id']} film's name is {film['title']}")
    except requests.exceptions.RequestException as error:
        print('Error:', error)

# Function to find vehicles with max_atmosphering_speed over 1000
def over_one_thousand_speed():
    try:
        page = 1
        results = []
        while True:
            response = requests.get(f'{base_url}vehicles/?page={page}')
            response.raise_for_status()
            vehicle_data = response.json()
            results.extend(vehicle_data['results'])
            if not vehicle_data.get('next'):
                break
            page += 1

        for vehicle in results:
            max_speed = vehicle['max_atmosphering_speed']
            if max_speed.isdigit() and int(max_speed) > 1000:
                print(f"The {vehicle['name']}'s speed is over 1000, it is {max_speed}")
    except requests.exceptions.RequestException as error:
        print('Error:', error)

# Main function to run all tasks
def main():
    get_species()
    list_all_films()
    over_one_thousand_speed()

if __name__ == '__main__':
    main()
