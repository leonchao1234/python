from pytube import YouTube 
@bot.slash_command(name="repeat",description="可以重複顯示特定的文字")
@discord.option(name="times",description="要重複的次數",resuired=False,defult=1)
async def repeat(ctx,times:int):
    result=""
    for i in range(times):
        result += f"重複第{i+1}次\n"
    await ctx.respond(result)


yt = YouTube("https://www.youtube.com/watch?v=WlfIYn8-1pI")
@bot.slash_command(name="yt_info",description="輸入連結")
@discord.option(name="url",description="超連結",resuired=False,defult=1)
async def yt_info(ctx,url:str):
    result=""
    for i in range(url):
        print(f"影片名稱:{yt.title}")  # 取得影片的標題資訊
        print(f"影片作者:{yt.author}")  # 取得影片的作者資訊
        print(f"影片長度:{yt.length}秒")  # 取得影片的長度資訊
        print(f"縮圖網址:{yt.thumbnail_url}")  # 取得影片的縮圖網址

