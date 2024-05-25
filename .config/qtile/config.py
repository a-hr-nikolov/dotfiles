# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

import os
import subprocess

# import colors
from libqtile import (  # type: ignore # noqa: F401
    bar,
    extension,
    hook,
    layout,
    qtile,
)
from libqtile.config import (  # type: ignore
    Click,
    Drag,
    Group,
    Key,
    # KeyChord,
    Match,
    Screen,
)
from libqtile.lazy import lazy  # type: ignore

# Make sure 'qtile-extras' is installed or this config will not work.
from qtile_extras import widget  # type: ignore
from qtile_extras.widget.decorations import BorderDecoration  # type: ignore

# Key constants
WIN = "mod4"  # mod4 = super/win in qtile config
ALT = "mod1"  # mod1 = alt
SHIFT = "shift"
CTRL = "control"
L_ARROW = "Left"  # "leftarrow"
R_ARROW = "Right"  # "rightarrow"
U_ARROW = "Up"  # "uparrow"
D_ARROW = "Down"  # "downarrow"
SPACE = "space"
ENTER = "Return"

# User apps
USR_TERM = "kitty"  # My terminal of choice
USR_BRWSR = "firefox"  # My browser of choice
USR_LNCHR = "krunner"  # My launcher of choice
USR_CODE = "code"


# A function for hide/show all the windows in a group
@lazy.function
def minimize_all(qtile):
    for win in qtile.current_group.windows:
        if hasattr(win, "toggle_minimize"):
            win.toggle_minimize()


# A function for toggling between MAX and MONADTALL layouts
@lazy.function
def maximize_by_switching_layout(qtile):
    current_layout_name = qtile.current_group.layout.name
    if current_layout_name == "monadtall":
        qtile.current_group.layout = "max"
    elif current_layout_name == "max":
        qtile.current_group.layout = "monadtall"


keys = [
    ##################
    ### ESSENTIALS ###
    ##################
    Key([WIN], ENTER, lazy.spawn(USR_TERM), desc="Terminal"),
    # Key([MOD, SHIFT], ENTER, lazy.spawn("rofi -show drun"), desc="Run Launcher"),
    # Key([WIN, SHIFT], ENTER, lazy.spawn(USR_LNCHR), desc="Run Launcher"),
    Key([ALT], SPACE, lazy.spawn(USR_LNCHR), desc="Run Launcher"),
    Key([WIN], "b", lazy.spawn(USR_BRWSR), desc="Web browser"),
    Key([WIN], "t", lazy.spawn(USR_TERM), desc="Terminal"),
    # Key([WIN], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([WIN, ALT], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([WIN, SHIFT], "r", lazy.reload_config(), desc="Reload the config"),
    # Key([WIN, SHIFT], "q", lazy.spawn("dm-logout -r"), desc="Logout menu"),
    Key([WIN, CTRL], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key(
        [WIN],
        "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget",
    ),
    ########################
    ### WINDOW SWITCHING ###
    ########################
    # Some layouts like 'monadtall' only need to use j/k to move
    # through the stack, but other layouts like 'columns' will
    # require all four directions h/j/k/l to move around.
    Key([WIN], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([WIN], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([WIN], "j", lazy.layout.down(), desc="Move focus down"),
    Key([WIN], "k", lazy.layout.up(), desc="Move focus up"),
    Key([WIN, ALT], L_ARROW, lazy.layout.left(), desc="Move focus to left"),
    Key([WIN, ALT], R_ARROW, lazy.layout.right(), desc="Move focus to right"),
    Key([WIN, ALT], D_ARROW, lazy.layout.down(), desc="Move focus down"),
    Key([WIN, ALT], U_ARROW, lazy.layout.up(), desc="Move focus up"),
    Key(
        [WIN, ALT],
        SPACE,
        lazy.layout.next(),
        desc="Move window focus to other window",
    ),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [WIN, SHIFT],
        "h",
        lazy.layout.shuffle_left(),
        lazy.layout.move_left().when(layout=["treetab"]),
        desc="Move window to the left/move tab left in treetab",
    ),
    Key(
        [WIN, SHIFT],
        "l",
        lazy.layout.shuffle_right(),
        lazy.layout.move_right().when(layout=["treetab"]),
        desc="Move window to the right/move tab right in treetab",
    ),
    Key(
        [WIN, SHIFT],
        "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down().when(layout=["treetab"]),
        desc="Move window down/move down a section in treetab",
    ),
    Key(
        [WIN, SHIFT],
        "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up().when(layout=["treetab"]),
        desc="Move window up/move up a section in treetab",
    ),
    Key(
        [WIN],
        L_ARROW,
        lazy.layout.shuffle_left(),
        lazy.layout.move_left().when(layout=["treetab"]),
        desc="Move window to the left/move tab left in treetab",
    ),
    Key(
        [WIN],
        R_ARROW,
        lazy.layout.shuffle_right(),
        lazy.layout.move_right().when(layout=["treetab"]),
        desc="Move window to the right/move tab right in treetab",
    ),
    Key(
        [WIN],
        D_ARROW,
        lazy.layout.shuffle_down(),
        lazy.layout.section_down().when(layout=["treetab"]),
        desc="Move window down/move down a section in treetab",
    ),
    Key(
        [WIN],
        U_ARROW,
        lazy.layout.shuffle_up(),
        lazy.layout.section_up().when(layout=["treetab"]),
        desc="Move window up/move up a section in treetab",
    ),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [WIN, SHIFT],
        SPACE,
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    #######################
    ### WINDOW RESIZING ###
    #######################
    # Grow/shrink windows left/right.
    # This is mainly for the 'monadtall' and 'monadwide' layouts
    # although it does also work in the 'bsp' and 'columns' layouts.
    Key(
        [WIN],
        "equal",
        lazy.layout.grow_left().when(layout=["bsp", "columns"]),
        lazy.layout.grow().when(layout=["monadtall", "monadwide"]),
        desc="Grow window to the left",
    ),
    Key(
        [WIN],
        "minus",
        lazy.layout.grow_right().when(layout=["bsp", "columns"]),
        lazy.layout.shrink().when(layout=["monadtall", "monadwide"]),
        desc="Grow window to the left",
    ),
    # Grow windows up, down, left, right.  Only works in certain layouts.
    # Works in 'bsp' and 'columns' layout.
    Key([WIN, CTRL], "h", lazy.layout.grow_left(), desc="Grow window left"),
    Key([WIN, CTRL], "l", lazy.layout.grow_right(), desc="Grow window right"),
    Key([WIN, CTRL], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([WIN, CTRL], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([WIN], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key(
        [WIN],
        "m",
        lazy.layout.maximize(),
        desc="Toggle between min and max sizes",
    ),
    Key([WIN, ALT], "f", lazy.window.toggle_floating(), desc="toggle floating"),
    Key(
        [WIN],
        "f",
        maximize_by_switching_layout(),
        lazy.window.toggle_fullscreen(),
        desc="toggle fullscreen",
    ),
    Key(
        [WIN, SHIFT],
        "m",
        minimize_all(),
        desc="Toggle hide/show all windows on current group",
    ),
    ################
    ### MONITORS ###
    ################
    Key([WIN], "period", lazy.next_screen(), desc="Move focus to next monitor"),
    Key([WIN], "comma", lazy.prev_screen(), desc="Move focus to prev monitor"),
]

groups = []
group_names = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]

group_labels = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]
# group_labels = ["DEV", "WWW", "SYS", "DOC", "VBOX", "CHAT", "MUS", "VID", "GFX",]

group_layouts = [
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        )
    )

for group in groups:
    keys.extend(
        [
            # win + letter of group = switch to group
            Key(
                [WIN],
                group.name,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # win + shift + letter of group = move focused window to group
            Key(
                [WIN, SHIFT],
                group.name,
                lazy.window.togroup(group.name, switch_group=False),
                desc="Move focused window to group {}".format(group.name),
            ),
        ]
    )

colors = [
    ["#282c34", "#282c34"],  # bg
    ["#bbc2cf", "#bbc2cf"],  # fg
    ["#1c1f24", "#1c1f24"],  # color01
    ["#ff6c6b", "#ff6c6b"],  # color02
    ["#98be65", "#98be65"],  # color03
    ["#da8548", "#da8548"],  # color04
    ["#51afef", "#51afef"],  # color05
    ["#c678dd", "#c678dd"],  # color06
    ["#46d9ff", "#46d9ff"],  # color15
]

layout_theme = {
    "border_width": 2,
    "margin": 8,
    "border_focus": colors[8],
    "border_normal": colors[0],
}

layouts = [
    layout.MonadTall(**layout_theme),
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
]

widget_defaults = dict(font="Ubuntu Bold", fontsize=12, padding=0, background=colors[0])

extension_defaults = widget_defaults.copy()


def init_widgets_list():
    widgets_list = [
        widget.Image(
            filename="~/.config/qtile/icons/logo.png",
            scale="False",
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(USR_TERM)},
        ),
        widget.Prompt(font="Ubuntu Mono", fontsize=14, foreground=colors[1]),
        widget.GroupBox(
            fontsize=11,
            margin_y=5,
            margin_x=5,
            padding_y=0,
            padding_x=1,
            borderwidth=3,
            active=colors[8],
            inactive=colors[1],
            rounded=False,
            highlight_color=colors[2],
            highlight_method="line",
            this_current_screen_border=colors[7],
            this_screen_border=colors[4],
            other_current_screen_border=colors[7],
            other_screen_border=colors[4],
        ),
        widget.TextBox(
            text="|", font="Ubuntu Mono", foreground=colors[1], padding=2, fontsize=14
        ),
        widget.CurrentLayoutIcon(
            # custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
            foreground=colors[1],
            padding=4,
            scale=0.6,
        ),
        widget.CurrentLayout(foreground=colors[1], padding=5),
        widget.TextBox(
            text="|", font="Ubuntu Mono", foreground=colors[1], padding=2, fontsize=14
        ),
        widget.WindowName(foreground=colors[6], max_chars=40),
        widget.GenPollText(
            update_interval=300,
            func=lambda: subprocess.check_output(
                "printf $(uname -r)", shell=True, text=True
            ),
            foreground=colors[3],
            fmt="❤  {}",
            decorations=[
                BorderDecoration(
                    colour=colors[3],
                    border_width=[0, 0, 2, 0],
                )
            ],
        ),
        widget.Spacer(length=8),
        widget.CPU(
            format="▓  Cpu: {load_percent}%",
            foreground=colors[4],
            decorations=[
                BorderDecoration(
                    colour=colors[4],
                    border_width=[0, 0, 2, 0],
                )
            ],
        ),
        widget.Spacer(length=8),
        widget.Memory(
            foreground=colors[8],
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(USR_TERM + " -e htop")},
            format="{MemUsed: .0f}{mm}",
            fmt="🖥  Mem: {} used",
            decorations=[
                BorderDecoration(
                    colour=colors[8],
                    border_width=[0, 0, 2, 0],
                )
            ],
        ),
        widget.Spacer(length=8),
        widget.DF(
            update_interval=60,
            foreground=colors[5],
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(USR_TERM + " -e df")},
            partition="/",
            # format = '[{p}] {uf}{m} ({r:.0f}%)',
            format="{uf}{m} free",
            fmt="🖴  Disk: {}",
            visible_on_warn=False,
            decorations=[
                BorderDecoration(
                    colour=colors[5],
                    border_width=[0, 0, 2, 0],
                )
            ],
        ),
        widget.Spacer(length=8),
        widget.Volume(
            foreground=colors[7],
            fmt="🕫  Vol: {}",
            decorations=[
                BorderDecoration(
                    colour=colors[7],
                    border_width=[0, 0, 2, 0],
                )
            ],
        ),
        widget.Spacer(length=8),
        widget.KeyboardLayout(
            foreground=colors[4],
            fmt="⌨  Kbd: {}",
            decorations=[
                BorderDecoration(
                    colour=colors[4],
                    border_width=[0, 0, 2, 0],
                )
            ],
        ),
        widget.Spacer(length=8),
        widget.Clock(
            foreground=colors[8],
            format="⏱  %a, %b %d - %H:%M",
            decorations=[
                BorderDecoration(
                    colour=colors[8],
                    border_width=[0, 0, 2, 0],
                )
            ],
        ),
        widget.Spacer(length=8),
        widget.Systray(padding=3),
        widget.Spacer(length=8),
    ]
    return widgets_list


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


# All other monitors' bars will display everything but widgets 22 (systray) and 23 (spacer).
def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    del widgets_screen2[22:24]
    return widgets_screen2


# For adding transparency to your bar, add (background="#00000000") to the "Screen" line(s)
# For ex: Screen(top=bar.Bar(widgets=init_widgets_screen2(), background="#00000000", size=24)),


def init_screens():
    return [
        Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=26)),
        Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26)),
        Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26)),
    ]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()


def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)


def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)


def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


mouse = [
    Drag(
        [WIN],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [WIN],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size(),
    ),
    Click([WIN], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=colors[8],
    border_width=2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="dialog"),  # dialog boxes
        Match(wm_class="download"),  # downloads
        Match(wm_class="error"),  # error msgs
        Match(wm_class="file_progress"),  # file progress boxes
        Match(wm_class="kdenlive"),  # kdenlive
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="notification"),  # notifications
        Match(wm_class="pinentry-gtk-2"),  # GPG key password entry
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="toolbar"),  # toolbars
        Match(wm_class="Yad"),  # yad boxes
        Match(title="branchdialog"),  # gitk
        Match(title="Confirmation"),  # tastyworks exit box
        Match(title="Qalculate!"),  # qalculate-gtk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="tastycharts"),  # tastytrade pop-out charts
        Match(title="tastytrade"),  # tastytrade pop-out side gutter
        Match(title="tastytrade - Portfolio Report"),  # tastytrade pop-out allocation
        Match(wm_class="tasty.javafx.launcher.LauncherFxApp"),  # tastytrade settings
    ],
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

# DPI scaling for 4K
dpi_scale = 1.375
