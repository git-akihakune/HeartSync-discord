# Because it's better not to rely on external libraries

class logging:
    # Actual code to format strings' colour, src: https://www.geeksforgeeks.org/print-colors-python-terminal/
    # Formating strings to have them inline, column by column
    def debug(self, text): print("{} {}".format("\033[94m[debug]\033[00m", text))
    def info(self, text): print("{}  {}".format("\033[96m[info]\033[00m", text))
    def warning(self, text): print("{}  {}".format("\033[93m[warn]\033[00m", text))
    def success(self, text): print("{}   {}".format("\033[92m[suc]\033[00m", text))
    def error(self, text): print("{} {}".format("\033[95m[error]\033[00m", text))
    def critical(self, text): print("{}  {}".format("\033[91m[crit]\033[00m", text)) 