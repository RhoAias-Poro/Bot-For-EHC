from dotenv import load_dotenv

from src.utils import functions as util

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
    BREAK_FILE = "linkToNuclearWeapon.txt"

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
            await ctx.send(util.syntaxHighlight("You did not enter password on time, automatically exit", "fix"))
            return False

        if password.content == self.DECODE_NORMAL_PASS:  # same pass
            await ctx.send(util.syntaxHighlight(f"Login to {self.host} as normal user port 80 successfully\n", ""))
            await ctx.send(util.embedColor(
                "When you have access to the host machine, you should do the command $ls to list all the file that can be access to",
                'diff', 'PORT 80'))
            port80.normalUser = True
            return True
        elif password.content == self.ENCODE_NORMAL_PASS:
            await ctx.send(embed=util.embedColor(
                "Oh crap, the password is encoded by some type of encryption\nComputer has analyzed but can not do anything, just figure out it is ROT13\nPlease ssh again with the decoded password",
                "", "WARNING"))
            return False
        elif password.content == self.ROOT_PASS:
            await ctx.send(util.syntaxHighlight(f"Login to {self.host} as root user port 80 successfully\n", ""))
            await ctx.send(util.embedColor(
                "When you have access to the root user, you should do the command $ls again to list all the file that which used to be hidden from you"
                'diff', 'PORT 80'))
            port80.rootUser = True
            return True
        elif password.content == self.UPDATE_ROOT_ENCODE_PASS:
            await ctx.send(embed=util.embedColor(
                "The new password use the new encryption call base64, it totally different from ROT13.Please ssh again",
                "fix", "WARNING"))
            return False
        else:
            await ctx.send(embed=util.embedColor("- Wrong password, please login again -", "diff", "ERROR"))
            return False

    async def listAllFile(self, ctx):
        if self.normalUser:
            await ctx.send(util.syntaxHighlight("1. key1.txt\n2. rootPassword.txt\n"))
            await ctx.send(util.embedColor(
                "To see the conntent of a file, please use command $cat"
                'diff', 'CAT COMMAND'))
        if self.rootUser:
            await ctx.send(util.syntaxHighlight(
                "1. key1.txt\n2. rootPassword.txt\n3. FullKey.txt\n4. Key2.txt\n5. linkToNuclearWeapon.txt\n", ""))
            await ctx.send(util.embedColor(
                "To see the conntent of a file, please use command $cat"
                'diff', 'CAT COMMAND'))

    async def printFile(self, ctx, fileName: str):
        if fileName == 'key1.txt':
            await ctx.send(embed=util.embedColor("EHC{IA-", "", "FILE: key1.txt"))
            await ctx.send(util.syntaxHighlight(
                "Here is 1/3 of the key, good job", ""))
        elif fileName == "rootPassword.txt":
            await ctx.send(embed=util.embedColor("tryhackme", "", "FILE: rootPassword.txt"))
            await ctx.send(embed=util.embedColor(
                "Right now you are in normal user login, here you have root password, please use command $exit and login again with root password"))
            return True
        elif self.rootUser:
            if fileName == 'FullKey.txt':
                await ctx.send(embed=util.embedColor("EHC{try-your-best}", "", "FILE: FullKey.txt"))
                await ctx.send(util.syntaxHighlight(
                    "Looks like the key we are looking for, but it feel so strange", ""))
            elif fileName == 'Key2.txt':
                await ctx.send(embed=util.embedColor("-IS-", "", "FILE: Key2.txt"))
                await ctx.send(util.syntaxHighlight(
                    "We have 2/3 know, try to find the last one", ""))
            elif fileName == 'linkToNuclearWeapon.txt':
                await ctx.send(embed=util.embedColor("antoineHackerLord.com\nuser: shine102\npassword: picoctf", "",
                                                     "FILE: linkToNuclearWeapon.txt"))
                await ctx.send(util.syntaxHighlight(
                    "A website huh, look weird, you should $scan it first to get the port of it", ""))
        else:
            await ctx.send(embed=util.embedColor("- No such file exists - ", "diff", "ERROR"))
        return True

    async def cat(self, ctx, fileName: str):
        if fileName == self.BREAK_FILE and self.ROOT_PASS == "tryhackme":
            port80.ROOT_PASS = self.UPDATE_ROOT_DECODE_PASS
            string = "The computer recognizes unauthorized entry, automatically exit and change the login password. Please ssh back to port 22 to find the new password"
            await ctx.send(embed=util.embedColor(string, "", "WARNING"))
            return False
        return await self.printFile(ctx, fileName)
