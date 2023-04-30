from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message


API_TOKEN: str = '5976510239:AAE_GAdpynTlNEHbJNtdIroDDjRzXwl_8xY'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


# Хендлер для команды /start
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут эхо-бот!\nНапиши мне что-нибудь)')


# Хендлер для команды /help
async def process_help_command(message: Message):
    # message.answer отправляет в чат сообщение, а message.reply отправляет ответ на сообщение
    await message.answer('Напиши что-нибудь и в ответ пришлю тебе твое сообщение')


# Хендлер для обработки изображений
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)


# Хендлер для обработки стикеров
async def send_sticker_echo(message: Message):
    # print(message.json(indent=4, exclude_none=True))
    await message.answer_sticker(message.sticker.file_id)


# Хендлер для прочих команд кроме /start and /help
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text='Данный тип апдейтов не поддерживается send_copy')


# Регистрируем хэндлеры
dp.message.register(process_start_command, Command(commands=['start']))
dp.message.register(process_help_command, Command(commands=['help']))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_sticker_echo, F.sticker)
dp.message.register(send_echo)


if __name__ == '__main__':
    dp.run_polling(bot)
