import os
from matplotlib import font_manager

environ = os.environ
fonts = os.listdir(os.path.join(os.environ['WINDIR'],'fonts'))
env_values = environ.values()

fonts = []
for x in font_manager.win32InstalledFonts():
    x = x[::-1]
    dot = x.find('.')
    slash = x.find('\\')
    x = x[slash-1:dot:-1]
    fonts += [x]
fonts.sort()
for x in fonts:
    print(x)


fonts
