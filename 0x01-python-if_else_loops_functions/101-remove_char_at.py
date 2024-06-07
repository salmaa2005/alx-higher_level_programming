#!/usr/bin/python3
# creates a COPY of the string without the character n
def remove_char_at(str, n):
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
