from setuptools import setup


readme = ""
with open("README.md", encoding="utf-8") as f:
    readme = f.read()


setup(
    name="discord-ext-games",
    author="Wiper-R",
    version="1.1.5",
    url="https://github.com/Wiper-R/discord-ext-games",
    packages=["discord.ext.games", "discord.ext.games.tic_tac_toe"],
    license="MIT",
    description="This library provides bunch of games that can be played on discord.",
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=["discord.py>=1.6.1"],
    python_requires=">=3.6.0",
)
