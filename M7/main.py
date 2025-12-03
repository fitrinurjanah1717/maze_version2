#from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import  QWidget, QApplication,  QPushButton, QHBoxLayout, QVBoxLayoutpip


# main window:
app = QApplication([])
window = QWidget()
window.setWindowTitle('Try your luck, friend!')
window.resize(300, 300)


#Step 1. Create five buttons with numbers
button1 = QPushButton('1')
button2 = QPushButton('2')
button3 = QPushButton('3')
button4 = QPushButton('4')
button5 = QPushButton('5')


#Step 2. Create 4 layouts: 3 horizontal and 1 vertical
layoutV = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()


#Step 3. Link the objects to horizontal layouts. Remember to use the alignment parameter
layoutH1.addWidget(button1, alignment = Qt.AlignLeft)
layoutH1.addWidget(button2, alignment = Qt.AlignRight)
layoutH2.addWidget(button3, alignment = Qt.AlignCenter)
layoutH3.addWidget(button4, alignment = Qt.AlignLeft)
layoutH3.addWidget(button5, alignment = Qt.AlignRight)


#Step 4. Link the horizontal layouts to the vertical layout
layoutV.addLayout(layoutH1)
layoutV.addLayout(layoutH2)
layoutV.addLayout(layoutH3)
window.setLayout(layoutV)
window.setLayout(layoutV)


window.show()
app.exec_()

#Level 2.

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel


app = QApplication([])
window = QWidget()
window.setWindowTitle('Programming Languages')
window.resize(400, 300)


#Step 1. Create 6 labels with the names of programming languages
sentence1 = QLabel('PHP')
sentence2 = QLabel('JavaScript')
sentence3 = QLabel('Python')
sentence4 = QLabel('Pascal')
sentence5 = QLabel('SQL')
sentence6 = QLabel('C++')


#Step 2. Create 4 layouts: 3 horizontal and 1 vertical
layoutV = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()


#Step 3. Link 6 objects to horizontal layouts
layoutH1.addWidget(sentence1, alignment = Qt.AlignCenter)
layoutH1.addWidget(sentence2, alignment = Qt.AlignCenter)
layoutH2.addWidget(sentence3, alignment = Qt.AlignCenter)
layoutH2.addWidget(sentence4, alignment = Qt.AlignCenter)
layoutH3.addWidget(sentence5, alignment = Qt.AlignCenter)
layoutH3.addWidget(sentence6, alignment = Qt.AlignCenter)


#Step 4. Link the horizontal layouts to the vertical layout
layoutV.addLayout(layoutH1)
layoutV.addLayout(layoutH2)
layoutV.addLayout(layoutH3)
window.setLayout(layoutV)


window.show()
app.exec_()


#Level 3.

#connecting the module with layouts
from PyQt5.QtCore import Qt
#connecting the required widgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QRadioButton, QButtonGroup


#creating an application object
app = QApplication([])
# creating the main window object
my_win = QWidget()
# creating the name of the main window
my_win.setWindowTitle('My first app')
# setting the point where the window will show up on the computer screen
my_win.move(900, 70)
# setting the window size
my_win.resize(400, 200)
# giving the window the command to show up
my_win.show()


# creating a vertical layout
line = QVBoxLayout()


# creating radio button objects
radio_button_1 = QRadioButton('1')
# setting the radio button that will be selected when the program starts.
radio_button_1.setChecked(True)


radio_button_2 = QRadioButton('2')
radio_button_3 = QRadioButton('3')


# creating a group of radio buttons and adding the previously created radio button objects there
button_group = QButtonGroup()
button_group.addButton(radio_button_1, id = 1)
button_group.addButton(radio_button_2, id = 2)
button_group.addButton(radio_button_3, id = 3)


# placing the radio buttons on the vertical layout
line.addWidget(radio_button_1)
line.addWidget(radio_button_2)
line.addWidget(radio_button_3)


# creating a button object and setting a label on it
button = QPushButton('Check')


# placing the button on the center of the layout
line.addWidget(button, alignment = Qt.AlignCenter)


# adding the resulting line to the application window
my_win.setLayout(line)


# creating a field where the text about the selected button will be displayed
title = QLabel()
line.addWidget(title, alignment = Qt.AlignCenter)
my_win.setLayout(line)


#a function that changes the information (text) about the new button
def radio_button_check():
    title.setText("Selected: button number " + str(button_group.checkedId()))


# linking a button press to a function call
button.clicked.connect(radio_button_check)


#Leaves the app open until the exit button is pressed
app.exec_()