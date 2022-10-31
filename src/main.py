import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=os.getenv("PREFIX"), intents=intents)


@bot.event
async def on_ready():  # event call when the bot is ready to use
    print(f"Logged in as : {bot.user.name}")
    await bot.load_extension(f'cog.tools')


bot.run(os.getenv("TOKEN"))
