from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = config('TOKEN')

# TOKEN = '5919471305:AAGeCb6ok69RLIVupnsJNwmlCex04m-S7i0'
ADMIN = (878246291)
bot = Bot(TOKEN)
db = Dispatcher(bot=bot, storage=storage)
