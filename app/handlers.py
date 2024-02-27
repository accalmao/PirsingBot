from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from app.database.request import get_product
from config import ADMIN_ID
from app.sender import sender


import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать!', reply_markup=kb.main)
    if message.from_user.id == int(ADMIN_ID):
        await message.answer(f'Вы авторизовались как администратор!', reply_markup=kb.main_admin)


@router.message(F.text == 'Админка')
async def catalog(message: Message):
    if message.from_user.id == int(ADMIN_ID):
        await message.answer(f'Вы вошли в админ панель', reply_markup=kb.admin_panel)
    else:
        await message.answer('Я вас не понимаю!')


#@router.message(F.text =='id')
#async def cmd_id(message: Message):
#    return message.answer(f'{message.from_user.id}')


@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберите вариант из каталога', reply_markup=await kb.categories())


@router.message(F.text == 'Контакты')
async def about(message: Message):
    await message.answer(f'наш инстаграм: inst/test\nнаш вк паблик /test\nнаш тг канал\n')


@router.callback_query(F.data.startswith('category_'))
async def category_selected(callback: CallbackQuery):
    category_id = callback.data.split('_')[1]
    await callback.message.answer(f'Пирсинг в категории "{category_id}":', reply_markup=await kb.products(category_id))
    await callback.answer('')


@router.callback_query(F.data.startswith('product_'))
async def product_selected(callback: CallbackQuery):
    product_id = callback.data.split('_')[1]
    product = await get_product(product_id=product_id)
    await callback.message.answer(f'Выбраный прокол <b>{product.name}</b>\n\nЦена прокола: {product.price}.\n{product.description}')
    await callback.answer('')

@router.message()
async def answerDefault(message: Message):
    await message.reply('Я вас не понимаю!')
