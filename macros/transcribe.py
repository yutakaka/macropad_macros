# MACROPAD Hotkeys: Transcribe! software

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.mouse import Mouse

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Transcribe!', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x006699, 'Mute', [[ConsumerControlCode.MUTE]]),
        (0x004000, 'Vol-', [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0x004000, 'Vol+', [[ConsumerControlCode.VOLUME_INCREMENT]]),      #
        # 2nd row ----------
        (0x202000, 'Zoom-', [Keycode.CONTROL, Keycode.LEFT_ARROW]),
        (0x202000, 'Whole', [Keycode.LEFT_ALT, Keycode.I]),
        (0x202000, 'Zoom+', [Keycode.CONTROL, Keycode.RIGHT_ARROW]),
        # 3rd row ----------
        (0x000040, 'Slow', [Keycode.LEFT_SHIFT, Keycode.COMMA]), # Slower speed
        (0x101010, 'Reset', [Keycode.CONTROL, Keycode.R]),
        (0x6600CC, 'Fast', [Keycode.LEFT_SHIFT, Keycode.PERIOD]), # Faster speed
        # 4th row ----------
        #(0x800000, '<<', [{'wheel': -10}]),   #
        (0x800000, '<<', [Keycode.LEFT_ARROW]),
        (0x800000, 'Play/Pause', [Keycode.SPACEBAR]),   # Toggle Play/Pause
        (0x800000, '>>', [Keycode.RIGHT_ARROW]), #
        # Encoder button ---
        (0x000000, '', [Keycode.F11]) # Close window/tab
    ]
}
