import pandas as pd
import requests as re

_config_file = open('config.txt', 'r')
client_name = 'gamers-stats'
api_key = _config_file.readline()

def get_all_apps():
    all_steam_apps = re.get('https://api.steampowered.com/ISteamApps/GetAppList/v2/').json()['applist']['apps']
    df_apps = pd.DataFrame(all_steam_apps)
    df_apps['name_lower'] = df_apps['name'].apply(lambda x: x.lower())
    return df_apps

def get_app_details(appid):

    return None