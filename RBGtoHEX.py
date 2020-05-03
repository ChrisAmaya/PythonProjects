# RGB to Hex Conversion


def rgb(r, g, b):
    """
    purpose:
        convert a rgb value to its corresponding hex value
    Pre:
        :param r: an integer, if r<0, assume 0, if r>255, assume 255
        :param g: an integer, if g<0, assume 0, if g>255, assume 255
        :param b: an integer, if b<0, assume 0, if b>255, assume 255

    post:
         None
    :return:
        The Hex value for the rbg as a string
    """
    def rounder(c):
        if c < 0:
            c = 0
            return c
        elif c >= 255:
            c = 255
            return c
        else:
            return c

    def rgb_helper(c):
        color = list()
        if c == 0:
            color.append(0)
            color.append(0)
            return color
        elif c < 9:
            color.append(c)
            color.append(0)
            return color
        else:
            while c > 0:
                color.append(c % 16)
                c = c//16
            return color

    def converter(color):
        # where color is a list
        for i in range(len(color)):
            if color[i] == 15:
                color[i] = "F"
            elif color[i] == 14:
                color[i] = "E"
            elif color[i] == 13:
                color[i] = "D"
            elif color[i] == 12:
                color[i] = "C"
            elif color[i] == 11:
                color[i] = "B"
            elif color[i] == 10:
                color[i] = "A"
            else:
                color[i] = str(color[i])
        return color
        # reverse of the list to get proper HEX value

    r = rounder(r)
    g = rounder(g)
    b = rounder(b)

    red = rgb_helper(r)
    green = rgb_helper(g)
    blue = rgb_helper(b)

    r = converter(red)[::-1]
    g = converter(green)[::-1]
    b = converter(blue)[::-1]

    rgb = r+g+b

    return "".join(rgb)


