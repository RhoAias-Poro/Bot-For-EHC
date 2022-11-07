import asyncio

from dotenv import load_dotenv

from src.utils import functions as util

load_dotenv()


class port22:
    NEW_ENCODE_ROOT_PASS = "cG9zdHN3aWdnZXI="
    FAKE_ENCODE_ROOT_PASS = "https://www.youtube.com/watch?v=GPXkjtpGCFI&ab_channel=KushMaster"
    host = "antoine@192.168.0.0"

    def __init__(self):
        pass

    async def loginCheck(self, ctx):
        await ctx.send(util.syntaxHighlight(f"Login to {self.host} 22 successfully\n", ""))
        await ctx.send(util.embedColor(
            "This is where the changed password is hidden. Hurry and find it"
            'diff', 'PORT 22'))
        await ctx.send(util.embedColor(
            "When you have access to the host machine, you should do the command $ls to list all the file that can be "
            "access to",
            'diff', 'LS COMMAND'))
        return True

    async def listAllFile(self, ctx):
        await ctx.send(util.syntaxHighlight("1. changedKey.txt\n2. changedKey.text", ""))
        await ctx.send(util.embedColor(
            "To see the conntent of a file, please use command $cat"
            'diff', 'CAT COMMAND'))

    async def cat(self, ctx, fileName: str):
        if fileName == 'changedKey.txt':
            await ctx.send(embed=util.embedColor(f"{self.FAKE_ENCODE_ROOT_PASS}", "", "FILE: changedKey.txt"))
            await ctx.send(util.syntaxHighlight(
                "It looks like a link to somewhere, try to open it",
                ""))
        elif fileName == 'changedKey.text':
            await ctx.send(embed=util.embedColor(f"{self.NEW_ENCODE_ROOT_PASS}", "", "FILE: changedKey.text"))
            await asyncio.sleep(3)
            await ctx.send(util.syntaxHighlight(
                "The new password uses modern encryption called Base64, it is totally different from ROT13. Please "
                "encrypt it and login port 80 again",
                ""))
        else:
            await ctx.send(embed=util.embedColor("- File not found, please try again - ", "diff", "ERROR"))
        return True
