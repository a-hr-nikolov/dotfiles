"""
Since a lot of the configuration in config.py has to be commented out, here are most of
the snippets that can be used to restore the config.
"""

layouts = [
    # layout.Bsp(**layout_theme),
    # layout.Floating(**layout_theme)
    # layout.RatioTile(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    layout.MonadTall(**layout_theme),
    # layout.MonadWide(**layout_theme),
    layout.Tile(
        shift_windows=True,
        border_width=0,
        margin=0,
        ratio=0.335,
    ),
    layout.Max(
        border_width=0,
        margin=0,
    ),
    # layout.Stack(**layout_theme, num_stacks=2),
    # layout.Columns(**layout_theme),
    # layout.TreeTab(
    #     font = "Ubuntu Bold",
    #     fontsize = 11,
    #     border_width = 0,
    #     bg_color = colors[0],
    #     active_bg = colors[8],
    #     active_fg = colors[2],
    #     inactive_bg = colors[1],
    #     inactive_fg = colors[0],
    #     padding_left = 8,
    #     padding_x = 8,
    #     padding_y = 6,
    #     sections = ["ONE", "TWO", "THREE"],
    #     section_fontsize = 10,
    #     section_fg = colors[7],
    #     section_top = 15,
    #     section_bottom = 15,
    #     level_shift = 8,
    #     vspace = 3,
    #     panel_width = 240
    #     ),
    # layout.Zoomy(**layout_theme),
]


# Found in the keys array

# Dmenu/rofi scripts launched using the key chord SUPER+p followed by 'key'
# KeyChord(
#     [WIN],
#     "p",
#     [
#         Key([], "h", lazy.spawn("dm-hub -r"), desc="List all dmscripts"),
#         Key([], "a", lazy.spawn("dm-sounds -r"), desc="Choose ambient sound"),
#         Key([], "b", lazy.spawn("dm-setbg -r"), desc="Set background"),
#         Key([], "c", lazy.spawn("dtos-colorscheme -r"), desc="Choose color scheme"),
#         Key(
#             [],
#             "e",
#             lazy.spawn("dm-confedit -r"),
#             desc="Choose a config file to edit",
#         ),
#         Key([], "i", lazy.spawn("dm-maim -r"), desc="Take a screenshot"),
#         Key([], "k", lazy.spawn("dm-kill -r"), desc="Kill processes "),
#         Key([], "m", lazy.spawn("dm-man -r"), desc="View manpages"),
#         Key([], "n", lazy.spawn("dm-note -r"), desc="Store and copy notes"),
#         Key([], "o", lazy.spawn("dm-bookman -r"), desc="Browser bookmarks"),
#         Key([], "p", lazy.spawn("rofi-pass"), desc="Logout menu"),
#         Key([], "q", lazy.spawn("dm-logout -r"), desc="Logout menu"),
#         Key([], "r", lazy.spawn("dm-radio -r"), desc="Listen to online radio"),
#         Key([], "s", lazy.spawn("dm-websearch -r"), desc="Search various engines"),
#         Key([], "t", lazy.spawn("dm-translate -r"), desc="Translate text"),
#     ],
# ),
