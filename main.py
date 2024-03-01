import asyncio
import requests
import json
from users.user_dao import UserDao
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from config import settings
from markup.requests_markup import waether_markup, location_markup

bot = Bot(settings.TELEGRAM_TOKEN)
dp = Dispatcher()

headers = {
    "X-Yandex-API-Key": settings.API_YANDEX_WEATHER_TOKEN
}


@dp.message(CommandStart())
async def hi_func(message: types.Message):
    user = await UserDao.find_by_id(str(message.from_user.id))
    if user:
        await message.answer(text="Привет", reply_markup=waether_markup)
    else:
        await message.answer(text="Привет", reply_markup=location_markup)


@dp.message(F.location)
async def location(message: types.Message):
    await UserDao.insert_row(id=str(message.from_user.id), lat=message.location.latitude, lon=message.location.longitude)
    await message.answer("Геопозиция сохранена", reply_markup=waether_markup)


@dp.message(Command("Weather"))
async def get_weather(message: types.Message):
    user = await UserDao.find_by_id(str(message.from_user.id))
    if user:
        query = f"""{{
          weatherByPoint(request: {{ lat: {user.lat}, lon: {user.lon} }}) {{
            now {{
              humidity
              pressure
              temperature
              windSpeed
              windDirection
            }}
          }}
        }}"""
        response = json.loads(requests.post('https://api.weather.yandex.ru/graphql/query', headers=headers, json={'query': query}).text)
        print(response)
        await message.answer(text=f'Влажность: {response["data"]["weatherByPoint"]["now"]["humidity"]} \n'
                                  f'Давление: {response["data"]["weatherByPoint"]["now"]["pressure"]} \n'
                                  f'Температура: {response["data"]["weatherByPoint"]["now"]["temperature"]} \n'
                                  f'Скорость ветра: {response["data"]["weatherByPoint"]["now"]["windSpeed"]} \n', reply_markup=waether_markup)
    else:
        await message.answer(text="Привет", reply_markup=location_markup)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
