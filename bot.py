from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import config
import keyboards

bot = Bot(token=config.token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def send_welcome(message):
    await bot.send_message(message.from_user.id, config.start_message, reply_markup=keyboards.mainKeyboard)

@dp.message_handler(commands=["help"])
async def send_help(message):
    await bot.send_message(message.from_user.id, config.help_message, reply_markup=keyboards.helpKeyboard)

@dp.callback_query_handler(lambda callback: callback.data in ["help_yes", "help_no"])
async def accessGet(call):
    if call.data == "help_yes":
        await bot.send_message(call.from_user.id, config.yes_message)
    elif call.data == "help_no":
        await bot.send_message(call.from_user.id, config.no_message)
    await bot.send_message(call.from_user.id, config.default_message, reply_markup=keyboards.mainKeyboard)

@dp.callback_query_handler(lambda callback: callback.data in ["vip"])
async def vipCall(call):
    await bot.send_message(call.from_user.id, config.goodT_message)

async def helpCall(call):
    if call.text == "Описание платных подписок":
        await bot.send_message(call.from_user.id, config.aboutSubs)
        await bot.send_message(call.from_user.id, config.helpN_message, reply_markup=keyboards.accessKeyboard)
    elif call.text == "Описание возможных проблем":
        await bot.send_message(call.from_user.id, config.problems_message)
        await bot.send_message(call.from_user.id, config.helpN_message, reply_markup=keyboards.accessKeyboard)
    elif call.text == "Инструкция к программе":
        await call.reply_document(open('guide.pdf', 'rb'), reply_markup=keyboards.noneKeyboard)
        await bot.send_message(call.from_user.id, config.helpN_message, reply_markup=keyboards.accessKeyboard)
    elif call.text == "Инструкция к боту":
        await call.reply_document(open('botguide.pdf', 'rb'), reply_markup=keyboards.noneKeyboard)
        await bot.send_message(call.from_user.id, config.helpN_message, reply_markup=keyboards.accessKeyboard)
    elif call.text == "Назад":
        await bot.send_message(call.from_user.id, config.default_message, reply_markup=keyboards.mainKeyboard)
    else:
        await bot.send_message(call.from_user.id, config.error_command_message)
        await bot.send_message(call.from_user.id, config.default_message, reply_markup=keyboards.mainKeyboard)

@dp.message_handler()
async def echo(message):
    try:
        id = int(message.text)
    except:
        await helpCall(message)
    else:
        if id > 147:
            await bot.send_message(message.from_user.id, config.error_id_message)
            await bot.send_message(message.from_user.id, config.default_message, reply_markup=keyboards.mainKeyboard)
        else:
            if id in config.vip_ids:
                await bot.send_message(message.from_user.id, config.vip_message)
                await bot.send_message(message.from_user.id, config.default_message, reply_markup=keyboards.mainKeyboard)
            elif id in config.mvp_ids:
                await bot.send_message(message.from_user.id, config.mvp_message)
                await bot.send_message(message.from_user.id, config.default_message, reply_markup=keyboards.mainKeyboard)
            elif id in config.god_ids:
                await bot.send_message(message.from_user.id, config.god_message)
                await bot.send_message(message.from_user.id, config.default_message, reply_markup=keyboards.mainKeyboard)
            else:
                await bot.send_message(message.from_user.id, config.good_message, reply_markup=keyboards.mainKeyboard)



if __name__ == '__main__':
    executor.start_polling(dp)
