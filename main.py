import sys

from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow,
    QPushButton,
    QFileDialog,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
)

from PySide6.QtHttpServer import QHttpServer
from PySide6.QtNetwork import QHostAddress, QTcpServer


def route(request):
    print(f"processing request: {request}")
    return "response"


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.button = QPushButton(self)
        self.button.setText("Start listening")
        self.button.clicked.connect(self.start_listen_clicked)

    def start_listen_clicked(self):
        httpServer = QHttpServer()
        httpServer.route("/", route)

        httpServer.listen(QHostAddress.LocalHost, 19841)
        self.server = httpServer
        print(f"Server: {self.server}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = Window()
    win.show()

    sys.exit(app.exec())
