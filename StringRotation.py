'''
Assume you have a method isSubstring which checks if one word is a substring of another.
Given two strings s1 and s2, write code to check if s2 is a rotation of s1 using only one
call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat")
'''

def isRotation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    s2 += s2
    return s1 in s2