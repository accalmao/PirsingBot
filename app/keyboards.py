from aiogram.types import ReplyKeyboardMarkup,InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from app.database.request import get_categories, get_products

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Контакты')]
],resize_keyboard=True, input_field_placeholder='Выберите пункт ниже')


main_admin = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Контакты')],
[KeyboardButton(text='Админка')]
],resize_keyboard=True, input_field_placeholder='Выберите пункт ниже')


admin_panel = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Создать рассылку')],
    [KeyboardButton(text='Назад')]
],resize_keyboard=True)


async def categories():
    categories_kb = InlineKeyboardBuilder()
    categories = await get_categories()
    for category in categories:
        categories_kb.add(InlineKeyboardButton(text=category.name, callback_data=f'category_{category.id}'))
    return categories_kb.adjust(2).as_markup()


async def products(category_id):
    products_kb = InlineKeyboardBuilder()
    products = await get_products(category_id)
    for product in products:
        products_kb.add(InlineKeyboardButton(text=product.name, callback_data=f'product_{product.id}'))
    return products_kb.adjust(2).as_markup()


async def age():
    agekeyboard = InlineKeyboardBuilder()
    agekeyboard.add(InlineKeyboardButton(text='Да', callback_data='Да'))
    agekeyboard.add(InlineKeyboardButton(text='Нет', callback_data='Нет'))
    return agekeyboard.adjust(2).as_markup()
