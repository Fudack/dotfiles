import threading
from libqtile.config import Screen
from libqtile import bar, hook
from libqtile.log_utils import logger
from .widgets import primary_widgets, secondary_widgets
from .path import wallpaper_dir
import subprocess
import os
import random

def call_later(delay, func, *args, **kwargs):
    timer = threading.Timer(delay, func, args, kwargs)
    timer.start()

def status_bar(widgets):
    return bar.Bar(widgets, 24, opacity=0.92)

screens = [Screen(top=status_bar(primary_widgets))]

xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"

command = subprocess.run(
    xrandr,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

if command.returncode != 0:
    error = command.stderr.decode("UTF-8")
    logger.error(f"Failed counting monitors using {xrandr}:\n{error}")
    connected_monitors = 1
else:
    connected_monitors = int(command.stdout.decode("UTF-8"))

if connected_monitors > 1:
    for _ in range(1, connected_monitors):
        screens.append(Screen(top=status_bar(secondary_widgets)))

def get_wallpapers(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def change_wallpaper():
    wallpapers = get_wallpapers(wallpaper_dir)
    if wallpapers:
        random_wallpaper = random.choice(wallpapers)
        command = f"feh --bg-scale '{random_wallpaper}' --bg-scale '{random_wallpaper}'"
        subprocess.call(command, shell=True)
    else:
        logger.error(f"No wallpapers found in {wallpaper_dir}")

@hook.subscribe.startup_once
def startup_once():
    change_wallpaper()

@hook.subscribe.startup
def startup():
    change_wallpaper()
    call_later(1800, change_wallpaper)  # 1800 segundos = 30 minutos

