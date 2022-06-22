#!/usr/bin/python3
import discord
import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

client = discord.Client()

allowedJokeTypes = ['Any', 'Misc', 'Programming', 'Dark', 'Pun', 'Spooky', 'Christmas']

@client.event
async def on_message(message):
    # Avoid itself
    if message.author == client.user:
        return

    if message.content == '!help':
        await message.channel.send(
            "I currently understand the following commands:\n"
            "!help - Displays a list of all commands supported by me.\n"
            "!joke - I tell a random joke. You can specify the type of joke by appending with one of the following: " + ' '.join(allowedJokeTypes) + "\n"
        )

    if message.content.startswith('!joke'):
        jokeType = None
        jokeMessage = message.content.split()

        if len(jokeMessage) < 2:
            jokeType = 'Any'

        if len(jokeMessage) >= 2 and jokeMessage[1].capitalize() not in allowedJokeTypes:
            await message.channel.send("I don't understand that joke type. Accepted types are: " + ' '.join(allowedJokeTypes))
            return

        if len(jokeMessage) >= 2 and jokeMessage[1]:
            jokeType = jokeMessage[1].capitalize()

        if jokeType:
            response = requests.get('https://v2.jokeapi.dev/joke/' + jokeType)
            parsed = response.json()

            if parsed['error'] == False:
                await message.channel.send("Here's a cool " + parsed['category'] + " joke.")

                if 'setup' in parsed and 'delivery' in parsed:
                    await message.channel.send(parsed['setup'])
                    time.sleep(1)
                    await message.channel.send(parsed['delivery'])
                elif 'joke' in parsed:
                    await message.channel.send(parsed['joke'])
                else:
                    await message.channel.send("Weird, I've forgotton it already...")
            else:
                await message.channel.send('I have no jokes for you right now. Try again later.')

# Bot token
client.run(BOT_TOKEN)