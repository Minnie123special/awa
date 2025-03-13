
import discord
import asyncio
import random
from discord.ext import commands

# 設定機器人指令前綴
intents = discord.Intents.default()
intents.message_content = True  # 允許讀取訊息內容
bot = commands.Bot(command_prefix="!", intents=intents)

# 指定頻道 ID（請更換為你的 Discord 頻道 ID）
TARGET_CHANNEL_ID = 1341067426577776710  # 這裡填入你的頻道 ID

# 儲存 ping 任務
ping_tasks = {}

@bot.event
async def on_ready():
    print(f"✅ 已登入機器人：{bot.user}")

@bot.command()
async def ping(ctx, member: discord.Member):
    """ 開始持續 Ping 指定用戶（僅限指定頻道） """
    if ctx.channel.id != TARGET_CHANNEL_ID:1341067426577776710
        return

    if member.id in ping_tasks:
        await ctx.send(f"{member.mention} 已經在被 Ping 了！")
        return

    async def ping_loop():
        while member.id in ping_tasks:
            await ctx.send(f"{member.mention} 🏓")
            await asyncio.sleep(2)  # 每 2 秒 Ping 一次

    ping_tasks[member.id] = bot.loop.create_task(ping_loop())
    await ctx.send(f"開始 Ping {member.mention}！")

@bot.command()
async def stop(ctx, member: discord.Member):
    """ 停止 Ping 指定用戶（僅限指定頻道） """
    if ctx.channel.id != TARGET_CHANNEL_ID:1341067426577776710
        return

    if member.id in ping_tasks:
        ping_tasks[member.id].cancel()
        del ping_tasks[member.id]
        await ctx.send(f"已停止 Ping {member.mention}！")
    else:
        await ctx.send(f"{member.mention} 沒有在被 Ping！")

@bot.command()
async def 說(ctx, *, message):
    """ 讓機器人說話（僅限指定頻道） """
    if ctx.channel.id == TARGET_CHANNEL_ID:
        await ctx.send(message)

@bot.command()
async def 隨機(ctx, min_num: int, max_num: int):
    """ 產生一個隨機數字（僅限指定頻道） """
    if ctx.channel.id != TARGET_CHANNEL_ID:
        return

    if min_num > max_num:
        await ctx.send("請確保最小值小於最大值！")
    else:
        number = random.randint(min_num, max_num)
        await ctx.send(f"🎲 隨機數字：{number}")

# 啟動機器人（請填入你的 Token）
bot.run("MTM0OTc1NjM0NjQyNTE0NzUyMw.GDRyZp.r6tA6V-orxZr-LlOfe9hS8DLb3idz-wwyP5CcE")