from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button1 = KeyboardButton(text="/Weather")
button2 = KeyboardButton(text="Отправить геолокацию", request_location=True)
waether_markup = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[button1]])
location_markup = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[button2]])
