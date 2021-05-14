from setuptools import setup

setup(
    name="discord-ext-games",
    author="Wiper-R",
    version="1.1.3",
    url="https://github.com/Wiper-R/discord-ext-games",
    packages=["discord.ext.games", "discord.ext.games.tic_tac_toe"],
    license="MIT",
    description="This library provides bunch of games that can be played on discord.",
    install_requires=["discord.py>=1.6.1"],
    python_requires=">=3.6.0",
)
