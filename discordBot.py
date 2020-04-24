import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')

@client.command(aliases=['emoji'])
async def cursed_emoji(ctx):
    await ctx.send(file=discord.File('cursedKevinImage.png'))

@client.command(aliases=['8ball'])
async def _8ball(ctx,*, question):
    responses = [
        'It is certain',
        'Most Likely',
        'Possibly',
        'No',
        'Definitely not'
        ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
async def spelling(ctx):
    x= await ctx.channel.history(limit=2).flatten()
    message=x[1].content
    sarcasm = ''
    for i in range(len(message)):
        if i % 2 == 0:
            sarcasm += message[i].upper()
        else:
            sarcasm += message[i].lower()
    print(sarcasm)

    await ctx.send(sarcasm)


client.run('TOKEN')
