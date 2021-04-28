from setuptools import setup

setup(
    name="discord-ext-games",
    author="Wiper-R",
    version="1.0.6",
    packages=["discord.ext.games", "discord.ext.games.tic_tac_toe"],
    license="MIT",
    description="This library provides bunch of games that can be played on discord.",
    install_requires=["discord.py>=1.6.1"],
    python_requires=">=3.6.0",
)

import discord
from discord.ext.games.tic_tac_toe import TicTacToe, Config as TicTacToeConfig
from discord.ext import commands

bot = commands.Bot("!")


@bot.event
async def on_ready():
    print("Bot is Ready!")


# For custom emojis just put in emojis_id or for unicode just put in unicode char.
TicTacToeConfig.update(
    # Reaction Emojis
    down_right=675624269073481749,
    # Blocks
    x=536043344569303041,
)


@bot.command()
async def ttt(ctx, member: discord.Member):
    await TicTacToe(ctx, [ctx.author, member]).start()


bot.run("")