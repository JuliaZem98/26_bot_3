from aiogram.utils import executor
import logging
from config import db
from handler import client, callback, extra, admin, fsm_anketa

fsm_anketa.reg_hand_anketa(db)
admin.reg_ban(db)
client.reg_client(db)
callback.reg_hand_callback(db)
extra.reg_hand_extra(db)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)
