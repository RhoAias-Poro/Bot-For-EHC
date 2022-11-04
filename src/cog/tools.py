import asyncio
from discord.ext import commands
from dotenv import load_dotenv

from entity.Port22 import port22
from entity.Port443 import port443
from entity.Port80 import port80
# import entity.Port22 as port22
# import entity.Port443 as port443
# import entity.Port80 as port80
from entity.UserData import Users
from utils import functions as util

load_dotenv()
users = {}


class Tools(commands.Cog):
    encodeNormalPass = "gelunpxzr"
    host = "antoine@192.168.0.0"
    website = "antoineHackerLord.com"

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online')

    @commands.command()
    async def start(self, ctx):
        users[ctx.author.id] = Users()
        line1 = await ctx.send(embed=util.embedColor(
            'Good afternoon Mr/Mrs, the EHC has identified an attack on the government as the key to creating serum '
            'that '
            'can create super soldiers which was created by the Germans in World War 2.\n', "", "STORY"))
        await asyncio.sleep(5)
        line2 = await ctx.send(embed=util.embedColor(
            'There is some trace we can find about the attacker, EHC suspects that Antoine who is committed to '
            'inciting '
            'revolution by enabling acts of terror in the nation has done it based on the IP and some code left.\n', "", "STORY"))
        await asyncio.sleep(5)
        line3 = await ctx.send(embed=util.embedColor(
            'Your mission, should you choose to accept it is to penetrate his machine, retreat the key and delete it. '
            'If '
            'you got caught during this mission, the EHC will disavow any knowledge of your actions. Good luck\nThis '
            'message will be self destructed after 10 seconds\n', "", "MISSION"))
        await asyncio.sleep(10)
        await line1.delete()  # delete the lines
        await line2.delete()
        await line3.delete()
        await ctx.send(embed=util.embedColor("Few notes for you: \n  - Look carefully for the spaces in the command, they are very important\n  - If you encounter any encryption, you can look for decoder by google with the key word 'encryption_name + decoder + online'\n\nOK LET'S BEGIN", "fix", "NOTE"))
        await ctx.send(embed=util.embedColor(f"Host address: {self.host}\nPassword: {self.encodeNormalPass}\nEvil website: {self.website}", "", "INFORMATION YOU NEED"))
        await ctx.send(embed=util.embedColor("First, you need to scan the host or website to get the appropriate ports. After that you can connect to his machine through those ports.\nTo scan a host, you can use the scan command: scan host address/website (information above)", "", "STEP 1"))
        await ctx.send(embed=util.embedColor(
            'In order to connect the host machine, you need to use SSH( a network protocol that give a secure way to '
            'access a computer remotely\nFor more information you can access: '
            'https://www.techtarget.com/searchsecurity/definition/Secure-Shell\n'
            + 'SSH usage: ssh UserName@SSHserver.example.com(host address)  -p port_number\n', "", "STEP 2"))

    @commands.command()
    async def scan(self, ctx, hostStr: str):
        if hostStr == self.host:  # if the correct host then return the portal
            await ctx.send(embed=util.embedColor("Port for host is: 22, 80\n", "", "SCAN RESULT"))
        elif hostStr == self.website:
            await ctx.send(embed=util.embedColor("Port for host is: 443\n", "", "SCAN RESULT"))
        else:
            await ctx.send(embed=util.embedColor("'Invalid host address\n'", "diff", "ERROR"))

    @scan.error
    async def scan_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=util.embedColor("Missing required arguments\nUsage: scan host_name/website\n", "diff", "ERROR"))

    @commands.command()
    async def ssh(self, ctx, hostStr: str, portStr: str, portNum: str):
        users[ctx.author.id].portNumber = portNum
        if users[ctx.author.id].Login:  # check if user have entered already
            await ctx.send(util.syntaxHighlight(f"'You have already connect to the host: {self.host}\n", ""))
        else:
            if portStr != '-p':
                await ctx.send(embed=util.embedColor("- Invalid attribute. Must be -p ", "diff", "ERROR"))
            else:
                match portNum:
                    case '80':
                        if hostStr != self.host:
                            await ctx.send(embed=util.embedColor("- Invalid host connect - ", "diff", "ERROR"))
                        else:
                            users[ctx.author.id].port = port80()
                            users[ctx.author.id].Login = await users[ctx.author.id].port.loginCheck(ctx)
                    case '22':
                        if hostStr != self.host:
                            await ctx.send(embed=util.embedColor("- Invalid host connect - ", "diff", "ERROR"))
                        else:
                            users[ctx.author.id].port = port22()
                            users[ctx.author.id].Login = await users[ctx.author.id].port.loginCheck(ctx)
                    case '443':
                        if hostStr != self.website:
                            await ctx.send(embed=util.embedColor("- Invalid host connect - ", "diff", "ERROR"))
                        else:
                            users[ctx.author.id].port = port443()
                            users[ctx.author.id].Login = await users[ctx.author.id].port.loginCheck(ctx)
                    case _:
                        await ctx.send(embed=util.embedColor(f"This host does not have port {portStr} to connect\n'", "diff", "ERROR"))

    @ssh.error
    async def ssh_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=util.embedColor("- Missing required arguments.\nUsage: ssh host_address -p port_number\n", "diff", "ERROR"))

    @commands.command()
    async def exit(self, ctx):
        if users[ctx.author.id].Login:  # if user have login to the host, then exit
            await ctx.send('Exit host: ' + self.host + ' port ' + users[ctx.author.id].portNumber + ' successfully\n')
            users[ctx.author.id].Login = False
        else:  # if not
            await ctx.send('You have not enter any host to exist\n')

    # @commands.command()
    # async def ls(self, ctx):
    #     if users[ctx.author.id].Login:
    #         await users[ctx.author.id].port.listAllFile(ctx)
    #     else:
    #         await ctx.send('Command not found')
    @commands.command()
    async def ls(self, ctx, *args):
        if users[ctx.author.id].Login:
            if len(args) != 1:
                await users[ctx.author.id].port.listAllFile(ctx)
            else:
                if args[0] == "-a" and users[ctx.author.id].getPortNumber() == '443':
                    await users[ctx.author.id].port.listAllHiddenFile(ctx)
                elif args[0] == "-a" and users[ctx.author.id].getPortNumber() == '80' or args[0] == "-a" and users[ctx.author.id].getPortNumber() == '22':
                    await users[ctx.author.id].port.listAllFile(ctx)
                else:
                    await ctx.send(embed=util.embedColor("- INVALID ARGUMENT -\n", "diff", "ERROR"))
        else:
            raise commands.CommandInvokeError
    @ls.error
    async def ls_error(ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(util.syntaxHighlight("- INVALID ARGUMENT -", "diff"))
        if isinstance(error, commands.CommandError):
            await ctx.send(util.syntaxHighlight("- PLEASE LOGIN FIRST ! -", "diff"))

    @commands.command()
    async def cat(self, ctx, fileName: str):
        if users[ctx.author.id].Login and users[ctx.author.id].portNumber != '443':
            users[ctx.author.id].Login = await users[ctx.author.id].port.cat(ctx, fileName)
        else: raise commands.CommandInvokeError(Exception)
    @cat.error
    async def cat_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(embed=util.embedColor("- COMMAND ONLY AVAILABLE AT PORT 22,80 -", "diff","ERROR"))
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=util.embedColor("- Missing required arguments -\n", "diff", "ERROR"))
            

    @commands.command()
    async def xdg_open(self, ctx, fileName: str):
        if users[ctx.author.id].Login and users[ctx.author.id].portNumber == '443':
            users[ctx.author.id].Login = await users[ctx.author.id].port.xdg_open(ctx, fileName)
        else: raise commands.CommandInvokeError
    @xdg_open.error
    async def xdg_open_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(embed=util.embedColor("- COMMAND ONLY AVAILABLE AT PORT 443 -", "diff","ERROR"))
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=util.embedColor("- Missing required arguments -\n", "diff", "ERROR"))


async def setup(bot):
    await bot.add_cog(Tools(bot))
