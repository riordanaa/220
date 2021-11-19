"""
Name: <Aidan Riordan>
program name: <weighted_average>
I Aidan Riordan certify that this is my own work
"""
from random import randint
from graphics import GraphWin, Point, Rectangle, Text
from button import Button


def main():
    win = GraphWin("Three Button Game", 400, 400)
    button_1 = Button(Rectangle(Point(40, 200), Point(120, 140)), "door1")
    button_2 = Button(Rectangle(Point(160, 200), Point(240, 140)), "door2")
    button_3 = Button(Rectangle(Point(280, 200), Point(360, 140)), "door3")
    button_1.draw(win)
    button_2.draw(win)
    button_3.draw(win)

    message_top = Text(Point(200,50), "I have a secret door")
    message_top.draw(win)
    message_bot = Text(Point(200,350), "Click to choose door")
    message_bot.draw(win)
    choice = randint(1, 3)

    pont = win.getMouse()
    if button_1.is_clicked(pont) and choice == 1:
        message_top.setText("You win!")
        message_bot.setText("click to close")
        button_1.color_button("green")
    elif button_1.is_clicked(pont):
        message_top.setText("You lost!")
        message_bot.setText("Door " + str(choice) + " is my secret door")
        button_1.color_button("red")
    if button_2.is_clicked(pont) and choice == 2:
        message_top.setText("You win!")
        message_bot.setText("click to close")
        button_2.color_button("green")
    elif button_2.is_clicked(pont):
        message_top.setText("You lost!")
        message_bot.setText("Door " + str(choice) + " is my secret door")
        button_2.color_button("red")
    if button_3.is_clicked(pont) and choice == 3:
        message_top.setText("You win!")
        message_bot.setText("click to close")
        button_3.color_button("green")
    elif button_3.is_clicked(pont):
        message_top.setText("You lost!")
        message_bot.setText("Door " + str(choice) + " is my secret door")
        button_3.color_button("red")
    win.getMouse()


if __name__ == '__main__':
    main()
