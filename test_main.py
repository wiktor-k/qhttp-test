from main import Window
from PySide6 import QtCore
from http.client import HTTPConnection


def test_no_op(qtbot):
    assert True


def test_start_server(qtbot):
    window = Window()
    qtbot.addWidget(window)
    qtbot.mouseClick(window.button, QtCore.Qt.MouseButton.LeftButton)

    conn = HTTPConnection("127.0.0.1", 19841)

    conn.request("GET", "/")

    print("Before")
    resp = conn.getresponse()
    print("After")
    assert resp.status == 200
