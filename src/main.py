import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()  # environment variables

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/",
                   intents=intents)  # set prefix to use command


@bot.command(name="hi")  # if user enter /hi then print out hello
async def SendMessage(ctx):
    await ctx.send('Hello!')


@bot.event
async def on_ready():  # event call when the bot is ready to use
    print(f"Logged in as : {bot.user.name}")
    # await five_minutes_images()


pwd = os.getenv("TOKEN")
bot.run(pwd)
