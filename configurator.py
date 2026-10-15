import os

print("""
Your answers in the questions should be given in numbers corresponding to this:
1. Blades
2. NXE
3. BetaNXE
4. Kinect
5. Metro
""")

current = int(input("What dashboard configuration are you currently using:"))

if current == 1:
    os.rename("Proto.ini", "Proto - Blades.ini")
    os.rename("PluginUI.ini", "PluginUI - Blades.ini")
elif current == 2:
    os.rename("Proto.ini", "Proto - NXE.ini")
    os.rename("PluginUI.ini", "PluginUI - NXE.ini")
elif current == 3:
    os.rename("Proto.ini", "Proto - BetaNXE.ini")
    os.rename("PluginUI.ini", "PluginUI - BetaNXE.ini")
elif current == 4:
    os.rename("Proto.ini", "Proto - Kinect.ini")
    os.rename("PluginUI.ini", "PluginUI - Kinect.ini")
if current == 5:
    os.rename("Proto.ini", "Proto - Metro.ini")
    os.rename("PluginUI.ini", "PluginUI - Metro.ini")

new = int(input("What do you want to set as your new default dashboard configuration:"))

if new == 1:
    os.rename("Proto - Blades.ini", "Proto.ini")
    os.rename("PluginUI - Blades.ini", "PluginUI.ini")
if new == 2:
    os.rename("Proto - NXE.ini", "Proto.ini")
    os.rename("PluginUI - NXE.ini", "PluginUI.ini")
if new == 3:
    os.rename("Proto - BetaNXE.ini", "Proto.ini")
    os.rename("PluginUI - BetaNXE.ini", "PluginUI.ini")
if new == 4:
    os.rename("Proto - Kinect.ini", "Proto.ini")
    os.rename("PluginUI - Kinect.ini", "PluginUI.ini")
if new == 5:
    os.rename("Proto - Metro.ini", "Proto.ini")
    os.rename("PluginUI - Metro.ini", "PluginUI.ini")
