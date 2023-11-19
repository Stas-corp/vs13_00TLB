import botinit

import telebot as tlb
import os
import arrow
import random

bot = botinit.bot

class Photgraph:
    def __init__(self) -> None:
        self.photo = None
        self.userpath = None
        self.path = 'photo'

    def check_dir(self, user_id) -> None:
        self.userpath = os.path.join(self.path, user_id)
        if not os.path.exists(self.userpath):
            os.mkdir(self.userpath)
    
    def save_photo(self, photo:tlb.types.PhotoSize) -> None:
        date = arrow.now().format('YYMMDD_HHmmss')
        soll = random.randint(1000000, 9000000)
        file_info = bot.get_file(photo.file_id)
        download_file = bot.download_file(file_info.file_path)
        with open(os.path.join(self.path, f'{date}_{soll}.jpg'), 'wb') as file:
            file.write(download_file)

    def main(self, photos:list) -> None:
        self.check_dir()
        self.save_photo(photos[-1])