import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram import F
from aiogram.filters.command import Command
import emoji
import gif
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from geopy.distance import geodesic


TOKEN = ("6913490279:AAEs9FpE8IcLGEyD0wX63rsokLD5hPqXDQk")

dp = Dispatcher()

fitnes_branches = [
    {"name": "G'uncha", "location": (69.219087 , 41.332013)},
    {"name": "Tashkent City", "location": (69.219087 , 41.332013)},

]


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")



@dp.message(F.location)
async def location_handler(msg : types.Message):
    map_ = []
    user_location = (msg.location.latitude , msg.location.longitude)
    for branch in fitnes_branches:
        branch_location = branch["location"]
        distance = geodesic(user_location, branch_location).kilometers
        map_.append({"name": branch["name"], "distance": distance , "location" : branch_location})
    near = min(map_ , key=lambda x : x.get('distance'))
    await msg.answer_location(*near.get('location')[::-1])




@dp.message()
async def buttons():
    btn1 = KeyboardButton(text = "Filial")
    btn2 = KeyboardButton(text="Start")
    btn3 = KeyboardButton(text="Admin")

    design_1 = [
        [btn1, btn2, btn3]
    ]
    return ReplyKeyboardMarkup(keyboard=design_1 , resize_keyboard=True)


async def New_Post():
    btn1=KeyboardButton(text = "FB Low Impact Round 2 - Build Muscle & Burn Fat - 40 Minutes or Less")
    btn2=KeyboardButton(text = "FB Blend - Burn Fat, Build Muscle, Tone; 35 or 55 Minutes a Day")
    btn3=KeyboardButton(text = "FB 30 - Fat Loss Program For Busy People")
    btn4 =KeyboardButton(text="FB Bodyweight - Bodyweight Only Fat Loss Program")
    design_2 = [
        [btn1, btn2, btn3, btn4]
    ]
    return ReplyKeyboardMarkup(keyboard=design_2 , resize_keyboard=True)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())



























@dp.message()
async def echo_message_handler(msg: Message):
    await msg.answer_animation("CgACAgQAAxkBAAN2ZVdEmUrevoBmWPiBQVgzTSSq_YAAAksDAAIZpART2IBLuYNDmrkzBA")

@dp.message(F.photo)
async def photo_handler(msg: Message):
    await msg.answer("Photo handler successfull")
    await msg.answer(f"{msg.photo[0].file.id}")

@dp.message(F.document)
async def photo_handler(msg: Message):
    await msg.answer(f"Document handler successfull\n{msg.document.file_id}")


@dp.message(F.video)
async def photo_handler(msg: Message):
    await msg.answer("Video handler successfull")
    await msg.answer(f"{msg.video.file_id}")

@dp.message(F.audio)
async def photo_handler(msg: Message):
    await msg.answer("Audio handler successfull")
    await msg.answer(f"{msg.audio.file_id}")


@dp.message(F.sticker)
async def photo_handler(msg: Message):
    await msg.answer("Sticker handler successfull")

@dp.message(F.voice)
async def photo_handler(msg: Message):
    await msg.answer("Voice handler successfull")

@dp.message(lambda msg : emoji.emoji_count(msg.text)>0)
async def photo_handler(msg: Message):
    await msg.answer("Emoji handler successfull")


@dp.message(Command('start'))
@dp.message(Command('admin'))
@dp.message(Command('panel'))
# async def digit_handler(msg : Message ):
#      await msg.answer("Hello world", reply_markup=number_button())
#
#
@dp.message(lambda msg: msg.text.isdigit() and 1 <= int(msg.text) <=100)
async def digit_handler(msg : Message):
   await msg.answer(msg.text)


@dp.message(F.text.isdigit())
async def digit_handler(msg : Message):
   await msg.answer(msg.text)















