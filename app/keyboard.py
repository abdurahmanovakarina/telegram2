from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder, KeyboardBuilder



main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Гороскопы', callback_data='horoscopes')],
                                                [InlineKeyboardButton(text='Натальная карта', callback_data='natal_chart')]])


years = InlineKeyboardBuilder(markup=[[InlineKeyboardButton(text=str(i), callback_data=str(i))] for i in range(1933, 2024)]).adjust(5).as_markup()


months_dict = {
    "January": "Январь",
    "February": "Февраль",
    "March": "Март",
    "April": "Апрель",
    "May": "Май",
    "June": "Июнь",
    "July": "Июль",
    "August": "Август",
    "September": "Сентябрь",
    "October": "Октябрь",
    "November": "Ноябрь",
    "December": "Декабрь"
}

months = InlineKeyboardBuilder(markup=[[InlineKeyboardButton(text=k, callback_data=i)] for i, k in months_dict.items()]).adjust(3).as_markup()

genders = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Женский', callback_data='f')],[InlineKeyboardButton(text='Мужской', callback_data='m')]])

day = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

days = InlineKeyboardBuilder(markup=[[InlineKeyboardButton(text=str(i), callback_data=str(i))] for i in day]).adjust(5).as_markup()

zodiac_dict = {
    "aries": "Овен ♈️",
    "taurus": "Телец ♉️",
    "gemini": "Близнецы ♊️",
    "cancer": "Рак ♋️",
    "leo": "Лев ♌️",
    "virgo": "Дева ♍️",
    "libra": "Весы ♎️",
    "scorpio": "Скорпион ♏️",
    "sagittarius": "Стрелец ♐️",
    "capricorn": "Козерог ♑️",
    "aquarius": "Водолей ♒️",
    "pisces": "Рыбы ♓️"
}

zodiac = InlineKeyboardBuilder(markup=[[InlineKeyboardButton(text=k, callback_data=i)] for i, k in zodiac_dict.items()]).adjust(3).as_markup()

period_dict = {
    "today": "Сегодня",
    "tomorrow": "Завтра",
    "month": "Месяц",
    "year": "Год"
}

period = InlineKeyboardBuilder(markup=[[InlineKeyboardButton(text=k, callback_data=i)] for i, k in period_dict.items()]).adjust(2).as_markup()

