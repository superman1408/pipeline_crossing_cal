from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import main_app # Import main_app at the top to access its global_app_info

class InfinityLoader(QtWidgets.QWidget):


    def __init__(self):
        super().__init__()
        self.setFixedSize(120, 80)
        self.path = self.create_infinity_path()
        self.percent = 0.0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_position)
        self.timer.start(16)


    def create_infinity_path(self):
        path = QtGui.QPainterPath()
        center = QtCore.QPointF(self.width() / 2, self.height() / 2)
        scale = 30
        path.moveTo(center)
        path.cubicTo(center.x() + scale, center.y() - scale,
                     center.x() + scale, center.y() + scale,
                     center.x(), center.y())
        path.cubicTo(center.x() - scale, center.y() - scale,
                     center.x() - scale, center.y() + scale,
                     center.x(), center.y())
        return path


    def update_position(self):
        self.percent += 0.005
        if self.percent >= 1.0:
            self.percent = 0.0
        self.update()


    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        pen = QtGui.QPen(QtGui.QColor(100, 100, 255, 80), 2)
        painter.setPen(pen)
        painter.drawPath(self.path)
        point = self.path.pointAtPercent(self.percent)
        painter.setBrush(QtGui.QColor(0, 191, 255))
        painter.setPen(QtCore.Qt.NoPen)
        painter.drawEllipse(point, 6, 6)
class TypingDialog(QtWidgets.QDialog):


    def __init__(self, message):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet("background-color: black;")
        self.setFixedSize(700, 100)
        self.label = QtWidgets.QLabel("")
        self.label.setStyleSheet("color: white; font-size: 16px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.full_text = message
        self.index = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_text)
        self.timer.start(30)


    def update_text(self):
        if self.index < len(self.full_text):
            self.label.setText(self.full_text[:self.index + 1])
            self.index += 1
        else:
            self.timer.stop()
            QtCore.QTimer.singleShot(10000, self.accept) # Increased delay to 10 seconds (10000 ms)
class LoginPage(QtWidgets.QDialog):


    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 350)
        self.setWindowTitle("Login Page")
        self.setStyleSheet("""
            QLabel#title {
                font-size: 24px;
                font-weight: bold;
            }
            QLabel {
                font-size: 14px;
            }
            QLineEdit {
                padding: 8px;
                font-size: 14px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            QPushButton {
                padding: 10px;
                font-size: 16px;
                background-color: #E46025;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #d94f13;
            }
        """)
        layout = QtWidgets.QVBoxLayout()
        logo = QtWidgets.QLabel()
        logo.setPixmap(QtGui.QPixmap("Assests//Ashkam LOGO (300 x 100 px).png").scaled(60, 60, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        logo.setAlignment(QtCore.Qt.AlignCenter)
        title = QtWidgets.QLabel("Welcome!")
        title.setObjectName("title")
        title.setAlignment(QtCore.Qt.AlignCenter)
        form_layout = QtWidgets.QFormLayout()
        self.username_input = QtWidgets.QLineEdit()
        self.date_input = QtWidgets.QLineEdit(QtCore.QDate.currentDate().toString("MMM dd, yyyy")) # Format date consistently
        self.project_input = QtWidgets.QLineEdit("Pipeline Crossing Project")
        form_layout.addRow("Username:", self.username_input)
        form_layout.addRow("Date:", self.date_input)
        form_layout.addRow("Project Name:", self.project_input)
        self.login_button = QtWidgets.QPushButton("Login")
        self.login_button.clicked.connect(self.accept)
        layout.addWidget(logo)
        layout.addWidget(title)
        layout.addSpacing(10)
        layout.addLayout(form_layout)
        layout.addSpacing(20)
        layout.addWidget(self.login_button)
        self.setLayout(layout)
class Launcher(QtWidgets.QMainWindow):


    def __init__(self):
        super().__init__()
        self.setWindowTitle("ASHKAM Energy Launcher")
        self.setFixedSize(600, 400)
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.central_widget.setStyleSheet("background-color: black;")
        self.show_loading_screen()


    def clear_layout(self):
        while self.layout.count():
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()


    def show_loading_screen(self):
        self.clear_layout()
        self.loader = InfinityLoader()
        label = QtWidgets.QLabel("Loading...")
        label.setStyleSheet("color: white; font-size: 18px;")
        label.setAlignment(QtCore.Qt.AlignCenter)
        container = QtWidgets.QWidget()
        vbox = QtWidgets.QVBoxLayout(container)
        vbox.addStretch()
        vbox.addWidget(self.loader, alignment=QtCore.Qt.AlignHCenter)
        vbox.addSpacing(10)
        vbox.addWidget(label)
        vbox.addStretch()
        self.layout.addWidget(container)
        self.fade_in_widget(container)
        QtCore.QTimer.singleShot(10000, self.show_typing_dialog) # Increased delay to 10 seconds (10000 ms)


    def show_typing_dialog(self):
        self.close()
        self.typing_dialog = TypingDialog("Please wait, the application is being programmed as per your computer resolution.")
        self.typing_dialog.finished.connect(self.show_login_screen)
        self.typing_dialog.exec_()


    def show_login_screen(self):
        login = LoginPage()
        if login.exec_() == QtWidgets.QDialog.Accepted:
            username = login.username_input.text()
            date = login.date_input.text()
            project = login.project_input.text()
            main_app.global_app_info["username"] = username
            main_app.global_app_info["project_name"] = project
            print("---- User Login Information (Stored Globally) ----")
            print(f"Username          : {main_app.global_app_info['username']}")
            print(f"Project Name      : {main_app.global_app_info['project_name']}")
            print("--------------------------------------------------")
            self.launch_main_app()
        else:
            # If login is cancelled, gracefully exit the application
            print("Login cancelled. Exiting application.")
            sys.exit(0) # Or QtWidgets.QApplication.quit()


    def launch_main_app(self):
        self.main_app = main_app.PipelineSimulationApp()
        self.main_app.showMaximized()
        self.close()


    def fade_in_widget(self, widget, duration=800):
        effect = QtWidgets.QGraphicsOpacityEffect()
        widget.setGraphicsEffect(effect)
        anim = QtCore.QPropertyAnimation(effect, b"opacity")
        anim.setDuration(duration)
        anim.setStartValue(0)
        anim.setEndValue(1)
        anim.start()
        self.anim = anim


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    launcher = Launcher()
    launcher.show()
    sys.exit(app.exec_())