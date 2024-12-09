import sys
import random
import string
from PyQt5.QtWidgets import QApplication, QMainWindow
from login import Ui_Form  # Import the generated Python code from the .ui file


class LoginApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()  # Initialize the UI from login.py
        self.ui.setupUi(self)

        # Connect the "Generate" button to the function
        self.ui.generateButton.clicked.connect(self.generate_login_name)

    def generate_login_name(self):
        # Get the student name and ID from the input fields
        student_name = self.ui.studentNameInput.text().strip()
        student_id = self.ui.studentIdInput.text().strip()

        # Check if both fields are filled
        if student_name and student_id:
            # Generate the login name by concatenating name and ID
            login_name = f"{student_name}@{student_id}"

            # Generate a random password (e.g., length 8)
            password = self.generate_password()

            # Set the generated login and password to the labels
            self.ui.login.setText(f" {login_name}")  # Display login in QLabel
            self.ui.password.setText(f"{password}")  # Display password in QLabel
        else:
            self.ui.login.setText("Please fill in both fields!")
            self.ui.password.setText("")

    def generate_password(self):
        # Generate a random password with letters and digits (length 8)
        password_length = 8
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for _ in range(password_length))
        return password


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec_())
