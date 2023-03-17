import discord
import requests
from load import cities

client = discord.Client(intents=discord.Intents.all())
TOKEN = 'MTA4NTU2NTkxMjA0MTY1NjM4Mg.GDYDPz.xTYYRVPLEX1uxXstYmWLm2Oe0XchSMp_AwiTnM'


def get_duck_url():
    res = requests.get('https://random-d.uk/api/random').json()
    return res['url']


def get_fox():
    res = requests.get('https://randomfox.ca/floof/').json()
    return res['link']

gameon = False

@client.event
async def on_message(message):
    global gameon
    if message.author == client.user:
        return
    if gameon:
        city_user = message.content.lower()
        if city_user not in cities:
            await message.channel.send('Такого города я не знаю')
            return 
        for city in cities:
            if city[0] == city_user[-1]:
                await message.channel.send(city)
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
