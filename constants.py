## constants
SIZE_X = 7 # must be >= 4
SIZE_Y = 6 # must be >= 4
FOUR = 4

COLOR = True
if COLOR:
    CHAR_EMPTY = '\u001b[30;1m_\u001b[0m'
    CHAR_0 = '\u001b[31;1mO\u001b[0m'
    CHAR_1 = '\u001b[37;1mX\u001b[0m'
else:
    CHAR_EMPTY = '_'
    CHAR_0 = 'O'
    CHAR_1 = 'X'
