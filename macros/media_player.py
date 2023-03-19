# MACROPAD Hotkeys: MPC-HC Media Player

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Media Player', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x006699, 'Mute', [Keycode.CONTROL, Keycode.M]),
        (0x004000, 'Vol-', [Keycode.DOWN_ARROW]),
        (0x004000, 'Vol+', [Keycode.UP_ARROW]),      #
        # 2nd row ----------
        (0x202000, 'Frame-', [Keycode.CONTROL, Keycode.LEFT_ARROW]),
        (0x101010, 'To Img', [Keycode.LEFT_ALT, Keycode.I]),
        (0x202000, 'Frame+', [Keycode.CONTROL, Keycode.RIGHT_ARROW]),
        # 3rd row ----------
        (0x000040, 'Slow', [Keycode.CONTROL, Keycode.DOWN_ARROW]), # Slower speed
        (0x400000, 'Reset', [Keycode.CONTROL, Keycode.R]),
        (0x6600CC, 'Fast', [Keycode.CONTROL, Keycode.UP_ARROW]), # Faster speed
        # 4th row ----------
        (0x800000, '<<', [Keycode.LEFT_ARROW]),   #
        (0x800000, 'Play/Pause', [Keycode.SPACEBAR]),   # Toggle Play/Pause
        (0x800000, '>>', [Keycode.RIGHT_ARROW]), #
        # Encoder button ---
        (0x000000, '', [Keycode.F11]) # Close window/tab
    ]
}
