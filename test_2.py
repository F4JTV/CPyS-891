#!/usr/bin/python3
import sys
from datetime import datetime

import Hamlib
import serial.tools.list_ports
from PyQt5.Qt import *
Hamlib.rig_set_debug(Hamlib.RIG_DEBUG_VERBOSE)

APP_NAME = "App Name"
APP_VERSION = datetime.strftime(datetime.now(), "%y%m%d")
APP_TITLE = f"{APP_NAME} - v{APP_VERSION}"
ICON = "./images/icon.png"
FONT = "./fonts/Quicksand-Regular.ttf"
FONT_FAMILY = "Quicksand"
FONT_SIZE = 12
VFOA = Hamlib.RIG_VFO_A
VFOB = Hamlib.RIG_VFO_B
RIG = Hamlib.RIG_MODEL_FT891


def get_ports():

    port_list = serial.tools.list_ports.comports(True)
    if not port_list:
        return False, "No port available"
    return True, port_list


class MainWindow(QMainWindow):
    """ Main Window """

    def __init__(self, appli, **kwargs):
        super().__init__(**kwargs)

        # ####### Main Window config
        self.setWindowTitle(APP_TITLE)
        self.setWindowIcon(QIcon(ICON))
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)

        # ####### Variables
        self.app = appli
        self.rig = Hamlib.Rig(RIG)
        self.serial_speed = None
        self.device_path = None

        # ####### Central Widget
        self.central_Widget = QWidget()
        self.setCentralWidget(self.central_Widget)

        # ####### Main Layout
        self.main_layout = QVBoxLayout()
        self.central_Widget.setLayout(self.main_layout)

        # ####### Main Layout
        self.band_grp = QGroupBox("Bands")
        self.mode_grp = QGroupBox("Mode")
        self.main_layout.addWidget(self.band_grp,)
        self.main_layout.addWidget(self.mode_grp)

        # ####### Bands Layout
        self.band_layout = QGridLayout()
        self.band_grp.setLayout(self.band_layout)

        self.band_btn_grp = QButtonGroup()
        self.btn_80_m = QPushButton("80m")
        self.btn_60_m = QPushButton("60m")
        self.btn_40_m = QPushButton("40m")
        self.btn_30_m = QPushButton("30m")
        self.btn_20_m = QPushButton("20m")
        self.btn_17_m = QPushButton("17m")
        self.btn_15_m = QPushButton("15m")
        self.btn_12_m = QPushButton("12m")
        self.btn_10_m = QPushButton("10m")
        self.btn_6_m = QPushButton("6m")

        self.btn_80_m.clicked.connect(lambda: self.rig.set_freq(Hamlib.RIG_VFO_A, 3500000))
        self.btn_60_m.clicked.connect(lambda: self.rig.set_freq(Hamlib.RIG_VFO_A, 5351500))
        self.btn_40_m.clicked.connect(lambda: self.rig.set_freq(Hamlib.RIG_VFO_A, 7000000))
        self.btn_30_m.clicked.connect(lambda: self.rig.set_freq(Hamlib.RIG_VFO_A, 10100000))
        self.btn_20_m.clicked.connect(lambda: self.rig.set_freq(Hamlib.RIG_VFO_A, 14000000))
        self.btn_17_m.clicked.connect(lambda: self.rig.set_freq(Hamlib.RIG_VFO_A, 18068000))
        self.btn_15_m.clicked.connect(lambda: self.rig.set_freq(Hamlib.RIG_VFO_A, 21000000))
        self.btn_12_m.clicked.connect(lambda: self.rig.set_freq(Hamlib.RIG_VFO_A, 24890000))
        self.btn_10_m.clicked.connect(lambda: self.rig.set_freq(Hamlib.RIG_VFO_A, 28000000))
        self.btn_6_m.clicked.connect(lambda: self.rig.set_freq(Hamlib.RIG_VFO_A, 50000000))

        self.band_btn_grp.addButton(self.btn_80_m)
        self.band_btn_grp.addButton(self.btn_60_m)
        self.band_btn_grp.addButton(self.btn_40_m)
        self.band_btn_grp.addButton(self.btn_30_m)
        self.band_btn_grp.addButton(self.btn_20_m)
        self.band_btn_grp.addButton(self.btn_17_m)
        self.band_btn_grp.addButton(self.btn_15_m)
        self.band_btn_grp.addButton(self.btn_12_m)
        self.band_btn_grp.addButton(self.btn_10_m)
        self.band_btn_grp.addButton(self.btn_6_m)

        self.btn_80_m.setCheckable(True)
        self.btn_60_m.setCheckable(True)
        self.btn_40_m.setCheckable(True)
        self.btn_30_m.setCheckable(True)
        self.btn_20_m.setCheckable(True)
        self.btn_17_m.setCheckable(True)
        self.btn_15_m.setCheckable(True)
        self.btn_12_m.setCheckable(True)
        self.btn_10_m.setCheckable(True)
        self.btn_6_m.setCheckable(True)

        self.band_layout.addWidget(self.btn_80_m, 0, 0, 1, 1)
        self.band_layout.addWidget(self.btn_60_m, 0, 1, 1, 1)
        self.band_layout.addWidget(self.btn_40_m, 0, 2, 1, 1)
        self.band_layout.addWidget(self.btn_30_m, 0, 3, 1, 1)
        self.band_layout.addWidget(self.btn_20_m, 0, 4, 1, 1)
        self.band_layout.addWidget(self.btn_17_m, 1, 0, 1, 1)
        self.band_layout.addWidget(self.btn_15_m, 1, 1, 1, 1)
        self.band_layout.addWidget(self.btn_12_m, 1, 2, 1, 1)
        self.band_layout.addWidget(self.btn_10_m, 1, 3, 1, 1)
        self.band_layout.addWidget(self.btn_6_m, 1, 4, 1, 1)

        # ####### Mode Layout
        self.mode_layout = QGridLayout()
        self.mode_grp.setLayout(self.mode_layout)

        self.cw_mode = QPushButton("CW")
        self.ssb_mode = QPushButton("SSB")
        self.am_mode = QPushButton("AM")
        self.nfm_mode = QPushButton("NFM")
        self.data_mode = QPushButton("DATA")

        self.cw_mode.clicked.connect(lambda: self.rig.set_mode(Hamlib.RIG_MODE_CW))
        self.ssb_mode.clicked.connect(lambda: self.rig.set_mode(Hamlib.RIG_MODE_LSB))
        self.am_mode.clicked.connect(lambda: self.rig.set_mode(Hamlib.RIG_MODE_AM))
        self.nfm_mode.clicked.connect(lambda: self.rig.set_mode(Hamlib.RIG_MODE_FM))
        self.data_mode.clicked.connect(lambda: self.rig.set_mode(Hamlib.RIG_MODE_PKTUSB))

        self.mode_layout.addWidget(self.cw_mode, 0, 0, 1, 1)
        self.mode_layout.addWidget(self.ssb_mode, 0, 1, 1, 1)
        self.mode_layout.addWidget(self.am_mode, 0, 2, 1, 1)
        self.mode_layout.addWidget(self.nfm_mode, 0, 3, 1, 1)
        self.mode_layout.addWidget(self.data_mode, 0, 4, 1, 1)

        self.cw_mode.setCheckable(True)
        self.ssb_mode.setCheckable(True)
        self.am_mode.setCheckable(True)
        self.nfm_mode.setCheckable(True)
        self.data_mode.setCheckable(True)

        self.mode_btn_grp = QButtonGroup()
        self.mode_btn_grp.addButton(self.cw_mode)
        self.mode_btn_grp.addButton(self.ssb_mode)
        self.mode_btn_grp.addButton(self.am_mode)
        self.mode_btn_grp.addButton(self.nfm_mode)
        self.mode_btn_grp.addButton(self.data_mode)

        self.config = ConfigWindow(self)
        self.config.exec()

        self.get_rig_info()

    def get_rig_info(self):
        freq = int(self.rig.get_freq(Hamlib.RIG_VFO_A))
        mode = self.rig.get_mode(Hamlib.RIG_VFO_A)[0]

        if mode == Hamlib.RIG_MODE_LSB:
            self.ssb_mode.setChecked(True)
        elif mode == Hamlib.RIG_MODE_USB:
            self.ssb_mode.setChecked(True)
        elif mode == Hamlib.RIG_MODE_FM:
            self.nfm_mode.setChecked(True)
        elif mode == Hamlib.RIG_MODE_AM:
            self.am_mode.setChecked(True)
        elif mode == Hamlib.RIG_MODE_CW:
            self.cw_mode.setChecked(True)

    def connect_rig(self):
        self.rig.set_conf("rig_pathname", self.device_path)
        self.rig.set_conf("retry", "5")
        self.rig.set_conf("serial_speed", self.serial_speed)
        self.rig.open()

    def closeEvent(self, a0):
        self.rig.close()


class ConfigWindow(QDialog):
    def __init__(self, master, **kwargs):
        super().__init__(**kwargs)

        self.master = master

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)

        self.combo_port = QComboBox()
        self.combo_speed = QComboBox()
        self.main_layout.addWidget(self.combo_port, 0, 0, 1, 1)
        self.main_layout.addWidget(self.combo_speed, 0, 1, 1, 1)

        self.combo_speed.addItems(["4800", "9600", "19200", "38400"])
        self.combo_speed.setEditable(True)
        self.combo_speed.setMinimumWidth(200)
        self.combo_speed.lineEdit().setReadOnly(True)
        self.combo_speed.lineEdit().setAlignment(Qt.AlignCenter)
        for i in range(0, self.combo_speed.count()):
            self.combo_speed.setItemData(i, Qt.AlignCenter, Qt.TextAlignmentRole)

        self.combo_port.setEditable(True)
        self.combo_port.setMinimumWidth(200)
        self.combo_port.lineEdit().setReadOnly(True)
        self.combo_port.lineEdit().setAlignment(Qt.AlignCenter)

        rep, data = get_ports()
        if rep:
            # self.combo_port.addItems(data)
            for port in sorted(data):
                self.combo_port.addItem(port.device)
        else:
            self.combo_port.addItem(data)

        for i in range(0, self.combo_port.count()):
            self.combo_port.setItemData(i, Qt.AlignCenter, Qt.TextAlignmentRole)

        self.ok_btn = QPushButton("Ok")
        self.main_layout.addWidget(self.ok_btn, 1, 0, 1, 2)
        self.ok_btn.clicked.connect(self.validate_rig)

    def validate_rig(self):
        self.master.serial_speed = self.combo_speed.currentText()
        self.master.device_path = self.combo_port.currentText()
        self.master.connect_rig()
        self.close()


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
    splash.finish(window.config)
    window.show()
    window.resize(window.minimumSizeHint())
    sys.exit(app.exec_())
