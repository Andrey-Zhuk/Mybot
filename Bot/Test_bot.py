import requests
import misc
import json

# https://api.telegram.org/bot722255162:AAFCZgz85tj-hNiBAl8pk4fyRAv16NIXb-w/sendmessage?chat_id=876648566&text=hi


token = misc.token

URL = "https://api.telegram.org/bot" + token + "/"

def get_updetes():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def main():
    d = get_updetes()


    with open('updates.json', 'w') as file:
        json.dump(d, file, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()