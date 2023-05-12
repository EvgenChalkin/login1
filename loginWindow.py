from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtGui import QFont
import sys
from modalsWindow import ModalLogin, CaptchaLogin

class LoginWindow(QWidget):
    def enterClicked(self, login, password):
            if login == "user" and password == "user":
                self.modal = ModalLogin()
                self.modal.show()
            else:
                self.captchaModal = CaptchaLogin()
                self.captchaModal.show()

    
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("Вход")
        self.setFixedSize(300, 400)

        self.login_lbl = QLabel("Введите логин:")
        self.password_lbl = QLabel("Введите пароль:")
        self.login_edit = QLineEdit()
        self.password_edit = QLineEdit()
        self.enter_btn = QPushButton("Вход")
    
        font = QFont("Comic Sans MS", pointSize=25)
        font_btn = QFont("Comic Sans MS", pointSize=20)
        self.login_lbl.setFont(font)
        self.login_edit.setFont(font)
        self.password_lbl.setFont(font)
        self.password_edit.setFont(font)
        self.enter_btn.setFont(font_btn)
        self.login_edit.setPlaceholderText("Логин")
        self.password_edit.setPlaceholderText("Пароль")

        self.enter_btn.clicked.connect(lambda: self.enterClicked(self.login_edit.text(), self.password_edit.text()))

        vbox = QVBoxLayout()
        vbox.addWidget(self.login_lbl)
        vbox.addWidget(self.login_edit)
        vbox.addWidget(self.password_lbl)
        vbox.addWidget(self.password_edit)
        vbox.addWidget(self.enter_btn)
        self.setLayout(vbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginWindow = LoginWindow()
    loginWindow.show()
    app.exec()