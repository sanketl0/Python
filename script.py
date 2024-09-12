import pyfiglet
from termcolor import colored

text = ["Happy", "Programmer's", "Day!"]
mini_code = {
    "Happy": "\n(defn happy [mood]),\t\t\t (defn happy [mood])",
    "Programmer's": "\n\t\t\t\t\t(lambda (code))",
    "Day!": "\n(if '2024-09-12))  \t\t Happy Codinggg"
}
fonts = ["slant"]

for i, word in enumerate(text):
    font = pyfiglet.Figlet(font=fonts[i % len(fonts)])
    color = ["red", "green", "yellow", "blue", "magenta"][i % 5]
    ascii_art = font.renderText(word)
    print(colored(mini_code[word], "cyan")) 
    print(colored(ascii_art, color))
