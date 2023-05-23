import discord
from discord.ext import commands
from random import randint , choice
import seven
import os
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
points = 0



@bot.command('dice')
async def dice(ctx):
    global points
    points += seven.dice()
    await ctx.channel.send(points)
    


@bot.command('guess_number')
async def guess_number(ctx,x):
    global points
    a,b = seven.guess_number(int(x))
    points += a 
    await ctx.channel.send(f'Вы набрали {a}), выпало такое то число {b} вы выбрали {x}')
    


@bot.command('twenty_one')
async def twenty_one(ctx):
    global points
    pass


@bot.command('img')
async def img(ctx):
    global points
    if points >= 5:
        img_name = choice(os.listdir('img'))
        with open('img/' + img_name, 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    else:
        await ctx.channel.send(f'у тебя не хватает поинтов, твое колличество = {points}')

bot.run('MTAzODc3MjQyOTc0NjYyMjUxNg.GBRWZ2.OJSKhIQ7IERSpzRxI7_-Dp9if_HtLcoQZlVJJE') 


