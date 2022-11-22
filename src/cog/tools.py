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


class Tools(commands.Cog):
    encodeNormalPass = "unpxgurobk"
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
    async def start(self, ctx, *args):
        if len(args) == 0:
            Users.users[ctx.author.id] = Users()
            await ctx.send(embed=util.embedColor(
                f'Rất mừng khi được gặp lại trong nhiệm vụ lần này, EHC đã xác nhận những cuộc tấn công mạng tới máy chủ của chính phủ nhằm chiếm đoạt lấy Key, là chìa khóa để phóng 1 đầu đạn hạt nhân, nếu hẵn có thể kích hoạt được thì nó sẽ mở ra 1 cuộc thảm sát hạt nhân và là cơ sở để các quốc gia cắn xé lẫn nhau, trật tự bị đảo lộn, hòa bình sẽ không còn tồn tại nữa\n',
                "", "STORY"))
            await asyncio.sleep(10)
            await ctx.send(embed=util.embedColor(
                'Có một vài dấu vết hacker đã để lại mà chúng tôi có thể tìm thấy được. EHC nghi ngờ rằng Antoine, 1 phần tử khủng bố, người đã kích động cách mạng bằng cách thực hiện các hành động khủng bố ở nhiều quốc gia là người đứng sau tấm màn.\n',
                "", "STORY"))
            await asyncio.sleep(7)
            await ctx.send(embed=util.embedColor(
                'Nhiệm vụ của bạn, dù bạn chọn chấp nhận, đó là thâm nhập vào máy chủ của hắn, đoạt lại Key cũng như tìm thời gian diễn ra cuộc tấn công. Nếu như bạn bị bắt hoặc bị giết trong thời gian thực thi nhiệm vụ, EHC sẽ từ chối mọi thông tin liên quan tới hành động nào của bạn. Chúc may mắn.\n',
                "", "MISSION"))
            await asyncio.sleep(10)
            await ctx.send(embed=util.embedColor(
                "Một vài note cho bạn: \n  - Key mà bạn cần tìm là: EHC{..._..._..._...}\n  - Hãy cẩn thận các dấu cách(space) trong câu lệnh, chúng rất là quan trong.\n  - Nếu bạn gặp phải bất kì loại mã hóa nào thì bạn có thể tìm kiếm những phương thức giải mã trực tuyến với từ khóa như 'encryption_name + decoder + online'\n\nOK LET'S BEGIN",
                "fix", "NOTE"))
            await asyncio.sleep(7)
            await ctx.send(embed=util.embedColor(
                f"Host address: {self.host}\nPassword: {self.encodeNormalPass}\nĐây là những thông tin mà chúng tôi có thể tìm được, tuy không biết mật khẩu của port nào nhưng nó đã bị mã hóa bằng ROT13, hãy thử giải mã nó 😥",
                "", "INFORMATION YOU NEED"))
            await asyncio.sleep(7)
            await ctx.send(embed=util.embedColor(
                "Việc bạn cần làm tiếp theo đó là scan host hoặc website để có thể tìm được ra cổng để có thể kết nối tới\nĐể scan được 1 host thì bạn có thể sử dụng lệnh scan: $scan host/address/website",
                "", "SCAN COMMAND"))
        else:
            raise commands.CommandInvokeError(self, Exception)

    @start.error
    async def start_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(
                embed=util.embedColor("Nhập sai lệnh, hãy nhập $start", "diff", "START"))

    @commands.command()
    @commands.dm_only()
    async def scan(self, ctx, *args):
        if len(args) == 1:
            if args[0] == self.host:  # if the correct host then return the portal
                await ctx.send(embed=util.embedColor(f"{self.host} trả về port: 80, 22\n", "", "SCAN RESULT"))
                await asyncio.sleep(2)
                await ctx.send(embed=util.embedColor(
                    'Để có thể kết nối tới host bạn cần sử dụng lệnh ssh(một giao thức mạng có thể cung cấp 1 phương pháp kết nối bảo mật tới 1 máy tính từ xa\nĐể hiểu hơn, bạn có thể truy cập vào đường link: '
                    + 'https://www.techtarget.com/searchsecurity/definition/Secure-Shell\n'
                    + 'lệnh SSH: $ssh host address -p port_number\n', "", "SSH COMMAND"))
            elif args[0] == self.website:
                await ctx.send(embed=util.embedColor(f"{self.website} trả về port: 443\n", "", "SCAN RESULT"))
                await asyncio.sleep(5)
                await ctx.send(embed=util.embedColor(
                    'Để kết nối tới website thì bạn có thể sử dụng lệnh ssh như lúc trước nhưng có 1 vài sự thay đổi '
                    + 'lệnh SSH: $ssh UserName@SSHserver.example.com  -p port_number\n', "", "SSH COMMAND"))
            else:
                await ctx.send(embed=util.embedColor("'Port kết nối tới không khả dụng\n'", "diff", "ERROR"))
        else:
            raise commands.CommandInvokeError(self, Exception)

    @scan.error
    async def scan_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(
                embed=util.embedColor(
                    "Thiếu hoặc thừa các tham số trong câu lệnh\nCách sử dụng: scan host_name/website\n",
                    "diff", "ERROR"))

    @commands.command()
    @commands.dm_only()
    async def ssh(self, ctx, *args):
        if len(args) == 3:
            if Users.users[ctx.author.id].Login:  # check if user have entered already
                await ctx.send(util.syntaxHighlight(
                    f"'Bạn đã kết nối tới host {self.host} port {Users.users[ctx.author.id].portNumber}\nBạn có thể sử dụng lệnh $exit để thoát ra khỏi host kết nối hiện tại",
                    ""))
            else:
                if args[1] != '-p':
                    await ctx.send(
                        embed=util.embedColor("- Thuộc tính không đúng. Bạn có thể sử dụng '-p' ", "diff", "ERROR"))
                else:
                    match args[2]:
                        case '80':
                            if args[0] != self.host:
                                await ctx.send(
                                    embed=util.embedColor("- Host kết nối không khả dụng - ", "diff", "ERROR"))
                            else:
                                Users.users[ctx.author.id].port = port80()
                                Users.users[ctx.author.id].portNumber = args[2]
                                await Users.users[ctx.author.id].port.loginCheck(ctx)
                        case '22':
                            if args[0] != self.host:
                                await ctx.send(
                                    embed=util.embedColor("- Host kết nối không khả dụng - ", "diff", "ERROR"))
                            else:
                                Users.users[ctx.author.id].port = port22()
                                Users.users[ctx.author.id].portNumber = args[2]
                                await Users.users[ctx.author.id].port.loginCheck(ctx)
                        case '443':
                            if args[0] != self.webLogin:
                                await ctx.send(
                                    embed=util.embedColor("- Host kết nối không khả dụng - ", "diff", "ERROR"))
                            else:
                                Users.users[ctx.author.id].port = port443()
                                Users.users[ctx.author.id].portNumber = args[2]
                                await Users.users[ctx.author.id].port.loginCheck(ctx)
                        case _:
                            await ctx.send(
                                embed=util.embedColor(f"Host hiện tại không có port {args[2]} để kết nối\n", "diff",
                                                      "ERROR"))
                    if Users.users[ctx.author.id].Login == False:
                        Users.users[ctx.author.id].port = None
                        Users.users[ctx.author.id].portNumber = None
        else:
            raise commands.CommandInvokeError(self, Exception)

    @ssh.error
    async def ssh_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(
                embed=util.embedColor(
                    "- Thiếu hoặc thừa các tham số trong câu lệnh.\nCách sử dụng: ssh host_address -p port_number\n",
                    "diff",
                    "ERROR"))

    @commands.command()
    @commands.dm_only()
    async def exit(self, ctx, *args):
        if Users.users[ctx.author.id].Login and len(args) == 0:  # if user have login to the host, then exit
            if Users.users[ctx.author.id].portNumber == '80' or Users.users[ctx.author.id].portNumber == '22':
                await ctx.send(
                    embed=util.embedColor(
                        'Thoát ra host: ' + self.host + ' port ' + Users.users[
                            ctx.author.id].portNumber + ' thành công\n',
                        'diff', "Exit Successfully"))
            elif Users.users[ctx.author.id].portNumber == '443':
                await ctx.send(
                    embed=util.embedColor(
                        'Thoát ra host: ' + self.website + ' port ' + Users.users[
                            ctx.author.id].portNumber + ' thành công\n',
                        'diff', 'Exit Successfully'))
            Users.users[ctx.author.id].Login = False
            Users.users[ctx.author.id].portNumber = None
        else:  # if not
            raise commands.CommandInvokeError(self, Exception)

    @exit.error
    async def exit_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError) and Users.users[ctx.author.id].Login == True:
            await ctx.send(util.syntaxHighlight("- Thừa giá trị trong câu lệnh -", "diff"))
        if isinstance(error, commands.CommandInvokeError) and Users.users[ctx.author.id].Login == False:
            await ctx.send(util.syntaxHighlight("- Hãy đăng nhập trước tiên ! -", "diff"))

    @commands.command()
    @commands.dm_only()
    async def ls(self, ctx, *args):
        if Users.users[ctx.author.id].Login:
            if len(args) == 0:
                await Users.users[ctx.author.id].port.listAllFile(ctx)
            else:
                if args[0] == "-a" and Users.users[ctx.author.id].portNumber == '443' and len(args) == 1:
                    await Users.users[ctx.author.id].port.listAllHiddenFile(ctx)
                elif args[0] == "-a" and (
                        Users.users[ctx.author.id].portNumber == '80' or Users.users[
                    ctx.author.id].portNumber == '22') and len(args) == 1:
                    await Users.users[ctx.author.id].port.listAllFile(ctx)
                else:
                    raise commands.CommandInvokeError(self, Exception)
        else:
            raise commands.CommandInvokeError(self, Exception)

    @ls.error
    async def ls_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError) and Users.users[ctx.author.id].Login == True:
            await ctx.send(util.syntaxHighlight("- Thuộc tính không đúng, bạn có thể sử dụng '-a' -", "diff"))
        if isinstance(error, commands.CommandInvokeError) and Users.users[ctx.author.id].Login == False:
            await ctx.send(util.syntaxHighlight("- Hãy đăng nhập trước tiên ! -", "diff"))

    @commands.command()
    @commands.dm_only()
    async def cat(self, ctx, *args):
        if Users.users[ctx.author.id].Login and len(args) == 1:
            await Users.users[ctx.author.id].port.cat(ctx, args[0])
        else:
            raise commands.CommandInvokeError(self, Exception)

    @cat.error
    async def cat_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError) and Users.users[ctx.author.id].Login == True:
            await ctx.send(
                embed=util.embedColor("- Thừa giá trị trong câu lệnh, cách sử dụng: $cat file -\n", "diff", "ERROR"))
        if isinstance(error, commands.CommandInvokeError) and Users.users[ctx.author.id].Login == False:
            await ctx.send(util.syntaxHighlight("- Hãy đăng nhập trước tiên ! -", "diff"))


async def setup(bot):
    await bot.add_cog(Tools(bot))
