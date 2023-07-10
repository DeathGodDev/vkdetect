from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

mainKeyboard = InlineKeyboardMarkup()
mainKeyboard.add(InlineKeyboardButton("👑 VIP - 199  рублей/месяц 👑", callback_data="vip"))
mainKeyboard.add(InlineKeyboardButton("💸 MVP - 999  рублей/месяц 💸", callback_data="vip"))
mainKeyboard.add(InlineKeyboardButton("💎 GOD - 4999 рублей/месяц 💎", callback_data="vip"))

accessKeyboard = InlineKeyboardMarkup()
accessKeyboard.row(InlineKeyboardButton("Да", callback_data="help_yes"), InlineKeyboardButton("Нет", callback_data="help_no"))

helpKeyboard = ReplyKeyboardMarkup()
helpKeyboard.add(KeyboardButton("Описание платных подписок"))
helpKeyboard.add(KeyboardButton("Описание возможных проблем"))
helpKeyboard.add(KeyboardButton("Инструкция к программе"))
helpKeyboard.add(KeyboardButton("Инструкция к боту"))
helpKeyboard.add(KeyboardButton("Назад"))

noneKeyboard = ReplyKeyboardMarkup()
