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
        await ctx.send(util.syntaxHighlight(f"Kết nối tới {self.host} port 22 thành công\n", ""))
        await ctx.send(
            embed=util.embedColor(
                "- Khi mà máy tính nhận ra sự hiện diện của bạn, nó sẽ tự động thay đổi mật khẩu của root user. Đây là nơi lưu trữ những mật khẩu đó. Hãy nhanh chóng tìm nó -",
                'diff',
                'PORT 22'))
        await ctx.send(embed=util.embedColor(
            "- Khi kết nối tới host, bạn nên sử dụng lệnh $ls để hiện các file có trong thư mục hiện tại -",
            'diff', 'PORT 80'))
        return True

    async def listAllFile(self, ctx):
        await ctx.send(util.syntaxHighlight("1. changedKey.txt\n2. changedKey.text", ""))
        await ctx.send(embed=util.embedColor(
            "Để thấy được nội dung của các file, hãy sử dụng lệnh cat: $cat file_name", 'diff', 'CAT COMMAND'))

    async def cat(self, ctx, fileName: str):
        if fileName == 'changedKey.txt':
            await ctx.send(embed=util.embedColor(f"{self.FAKE_ENCODE_ROOT_PASS}", "", "FILE: changedKey.txt"))
            await ctx.send(util.syntaxHighlight("It looks like a link to somewhere, try to open it", ""))
        elif fileName == 'changedKey.text':
            await ctx.send(embed=util.embedColor(f"{self.NEW_ENCODE_ROOT_PASS}", "", "FILE: changedKey.text"))
            await asyncio.sleep(3)
            await ctx.send(util.syntaxHighlight(
                "Mật khẩu mới đã bị mã hóa theo dạng BASE64, nó hoàn toàn khác với ROT13. Hãy giải mã nó và sử dụng lệnh $exit để đăng xuất và kết nối tới port 80 với mật khẩu đã thay đổi",
                ""))
        else:
            await ctx.send(embed=util.embedColor("- Không file nào như vậy tồn tại - ", "diff", "ERROR"))
        return True
