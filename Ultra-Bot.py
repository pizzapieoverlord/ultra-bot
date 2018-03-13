import discord
import asyncio
import random
client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as :")
    print(client.user.name)
    print("ID:")
    print(client.user.id)
    print("Ready to use")

@client.event
async def on_message (message):
    if message.author == client.user:
        return
    elif message.content.startswith("!ping"):
        await client.send_message(message.channel,"Pong!:ping_pong:")
    elif message.content.startswith("!Ping"):
        await client.send_message(message.channel,"Pong!:ping_pong:")
    elif message.content.startswith("!PING"):
        await client.send_message(message.channel,"Pong!:ping_pong:")
    elif message.content.startswith("!Who ya gonna call?"):
        await client.send_message(message.channel,"Ghost Busters! :ghost:")
    elif message.content.startswith("!Who you gonna call?"):
        await client.send_message(message.channel,"Ghost Busters! :ghost:")
    elif message.content.startswith("!who you gonna call?"):
        await client.send_message(message.channel,"Ghost Busters! :ghost:")
    elif message.content.startswith("!who ya gonna call?"):
        await client.send_message(message.channel,"Ghost Busters! :ghost:")
    elif message.content.startswith("!meme of the day"):
        await client.send_message(message.channel,"Here you go! https://www.youtube.com/watch?v=s8axkOWwyzQ")
    
    elif message.content.startswith("!8ball"):
        await client.send_message(message.channel, random.choice(["It is decidedly so :8ball:",
                                                                 "Without a doubt :8ball:",
                                                                 "Yes, definitely :8ball:",
                                                                 "You may rely on it :8ball:",
                                                                 "As I see it, yes :8ball:",
                                                                 "Most likely :8ball:",
                                                                 "Outlook good :8ball:",
                                                                 "Yes :8ball:",
                                                                 "Signs point to yes :8ball:",
                                                                 "Reply hazy try again :8ball:",
                                                                 "Ask again later :8ball:",
                                                                 "Better not tell you now :8ball:",
                                                                 "Cannot predict now :8ball:",
                                                                 "Concentrate and ask again :8ball:",
                                                                 "Don't count on it :8ball:",
                                                                 "My reply is no :8ball:",
                                                                 "My sources say no :8ball:",
                                                                 "Outlook not so good :8ball:",
                                                                 "Very doubtful :8ball:"]))

    elif message.content.startswith("!embed"):
        emb = (discord.Embed(description="This is an embed! Its pretty sweet! :upside_down:", colour=0x3DF270))
        emb.set_author(name="Hello World!", icon_url='https://profilepics.cf.kik.com/f3nceB8oA-2nP0hrqhn6pSnrTG4/orig.jpg')
        await client.send_message(message.channel, embed=emb)               
        
client.run("NDIyODAwMzkzMjQ4OTY0NjA4.DYhDGw.VVrfWdo5KHPWdKyojjp-YQRHuKo")

