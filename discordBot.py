import discord
from discord.ext import commands
import random
import re

client = commands.Bot(command_prefix = '.')



@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')

#idk why this is here
@client.command(aliases=['emoji'])
async def cursed_emoji(ctx):
    await ctx.send(file=discord.File('cursedKevinImage.png'))

#leftover from a tutorial my friends like it idk why its here
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


#I CaN SpElL GuYs
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


#ioausf ausiof asiof iouaqw uioawio uioua your did it
@client.command(aliases=['Your did it'])
async def your(ctx):
    await ctx.send(file=discord.File('yourDidIt.jpg'))


#alkjsfjkl afsafsj klfas kjla kljafs kljfa slkj im did it
@client.command()
async def im(ctx):
    await ctx.send(file=discord.File('imdidit.png'))

#bubble wrap text thing idk what I'm doing I never comment my code
@client.command()
async def bubble(ctx,*,line):
    n = 3
    x = [line[i:i+n] for i in range(0,len(line),n)]
    output = "||||".join(x)
    output = f'`||{output}||`'
    await ctx.send(output)

client.run('TOKEN')
