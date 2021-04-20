import requests as re

def get_app_details(app_name):
    try:
        _config_file = open('config.txt', 'r')
        api_key = _config_file.readline()
    except:
        api_key = str(os.environ.get('API_KEY', 3))

    url = f'https://api.rawg.io/api/games?key={api_key}&search_precise=true&search=%27{app_name.lower()}%27'
    call = re.get(url).json()
    return call