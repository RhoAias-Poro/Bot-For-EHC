import os

from dotenv import load_dotenv

load_dotenv()


class port80:
    normalUser = False
    rootUser = False
    rootPass = os.getenv('ROOT_PASS')
    decodeNormalPass = os.getenv('DECODE_NORMAL_PASS')
    encodeNormalPass = os.getenv('ENCODE_NORMAL_PASS')
    host = os.getenv('HOST')

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
            await ctx.send('you did not enter password on time, automatic exit')
            return False

        if password.content == self.decodeNormalPass:  # same pass
            await ctx.send('Login to ' + self.host + ' as normal user port 80 successfully\n')
            port80.normalUser = True
            return True
        elif password.content == self.encodeNormalPass:
            await ctx.send('Oh crap, the password is being encode by some type of encryption\n'
                           + 'Computer have analyze but can not do it, just know that the type use for it ROT13\n'
                           + 'Please ssh again')
            return False
        elif password.content == self.rootPass:
            await ctx.send('Login to ' + self.host + ' as root user port 80 successfully\n')
            port80.rootUser = True
            return True
        elif password.content == os.getenv("UPDATE_ROOT_ENCODE_PASS"):
            await ctx.send(
                'The new password use the new encryption call base64, it totally different from ROT13, Please ssh '
                'again')
            return False
        else:
            await ctx.send('Wrong password, please try again')
            return False

    async def listAllFile(self, ctx):
        if self.normalUser:
            await ctx.send('1.key1.txt\n2.rootPassword.txt\n')
        if self.rootUser:
            await ctx.send(
                '1. key1.txt\n2. rootPassword.txt\n3. FullKey.txt\n4. Key2.txt\n5. linkToNuclearWeapon.txt\n')

    async def printFile(self, ctx, fileName: str):
        if fileName == 'key1.txt':
            await ctx.send('EHC{IA-')
        elif fileName == 'rootPassword.txt':
            await ctx.send('tryhackme')
            return True
        elif self.rootUser:
            if fileName == 'FullKey.txt':
                await ctx.send('EHC{try-your-best}')
            elif fileName == 'Key2.txt':
                await ctx.send('-IS-')
            elif fileName == 'linkToNuclearWeapon.txt':
                await ctx.send('antoineHackerLord.com 443\nuser: EHCno1\npassword:1')
        else:
            await ctx.send('')
        return True

    async def cat(self, ctx, fileName: str):
        if fileName == os.getenv('BreakFile') and self.rootPass == os.getenv('ROOT_PASS'):
            port80.rootPass = os.getenv("UPDATE_ROOT_DECODE_PASS")
            await ctx.send(
                'máy tính nhận ra sự xâm nhập trái phép, tự động thực hiện giao thức trục xuất và thay đổi mật khẩu, '
                'hãy truy cập vào port 22 để tìm ra mk mới')
            return False
        return await self.printFile(ctx, fileName)
