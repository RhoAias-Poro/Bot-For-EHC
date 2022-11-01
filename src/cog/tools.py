import os
import time

from discord.ext import commands
from dotenv import load_dotenv

from src.entity.Port22 import port22
from src.entity.Port443 import port443
from src.entity.Port80 import port80

load_dotenv()


class Tools(commands.Cog):
    Login = False
    port = None
    encodeNormalPass = os.getenv("EN_CODE_NORMAL_PASS")
    host = os.getenv("HOST")
    portNumber = None
    website = os.getenv("website")

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online')

    @commands.command()
    async def start(self, ctx):
        line1 = await ctx.send(
            'Good afternoon Mr/Mrs, the EHC has identified the attack on the government as the key to creating serum '
            'that '
            'can create super soldiers which was created by the Germans in World War 2.\n')
        time.sleep(10)
        line2 = await ctx.send(
            'There is some trace we can find about the attacker, EHC suspects that Antoine who is committed to '
            'inciting '
            'revolution by enabling acts of terror in the nation has done it based on the IP and some code left.\n')
        time.sleep(10)
        line3 = await ctx.send(
            'Your mission, should you choose to accept it is to penetrate his machine, retreat the key and delete it. '
            'If '
            'you got caught during this mission, the EHC will disavow any knowledge of your actions. Good luck\nThis '
            'message will be self destructed after 10 seconds')
        time.sleep(10)
        await line1.delete()  # delete the line
        await line2.delete()
        await line3.delete()
        await ctx.send('Host: ' + self.host + ' | Password: ' + self.encodeNormalPass + '\n')
        await ctx.send(
            'In order to connect the host machine, you need to use SSH(a network protocol that give a secure way to '
            'access a computer over an unsecured network\nFor more information you can access: '
            'https://www.techtarget.com/searchsecurity/definition/Secure-Shell\n '
            + 'SSH command: ssh UserName@SSHserver.example.com  -px\n'
            + 'ssh contain 2 basic element, host address and port(-p), x above is the port number to connect to\n'
            + 'to scan a host, you can use scan command: scan UserName@SSHserver.example.com')

    @commands.command()
    async def scan(self, ctx, hostStr: str):
        if hostStr == self.host:  # if the correct host then return the portal
            await ctx.send('Port for host is: 22, 80\n')
        else:
            await ctx.send('Invalid host address\n')

    @commands.command()
    async def ssh(self, ctx, hostStr: str, portStr: str, portNum: str):
        Tools.portNumber = portNum
        if self.Login:  # check if user have entered already
            await ctx.send('You have already connect to the host: ' + self.host + '\n')
        else:
            if portStr != '-p':
                await ctx.send('Invalid attributes ' + portStr)
            else:
                match portNum:
                    case '80':
                        if hostStr != self.host:
                            await ctx.send('Invalid host connect')
                        else:
                            Tools.port = port80()
                            Tools.Login = await self.port.loginCheck(ctx)
                    case '22':
                        if hostStr != self.host:
                            await ctx.send('Invalid host connect')
                        else:
                            Tools.port = port22()
                            Tools.Login = await self.port.loginCheck(ctx)
                    case '443':
                        if hostStr != self.website:
                            await ctx.send('Invalid host connect')
                        else:
                            Tools.port = port443()
                            Tools.Login = await self.port.loginCheck(ctx)
                    case _:
                        await ctx.send('This host does not have port ' + portStr + ' to connect\n')

    @commands.command()
    async def exit(self, ctx):
        if self.Login:  # if user have login to the host, then exit
            await ctx.send('Exit host: ' + self.host + ' port ' + self.portNumber + ' successfully\n')
            self.Login = False
        else:  # if not
            await ctx.send('You have not enter any host to exist\n')

    @commands.command()
    async def ls(self, ctx):
        if self.Login:
            await self.port.listAllFile(ctx)
        else:
            await ctx.send('Command not found')
    # try:
    #     @commands.command()
    #     async def ls(self, ctx):
    #         if self.Login:
    #             await self.port.listAllFile(ctx, commandType)
    #         else:
    #             await ctx.send('Command not found')
    # except:
    #     async def ifNotA(self, ctx):
    #         await self.port.ultimateList

    @commands.command()
    async def cat(self, ctx, fileName: str):
        if self.Login and self.portNumber != '443':
            Tools.Login = await self.port.cat(ctx, fileName)
        else:
            await ctx.send('Command not found')

    @commands.command()
    async def xdg_open(self, ctx, fileName: str):
        if self.Login and self.portNumber == '443':
            Tools.Login = await self.port.xdg_open(ctx, fileName)
        else:
            await ctx.send('Command not found')


async def setup(bot):
    await bot.add_cog(Tools(bot))
