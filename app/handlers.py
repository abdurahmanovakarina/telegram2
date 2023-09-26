from aiogram import Router, types, F 
from aiogram.filters import Command
import app.keyboard as kb
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import app.database.requests as db

router = Router()

class Registration(StatesGroup):
    name = State()
    gender = State()
    year = State()
    month = State()
    day = State()
    time = State()


class Choice_of_horoscope(StatesGroup):
    zodiac = State()
    period = State()
    horoscope = State()


@router.message(Command('start'))
async def cmd_start(message: types.Message, state: FSMContext):
    if not db.get_user(message.from_user.id):
        await state.set_state(Registration.name)
        await state.update_data(tg_id=message.from_user.id)
        await message.answer(f'✨Добро пожаловать✨, введите Ваше имя🤗')
    else:
        await message.answer(f"{message.from_user.first_name},  Добро пожаловать!✨\n\nСпасибо, что выбрали данный астро бот.🌙", reply_markup=kb.main)



@router.message(Registration.name)
async def reg_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Registration.gender)
    await message.answer('♂ Выберите пол ♀', reply_markup=kb.genders)
    

@router.callback_query(Registration.gender)
async def reg_gender(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(gender=callback.data)
    await state.set_state(Registration.year)
    await callback.message.answer('📅Выберите год рождения', reply_markup=kb.years)
    

@router.callback_query(Registration.year)
async def reg_year(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(year=callback.data)
    await state.set_state(Registration.month)
    await callback.message.answer('📅Выберите месяц рождения', reply_markup=kb.months)
    
    
@router.callback_query(Registration.month)
async def reg_month(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(month=callback.data)
    await state.set_state(Registration.day)
    await callback.message.answer('📅Выберите день рождения',reply_markup=kb.days)
    
    
@router.callback_query(Registration.day)
async def reg_day(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(day=callback.data)
    data = await state.get_data()
    db.set_user(data['tg_id'], data['name'], data['gender'])
    await callback.message.answer(f"{data['name']},  Вы зарегистрированы!✨\n\nВыберите то что Вас интересует.🌙", reply_markup=kb.main)
    await state.clear()


# ГОРОСКОП
@router.callback_query(F.data == 'horoscopes')
async def choise_horoscope(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Choice_of_horoscope.zodiac)
    await callback.message.edit_text('☯ Выберите знак зодиака ☯', reply_markup=kb.zodiac)
    
    
@router.callback_query(Choice_of_horoscope.zodiac)
async def choise_zodiacI(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(zodiac=callback.data) 
    await state.set_state(Choice_of_horoscope.period)
    await callback.message.edit_text('Выберите период 🪐', reply_markup= kb.period)
    

@router.callback_query(Choice_of_horoscope.period)
async def horoscope_output(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(period=callback.data)
    data = await state.get_data()
    result = db.get_horoscope(data['zodiac'])
    await callback.message.edit_text(f'🪐Ваш гороскоп: {result[1 if data["period"] == "today" else 2 if data["period"] == "tomorrow" else 3 if data["period"] == "month" else 4 if data["period"] == "year" else None]}')
