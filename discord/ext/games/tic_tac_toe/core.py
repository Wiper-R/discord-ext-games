import asyncio
import itertools
import discord
from discord import message
from .config import Config
from enum import Enum
from discord.ext import tasks
import traceback


class Move(Enum):
    empty = "empty"
    x = "X"
    o = "O"


class TicTacToe:
    def __init__(self, ctx, users, *, config=None):
        self.ctx = ctx
        self.bot = ctx.bot
        self.users = users
        self._board = [Move.empty for _ in range(9)]
        self._moves = {users[0]: Move.x, users[1]: Move.o}
        self._cycle_users = itertools.cycle(users)
        self._turn_of = next(self._cycle_users)
        self.message = message
        self.winner = None
        self.config = config or {}
        self.refactor_config()
        self.remaining_moves()

    @property
    def emoji_board(self):
        data = []
        for move in self._board:
            if move == Move.empty:
                data.append(self._config["blank"])
            elif move == Move.x:
                data.append(self._config["emoji_x"])
            elif move == Move.o:
                data.append(self._config["emoji_o"])

        return data

    def refactor_config(self):
        self._config = {}
        for slot in Config.__slots__:
            try:
                value = self.config.pop(slot)
            except KeyError:
                value = getattr(Config, slot)

            if isinstance(value, int):
                emoji = self.bot.get_emoji(value)

            elif isinstance(value, str):
                emoji = value
            else:
                raise RuntimeError("Emoji must either be a discord snowflake or a unicode character.")

            self._config[slot] = emoji

        if len(self.config) > 0:
            raise RuntimeError("Invalid configuration values.")

    def remaining_moves(self):
        self._remaining_moves = {}
        for idx, slot in enumerate(Config.__slots__[3:]):
            key = str(self._config[slot])
            self._remaining_moves[key] = idx

    def board_to_embed(self):
        embed = discord.Embed(
            title=f"Tic Tac Toe match {self.users[0]} vs {self.users[1]}", color=discord.Color.blurple()
        )
        board = self.emoji_board
        messages = []

        if len(self._remaining_moves) == 0 and self.winner is None:
            messages.append("Match Draw!\n")
        elif self.winner is None and len(self._remaining_moves) > 0:
            messages.append(f"{self._turn_of} Turn **({self._moves[self._turn_of].value})**\n")
        elif self.winner is not None:
            messages.append(f"Winner {self.winner}!\n")

        messages.append(
            "\n".join(
                (
                    f"{board[0]}\u200b{board[1]}\u200b{board[2]}",
                    f"{board[3]}\u200b{board[4]}\u200b{board[5]}",
                    f"{board[6]}\u200b{board[7]}\u200b{board[8]}",
                )
            )
        )

        embed.description = "\n".join(messages)
        return embed

    @tasks.loop()
    async def take_moves(self):
        def check(payload):
            if self._turn_of != payload.member:
                return False

            if str(payload.emoji) not in self._remaining_moves:
                return False

            return True

        try:
            payload = await self.bot.wait_for("raw_reaction_add", check=check, timeout=30)
            emoji = str(payload.emoji)
        except asyncio.TimeoutError:
            await self.stop()
        else:
            await self.run_move(self._turn_of, emoji)

    async def stop(self):
        self.take_moves.stop()
        await self.ctx.send(f"{self._turn_of} failed to use move.")

    def determine_win(self):

        swapped_moves = {value: key for key, value in self._moves.items()}

        def check_and_store_win(row):
            if row.count(row[0]) == len(row) and row[0] != Move.empty:
                self.winner = swapped_moves[row[0]]
                self.take_moves.stop()
                return True

            return False

        board = self._board.copy()

        # Horizontal _
        for i in range(0, 9, 3):
            row = board[i : i + 3]
            if check_and_store_win(row):
                return

        # Verticle |
        for i in range(3):
            row = []

            for j in range(3):
                row.append(board[3 * j + i])

            if check_and_store_win(row):
                return

        # \ Diagonal
        row = []
        for i in range(0, 9, 4):
            row.append(board[i])

        if check_and_store_win(row):
            return

        # / Diagonal
        row = []
        for i in range(2, 7, 2):
            row.append(board[i])

        if check_and_store_win(row):
            return

    async def run_move(self, member, emoji):
        self._turn_of = next(self._cycle_users)
        move = self._remaining_moves.pop(emoji)
        self._board[move] = self._moves[member]
        self.determine_win()
        embed = self.board_to_embed()
        await self.message.edit(embed=embed)
        if self.winner is None:
            await self.message.clear_reaction(emoji)
        else:
            await self.message.clear_reactions()

    @take_moves.error
    async def error(self, e):
        traceback.print_exc()

    async def send_initial_message(self):
        embed = self.board_to_embed()
        self.message = await self.ctx.send(embed=embed)

    async def apply_reactions(self):
        for move in list(self._config.values())[3:]:
            await self.message.add_reaction(move)

    async def start(self):
        await self.send_initial_message()
        await self.apply_reactions()
        self.take_moves.start()
