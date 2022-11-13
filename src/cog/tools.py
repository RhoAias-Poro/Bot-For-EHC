import asyncio

from discord.ext import commands
from dotenv import load_dotenv

from src.entity.Port22 import port22
from src.entity.Port443 import port443
from src.entity.Port80 import port80
# import entity.Port22 as port22
# import entity.Port443 as port443
# import entity.Port80 as port80
from src.entity.UsersData import Users
from src.utils import functions as util

load_dotenv()
users = {}


class Tools(commands.Cog):
    encodeNormalPass = "gelunpxzr"
    host = "antoine@192.168.0.0"
    webLogin = "shine102@antoineHackerLord.com"
    website = 'antoineHackerLord.com'

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online')

    @commands.command()
    @commands.dm_only()
    async def start(self, ctx):
        users[ctx.author.id] = Users()
        await ctx.send(embed=util.embedColor(
            f'Rất mừng khi được gặp lại trong nhiệm vụ lần này, EHC đã xác nhận những cuộc tấn công mạng tới máy chủ của chính phủ nhằm chiếm đoạt lấy Key, là chìa khóa để phóng 1 đầu đạn hạt nhân, nếu hẵn có thể kích hoạt được thì nó sẽ mở ra 1 cuộc thảm sát hạt nhân và là cơ sở để các quốc gia cắn xé lẫn nhau, trật tự bị đảo lộn, hòa bình sẽ không còn tồn tại nữa\n',
            "", "STORY"))
        await asyncio.sleep(10)
        await ctx.send(embed=util.embedColor(
            'Có một vài dấu vết hacker đã để lại mà chúng tôi có thể tìm thấy được. EHC nghi ngờ rằng Antoine, 1 phần tử khủng bố, người đã kích động cách mạng bằng cách thực hiện các hành động khủng bố ở nhiều quốc gia là người đứng sau tấm màn.\n',
            "", "STORY"))
        await asyncio.sleep(7)
        await ctx.send(embed=util.embedColor(
            'Nhiệm vụ của bạn, việc bạn chọn chấp nhận, đó là thâm nhập vào máy chủ của hắn, đoạt lại Key cũng như tìm địa điểm của nơi hắn định tấn công. Nếu như bạn bị bắt hoặc bị giết trong thời gian thực thi nhiệm vụ, EHC sẽ từ chối mọi thông tin liên quan tới hành động nào của bạn. Chúc may mắn.\n',
            "", "MISSION"))
        await asyncio.sleep(10)
        await ctx.send(embed=util.embedColor(
            "Một vài note cho bạn: \n  - Key mà bạn cần tìm là: EHC{...-...-...}\n  - Hãy cẩn thận các dấu cách(space) trong câu lệnh, chúng rất là quan trong.\n  - Nếu bạn gặp phải bất kì loại mã hóa nào thì bạn có thể tìm kiếm những phương thức giải mã trực tuyến với từ khóa như 'encryption_name + decoder + online'\n\nOK LET'S BEGIN",
            "fix", "NOTE"))
        await ctx.send(embed=util.embedColor(
            f"Host address: {self.host}\nPassword: {self.encodeNormalPass}\nCó vẻ như mật khẩu đã bị mã hóa bằng ROT13, hãy thử giải mã nó 😥",
            "",
            "INFORMATION YOU NEED"))
        await ctx.send(embed=util.embedColor(
            "Việc bạn cần làm tiếp theo đó là scan host hoặc website để có thể tìm được ra cổng để có thể kết nối tới\nĐể scan được 1 host thì bạn có thể sử dụng lệnh scan: $scan host/address/website",
            "", "SCAN COMMAND"))

    @commands.command()
    @commands.dm_only()
    async def scan(self, ctx, hostStr: str):
        if hostStr == self.host:  # if the correct host then return the portal
            await ctx.send(embed=util.embedColor(f"{self.host} trả về port: 22, 80\n", "", "SCAN RESULT"))
            await asyncio.sleep(4)
            await ctx.send(embed=util.embedColor(
                'Để có thể kết nối tới host bạn cần sử dụng lệnh ssh(một giao thức mạng có thể cung cấp 1 phương pháp kết nối bảo mật tới 1 máy tính từ xa\nĐể hiểu hơn, bạn có thể truy cập vào đường link: '
                + 'https://www.techtarget.com/searchsecurity/definition/Secure-Shell\n'
                + 'lệnh SSH: $ssh host address -p port_number\n', "", "SSH COMMAND"))
        elif hostStr == self.website:
            await ctx.send(embed=util.embedColor(f"{self.website} trả về port: 443\n", "", "SCAN RESULT"))
            await asyncio.sleep(4)
            await ctx.send(embed=util.embedColor(
                'Để kết nối tới website thì bạn có thể sử dụng lệnh ssh như lúc trước nhưng có 1 vài sự thay đổi '
                + 'lệnh SSH: $ssh UserName@SSHserver.example.com  -p port_number\n', "", "SSH COMMAND"))
        else:
            await ctx.send(embed=util.embedColor("'Port kết nối tới không khả dụng\n'", "diff", "ERROR"))

    @scan.error
    async def scan_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                embed=util.embedColor("Thiếu các tham số trong câu lệnh\nCách sử dụng: scan host_name/website\n",
                                      "diff", "ERROR"))

    @commands.command()
    @commands.dm_only()
    async def ssh(self, ctx, hostStr: str, portStr: str, portNum: str):
        if users[ctx.author.id].Login:  # check if user have entered already
            await ctx.send(util.syntaxHighlight(
                f"'Bạn đã kết nối tới host {self.host} port {users[ctx.author.id].portNumber}\nBạn có thể sử dụng lệnh $exit để thoát ra khỏi host kết nối hiện tại",
                ""))
        else:
            if portStr != '-p':
                await ctx.send(
                    embed=util.embedColor("- Thuộc tính không đúng. Bạn có thể sử dụng '-p' ", "diff", "ERROR"))
            else:
                match portNum:
                    case '80':
                        if hostStr != self.host:
                            await ctx.send(embed=util.embedColor("- Host kết nối không khả dụng - ", "diff", "ERROR"))
                        else:
                            users[ctx.author.id].port = port80()
                            users[ctx.author.id].portNumber = portNum
                            users[ctx.author.id].Login = await users[ctx.author.id].port.loginCheck(ctx)
                    case '22':
                        if hostStr != self.host:
                            await ctx.send(embed=util.embedColor("- Host kết nối không khả dụng - ", "diff", "ERROR"))
                        else:
                            users[ctx.author.id].port = port22()
                            users[ctx.author.id].portNumber = portNum
                            users[ctx.author.id].Login = await users[ctx.author.id].port.loginCheck(ctx)
                    case '443':
                        if hostStr != self.webLogin:
                            await ctx.send(embed=util.embedColor("- Host kết nối không khả dụng - ", "diff", "ERROR"))
                        else:
                            users[ctx.author.id].port = port443()
                            users[ctx.author.id].portNumber = portNum
                            users[ctx.author.id].Login = await users[ctx.author.id].port.loginCheck(ctx)
                    case _:
                        await ctx.send(
                            embed=util.embedColor(f"Host hiện tại không có port {portStr} để kết nối\n'", "diff",
                                                  "ERROR"))

    @ssh.error
    async def ssh_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                embed=util.embedColor(
                    "- Thiếu các tham số trong câu lệnh.\nCách sử dụng: ssh host_address -p port_number\n", "diff",
                    "ERROR"))

    @commands.command()
    @commands.dm_only()
    async def exit(self, ctx):
        if users[ctx.author.id].Login:  # if user have login to the host, then exit
            if users[ctx.author.id].portNumber == '80' or users[ctx.author.id].portNumber == '22':
                await ctx.send(
                    embed=util.embedColor(
                        'Thoát ra host: ' + self.host + ' port ' + users[ctx.author.id].portNumber + ' thành công\n',
                        'diff', "Exit Successfully"))
            elif users[ctx.author.id].portNumber == '443':
                await ctx.send(
                    embed=util.embedColor(
                        'Thoát ra host: ' + self.website + ' port ' + users[ctx.author.id].portNumber + ' thành công\n',
                        'diff', 'Exit Successfully'))
            users[ctx.author.id].Login = False
            users[ctx.author.id].portNumber = None
        else:  # if not
            await ctx.send(embed=util.embedColor('Bạn chưa đăng nhập vào host hay website nào để đăng xuất\n', 'diff',
                                                 'EXIT ERROR'))

    @commands.command()
    @commands.dm_only()
    async def ls(self, ctx, *args):
        if users[ctx.author.id].Login:
            if len(args) != 1:
                await users[ctx.author.id].port.listAllFile(ctx)
            else:
                if args[0] == "-a" and users[ctx.author.id].portNumber == '443':
                    await users[ctx.author.id].port.listAllHiddenFile(ctx)
                elif args[0] == "-a" and (
                        users[ctx.author.id].portNumber == '80' or users[ctx.author.id].portNumber == '22'):
                    await users[ctx.author.id].port.listAllFile(ctx)
                else:
                    raise commands.CommandInvokeError(self, Exception)
        else:
            raise commands.CommandInvokeError(self, Exception)

    @ls.error
    async def ls_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError) and users[ctx.author.id].Login == True:
            await ctx.send(util.syntaxHighlight("- Thuộc tính không đúng, bạn có thể sử dụng '-a' -", "diff"))
        if isinstance(error, commands.CommandError) and users[ctx.author.id].Login == False:
            await ctx.send(util.syntaxHighlight("- Hãy đăng nhập trước tiên ! -", "diff"))

    @commands.command()
    @commands.dm_only()
    async def cat(self, ctx, fileName: str):
        if users[ctx.author.id].Login:
            users[ctx.author.id].Login = await users[ctx.author.id].port.cat(ctx, fileName)
        else:
            raise commands.CommandInvokeError(self, Exception)

    @cat.error
    async def cat_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError) and users[ctx.author.id].Login == True:
            await ctx.send(embed=util.embedColor("- Thiếu các tham số trong câu lệnh -\n", "diff", "ERROR"))
        if isinstance(error, commands.CommandError) and users[ctx.author.id].Login == False:
            await ctx.send(util.syntaxHighlight("- Hãy đăng nhập trước tiên ! -", "diff"))


async def setup(bot):
    await bot.add_cog(Tools(bot))
