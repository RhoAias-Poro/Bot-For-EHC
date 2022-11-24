import asyncio

from dotenv import load_dotenv

from src.entity.UsersData import Users
from src.utils import functions as util

load_dotenv()


class port443:
    ############# set up variable #######################################################
    userLogin = False
    host = "antoineHackerLord.com"
    HTML = '''
    <!DOCTYPE html>
       <html lang="en">
         <head>
           <meta charset="UTF-8">
           <meta name="viewport" content="width=device-width, initial-scale=1.0">
           <meta http-equiv="X-UA-Compatible" content="ie=edge">
           <link rel="stylesheet" href="style.css">
           <title>On Includes</title>
         </head>
         <body>
           <script src="script.js"></script>
            <!-- you can open file script.js and style.css -->
           <h1>My Life as Terror</h1>
           <p>The greater the suffer, the greater the piece.</p>
           <br>
           <p> Source: EHC </p>
           <button type="button" onclick="greetings();">Say hello</button>
         </body>
       </html>
    '''
    CSS = '''
    body {
        background-color: lightblue;
        /* at_aga1n */
          }'''
    JS = '''function detonate()
     {
       alert("Self destructed!")
     }'''
    YOUTUBE = 'NB2HI4DTHIXS653XO4XHS33VOR2WEZJOMNXW2L3XMF2GG2B7OY6WIULXGR3TSV3HLBRVC==='
    WEBSITE = 'antoineHackerLord.com'
    FINALE = """
    - COMPLETED ATTACKS: 
        +) 11/09/2001: Suicide terrorist attack in the US
        +) 08/03/2014: MH370 DISAPPEARED
        +) 13/11/2015: Bomb in Paris, France
        +) 26/09/2016: Uber's biggest breach
        +) 12/05/2017: Distribute ransomware WannaCry 
    - PLANNING ATTACKS: 
        +) ??/??/????: FPT UNIVERSITY (FOR SECURITY REASON ONLY SHOW THE ENCODED DATE)"""
    PASSWORD = 'picoctf'
    user = 'shine102'

    ##################################################################################################
    def __init__(self):
        pass

    async def loginCheck(self, ctx):
        await ctx.send("Hãy nhập mật khẩu: ")

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

        if password.content == self.PASSWORD:  # same pass
            port443.userLogin = True
            Users.users[ctx.author.id].Login = True
            await ctx.send(util.syntaxHighlight(f"Đăng nhập tới {self.host} qua port 443 thành công\n", ""))
            await asyncio.sleep(2)
            await ctx.send(
                embed=util.embedColor("- Hãy nhớ rằng mỗi câu lệnh đều bắt đầu bằng $ -", "diff", "PREFIX REMINDER"))
            await asyncio.sleep(2)
            await ctx.send(embed=util.embedColor(
                "- Khi kết nối tới host, bạn nên sử dụng lệnh $ls để hiện các file có trong thư mục hiện tại -",
                'diff', 'PORT 443'))
            return
        else:
            Users.users[ctx.author.id].Login = False
            await ctx.send(embed=util.embedColor("- Sai mật khẩu, hãy kết nối và thử lại -", "diff", "ERROR"))
            return

    async def listAllFile(self, ctx):
        await ctx.send(
            util.syntaxHighlight("1. base.html\n2. script.js\n3. style.css\n4. antoineHackerLordTest.txt\n", ""))
        await asyncio.sleep(2)
        await ctx.send(embed=util.embedColor(
            "Để thấy được nội dung của các file, hãy sử dụng lệnh cat: $cat file_name", 'diff', 'CAT COMMAND'))

    async def cat(self, ctx, fileName: str):
        Users.users[ctx.author.id].Login = True
        if fileName == 'base.html':
            await ctx.send(embed=util.embedColor(self.HTML, "html", "FILE: base.html"))
        elif fileName == 'script.js':
            await ctx.send(embed=util.embedColor(self.JS, "js", "FILE: script.js"))
        elif fileName == 'style.css':
            await ctx.send(embed=util.embedColor(self.CSS, "css", "FILE: style.css"))
            await asyncio.sleep(2)
            string = '''Chúc mừng, bạn đã tìm thấy Key của đầu đạn. Những đặc vụ khác cũng đã biết địa điểm tấn công nhưng chúng ta vẫn lo lắng rằng chưa biết thời gian bắt đầu tấn công mà hắn chọn sẽ diễn ra bao giờ.\nNhiệm vụ cuối cùng của bạn là tìm file tài liệu chứa thông tin về thời gian sẽ diễn ra cuộc tấn công và báo cáo lại.\nCÁCH NỘP KEY VÀ Thời gian: EHC{key_DD/MM/YYYY}'''
            await ctx.send(embed=util.embedColor(string, "", "FINAL MISSION"))
            await asyncio.sleep(2)
            string = "Theo như thông tin quét được của siêu máy tính thì nó có thể bị ẩn ở đường dẫn hiện tại. Hãy kiểm tra nó.\nNhớ rằng bạn chỉ còn 5 phút trước khi Antoine phát động tấn công. Good luck !\n(P/s: Cái nàyc có thể giúp ích: https://devconnected.com/how-to-show-hidden-files-on-linux/. Nhưng mà câu lệnh là: $ls -a 😜)"
            await ctx.send(embed=util.embedColor(string, "", "HINT FOR YOU"))
        elif fileName == 'antoineHackerLordTest.txt':
            await ctx.send(embed=util.embedColor("YOU ARE LATE", "", "FILE: antoineHackerLordTest.txt"))
            await asyncio.sleep(2)
            await ctx.send(util.syntaxHighlight("Không ổn, thời gian sắp hết, bạn phải nhanh lên!!!!!", ""))
        elif fileName == '.secret.txt':
            await ctx.send(embed=util.embedColor(self.YOUTUBE, "", "FILE: .secret.txt"))
            await asyncio.sleep(2)
            await ctx.send(
                util.syntaxHighlight(
                    "Lại 1 loại mã hóa khác. Phân tích cho thấy nó giống như Base64 nhưng không phải. Có lẽ, Base 64/2=? ",
                    ""))
        elif fileName == '.nothing_special_here.txt':
            await ctx.send(embed=util.embedColor(self.FINALE, "", "FILE: .nothing_special_here.txt"))
            # await ctx.send(file=discord.File('QRCODE.png'))
            #
            # await ctx.send(util.syntaxHighlight(
            #     "Hình ảnh này thật là kì lạ, đến siêu máy tính không thể phân tích được nó, bạn có thể sử dụng Google Lens để tìm hiểu thêm.\nĐã gần đến hồi kết của nhiệm vụ này rồi, chúng tôi không thể trợ giúp được gì thêm, hãy nộp Key và địa điểm để thoát khỏi kế hoạch của hắn nào",
            #     ""))
            await asyncio.sleep(2)
            await ctx.send(
                embed=util.embedColor("Lúc bắt đầu cũng sẽ là lúc mọi thứ chấm dứt, hãy chấp nhận đi. TAO ĐÃ THẮNG",
                                      "diff", "REVENGE"))
            await asyncio.sleep(3)
            await ctx.send(util.syntaxHighlight(
                "Ôi không, sao ta lại không nghĩ ra, thời gian tấn công sẽ rơi vào lúc thành lập của EHC, bạn hãy tìm nó ...., tìm lấ.....\nLINK RETURN: https://www.facebook.com/ehc.fptu",
                ""))
        else:
            await ctx.send(embed=util.embedColor("- Không file nào như vậy tồn tại - ", "diff", "ERROR"))
        return

    async def listAllHiddenFile(self, ctx):
        await ctx.send(util.syntaxHighlight(
            "1. base.html\n2. script.js\n3. style.css\n4. antoineHackerLordTest.txt\n5. .secret.txt\n6. .nothing_special_here.txt",
            ""))
        await asyncio.sleep(2)
        await ctx.send(embed=util.embedColor(
            "Để thấy được nội dung của các file, hãy sử dụng lệnh cat: $cat file_name", 'diff', 'CAT COMMAND'))
