import os

from dotenv import load_dotenv
from utils import functions as util
load_dotenv()


class port80:
    normalUser = False
    rootUser = False
    ROOT_PASS = "tryhackme"
    DECODE_NORMAL_PASS = "hackthebox"
    ENCODE_NORMAL_PASS = "gelunpxzr"
    UPDATE_ROOT_ENCODE_PASS = "cG9zdHN3aWdnZXI="
    UPDATE_ROOT_DECODE_PASS = "postswigger"
    host = "antoine@192.168.0.0"
    BREAK_FILE = "Key2.txt"

    def __init__(self):
        pass

    async def loginCheck(self, ctx):
        await ctx.send("Enter password: ")

        def check(msg):  # check if the information come from the same person
            return msg.author == ctx.author and msg.channel == ctx.channel

        try:
            # take user input with 'message' placeholder
            password = await ctx.bot.wait_for('message', check=check, timeout=60.0)
            # after this password is like an object that have lots of attributes, so we need to access the
            # content of it
        except TimeoutError:
            # if over 60 seconds then kick
            await ctx.send(util.syntaxHighlight("You did not enter password on time, automatically exit","fix"))
            return False

        if password.content == self.DECODE_NORMAL_PASS:  # same pass
            await ctx.send(util.syntaxHighlight(f"Login to {self.host} as normal user port 80 successfully\n",""))
            port80.normalUser = True
            return True
        elif password.content == self.ENCODE_NORMAL_PASS:
            await ctx.send(embed=util.embedColor("Oh crap, the password is encoded by some type of encryption\nComputer has analyzed but can not do anything, just figure out it is ROT13\nPlease ssh again with the decoded password","","WARNING"))
            return False
        elif password.content == self.ROOT_PASS:
            await ctx.send(util.syntaxHighlight(f"Login to {self.host} as root user port 80 successfully\n",""))
            port80.rootUser = True
            return True
        elif password.content == self.UPDATE_ROOT_ENCODE_PASS:
            await ctx.send(embed=util.embedColor("The new password use the new encryption call base64, it totally different from ROT13.Please ssh again","fix","WARNING"))
            return False
        else:
            await ctx.send(embed=util.embedColor("- Wrong password, please try again -","diff","ERROR"))
            return False

    async def listAllFile(self, ctx):
        if self.normalUser:
            await ctx.send(util.syntaxHighlight("1. key1.txt\n2. rootPassword.txt\n",""))
        if self.rootUser:
            await ctx.send(util.syntaxHighlight("1. key1.txt\n2. rootPassword.txt\n3. FullKey.txt\n4. Key2.txt\n5. linkToNuclearWeapon.txt\n",""))

    async def printFile(self, ctx, fileName: str):
        if fileName == 'key1.txt':
            await ctx.send(embed=util.embedColor("EHC{IA-","","FILE: key1.txt"))
        elif fileName == "rootPassword.txt":
            await ctx.send(embed=util.embedColor("tryhackme","","FILE: rootPassword.txt"))
            return True
        elif self.rootUser:
            if fileName == 'FullKey.txt':
                await ctx.send(embed=util.embedColor("EHC{try-your-best}","","FILE: FullKey.txt"))
            elif fileName == 'Key2.txt':
                await ctx.send(embed=util.embedColor("-IS-","","FILE: Key2.txt"))
            elif fileName == 'linkToNuclearWeapon.txt':
                await ctx.send(embed=util.embedColor("antoineHackerLord.com\nuser: EHCno1\npassword:1","","FILE: linkToNuclearWeapon.txt"))
        else:
            await ctx.send(embed=util.embedColor("- No such file exists - ","diff","ERROR"))
        return True

    async def cat(self, ctx, fileName: str):
        if fileName == self.BREAK_FILE and self.ROOT_PASS == "tryhackme":
            port80.ROOT_PASS = self.UPDATE_ROOT_DECODE_PASS
            string = "The computer recognizes unauthorized entry, automatically exit and change the login password. Please ssh back to port 22 to find the new password"
            await ctx.send(embed=util.embedColor(string,"","WARNING"))
                #máy tính nhận ra sự xâm nhập trái phép, tự động thực hiện giao thức trục xuất và thay đổi mật khẩu, '
                #'hãy truy cập vào port 22 để tìm ra mk mới
            return False
        return await self.printFile(ctx, fileName)
