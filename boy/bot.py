import discord
from nine import *


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
cities = reads_cities()
city = ' '
start = False


mes = []
@client.event
async def on_ready():
    print(f'я запустился')

@client.event

async def on_message(message):
    global city, start
    if message.author == client.user:
        return
    if message.content.startswith('/start'):
        city = random.choice(cities)
        await message.channel.send(city)
        start = True 
        return
    if not start:
        await message.channel.send('Для того чтоыб начать игру напиши старт')
        return
    #============================================================================


    if message.content[0] == city[-1]: 
        city = get_random_citt(message.content[-1])
        await message.channel.send(city)
    else:
        await message.channel.send('Ты проиграл тк я так захотел')
        start = False
    
    
client.run('MTAzODc3MjQyOTc0NjYyMjUxNg.G7sq8X.nbc-nlkMoc1xRzWhNIsC_-Eh0pOEGz1E1lwtZg')
