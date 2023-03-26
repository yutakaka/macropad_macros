# MACROPAD Hotkeys example: Tones

# The syntax for Tones in macros is highly peculiar, in order to maintain
# backward compatibility with the original keycode-only macro files.
# The third item for each macro is a list in brackets, and each value within
# is normally an integer (Keycode), float (delay) or string (typed literally).
# Consumer Control codes were added as list-within-list, and then mouse and
# tone further complicate this by adding dicts-within-list. Each tone-related
# item is the key 'tone' with either an integer frequency value, or 0 to stop
# the tone mid-macro (tone is also stopped when key is released).
# Helpful: https://en.wikipedia.org/wiki/Piano_key_frequencies

# This example ONLY shows tones (and delays), but really they can be mixed
# with other elements (keys, codes, mouse) to provide auditory feedback.

app = {               # REQUIRED dict, must be named 'app'
    'name' : 'Tones C4 - B4', # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x101010, 'A4', [{'tone':440}]),
        (0x006699, 'A4#', [{'tone':466}]),
        (0x101010, 'B4', [{'tone':494}]),
        # 2nd row ----------
        (0x006699, 'F4#', [{'tone': 370}]),
        (0x101010, 'G4', [{'tone': 392}]),
        (0x006699, 'G4#', [{'tone': 415}]),
        # 3rd row ----------
        (0x006699, 'D4#', [{'tone': 311}]),
        (0x101010, 'E4', [{'tone': 330}]),
        (0x101010, 'F4', [{'tone': 349}]),
        # 4th row ----------
        (0x101010, 'C4', [{'tone': 262}]),
        (0x006699, 'C4#', [{'tone': 277}]),
        (0x101010, 'D4', [{'tone': 294}]),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
