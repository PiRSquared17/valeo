
__version__ = '$Id: terminal_interface.py,v 1.11 2006/03/07 00:23:33 wikipedian Exp $'

import config, transliteration
import traceback, re, sys

try:
    import ctypes
    ctypes_found = True
except ImportError:
    ctypes_found = False

# TODO: other colors
unixColors = {
    None: chr(27) + '[0m',     # Unix end tag to switch back to default
    9:    chr(27) + '[94;1m',  # Light Blue start tag
    10:   chr(27) + '[92;1m',  # Light Green start tag
    11:   chr(27) + '[36;1m',  # Light Aqua start tag
    12:   chr(27) + '[91;1m',  # Light Red start tag
    13:   chr(27) + '[35;1m',  # Light Purple start tag
    14:   chr(27) + '[33;1m',  # Light Yellow start tag
}

class UI:
    def __init__(self):
        pass

    # NOTE: We use sys.stdout.write() instead of print because print adds a
    # newline.
    
    def printColorizedInUnix(self, text, colors, targetStream):
        result = ""
        lastColor = None
        for i in range(0, len(colors)):
            if colors[i] != lastColor:
                # add an ANSI escape character
                result += unixColors[colors[i]]
            # append one text character
            result += text[i]
            lastColor = colors[i]
        if lastColor != None:
            # reset the color to default at the end
            result += unixColors[None]
        targetStream.write(result.encode(config.console_encoding, 'replace'))

    def printColorizedInWindows(self, text, colors, targetStream):
        """
        This only works in Python 2.5 or higher.
        """
        if ctypes_found:
            std_out_handle = ctypes.windll.kernel32.GetStdHandle(-11)
            lastColor = None
            for i in range(0, len(colors)):
                if colors[i] != lastColor:
                    #targetStream.flush()
                    if colors[i] == None:
                        ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, config.defaultcolor)
                    else:
                        ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, colors[i])
                # print one text character.
                targetStream.write(text[i].encode(config.console_encoding, 'replace'))
                lastColor = colors[i]
            if lastColor != None:
                # reset the color to default at the end
                ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, config.defaultcolor)
        else:
            # ctypes is only available since Python 2.5, and we won't
            # try to colorize without it. Instead we add *** after the text as a whole
            # if anything needed to be colorized.
            somecolor = False
            for i in colors:
                if not i is None:
                    somecolor = True
            if somecolor:
                if text[-1] == "\n":
                    targetStream.write((text[:-1]+"***\n").encode(config.console_encoding, 'replace'))
                else:
                    targetStream.write((text+"***").encode(config.console_encoding, 'replace'))
            else:
                targetStream.write(text.encode(config.console_encoding, 'replace'))

    def printColorized(self, text, colors, targetStream):
        if colors and config.colorized_output:
            if sys.platform == 'win32':
                self.printColorizedInWindows(text, colors, targetStream)
            else:
                self.printColorizedInUnix(text, colors, targetStream)
        else:
            targetStream.write(text.encode(config.console_encoding, 'replace'))

    def output(self, text, colors = None, newline = True, toStdout = False):
        """
        If a character can't be displayed in the encoding used by the user's
        terminal, it will be replaced with a question mark or by a
        transliteration.

        colors is a list of integers, one for each character of text. If a
        list entry is None, the default terminal color will be used for the
        character at that position. Take care that the length of the colors
        list equals the text length.

         0 = Black
         1 = Blue
         2 = Green
         3 = Aqua
         4 = Red
         5 = Purple
         6 = Yellow
         7 = White
         8 = Gray
         9 = Light Blue
        10 = Light Green
        11 = Light Aqua
        12 = Light Red
        13 = Light Purple
        14 = Light Yellow
        15 = Bright White
        """
        if colors:
            if len(colors) != len(text):
                print "DBG> BUG: Text color list length different from text length!"
                print traceback.print_stack()
                print "DBG> Attempting to recover, but please report this problem"
        else:
            colors = [None for char in text]
        if config.transliterate:
            # Encode our unicode string in the encoding used by the user's console,
            # and decode it back to unicode. Then we can see which characters
            # can't be represented in the console encoding.
            codecedText = text.encode(config.console_encoding, 'replace').decode(config.console_encoding)
            transliteratedText = ''
            # A transliteration replacement might be longer than the original
            # character, e.g. ? is transliterated to ch.
            # We need to reflect this growth in size by shifting the color list
            # entries. This variable counts how much the size has grown.
            sizeIncrease = 0
            prev = "-"
            for i in xrange(len(codecedText)):
                # work on characters that couldn't be encoded, but not on
                # original question marks.
                if codecedText[i] == '?' and text[i] != u'?':
                    try:
                        transliterated = transliteration.trans(text[i], default = '?', prev = prev, next = text[i+1])
                    except IndexError:
                        transliterated = transliteration.trans(text[i], default = '?', prev = prev, next = ' ')
                    # transliteration was successful. The replacement
                    # could consist of multiple letters.
                    transliteratedText += transliterated
                    transLength = len(transliterated)
                    # mark the transliterated letters in yellow.
                    color = colors[i + sizeIncrease] or 14
                    colors = colors[:i + sizeIncrease] + [color] * transLength + colors[i + sizeIncrease + 1:]
                    # memorize if we replaced a single letter by multiple letters.
                    sizeIncrease += transLength - 1
                    if len(transliterated) > 0:
                        prev = transliterated[-1]
                else:
                    # no need to try to transliterate.
                    transliteratedText += codecedText[i]
                    prev = codecedText[i]
            text = transliteratedText
        if newline:
            text += u'\n'
            colors.append(None)

        if toStdout:
            targetStream = sys.stdout
        else:
            targetStream = sys.stderr
        self.printColorized(text, colors, targetStream)

    def input(self, question, colors = None):
        """
        Works like raw_input(), but returns a unicode string instead of ASCII.

        Unlike raw_input, this function automatically adds a space after the
        question.
        """

        # sound the terminal bell to notify the user
        if config.ring_bell:
            sys.stdout.write('\07')
        if colors:
            self.output(question + ' ', colors = colors + [None], newline=False)
        else:
            self.output(question + ' ', newline = False)
        text = raw_input()
        text = unicode(text, config.console_encoding)
        return text

    def inputChoice(self, question, options, hotkeys, default = None):
        for i in range(len(options)):
            option = options[i]
            hotkey = hotkeys[i]
            # try to mark a part of the option name as the hotkey
            m = re.search('[%s%s]' % (hotkey.lower(), hotkey.upper()), option)
            if m:
                pos = m.start()
                options[i] = '%s[%s]%s' % (option[:pos], hotkey, option[pos+1:])
            else:
                options[i] = '%s [%s]' % (option, hotkey)
        # loop until the user entered a valid choice
        while True:
            prompt = '%s (%s)' % (question, ', '.join(options))
            answer = self.input(prompt)
            if answer.lower() in hotkeys or answer.upper() in hotkeys:
                return answer.lower()
            elif default and answer=='':		# empty string entered
                return default

    def editText(self, text, jumpIndex = None, highlight = None):
        """
        Uses a Tkinter edit box because we don't have a console editor
        
        Parameters:
            * text      - a Unicode string
            * jumpIndex - an integer: position at which to put the caret
            * highlight - a substring; each occurence will be highlighted
        """
        import gui
        editor = gui.EditBoxWindow()
        return editor.edit(text, jumpIndex = jumpIndex, highlight = highlight)
