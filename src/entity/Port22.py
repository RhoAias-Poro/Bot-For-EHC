import os

from dotenv import load_dotenv
from utils import functions as util
import asyncio
load_dotenv()


class port22:
    NEW_ENCODE_ROOT_PASS = "cG9zdHN3aWdnZXI="
    FAKE_ENCODE_ROOT_PASS = "CryptoHack"
    host = "antoine@192.168.0.0"

    def __init__(self):
        pass

    async def loginCheck(self, ctx):
        await ctx.send(util.syntaxHighlight(f"Login to {self.host} 22 successfully\n",""))
        return True

    async def listAllFile(self, ctx):
        await ctx.send(util.syntaxHighlight("1. changedKey.txt\n2. changedKey.text",""))
        await ctx.send(
            util.syntaxHighlight("This is where the changed password is hidden. Hurry and find it",""))
        

    async def cat(self, ctx, fileName: str):
        if fileName == 'changedKey.txt':
            await ctx.send(embed=util.embedColor(f"{self.FAKE_ENCODE_ROOT_PASS}","","FILE: changedKey.txt"))
        elif fileName == 'changedKey.text':
            await ctx.send(embed=util.embedColor(f"{self.NEW_ENCODE_ROOT_PASS}","","FILE: changedKey.text"))
            await asyncio.sleep(3)
            await ctx.send(util.syntaxHighlight("The new password uses modern encryption called Base64, it is totally different from ROT13. Please encrypt it",""))
           
        else:
            await ctx.send(embed=util.embedColor("- File not found, please try again - ","diff","ERROR"))
        return True
