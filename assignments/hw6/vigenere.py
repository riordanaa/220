"""
Name: <Aidan Riordan>
program name: <vigenere>
I Aidan Riordan certify that this is my own work
"""

from graphics import *

def main():
    win = GraphWin("greeting card", 500, 500)
    win.setCoords(0, 0, 100, 100)

def encode_better():
    m = input("what is your message")
    shifter = input("what is your shifter")
    acc = ""
    for i in range(len(m)):
        c =ord(m[i])
        key = ord(shifter[i])
        z = c + key - 97
        acc = acc + chr(z)
    print(acc)

main()
encode_better()