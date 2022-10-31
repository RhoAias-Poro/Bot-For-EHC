import os

from dotenv import load_dotenv

load_dotenv()


class port443:
    host = os.getenv('HOST')
    HTML = os.getenv('HTML')
    JS = os.getenv('JS')
    CSS = os.getenv('CSS')

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
        elif fileName == 'test.antoineHackerLord.com':
            await ctx.send('')
        else:
            await ctx.send('Non such file exist')
        return True
