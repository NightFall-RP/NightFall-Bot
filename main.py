# インプレス
import discard
from discord.ext import commands
import logging
import os
import json
import datetime

# 開始前
token = os.getenv('token')
buildnumber = os.getenv('buildnumber')
prefix = os.getenv('prefix')
bot = commands.bot(command_prefix=prefix, intents=discord.Intents.all(), case_insensitive=True)
handler = logging.FileHandler(filename='bot.log', encoding='utf-8', mode='w')
discord.utils.setup_logging(handler=handler, level=logging.DEBUG)


@bot.event
async def on_ready():
    await bot.wait_until_ready()
    logging.info(f'ログイン名： {bot.user.name}#{bot.user.discriminator} | ({bot.user.id})')
    logging.info(f'{len(bot.guilds)}台のサーバーに接続し、 {len(bot.users)}人の可視ユーザーを持つ')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed=discord.Embed(title="建設中", description="コマンドは現在準備中です", color=0xffff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1020479011165569087/1020506110890868746/4034e17d0aad277363ee56842c073e33.png?size=4096")
        embed.add_field(name="コマンドはまだ作成中ですので、今は送信を控えてください。", value="", inline=False)
        embed.set_footer(text=f"四つぼっと、ロキによる | {buildnumber}")
        await ctx.send(embed=embed)
        



