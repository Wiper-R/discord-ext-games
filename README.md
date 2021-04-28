<u><h2>Tic Tac Toe</h2></u>


<h3>Basic Example - Without Custom Config</h3>

```py
import discord
from discord.ext.games.tic_tac_toe import TicTacToe
from discord.ext import commands

bot = commands.Bot("!")


@bot.event
async def on_ready():
    print("Bot is Ready!")


@bot.command()
async def ttt(ctx, member: discord.Member):
    await TicTacToe(ctx, [ctx.author, member]).start()


bot.run("")
```

<h3>Basic Example - With Custom Config</h3>

```py
import discord
from discord.ext.games.tic_tac_toe import TicTacToe, Config as TicTacToeConfig
from discord.ext import commands

bot = commands.Bot("!")


@bot.event
async def on_ready():
    print("Bot is Ready!")


# For custom emojis just put in emojis_id or for unicode just put in unicode char.
TicTacToeConfig.update(  
    down_right=675624269073481749, # Reaction Emojis
    x=536043344569303041, # Blocks
)


@bot.command()
async def ttt(ctx, member: discord.Member):
    await TicTacToe(ctx, [ctx.author, member]).start()


bot.run("")
```