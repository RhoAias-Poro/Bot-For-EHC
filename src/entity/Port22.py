import os

from dotenv import load_dotenv

load_dotenv()


class port22:
    newEncodeRootPass = os.getenv('UPDATE_ROOT_ENCODE_PASS')
    fakeEncodeRootPass = os.getenv('FAKE_PORT22')
    host = os.getenv('HOST')

    def __init__(self):
        pass

    async def loginCheck(self, ctx):
        await ctx.send('Login to ' + self.host + ' port 22 successfully\n')
        return True

    async def listAllFile(self, ctx):
        await ctx.send(
            "This is a part of storage system that store the changed password. Hurry and find the new password")
        await ctx.send('1. changedKey.txt\n2.changedKey.text')

    async def cat(self, ctx, fileName: str):
        if fileName == 'changedKey.txt':
            await ctx.send(self.fakeEncodeRootPass)
        elif fileName == 'changedKey.text':
            await ctx.send(
                'The new password use the new encryption call base64, it totally different from ROT13, Please encryt '
                + 'it \n')
            await ctx.send(self.newEncodeRootPass)
        else:
            await ctx.send("File not found, please try again.")
        return True
