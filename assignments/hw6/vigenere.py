"""
Name: <Aidan Riordan>
program name: <vigenere>
I Aidan Riordan certify that this is my own work
"""

from graphics import *


def main():
    win = GraphWin("greeting card", 500, 500)
    win.setCoords(0, 0, 100, 100)
    text = Text(Point(20, 90), "Message to encode")
    text.draw(win)
    text2 = Text(Point(20, 70), "Enter Keyword")
    text2.draw(win)
    input_text1 = Entry(Point(70, 90), 20)
    input_text2 = Entry(Point(70, 70), 10)
    input_text1.draw(win)
    input_text2.draw(win)

    button = Text(Point(70, 60), "Encode")
    rectangle = Rectangle(Point(60, 55), Point(80, 65))
    rectangle.draw(win)
    button.draw(win)
    win.getMouse()
    button.setText("")
    rectangle.undraw()
    message = input_text1.getText()
    keyword = input_text2.getText()
    encoded = code(message, keyword)
    button.setText("Resulting message" + "\n" + encoded + "\n" + "\n" + "Click anywhere to close window")

    win.getMouse()
    win.close()


def code(message, keyword):
    message = message.upper()
    message = message.replace(" ", "")
    keyword = keyword.upper()
    keyword = keyword.replace(" ", "")
    # adjust length of key accordingly
    len_dif = len(message) - len(keyword)
    remainder = len_dif % len(keyword)
    keyword = keyword * (len_dif + 1)
    keyword = keyword + keyword[0:remainder]
    list_key = []
    list_mes = []
    encoded_message = ""
    i = 0
    for letter in message:
        list_mes.append(ord(letter))
    for letter in keyword:
        list_key.append(ord(letter))
    for val in list_mes:
        x = (val + list_key[i]) % 26 + ord("A")
        encoded_message = encoded_message + str(chr(x))
        i = i + 1

    print(encoded_message)
    return encoded_message


if __name__ == '__main__':
    main()
