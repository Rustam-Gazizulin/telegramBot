import requests
import time


API_URL: str = 'https://api.telegram.org/bot'
API_CATS_URL: str = 'https://api.thecatapi.com/v1/images/search'
BOT_TOKEN: str = '5976510239:AAE_GAdpynTlNEHbJNtdIroDDjRzXwl_8xY'
TEXT: str = 'Good Job!!!'
MAX_COUNTER: int = 100

offset: int = -2
counter: int = 0
timeout: int = 20.63
chat_id: int
updates: dict


def do_something() -> None:
    print('Был апдейт')


while True:
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()
    if updates['result']:
        for result in updates['result']:
            print(result['message']['text'])
            offset = result['update_id']
            do_something()
            try:
                chat_id = result['message']['from']['id']
            except KeyError:
                chat_id = result['edited_message']['chat']['id']
            cat_response = requests.get(API_CATS_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()[0]['url']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text=Лови КОТИКА!')
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text=Нет нужной картинки')

    # time.sleep(3)
    end_time = time.time()
    print(f"Время между запросами к Телеграм АПИ {end_time - start_time}")
