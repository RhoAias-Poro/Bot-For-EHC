import os
import discord
from dotenv import load_dotenv
import asyncio
load_dotenv()


class port443:
    host = os.getenv('HOST')
    HTML = os.getenv('HTML')
    JS = os.getenv('JS')
    CSS = os.getenv('CSS')
    YOUTUBE = os.getenv('YOUTUBE')
    FINALE = os.getenv('FINALE')
    is_done = False
    def __init__(self):
        pass

    async def loginCheck(self, ctx):
        await ctx.send('Login to ' + self.host + ' port 443 successfully\n')
        return True

    async def listAllFile(self, ctx):
        await ctx.send('1. base.html\n2. test.antoineHackerLord.com\n')

    async def xdg_open(self, ctx, fileName: str):
        if fileName == 'base.html':
            await ctx.send(self.HTML)
        elif fileName == 'script.js':
            await ctx.send(self.JS)
        elif fileName == 'style.css':
            await ctx.send(self.CSS)
            await asyncio.sleep(5)
            string='Congrats on finding the nuclear key, you have saved many lives. Unfortunately,our spies have just discovered that Antoine is going to make a heavy weapon purchase with the Al-Qaeda terrorist group from the Middle East. However, details are yet to be revealed. Your final mission is to find the document file containing information about that transaction and find the exact name of the place where it takes place.'      
            temp = str("""```""")+string+str("""```""")
            embed = discord.Embed(color=0x206694, title="FINAL MISSION")
            embed.add_field(name=" ", value=temp)
            await ctx.send(embed=embed)
        elif fileName == 'test.antoineHackerLord.com':
            await ctx.send('')
        elif fileName == '.secret.txt':
            await ctx.send(self.YOUTUBE)
        elif fileName == '.nothing_special_here.txt':
            temp = str("""```""")+self.FINALE+str("""```""")
            embed = discord.Embed(color=0x206694, title="NOTE")
            embed.add_field(name=" ", value=temp)
            await ctx.send(embed=embed)
            # await ctx.send(self.FINALE)
            await ctx.send(file=discord.File('D:\Download\DiscordBot_EHC_Workshop\chall_QR.png'))
        else:
            await ctx.send('Non such file exist')
        return True

    async def listAllHiddenFile(self, ctx):
        await ctx.send('1. base.html\n2. test.antoineHackerLord.com\n3. .secret.txt\n 4. .nothing_special_here.txt') 
   
