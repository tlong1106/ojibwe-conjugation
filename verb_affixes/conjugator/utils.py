# Bold Red: \033[1;31mBold Red\033[0m
# Italic Green: \033[3;32mItalic Green\033[0m
# Underlined Cyan: \033[4;36mUnderlined Cyan\033[0m
# Strikethrough Blue: \033[9;34mStrikethrough Blue\033[0m

# # # personal prefix, suffix; possessive prefix:
# regular green = independent, positive -> prefix, suffix
# italic green = dependent, positive -> suffix (prefix for changed conjunct)
# bold green = imperative, positive -> suffix
# underline green = direct object, positive (vti, vta) -> suffix

# regular red = independent, negative -> prefix, suffi
# italic red = dependent, negative -> suffix (prefix for changed conjunct)
# bold red = imperative, negative -> suffix
# underline red = direct object, negative (vti, vta) -> suffix

# # # preverbs
# regular gray = lexical (4)
# italic gray = directional (2)
# bold gray = tense (1)
# underline gray = relational (3)

# # # nouns
# regular magenta = inanimate singular
# italic magenta = 
# bold magenta = inanimate bold
# underline magenta = 

# regular blue (36) = animate singular
# italic blue (36) = 
# bold blue (36) = animate bold
# underline blue (36) = obviate

def styled_text(text: str, style: str) -> str:

    styles = {
        "red_normal": "\033[0;31m",
        "red_dark": "\033[2;31m",
        "red_bold": "\033[1;31m",
        "red_italic": "\033[3;31m",
        "red_underline": "\033[4;31m",
        "red_strikethrough": "\033[9;31m",
        "red_background": "\033[7;31m",
        "green_normal": "\033[0;32m",
        "green_dark": "\033[2;32m",
        "green_bold": "\033[1;32m",
        "green_italic": "\033[3;32m",
        "green_underline": "\033[4;32m",
        "green_strikethrough": "\033[9;32m",
        "green_background": "\033[7;32m"
    }
    start = styles.get(style.lower(), "")
    end = "\033[00m" if start else ""
    return f"{start}{text}{end}"

def get_style(form: str, neg: bool) -> str:
    style_map = {
        ("independent", False): "green_normal",
        ("independent", True): "red_normal",
        ("dependent", False): "green_italic",
        ("dependent", True): "red_italic",
        ("imperative", False): "green_bold",
        ("imperative", True): "red_bold"
    }
    return style_map.get((form, neg), "")