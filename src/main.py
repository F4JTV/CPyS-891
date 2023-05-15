#!/usr/bin/python3
import sys
from datetime import datetime

import serial
from PyQt5.Qt import *
from py891 import constants

APP_NAME = "py891"
APP_VERSION = datetime.strftime(datetime.now(), "%y%m%d")
APP_TITLE = f"{APP_NAME} - v{APP_VERSION}"
ICON = "../images/icon.png"
FONT = "../fonts/Quicksand-Regular.ttf"
FONT_FAMILY = "Quicksand"
FONT_SIZE = 12


class MainWindow(QMainWindow):
    """ Main Window """

    def __init__(self, appli, **kwargs):
        super().__init__(**kwargs)

        # self.setWindowTitle(APP_TITLE)
        self.setWindowIcon(QIcon(ICON))
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)

        self.app = appli

        self.central_Widget = QWidget()
        self.setCentralWidget(self.central_Widget)

        self.main_layout = QVBoxLayout()
        self.central_Widget.setLayout(self.main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Font
    QFontDatabase.addApplicationFont(FONT)
    app.setFont(QFont(FONT_FAMILY, FONT_SIZE))

    # Splash Screen
    splash = QSplashScreen(QPixmap(ICON))
    splash.show()
    splash.showMessage(APP_NAME, Qt.AlignmentFlag.AlignHCenter |
                       Qt.AlignmentFlag.AlignBottom, Qt.GlobalColor.black)

    app.processEvents()
    window = MainWindow(app)
    splash.finish(window)
    window.show()
    # window.resize(window.minimumSizeHint())
    sys.exit(app.exec_())
