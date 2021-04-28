class _Config:
    def __init__(self):
        __slots__ = (
            "white_page",
            "emoji_x",
            "emoji_o",
            "up_left",
            "up",
            "up_right",
            "left",
            "mid",
            "right",
            "down_left",
            "down",
            "down_right",
        )
        self.__slots__ = __slots__
        self.update()

    def update(self, **kwargs):
        """
        BLOCKS : "white_page", "emoji_x", "emoji_o"

        REACTION_EMOJIS: "up_left", "up", "up_right", "left", "mid", "right", "down_left", "down", "down_right",
        """
        self.blank = kwargs.get("blank", "\N{LARGE BLUE SQUARE}")
        self.emoji_x = kwargs.get("x", "\N{REGIONAL INDICATOR SYMBOL LETTER X}")
        self.emoji_o = kwargs.get("o", "\N{REGIONAL INDICATOR SYMBOL LETTER O}")
        self.up_left = kwargs.get("up_left", "\N{NORTH WEST ARROW}")
        self.up = kwargs.get("up", "\N{UPWARDS BLACK ARROW}")
        self.up_right = kwargs.get("up_right", "\N{NORTH EAST ARROW}")
        self.left = kwargs.get("left", "\N{LEFTWARDS BLACK ARROW}")
        self.mid = kwargs.get("mid", "\N{BLACK SQUARE FOR STOP}")
        self.right = kwargs.get("right", "\N{BLACK RIGHTWARDS ARROW}")
        self.down_left = kwargs.get("bottom_left", "\N{SOUTH WEST ARROW}")
        self.down = kwargs.pop("down", "\N{DOWNWARDS BLACK ARROW}")
        self.down_right = kwargs.pop("down_right", "\N{SOUTH EAST ARROW}")


Config = _Config()