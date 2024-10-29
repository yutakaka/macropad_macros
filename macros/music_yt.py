# MACROPAD Hotkeys: YouTube Browser Playback

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Music - YT', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x006699, 'Mute', [Keycode.M]),
        (0x004000, 'Vol-', [Keycode.MINUS]),
        (0x004000, 'Vol+', [Keycode.EQUALS]),      #
        # 2nd row ----------
        (0x000040, 'Prev', [Keycode.K]), # Previous song
        (0x101010, 'Like', [Keycode.Q]), # Like song
        (0x000040, 'Next', [Keycode.J]), # Next song
        # 3rd row ----------
        (0xee6600, '<1s', [Keycode.LEFT_SHIFT, Keycode.H]), # Rewind 1 sec.
        (0x6600CC, 'Q', [Keycode.Q]), # Toggle queue/expanded player
        (0xee6600, '1s>', [Keycode.LEFT_SHIFT, Keycode.L]), # Forward 1 sec.
        # 4th row ----------
        (0x800000, '<10s', [Keycode.LEFT_SHIFT, Keycode.LEFT_ARROW]),   #
        (0x800000, 'Play/Pause', [Keycode.SPACEBAR]),   # Toggle Play/Pause
        (0x800000, '10s>', [Keycode.LEFT_SHIFT, Keycode.RIGHT_ARROW]), #
        # Encoder button ---
        (0x000000, '', [Keycode.FORWARD_SLASH]) # Close window/tab
    ]
}
