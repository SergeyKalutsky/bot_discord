import discord
import random
import requests
from load import cities
from api_token import TOKEN

client = discord.Client(intents=discord.Intents.all())


def get_duck_url():
    res = requests.get('https://random-d.uk/api/random').json()
    return res['url']


def get_fox():
    res = requests.get('https://randomfox.ca/floof/').json()
    return res['link']

gameon = False
used_cities = []
last_letter = ''
@client.event
async def on_message(message):
    global gameon, last_letter
    if message.author == client.user:
        return
    if gameon:
        city_user = message.content.lower()
        if city_user[0] != last_letter and last_letter != '':
            await message.channel.send('Нужно называть город на последнюю букву')
            return 
        if city_user in used_cities:
            await message.channel.send('Такого город уже называли! Попробуйте еще раз')
            return 
        if city_user not in cities:
            await message.channel.send('Такого города я не знаю!')
            return 
        used_cities.append(city_user)
        cities.remove(city_user)
        random.shuffle(cities)
        for city in cities:
            if city[0] == city_user[-1]:
                await message.channel.send(city)
                last_letter = city[-1]
                used_cities.append(city)
                cities.remove(city)
                return
    if message.content == '!game':
        gameon = True
        await message.channel.send('Введите любой город')
        return
    if message.content.lower() == '!duck':
        url = get_duck_url()
        await message.channel.send(url)
        return
    if message.content.lower() == 'как дела?':
        await message.channel.send('Хорошо а у тебя как')
        return
    if message.content.lower() == 'привет':
        await message.channel.send('Привет')
        return
    if message.content.lower() == 'кто самый умный?':
        await message.channel.send('Я')
        return
    await message.channel.send('Привет')


client.run(TOKEN)
