from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


API_TOKEN: str = '5976510239:AAE_GAdpynTlNEHbJNtdIroDDjRzXwl_8xY'

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут эхо-бот!\nНапиши мне что-нибудь)')


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Напиши что-нибудь и в ответ пришлю тебе твое сообщение')


@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)

if __name__ == '__main__':
    dp.run_polling(bot)
