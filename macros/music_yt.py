# MACROPAD Hotkeys: YouTube Browser Playback

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Music - YT', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x006699, 'Mute', [[ConsumerControlCode.MUTE]]),
        (0x004000, 'Vol-', [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0x004000, 'Vol+', [[ConsumerControlCode.VOLUME_INCREMENT]]),      #
        # 2nd row ----------
        (0x000000, '', [Keycode.COMMA]),
        (0x000000, '', [Keycode.C]),
        (0x000000, '', [Keycode.PERIOD]),
        # 3rd row ----------
        (0x000040, 'Prev', [Keycode.K]), # Slower speed
        (0x101010, 'LIKE', [Keycode.LEFT_SHIFT, Keycode.EQUALS]),
        (0x000040, 'Next', [Keycode.J]), # Faster speed
        # 4th row ----------
        (0x800000, '<<', [Keycode.LEFT_SHIFT, Keycode.LEFT_ARROW]),   #
        (0x800000, 'Play/Pause', [Keycode.SPACEBAR]),   # Toggle Play/Pause
        (0x800000, '>>', [Keycode.LEFT_SHIFT, Keycode.RIGHT_ARROW]), #
        # Encoder button ---
        (0x000000, '', [Keycode.Q]) # Close window/tab
    ]
}
