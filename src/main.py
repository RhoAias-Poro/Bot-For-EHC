import os
import discord
import time
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

@bot.command(name ="start")
async def SendMessage(ctx):
    line1 = await ctx.send('Good afternoon Mr/Mrs, the EHC has identified the attack on the government as the key to creating serum that can create super soldiers which was created by the Germans in World War 2.\n')
    time.sleep(10)
    line2 = await ctx.send('There is some trace we can find about the attacker, EHC suspects that Antoine who is committed to inciting revolution by enabling acts of terror in the nation has done it based on the IP and some code left.\n')
    time.sleep(10)
    line3 = await ctx.send('Your mission, should you choose to accept it is to penetrate his machine, retreat the key and delete it. If you got caught during this mission, the EHC will disavow any knowledge of your actions. Good luck\nThis message will be self destructed after 10 seconds')
    time.sleep(10)
    await line1.delete()
    await line2.delete()
    await line3.delete()
@bot.event
async def on_ready():  # event call when the bot is ready to use
    print(f"Logged in as : {bot.user.name}")

pwd = os.getenv("TOKEN")
bot.run(pwd)
