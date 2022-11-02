import asyncio
import os

import discord
from dotenv import load_dotenv

load_dotenv()
from ..utils import functions as util


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
            await ctx.send(embed=util.embedColor(self.CSS, "html", "FILE: base.html"))
        elif fileName == 'script.js':
            await ctx.send(embed=util.embedColor(self.CSS, "js", "FILE: script.js"))
        elif fileName == 'style.css':
            await ctx.send(embed=util.embedColor(self.CSS, "css", "FILE: style.css"))
            await asyncio.sleep(5)
            string = 'Congrats on finding the nuclear key, you have done well. However, we worry that he would change the attack but still happen at the same location. Your final mission is to find the document file containing information about that attack and find the exact name of the place where it takes place.'
            await ctx.send(embed=util.embedColor(string, "", "FINAL MISSION"))
            await asyncio.sleep(3)
            string = '''Our spy tells us that maybe it is hidden at the current directory. You should check it.
                        Remember that you only have 5 minutes left before Antoine finds out everything. Good luck !
                        (P/s: Maybe this could help you: https://devconnected.com/how-to-show-hidden-files-on-linux/.
                        However, due to technical reason, at this time only you must use \'ls_a\' to view the hidden files)
                    '''
            await ctx.send(embed=util.embedColor(string, "", "CLUES FOR YOU"))

        elif fileName == 'test.antoineHackerLord.com':
            await ctx.send('')
        elif fileName == '.secret.txt':
            await ctx.send(self.YOUTUBE)
        elif fileName == '.nothing_special_here.txt':
            await ctx.send(embed=util.embedColor(self.FINALE, "", "FILE: .nothing_special_here.txt"))
            await ctx.send(file=discord.File('C:\\Users\Public\Pictures\QRCODE.png'))
        else:
            await ctx.send('Non such file exist')
        return True

    async def listAllHiddenFile(self, ctx):
        await ctx.send('1. base.html\n2. test.antoineHackerLord.com\n3. .secret.txt\n 4. .nothing_special_here.txt')
