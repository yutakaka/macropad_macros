# MACROPAD Hotkeys: Transcribe! software

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.mouse import Mouse

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'vscode', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x006699, 'Sidebar', [Keycode.CONTROL, Keycode.B]),
        (0x004000, 'Back', [Keycode.LEFT_ALT, Keycode.LEFT_ARROW]),
        (0x004000, 'Fwd', [Keycode.LEFT_ALT, Keycode.RIGHT_ARROW]),      #
        # 2nd row ----------
        (0x202000, 'Search', [Keycode.CONTROL, Keycode.LEFT_SHIFT, 'f']),
        (0xee6600, 'Define', [Keycode.F12]),
        (0x202000, 'Speak', [Keycode.LEFT_SHIFT, Keycode.LEFT_ALT, Keycode.U]),
        # 3rd row ----------
        (0x000040, 'Prev', [Keycode.CONTROL, Keycode.LEFT_ALT, Keycode.J]), # Slower speed
        (0x101010, 'Bookmark', [Keycode.CONTROL, Keycode.LEFT_ALT, Keycode.K]),
        (0x6600CC, 'Next', [Keycode.CONTROL, Keycode.LEFT_ALT, Keycode.J]), # Faster speed
        # 4th row ----------
        #(0x800000, '<<', [{'wheel': -10}]),   #
        (0x800000, '<<', [Keycode.LEFT_ALT, Keycode.LEFT_ARROW]),
        (0x101010, '-', [Keycode.SPACEBAR]),   # Toggle Play/Pause
        (0x800000, '>>', [Keycode.LEFT_ALT, Keycode.RIGHT_ARROW]), #
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, Keycode.LEFT_SHIFT, Keycode.P]) # Close window/tab
    ]
}
