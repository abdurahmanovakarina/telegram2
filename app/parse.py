import asyncio
import requests
from bs4 import BeautifulSoup
from app.database.requests import set_horoscope


async def parse_hr(zodiac):
    
    day = ['today', 'tomorrow']
    data = []
    
    for i in day:
        print(i)
        response = requests.get(f'https://mirkosmosa.ru/horoscope/{zodiac}/{i}')
        soup = BeautifulSoup(response.text, 'html.parser')
        div = soup.find(class_="horoscope zodiac")
        p = div.p.p
        horoscope = str(p)[3:-4]
        data.append(horoscope)
    return data


async def parse_month_year(zodiac):
    period = ['2023/september', '2023']
    data_month_year = []
    
    for i in period:
        response = requests.get(f'https://mirkosmosa.ru/horoscope/{zodiac}/{i}')
        soup = BeautifulSoup(response.text, 'html.parser')
        div = soup.find(class_="horoscope zodiac")
        p = div.p
        horoscope = str(p)[3:-4]
        data_month_year.append(horoscope)
    return data_month_year


zodiac_signs = {
    'aries': 'aries',
    'taurus': 'taurus',
    'gemini': 'gemini',
    'cancer': 'cancer',
    'leo': 'leo',
    'virgo': 'virgo',
    'libra': 'libra',
    'scorpio': 'scorpio',
    'sagittarius': 'sagittarius',
    'capricorn': 'capricorn',
    'aquarius': 'aquarius',
    'pisces': 'pisces'
}


async def get_all():
    for n, zodiac in zodiac_signs.items():
        data1 = await parse_hr(zodiac)
        data2 = await parse_month_year(zodiac)
        set_horoscope(n, data1[0], data1[1], data2[0], data2[1])
