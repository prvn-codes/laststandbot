import os
import asyncio
import discord
from discord.ext import commands
from discord.ext.commands.core import command

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name="!help"))
    print("Ready!")


async def main():
    print("--- Loading Cogs ---")
    for _, _, files in os.walk('cogs/'):
        for file in files:
            file_name, ext = os.path.splitext(file)
            if file_name.startswith('cog'):
                print(f"{file}")
                await client.load_extension(f'cogs.{file_name}')
        break

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print("--- Done Loading Cogs ---")

# TODO: Enter discord API KEYs
client.run("MTAxODQwOTk4MDM4ODQ1ODU5Ng.GFRuZQ.PWM0nOlqKMjRA_Co31QkNjmoD9R9cSnxd3XKTo")

loop.close()