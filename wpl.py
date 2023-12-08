import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import subprocess

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.sub_buttons_main = []  # List to store sub-buttons under the main button
        self.sub_buttons_main2 = []  # List to store sub-buttons under the main button 2
        self.is_main_button_expanded = False  # Records the expansion state of the main button
        self.is_main_button2_expanded = False  # Records the expansion state of the main button 2
        self.initUI()

    # Initialize the interface
    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('PyQt5 Example')

        # Create the main button and connect it to the slot function
        self.main_button = QPushButton(self)
        self.setupButton(self.main_button, 'Main Button', self.toggleSubButtonsMain, '#4CAF50')  # Green

        # Create the main button 2 and connect it to the slot function
        self.main_button2 = QPushButton(self)
        self.setupButton(self.main_button2, 'Main Button 2', self.toggleSubButtonsMain2, '#2196F3')  # Blue

        # Create a vertical layout
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.main_button)  # Add the main button to the layout
        self.vbox.addWidget(self.main_button2)  # Add the main button 2 to the layout

        # Set the layout
        self.setLayout(self.vbox)

    # Set button properties and styles
    def setupButton(self, button, text, slot, color):
        button.setText(text)
        button.setIcon(QIcon('icon.png'))  # Replace 'icon.png' with your icon file path
        button.setIconSize(button.sizeHint() / 2)
        button.clicked.connect(slot)

        # Set button styles
        button.setStyleSheet(f'''
            QPushButton {{
                background-color: {color};
                color: white;
                border: 2px solid {color};
                border-radius: 5px;
                padding: 5px;
                margin: 2px;
                text-align: center;
                font-size: 12px;
            }}

            QPushButton:hover {{
                background-color: #1E88E5; /* Dark blue */
            }}
        ''')

    # Toggle the display status of sub-buttons under the main button
    def toggleSubButtonsMain(self):
        if not self.is_main_button_expanded:
            self.showSubButtonsMain()
        else:
            self.hideSubButtonsMain()

    # Toggle the display status of sub-buttons under the main button 2
    def toggleSubButtonsMain2(self):
        if not self.is_main_button2_expanded:
            self.showSubButtonsMain2()
        else:
            self.hideSubButtonsMain2()

    # Display sub-buttons under the main button
    def showSubButtonsMain(self):
        # Remove all buttons
        self.clearButtons()

        # Create four sub-buttons and connect them to the slot functions
        sub_button1 = QPushButton(self)
        self.setupButton(sub_button1, 'Sub Button 1', lambda: self.openExecutable('path/to/executable1'), '#FFC107')  # Yellow

        sub_button2 = QPushButton(self)
        self.setupButton(sub_button2, 'Sub Button 2', lambda: self.openExecutable('path/to/executable2'), '#FF5722')  # Orange

        sub_button3 = QPushButton(self)
        self.setupButton(sub_button3, 'Sub Button 3', lambda: self.openExecutable('path/to/executable3'), '#E91E63')  # Pink

        sub_button4 = QPushButton(self)
        self.setupButton(sub_button4, 'Sub Button 4', lambda: self.openExecutable('path/to/executable4'), '#795548')  # Brown

        # Add sub-buttons to the list for later management
        self.sub_buttons_main.extend([sub_button1, sub_button2, sub_button3, sub_button4])

        # Add all buttons back to the layout
        self.addButtons()

        # Update the expansion state
        self.is_main_button_expanded = True

    # Display sub-buttons under the main button 2
    def showSubButtonsMain2(self):
        # Remove all buttons
        self.clearButtons()

        # Create one sub-button and connect it to the slot function
        sub_button_main2 = QPushButton(self)
        self.setupButton(sub_button_main2, 'Sub Button under Main Button 2', lambda: self.openExecutable('path/to/executable_main2'), '#9C27B0')  # Purple

        # Create another sub-button
        sub_button2 = QPushButton(self)
        self.setupButton(sub_button2, 'Additional Sub Button 1', lambda: self.openExecutable("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"), '#009688')  # Cyan

        sub_button3 = QPushButton(self)
        self.setupButton(sub_button3, 'Additional Sub Button 2', lambda: self.openExecutable("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"), '#607D8B')  # Gray

        # Add sub-buttons to the list for later management
        self.sub_buttons_main2.extend([sub_button_main2, sub_button2, sub_button3])

        # Add all buttons back to the layout
        self.addButtons()

        # Update the expansion state
        self.is_main_button2_expanded = True

    # Hide sub-buttons under the main button
    def hideSubButtonsMain(self):
        for sub_button in reversed(self.sub_buttons_main):
            sub_button.hide()

        # Update the expansion state
        self.is_main_button_expanded = False

    # Hide sub-buttons under the main button 2
    def hideSubButtonsMain2(self):
        for sub_button in reversed(self.sub_buttons_main2):
            sub_button.hide()

        # Update the expansion state
        self.is_main_button2_expanded = False

    # Clear all buttons
    def clearButtons(self):
        for sub_button in self.sub_buttons_main + self.sub_buttons_main2:
            sub_button.setParent(None)

    # Add all buttons back to the layout
    def addButtons(self):
        # Get the index of the main button
        main_button_index = self.vbox.indexOf(self.main_button)

        # Add sub-buttons under the main button
        for sub_button in self.sub_buttons_main:
            main_button_index += 1
            self.vbox.insertWidget(main_button_index, sub_button)

        # Get the index of the main button 2
        main_button2_index = self.vbox.indexOf(self.main_button2)

        # Add sub-buttons under the main button 2
        for sub_button in self.sub_buttons_main2:
            main_button2_index += 1
            self.vbox.insertWidget(main_button2_index, sub_button)

    # Open the executable file
    def openExecutable(self, executable_path):
        try:
            subprocess.Popen([executable_path])
        except Exception as e:
            print(f"Error opening executable: {e}")

# Main program entry point
if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_widget = MyWidget()
    my_widget.show()
    sys.exit(app.exec_())
