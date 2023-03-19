# MACROPAD Hotkeys: YouTube Browser Playback

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'YouTube', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x006699, 'Mute', [[ConsumerControlCode.MUTE]]),
        (0x004000, 'Vol-', [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0x004000, 'Vol+', [[ConsumerControlCode.VOLUME_INCREMENT]]),      #
        # 2nd row ----------
        (0x202000, 'Frame-', [Keycode.COMMA]),
        (0x101010, 'CC', [Keycode.C]),
        (0x202000, 'Frame+', [Keycode.PERIOD]),
        # 3rd row ----------
        (0x000040, 'Slow', [Keycode.LEFT_SHIFT, Keycode.COMMA]), # Slower speed
        (0x101010, 'Theater', [Keycode.T]),
        (0x6600CC, 'Fast', [Keycode.LEFT_SHIFT, Keycode.PERIOD]), # Faster speed
        # 4th row ----------
        (0x800000, '<<', [Keycode.LEFT_ARROW]),   #
        (0x800000, 'Play/Pause', [Keycode.SPACEBAR]),   # Toggle Play/Pause
        (0x800000, '>>', [Keycode.RIGHT_ARROW]), #
        # Encoder button ---
        (0x000000, '', [Keycode.F]) # Close window/tab
    ]
}
