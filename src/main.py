import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import sys
load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=os.getenv("PREFIX"), intents=intents)
sys.path.insert(0,'D:\Download\Bot-For-EHC-master\src\entity')
sys.path.insert(1,'D:\Download\Bot-For-EHC-master\src\\utils')

@bot.event
async def on_ready():  # event call when the bot is ready to use
    print(f"Logged in as : {bot.user.name}")
    await bot.load_extension(f'cog.tools')

@bot.event
async def on_command_error(error,ctx):
    if isinstance(error, commands.CommandNotFound):
        await bot.send_message(ctx.message.channel, "No such command")
    else:
        raise commands.CommandNotFound

bot.run(os.getenv("TOKEN"))
