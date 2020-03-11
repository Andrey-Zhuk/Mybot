import requests
import misc
from yobit import get_btc


token = misc.token

URL = "https://api.telegram.org/bot" + token + "/"

# глобальная переменная
global last_update_id
last_update_id = 0


# запрос, обновление c необходимыми данными
def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


# Вызывает функцию get_updetes, получает объект json
# функция возвращает словарь messege
def get_message():
    data = get_updates()
    # отвечает только на новые сообщения
    # получаем update_id, каждого обновления
    # записывает его в переменную, а затем
    # сравнивает его с update_id последнего элемента
    # в списке result
    last_object = data["result"][-1]
    # текущее update_id
    current_update_id = last_object["update_id"]

    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id
        chat_id = last_object["message"]["chat"]["id"]
        message_text = last_object["message"]["text"]

        message = {"chat_id": chat_id,
                   "text": message_text}

        return message
    else:
        return None


def send_message(chat_id, text = "Wait a second, please..."):
    url = URL + "sendmessage?chat_id={}&text={}".format(chat_id, text)
    requests.get(url)


# глобальный цикл
def main():
    while True:
        answer = get_message()
        if answer != None:
            chat_id = answer["chat_id"]
            text = answer["text"]

            if text == "/btc":
                send_message(chat_id, get_btc())
        else:
            continue


if __name__ == "__main__":
    main()






















