import asyncio

from dotenv import load_dotenv

from src.entity.UsersData import Users
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
        await ctx.send(util.syntaxHighlight("Hãy nhập mật khẩu: ", ""))

        def check(msg):  # check if the information come from the same person
            return msg.author == ctx.author and msg.channel == ctx.channel

        try:
            # take user input with 'message' placeholder
            password = await ctx.bot.wait_for('message', check=check, timeout=60.0)
            # after this password is like an object that have lots of attributes, so we need to access the
            # content of it
        except TimeoutError:
            # if over 60 seconds then kick
            Users.users[ctx.author.id].Login = False
            await ctx.send(
                util.syntaxHighlight("Bạn không nhập mật khẩu trong 1 khoảng thời gian, tự động đăng xuất", "fix"))
            return
        if password.content == self.DECODE_NORMAL_PASS:  # same pass
            Users.users[ctx.author.id].Login = True
            port80.normalUser = True
            await ctx.send(util.syntaxHighlight(f"Đăng nhập tới {self.host} port 80 như normal user thành công\n", ""))
            await asyncio.sleep(2)
            await ctx.send(
                embed=util.embedColor("- Hãy nhớ rằng mỗi câu lệnh đều bắt đầu bằng $ -", "diff", "PREFIX REMINDER"))
            await asyncio.sleep(2)
            await ctx.send(embed=util.embedColor(
                "- Khi kết nối tới host, bạn nên sử dụng lệnh $ls để hiện các file có trong thư mục hiện tại -",
                'diff', 'PORT 80'))
            return
        elif password.content == self.ENCODE_NORMAL_PASS:
            Users.users[ctx.author.id].Login = False
            await ctx.send(embed=util.embedColor(
                "- Mật khẩu đã bị mã hóa theo dạng ROT13\nHãy kết nối lại với mật khẩu đã được giải mã -",
                "", "WARNING"))
            return
        elif password.content == self.ROOT_PASS:
            port80.rootUser = True
            Users.users[ctx.author.id].Login = True
            await ctx.send(util.syntaxHighlight(f"Đăng nhập tới {self.host} port 80 như root user thành công\n", ""))
            await asyncio.sleep(2)
            await ctx.send(
                embed=util.embedColor("- Hãy nhớ rằng mỗi câu lệnh đều bắt đầu bằng $ -", "diff", "PREFIX REMINDER"))
            await asyncio.sleep(2)
            await ctx.send(embed=util.embedColor(
                "- Khi đã có quyền hạn của root user, bạn nên sử dụng lệnh $ls lại để có thể nhìn thấy các file mà từng bị ẩn đi vì không đủ quyền hạn -",
                'diff', 'PORT 80'))
            return
        elif password.content == self.UPDATE_ROOT_ENCODE_PASS:
            Users.users[ctx.author.id].Login = False
            await ctx.send(embed=util.embedColor(
                "- Mật khẩu mới đã bị mã hóa theo dạng BASE64, nó hoàn toàn khác với ROT13\nHãy kết nối lại với mật khẩu đã được giải mã -",
                "fix", "WARNING"))
            return
        else:
            Users.users[ctx.author.id].Login = False
            await ctx.send(
                embed=util.embedColor("- Sai mật khẩu, xin hãy kết nối lại với mật khẩu đúng -", "diff", "ERROR"))
            return

    async def listAllFile(self, ctx):
        if self.normalUser:
            await ctx.send(util.syntaxHighlight("1. key1.txt\n2. rootPassword.txt\n", ""))
            await asyncio.sleep(2)
            await ctx.send(embed=util.embedColor(
                "Để thấy được nội dung của các file, hãy sử dụng lệnh cat: $cat file_name", 'diff', 'CAT COMMAND'))
        if self.rootUser:
            await ctx.send(util.syntaxHighlight(
                "1. key1.txt\n2. rootPassword.txt\n3. FullKey.txt\n4. Key2.txt\n5. linkToNuclearWeapon.txt\n", ""))
            await asyncio.sleep(2)
            await ctx.send(embed=util.embedColor(
                "Để thấy được nội dung của các file, hãy sử dụng lệnh cat: $cat file_name", 'diff', 'CAT COMMAND'))

    async def printFile(self, ctx, fileName: str):
        Users.users[ctx.author.id].Login = True
        if fileName == 'key1.txt':
            await ctx.send(embed=util.embedColor("mak3_", "", "FILE: key1.txt"))
            await asyncio.sleep(2)
            await ctx.send(util.syntaxHighlight(
                "Đây là 1/3 key, cố lên 🔥🔥🔥", ""))
        elif fileName == "rootPassword.txt":
            await ctx.send(embed=util.embedColor("tryhackme", "", "FILE: rootPassword.txt"))
            await asyncio.sleep(2)
            await ctx.send(util.syntaxHighlight(
                "Đây là mật khẩu của tài khoản quyền root, hãy đăng nhập lại với mật khẩu này để có quyền lợi cao hơn, để thoát bạn có thể dùng lệnh $exit",
                ""))
        elif self.rootUser:
            if fileName == 'FullKey.txt':
                await ctx.send(embed=util.embedColor("eHc{trY-yoUr_bezt}", "", "FILE: FullKey.txt"))
                await asyncio.sleep(3)
                await ctx.send(util.syntaxHighlight(
                    "Thật giống với Key mà chúng ta tìm, nhưng có gì đó không đúng lắm", ""))
            elif fileName == 'Key2.txt':
                await ctx.send(embed=util.embedColor("IA_gr3", "", "FILE: Key2.txt"))
                await asyncio.sleep(2)
                await ctx.send(util.syntaxHighlight(
                    "Chúng ta đã tìm được 2/3 Key rồi hãy tìm nốt mảnh còn lại nào", ""))
            elif fileName == 'linkToNuclearWeapon.txt':
                await ctx.send(embed=util.embedColor("antoineHackerLord.com\nuser: shine102\npassword: picoctf", "",
                                                     "FILE: linkToNuclearWeapon.txt"))
                await asyncio.sleep(2)
                await ctx.send(util.syntaxHighlight(
                    "1 website xuất hiện, trông thật đáng nghi, bạn hãy $scan để tìm cách kết nối tới nó trước", ""))
        else:
            await ctx.send(embed=util.embedColor("- Không có file nào như vậy tồn tại - ", "diff", "ERROR"))
        return

    async def cat(self, ctx, fileName: str):
        if fileName == self.BREAK_FILE and self.ROOT_PASS == "tryhackme":
            port80.ROOT_PASS = self.UPDATE_ROOT_DECODE_PASS
            Users.users[ctx.author.id].Login = False
            string = "Máy tính nhận ra sự xâm phạm trái phép, tự động thực hiện giao thức trục xuất và thay đổi mật khẩu của root user."
            await ctx.send(embed=util.embedColor(string, "", "WARNING"))
            await asyncio.sleep(7)
            await ctx.send(util.syntaxHighlight(
                "Không hay rồi, chúng ta sẽ phải quay lại nơi lưu trữ mật khẩu thay đổi vậy, theo như máy tính quét thì nó nằm ở port 22, hãy đến đó và lấy mật khẩu thay đổi",
                ""))
            return
        return await self.printFile(ctx, fileName)
