import asyncio

import discord
from dotenv import load_dotenv

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
        /* NO1} */
          }'''
    JS = '''function detonate()
     {
       alert("Self destructed!");
     }'''
    YOUTUBE = 'NB2HI4DTHIXS653XO4XHS33VOR2WEZJOMNXW2L3XMF2GG2B7OY6WIULXGR3TSV3HLBRVC==='
    WEBSITE = 'antoineHackerLord.com'
    FINALE = """
    - COMPLETED ATTACKS: 
        +) 29/02/2019: SPREAD OUT CORONA VIRUS
        +) 20/10/2020: HIJACK INTERNATIONAL AIRPLANE IN CHINA
        +) 09/11/2021: BOMB AT EIFEL TOWER IN FRANCE

    - PLANNING ATTACKS: 
        +) 26/11/2022 AT ********* ********* (FOR SECURITY REASON ONLY SHOW THE ENCODED IMAGE)"""
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
            await ctx.send(
                util.syntaxHighlight("Bạn không nhập mật khẩu trong 1 khoảng thời gian, tự động đăng xuất", "fix"))
            return False

        if password.content == self.PASSWORD:  # same pass
            await ctx.send(util.syntaxHighlight(f"Đăng nhập tới {self.host} qua port 443 thành công\n", ""))
            await ctx.send(embed=util.embedColor(
                "- Khi kết nối tới host, bạn nên sử dụng lệnh $ls để hiện các file có trong thư mục hiện tại -",
                'diff', 'PORT 443'))
            port443.userLogin = True
            return True
        else:
            await ctx.send(embed=util.embedColor("- Sai mật khẩu, hãy kết nối và thử lại -", "diff", "ERROR"))
            return False

    async def listAllFile(self, ctx):
        await ctx.send(
            util.syntaxHighlight("1. base.html\n2. script.js\n3. style.css\n4. antoineHackerLordTest.txt\n", ""))
        await ctx.send(embed=util.embedColor(
            "Để thấy được nội dung của các file, hãy sử dụng lệnh cat: $cat file_name", 'diff', 'CAT COMMAND'))

    async def cat(self, ctx, fileName: str):
        if fileName == 'base.html':
            await ctx.send(embed=util.embedColor(self.HTML, "html", "FILE: base.html"))
        elif fileName == 'script.js':
            await ctx.send(embed=util.embedColor(self.JS, "js", "FILE: script.js"))
        elif fileName == 'style.css':
            await ctx.send(embed=util.embedColor(self.CSS, "css", "FILE: style.css"))
            await asyncio.sleep(5)
            string = '''Xin chúc mừng việc tìm thấy Key của đầu đạn, Bạn đã làm rất tốt. Tuy nhiên, chúng ta vẫn lo lắng rằng chưa biết địa điểm tấn công mà hắn chọn cụ thể sẽ diễn ra ở đâu.\nNhiệm vụ cuối cùng của bạn là tìm file tài liệu chứa thông tin về nơi sẽ diễn ra cuộc tấn công và báo cáo.'''
            await ctx.send(embed=util.embedColor(string, "", "FINAL MISSION"))
            await asyncio.sleep(3)
            string = "Theo như thông tin quét được của siêu máy tính thì nó có thể bị ẩn ở đường dẫn hiện tại. Hãy kiểm tra nó.\nNhớ rằng bạn chỉ còn 5 phút trước khi Antoine phát động tấn công. Good luck !\n(P/s: Cái nàyc có thể giúp ích: https://devconnected.com/how-to-show-hidden-files-on-linux/. Nhưng mà câu lệnh là: $ls -a 😜)"
            await ctx.send(embed=util.embedColor(string, "", "HINT FOR YOU"))

        elif fileName == 'antoineHackerLordTest.txt':
            await ctx.send(embed=util.embedColor("YOU ARE LATE", "", "FILE: antoineHackerLordTest.txt"))
            await ctx.send(util.syntaxHighlight(
                "Không ổn, thời gian sắp hết, bạn phải nhanh lên!!!!!",
                ""))
        elif fileName == '.secret.txt':
            await ctx.send(embed=util.embedColor(self.YOUTUBE, "", "FILE: .secret.txt"))
            await ctx.send(
                util.syntaxHighlight(
                    "Lại 1 loại mã hóa khác. Phân tích cho thấy nó giống như Base64 nhưng không phải. Có lẽ, Base 64/2=? ",
                    ""))
        elif fileName == '.nothing_special_here.txt':
            await ctx.send(embed=util.embedColor(self.FINALE, "", "FILE: .nothing_special_here.txt"))
            await ctx.send(file=discord.File('C:\\Users\ADMIN\Pictures\QRCODE.png'))
            await ctx.send(util.syntaxHighlight(
                "Hình ảnh này thật là kì lạ, đến siêu máy tính không thể phân tích được nó, bạn có thể sử dụng Google Lens để tìm hiểu thêm và nhớ, double of something is the best 🐧.\nĐã gần đến hồi kết của nhiệm vụ này rồi, chúng tôi không thể trợ giúp được gì thêm, hãy nộp Key và địa điểm để thoát khỏi kế hoạch của hắn nào",
                ""))
        else:
            await ctx.send(embed=util.embedColor("- Không file nào như vậy tồn tại - ", "diff", "ERROR"))
        return True

    async def listAllHiddenFile(self, ctx):
        await ctx.send(util.syntaxHighlight(
            "1. base.html\n2. script.js\n3. style.css\n4. antoineHackerLordTest.txt\n5. .secret.txt\n6. .nothing_special_here.txt",
            ""))
