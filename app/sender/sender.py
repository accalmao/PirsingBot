from aiogram.types import Message
from aiogram import Bot
from aiogram.filters import CommandObject
from aiogram.fsm.context import FSMContext
from sender_state import Steps


async def get_sender(message: Message, command: CommandObject, state: FSMContext):
    if not command.args:
        await message.answer(f'Для создания рассылки введи команду /sender и имя рассылки')
        return

    await message.answer((f'Приступаем создавать рассылку. Имя рассылки -{command.args}\r\n\r\n'
                          f'Отправь мне сообщение которое будет использовано как рекламное'))

    await state.update_data(name_camp=command.args)
    await state.set_state(Steps.get_message)
