import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from src.utils.functions import embedColor

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=os.getenv("PREFIX"), intents=intents)


# sys.path.insert(0, 'D:\Download\Bot-For-EHC-master\src\entity')
# sys.path.insert(1, 'D:\Download\Bot-For-EHC-master\src\\utils')


@bot.event
async def on_ready():  # event call when the bot is ready to use
    print(f"Logged in as : {bot.user.name}")
    await bot.load_extension(f'src.cog.tools')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(embed=embedColor("- Lệnh không tồn tại!!!! -", "diff", "ERROR"))


@bot.command()
async def red_team(ctx):
    if ctx.channel.id == int(os.getenv("ID2")):
        channel = await ctx.author.create_dm()
        await channel.send(
            embed=embedColor("Welcome to the dark side. Please enter $start to begin the mission", 'diff', "RED TEAM"))
    else:
        await ctx.send("Lỗi vì nhập lệnh không đúng channel", delete_after=3)


bot.run(os.getenv("TOKEN"))
