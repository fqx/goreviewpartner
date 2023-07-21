# utils for porting python 2 to python 3

def fix_color(color: str) -> str:
    """
    tkinter in python 3 expects color name "black", or hex color "#ffff00"
    """
    color_names = ['black']

    # color = color.lower()
    if color.lower() in color_names:
        return color
    else:
        for char in color:
            if char.isdigit() or char.lower() in 'abcdef': # hexadecimal
                return "#"+color.lower()
            else:
                return color
