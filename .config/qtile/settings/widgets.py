from libqtile import widget
from .theme import colors
import subprocess

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=37,
        padding=-2
    )

def workspaces():
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]


primary_widgets = [
    widget.Prompt(
        prompt='Run: ',
        font='UbuntuMono Nerd Font',
        padding=10,
        foreground=colors['text'],
        background=colors['dark']
    ),

    *workspaces(),

    separator(),

    powerline('color5', 'dark'),

 
    powerline('color4', 'color5'),

    icon(bg='color4', text=' '),  # Icon: nf-fa-feed

    widget.GenPollText(
        **base(bg='color4'),
        func=lambda: subprocess.check_output("/home/fudack/scripts/get_ip.sh").decode("utf-8").strip(),
        update_interval=10,
        name="ip_widget"),

    widget.Net(**base(bg='color4'), interface='wlo1'),

    powerline('color3', 'color4'),

    icon(bg='color3', text='󰈀 '),  # Icon: nf-fa-feed

    widget.Net(**base(bg='color3'), interface='eno2'),

    powerline('color2', 'color3'),

    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),

    widget.CurrentLayout(**base(bg='color2'), padding=5),

    powerline('color1', 'color2'),

    icon(bg='color1', fontsize=17, text='󰃰 '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),

    powerline('color6', 'color1'),

    widget.Battery(
         **base(bg='color6'),
         format='{char} {percent:2.0%} {hour:d}:{min:02d}',
         update_interval=60,
         charge_char='⚡',
         discharge_char='🔋',
         full_char='🔌',
         unknown_char='❓',
         empty_char='❗',
         show_short_text=False,
      ),


    powerline('dark', 'color6'),

    widget.Memory(background=colors['dark'], padding=5),

]



secondary_widgets = [

    widget.Prompt(
        prompt='Run: ',
        font='UbuntuMono Nerd Font',
        padding=10,
        foreground=colors['text'],
        background=colors['dark']
    ),

    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 15,
    'padding': 3,
}
extension_defaults = widget_defaults.copy()
