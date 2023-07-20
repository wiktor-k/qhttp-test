from main import Window
from PySide6 import QtCore
from http.client import HTTPConnection
import threading


def test_no_op(qtbot):
    assert True


def test_start_server(qtbot):
    window = Window()
    qtbot.addWidget(window)
    qtbot.mouseClick(window.button, QtCore.Qt.MouseButton.LeftButton)

    conn = HTTPConnection("127.0.0.1", 19841)

    conn.request("GET", "/")

    print("Before")

    resp = None

    def get_response_in_thread():
        nonlocal resp
        resp = conn.getresponse()

    t = threading.Thread(target=get_response_in_thread)
    t.start()

    # waitUntil() waits for the response to arrive,
    # while keeping the Qt event loop running.
    qtbot.waitUntil(lambda: resp is not None)
    print("After")
    assert resp.status == 200
