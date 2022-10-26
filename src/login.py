import os
import discord
import time
import asyncio
from discord.ext import commands
from dotenv import load_dotenv


intents = discord.Intents.default()
intents.message_content = True
# set prefix '/' to use command
bot = commands.Bot(command_prefix="/", intents=intents)

load_dotenv()  # environment variables
# global const variable
host = os.getenv("HOST")  # host address
# first Encode Normal Password
encodeNormalPass = os.getenv("ENCODENORMALPASS")
# first Decode Normal Password
decodeNormalPass = os.getenv("DECODENORMALPASS")
normalLogin = False  # check if the user is login or not


@bot.command(name="hi")  # if user enter /hi then print out hello
async def SendMessage(ctx):
    await ctx.send('Hello!')


@bot.command(name="start")
async def SendMessage(ctx):
    line1 = await ctx.send('Good afternoon Mr/Mrs, the EHC has identified the attack on the government as the key to creating serum that can create super soldiers which was created by the Germans in World War 2.\n')
    time.sleep(10)
    line2 = await ctx.send('There is some trace we can find about the attacker, EHC suspects that Antoine who is committed to inciting revolution by enabling acts of terror in the nation has done it based on the IP and some code left.\n')
    time.sleep(10)
    line3 = await ctx.send('Your mission, should you choose to accept it is to penetrate his machine, retreat the key and delete it. If you got caught during this mission, the EHC will disavow any knowledge of your actions. Good luck\nThis message will be self destructed after 10 seconds')
    time.sleep(10)
    await line1.delete()  # delete the line
    await line2.delete()
    await line3.delete()
    await ctx.send('Host: ' + host + ' | Password: ' + encodeNormalPass + '\n')
    await ctx.send('In order to connect the host machine, you need to use SSH(a network protocol that give a secure way to access a computer over an unsecured network\nFor more information you can access: https://www.techtarget.com/searchsecurity/definition/Secure-Shell\n'
                   + 'SSH command: ssh UserName@SSHserver.example.com -p x\n'
                   + 'ssh contain 2 basic element, host address and port(-p), x above is the port number to connect to\n'
                   + 'to scan a host, you can use scan command: scan UserName@SSHserver.example.com')


@bot.command(name="scan")
async def scanPort(ctx, hostStr: str):
    if hostStr == host:  # if the correct host then return the portal
        await ctx.send('Port for host is: 22, 80, 443\n')
    else:
        await ctx.send('Invalid host address\n')


@bot.command(name="ssh")
async def connectToAServer(ctx, hostStr: str, portStr: str, portNum: str):
    global normalLogin  # for checking normal user login

    if hostStr != host:  # check host error
        await ctx.send('Invalid host address\n')

    elif portNum != '22' and portNum != '80' and portNum != '443':  # check invalid port
        await ctx.send('This host does not have port ' + portStr + ' to connect\n')

    elif portStr != '-p':  # check invalid paramater
        await ctx.send('Wrong parameter in ssh (recommend -p)\n')

    elif normalLogin == True:  # check if user have enter already
        await ctx.send('You have already connect to the host: ' + host + '\n')

    else:  # enter password
        await ctx.send('Enter password for the host: ')

        def check(msg):  # check if the information come from the same person
            return msg.author == ctx.author and msg.channel == ctx.channel

        try:
            # take user input with 'message' placeholder
            password = await bot.wait_for('message', check=check, timeout=60.0)
            # after this password is like a object that have lots of attributes so we need to access the content of it
        except:
            # if over 60 seconds then kick
            await ctx.send('you did not enter password on time, automatic exit')

        if password.content == decodeNormalPass:  # same pass
            await ctx.send('Login to ' + host + ' successfully\n')
            normalLogin = True
        else:
            await ctx.send('Oh crap, the password is being encode by some type of encryption\n'
                           + 'Computer have analyze but can not do it, just know that the type use for it ROT13\n'
                           + 'Please ssh again')


@bot.command(name="exit")
async def exitCommand(ctx):
    global normalLogin
    if normalLogin == True:  # if user have login to the host, then exit
        await ctx.send('Exist host: ' + host + ' successfully\n')
        normalLogin == False
    else:  # if not
        await ctx.send('You have not enter any host to exist\n')


@bot.event
async def on_ready():  # event call when the bot is ready to use
    print(f"Logged in as : {bot.user.name}")

pwd = os.getenv("TOKEN")
bot.run(pwd)
