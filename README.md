<u><h1>Tic Tac Toe</h1></u>
<h3>Example</h3>

```py
import discord
from discord.ext.games import TicTacToe
from discord.ext import commands

bot = commands.Bot("!")


@bot.event
async def on_ready():
    print("Bot is Ready!")


@bot.command()
async def ttt(ctx, member: discord.Member):
    await TicTacToe(ctx, [ctx.author, member], config={
        'down_right': 675624269073481749,
        'emoji_x':536043344569303041,
    }).start()


bot.run("")
```