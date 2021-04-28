<u><h1>Tic Tac Toe</h1></u>
<h3>Example</h3>

```py
import discord
from discord.ext.games.tic_tac_toe import TicTacToe
from discord.ext import commands

bot = commands.Bot("!")


@bot.event
async def on_ready():
    print("Bot is Ready!")

# If you don't want to customize emojis, Just ignore this function
TicTacToeConfig.update(down_right=675624269073481749, x=536043344569303041)


@bot.command()
async def ttt(ctx, member: discord.Member):
    await TicTacToe(ctx, [ctx.author, member]).start()


bot.run("")
```