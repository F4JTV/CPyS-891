#!/usr/bin/python3
##########################################################################
#   CPyS-891 is a CPS for the Yaesu FT-891 made with Python3 and PyQt5   #
#                 It uses serial module for CAT protocol                 #
#                                                                        #
#                  ___ ___      ___     ___ ___ _                        #
#                 / __| _ \_  _/ __|___( _ / _ / |                       #
#                | (__|  _| || \__ |___/ _ \_, | |                       #
#                 \___|_|  \_, |___/   \___//_/|_|                       #
#                          |__/                                          #
##########################################################################
import platform
import sys
from datetime import datetime
import configparser

import serial.tools.list_ports
from PyQt5.Qt import *

# TODO: Functions
# TODO: Memory
# TODO: save config to file (json)
# TODO: open config from file (json)
# TODO: Presets (json)
# TODO: About window

APP_NAME = "CPyS-891"
APP_VERSION = datetime.strftime(datetime.now(), "0.%m%d")
APP_TITLE = f"{APP_NAME} - v{APP_VERSION}"
ICON = "./images/icon.png"
FONT = "./fonts/Quicksand-Regular.ttf"
FONT_FAMILY = "Quicksand"
FONT_SIZE = 11
ENCODER = "ascii"
PEAK_HOLD = {"OFF": b"0", "0.5 sec": b"1",
             "1.0 sec": b"2", "2.0 sec": b"3"}
ZIN_LED = {"DISABLE": b"0", "ENABLE": b"1"}
POPUP_MENU = {"UPPER": b"0", "LOWER": b"1"}
KEYER_TYPE = {"OFF": b"0", "BUG": b"1", "ELEKEY-A": b"2",
              "ELEKEY-B": b"3", "ELEKEY-Y": b"4", "ACS": b"5"}
KEYER_DOT_DASH = {"NOR": b"0", "REV": b"1"}
NUMBER_STYLE = {"1290": b"0", "AUNO": b"1",
                "AUNT": b"2", "A2NO": b"3",
                "A2NT": b"4", "12NO": b"5",
                "12NT": b"6"}
CW_MEMORY = {"TEXT": b"0", "MESSAGE": b"1"}
NB_WIDHT = {"1 msec": b"0", "3 msec": b"1", "10 msec": b"2"}
NB_REJECTION = {"10 dB": b"0", "30 dB": b"1", "50 dB": b"2"}
RF_SQL_VR = {"RF": b"0", "SQL": b"1"}
CAT_RATE = {"4800 bds": b"0", "9600 bds": b"1",
            "19200 bps": b"2", "38400 bps": b"3"}
CAT_TOT = {"10 msec": b"0", "100 msec": b"1",
           "1000 msec": b"2", "3000 msec": b"3"}
CAT_RTS = {"DISABLE": b"0", "ENABLE": b"1"}
MEMORY_GROUP = {"DISABLE": b"0", "ENABLE": b"1"}
FM_SETTING = {"DISABLE": b"0", "ENABLE": b"1"}
REC_SETTING = {"DISABLE": b"0", "ENABLE": b"1"}
ATAS_SETTING = {"DISABLE": b"0", "ENABLE": b"1"}
MIC_SCAN = {"DISABLE": b"0", "ENABLE": b"1"}
MIC_SCAN_RESUME = {"PAUSE": b"0", "TIME": b"1"}
CLAR_SELECT = {"RX": b"0", "TX": b"1", "TRX": b"2"}
APO = {"OFF": b"0", "1 h": b"1", "2 h": b"2", "4 h": b"3",
       "6 h": b"4", "8 h": b"5", "10 h": b"6", "12 h": b"7"}
FAN_CONTROL = {"NORMAL": b"0", "CONTEST": b"1"}
LCUT_FREQ = {"OFF": b"00", "100 Hz": b"01", "150 Hz": b"02",
             "200 Hz": b"03", "250 Hz": b"04", "300 Hz": b"05",
             "350 Hz": b"06", "400 Hz": b"07", "450 Hz": b"08",
             "500 Hz": b"09", "550 Hz": b"10", "600 Hz": b"11",
             "650 Hz": b"12", "700 Hz": b"13", "750 Hz": b"14",
             "800 Hz": b"15", "850 Hz": b"16", "900 Hz": b"17",
             "950 Hz": b"18", "1000 Hz": b"19"}
HCUT_FREQ = {"OFF": b"00", "700 Hz": b"01", "750 Hz": b"02",
             "800 Hz": b"03", "850 Hz": b"04", "900 Hz": b"05",
             "950 Hz": b"06", "1000 Hz": b"07", "1050 Hz": b"08",
             "1100 Hz": b"09", "1150 Hz": b"10", "1200 Hz": b"11",
             "1250 Hz": b"12", "1300 Hz": b"13", "1350 Hz": b"14",
             "1400 Hz": b"15", "1450 Hz": b"16", "1500 Hz": b"17",
             "1550 Hz": b"18", "1600 Hz": b"19", "1650 Hz": b"20",
             "1700 Hz": b"21", "1750 Hz": b"22", "1800 Hz": b"23",
             "1850 Hz": b"24", "1900 Hz": b"25", "1950 Hz": b"26",
             "2000 Hz": b"27", "2050 Hz": b"28", "2100 Hz": b"29",
             "2150 Hz": b"30", "2200 Hz": b"31", "2250 Hz": b"32",
             "2300 Hz": b"33", "2350 Hz": b"34", "2400 Hz": b"35",
             "2450 Hz": b"36", "2500 Hz": b"37", "2550 Hz": b"38",
             "2600 Hz": b"39", "2650 Hz": b"40", "2700 Hz": b"41",
             "2750 Hz": b"42", "2800 Hz": b"43", "2850 Hz": b"44",
             "2900 Hz": b"45", "2950 Hz": b"46", "3000 Hz": b"47",
             "3050 Hz": b"48", "3100 Hz": b"49", "3150 Hz": b"50",
             "3200 Hz": b"51", "3250 Hz": b"52", "3300 Hz": b"53",
             "3350 Hz": b"54", "3400 Hz": b"55", "3450 Hz": b"56",
             "3500 Hz": b"57", "3550 Hz": b"58", "3600 Hz": b"59",
             "3650 Hz": b"60", "3700 Hz": b"61", "3750 Hz": b"62",
             "3800 Hz": b"63", "3850 Hz": b"64", "3900 Hz": b"65",
             "3950 Hz": b"66", "4000 Hz": b"67"}
AM_MIC_SELECT = {"MIC": b"0", "REAR": b"1"}
AM_PTT_SELECT = {"DAKY": b"0", "RTS": b"1", "DTR": b"2"}
CW_AUTO_MODE = {"OFF": b"0", "50M": b"1", "ON": b"2"}
CW_BFO = {"USB": b"0", "LSB": b"1", "AUTO": b"2"}
CW_BK_IN_TYPE = {"SEMI": b"0", "FULL": b"1"}
CW_WAVE_SHAPE = {"2 msec": b"1", "4 msec": b"2"}
CW_FREQ_DISPLAY = {"FREQ": b"0", "PITCH": b"1"}
PC_KEYING = {"OFF": b"0", "DAKY": b"1",
             "RTS": b"2", "DTR": b"3"}
QSK_DELAY_TIME = {"15 msec": b"0", "20 msec": b"1",
                  "25 msec": b"2", "30 msec": b"3"}
DATA_MODE = {"PSK": b"0", "OTHER": b"1"}
PSK_TONE = {"1000 Hz": b"0", "1500 Hz": b"1", "2000 Hz": b"2"}
SLOPE = {"6 dB/oct": b"0", "18 dB/oct": b"1"}
DATA_IN_SELECT = {"MIC": b"0", "REAR": b"1"}
DATA_PTT_SELECT = {"DAKY": b"0", "RTS": b"1", "DTR": b"2"}
DATA_BFO = {"USB": b"0", "LSB": b"1"}
FM_MIC_SELECT = {"MIC": b"0", "REAR": b"1"}
PKT_PTT_SELECT = {"DAKY": b"0", "RTS": b"1", "DTR": b"2"}
DCS_POLARITY = {"Tn-Rn": b"0", "Tn-Riv": b"1",
                "Tiv-Rn": b"2", "Tiv-Riv": b"3"}
RTTY_SHIT_PORT = {"SHIFT": b"0", "DTR": b"1", "RTS": b"2"}
RTTY_POLARITY = {"NOR": b"0", "REV": b"1"}
RTTY_SHIFT_FREQ = {"170 Hz": b"0", "200 Hz": b"1",
                   "425 Hz": b"2", "850 Hz": b"3"}
RTTY_MARK_FREQ = {"1275 Hz": b"0", "2125 Hz": b"1"}
RTTY_BFO = {"USB": b"0", "LSB": b"1"}
SSB_MIC_SELECT = {"MIC": b"0", "REAR": b"1"}
SSB_BFO = {"USB": b"0", "LSB": b"1", "AUTO": b"2"}
SSB_PTT_SELECT = {"DAKY": b"0", "RTS": b"1", "DTR": b"2"}
SSB_TX_BPF = {"100-3000": b"0", "100-2900": b"1",
              "200-2800": b"2", "300-2700": b"3",
              "400-2600": b"4"}
APF_WIDTH = {"NARROW": b"0", "MEDIUM": b"1", "WIDE": b"2"}
IF_NOTCH_WIDTH = {"NARROW": b"0", "WIDE": b"1"}
SCP_START_CYCLE = {"OFF": b"0", "3 sec": b"1",
                   "2.5 sec": b"2", "10 sec": b"3"}
SCP_SPAN_FREQ = {"37.5 kHz": b"00", "75 kHz": b"01",
                 "150 kHz": b"02", "375 kHz": b"03",
                 "750 kHz": b"04"}
QUICK_DIAL = {"50 kHz": b"0", "100 kHz": b"1", "500 kHz": b"2"}
SSB_DIAL_STEP = {"2 Hz": b"0", "5 Hz": b"1", "10 Hz": b"2"}
AM_DIAL_STEP = {"10 Hz": b"0", "100 Hz": b"1"}
FM_DIAL_STEP = {"10 Hz": b"0", "100 Hz": b"1"}
DIAL_STEP = {"2 Hz": b"0", "5 Hz": b"1", "10 Hz": b"2"}
AM_CH_STEP = {"2.5 kHz": b"0", "5 kHz": b"1",
              "9 kHz": b"2", "10 kHz": b"3",
              "12.5 kHz": b"4", "25 kHz": b"5"}
FM_CH_STEP = {"5 kHz": b"0", "6.25 kHz": b"1",
              "10 kHz": b"2", "12.5 kHz": b"3",
              "15 kHz": b"4", "20 kHz": b"5",
              "25 kHz": b"6"}
EQ_1_FREQ = {"OFF": b"00", "100 Hz": b"01", "200 Hz": b"02",
             "300 Hz": b"03", "400 Hz": b"04", "500 Hz": b"05",
             "600 Hz": b"06", "700 Hz": b"07"}
EQ_2_FREQ = {"OFF": b"00", "700 Hz": b"01", "800 Hz": b"02",
             "900 Hz": b"03", "1000 Hz": b"04", "1100 Hz": b"05",
             "1200 Hz": b"06", "1300 Hz": b"07", "1400 Hz": b"08",
             "1500 Hz": b"09"}
EQ_3_FREQ = {"OFF": b"00", "1500 Hz": b"01", "1600 Hz": b"02",
             "1700 Hz": b"03", "1800 Hz": b"04", "1900 Hz": b"05",
             "2000 Hz": b"06", "2100 Hz": b"07", "2200 Hz": b"08",
             "2300 Hz": b"09", "2400 Hz": b"10", "2500 Hz": b"11",
             "2600 Hz": b"12", "2700 Hz": b"13", "2800 Hz": b"14",
             "2900 Hz": b"15", "3000 Hz": b"16", "3100 Hz": b"17",
             "3200 Hz": b"18"}
TUNER_SELECT = {"OFF": b"0", "EXTERNAL": b"1",
                "ATAS": b"2", "LAMP": b"3"}
VOX_SELECT = {"MIC": b"0", "DATA": b"1"}
EMERGENCY_FREQ = {"DISABLE": b"0", "ENABLE": b"1"}
RESET = {"ALL": b"0", "DATA": b"1", "FUNC": b"2"}
BAUDRATE = ["4800", "9600", "19200", "38400"]
CLAR_STATE = {"ON": b"0", "OFF": b"1"}
MODES = {"LSB": b"1", "USB": b"2", "CW": b"3",
         "FM": b"4", "AM": b"5", "RTTY-LSB": b"6",
         "CW-R": b"7", "DATA-LSB": b"8", "FM-N": b"B",
         "DATA-USB": b"C", "AM-N": b"D"}
CTCSS_STATE = {"CTCSS OFF": b"0", "CTCSS ENC/DEC": b"1",
               "CTCSS ENC": b"2"}
RPT_SHIFT_DIR = {"Simplex": b"0", "Plus Shift": b"1",
                 "Minus Shift": b"2"}
TAG_STATE = {"TAG OFF": b"0", "TAG ON": b"1"}


def format_combo(combobox):
    for i in range(0, combobox.count()):
        combobox.setItemData(i, Qt.AlignCenter, Qt.TextAlignmentRole)


class MainWindow(QMainWindow):
    """ Main Window """

    def __init__(self, appli, **kwargs):
        super().__init__(**kwargs)

        # ####### Config
        try:
            self.config = configparser.ConfigParser()
            self.config.read("./CPyS.cfg")
        except FileNotFoundError:
            error_box = QMessageBox(QMessageBox.Critical,
                                    "Config error",
                                    '"CPyS.cfg" file not found',
                                    QMessageBox.Ok)
            error_box.setModal(True)
            error_box.exec_()
            sys.exit()

        if platform.system() == "Windows":
            self.com_port = self.config["DEFAULT"]["windows_port"]
        elif platform.system() == "Linux":
            self.com_port = self.config["DEFAULT"]["linux_port"]
        self.baudrate = self.config["DEFAULT"]["baudrate"]

        self.app = appli
        self.transfert = True
        self.old_beacon_interval = int()
        self.progressbar = QProgressBar()

        # ###### Status Bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        self.central_Widget = QWidget()
        self.setCentralWidget(self.central_Widget)

        self.main_layout = QVBoxLayout()
        self.central_Widget.setLayout(self.main_layout)

        # ###### Rig
        self.rig = serial.Serial(baudrate=self.baudrate,
                                 bytesize=8,
                                 timeout=0.1,
                                 stopbits=serial.STOPBITS_ONE,
                                 rtscts=True)  # Need the rts / cts active to comm to FT-891
        try:
            self.rig.setPort(self.com_port)
            """self.rig.open()  # In code change remove the '#' in front
            self.rig.write(b"FA;")
            rep = self.rig.read_until(";")
            rep = rep.replace(b";", b"")
            rep = rep.decode(ENCODER)
            if re.match("^FA\d{9}$", rep):
                self.status_bar.showMessage(self.com_port + ' Connected.')
            else:
                raise serial.SerialException"""

        except serial.SerialException:
            error_box = QMessageBox(QMessageBox.Critical,
                                    "Connection error",
                                    'Check "CPyS.cfg" file and check if the FT-891 is plugged',
                                    QMessageBox.Ok)
            error_box.setModal(True)
            error_box.exec_()
            sys.exit()

        # ###### Main Window config
        self.setWindowTitle(APP_TITLE)
        self.setWindowIcon(QIcon(ICON))
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setMouseTracking(True)

        # ###### Menu Bar
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        self.file_menu = QMenu("&Files")
        self.edit_menu = QMenu("&Edit")
        self.help_menu = QMenu("&Help")
        self.menu_bar.addMenu(self.file_menu)
        self.menu_bar.addMenu(self.edit_menu)
        self.menu_bar.addMenu(self.help_menu)

        # Files Actions
        self.save_config_action = QAction("&Save config")
        self.file_menu.addAction(self.save_config_action)

        self.open_config_action = QAction("&Open config file")
        self.file_menu.addAction(self.open_config_action)
        self.file_menu.addSeparator()

        self.exit_action = QAction("Exit")
        self.file_menu.addAction(self.exit_action)
        # noinspection PyTypeChecker
        self.exit_action.triggered.connect(self.close)

        # Edit Actions
        self.live_mode_action = QAction("&Live Mode")
        self.edit_menu.addAction(self.live_mode_action)
        self.edit_menu.addSeparator()
        self.live_mode_action.setCheckable(True)
        self.live_mode_action.setChecked(True)
        self.live_mode_action.triggered.connect(self.toggle_live_mode)

        self.send_to_radio_action = QAction("Send config to FT-891")
        self.edit_menu.addAction(self.send_to_radio_action)
        self.send_to_radio_action.setDisabled(True)
        self.send_to_radio_action.triggered.connect(self.send_config_2_radio)

        self.get_from_radio_action = QAction("Get config from FT-891")
        self.edit_menu.addAction(self.get_from_radio_action)
        self.get_from_radio_action.triggered.connect(self.get_config_from_radio)
        # self.get_from_radio_action.setDisabled(True)

        # Help Actions
        self.about_action = QAction("&About CPyS")
        self.help_menu.addAction(self.about_action)
        self.doc_action = QAction("Online &Doc")
        self.help_menu.addAction(self.doc_action)

        # ###### Tab
        self.tab = QTabWidget()
        self.main_layout.addWidget(self.tab)

        self.menu_tab = QWidget()
        self.memory_tab = QWidget()
        self.pms_tab = QWidget()

        self.tab.addTab(self.menu_tab, "Menu / Functions")
        self.tab.addTab(self.memory_tab, "Memory")
        self.tab.addTab(self.pms_tab, "PMS")

        # ###### Menu tab
        self.menu_layout = QHBoxLayout()
        self.menu_tab.setLayout(self.menu_layout)

        self.menu_table = QTableWidget(171, 3)
        self.function_layout = QScrollArea()
        self.menu_layout.addWidget(self.menu_table, 1)
        self.menu_layout.addWidget(self.function_layout, 3)

        # Menu Table
        self.menu_table.verticalHeader().setVisible(False)
        self.menu_table.horizontalHeader().setVisible(False)
        self.menu_table.setSortingEnabled(False)
        self.menu_table.setAlternatingRowColors(True)
        self.menu_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.menu_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.menu_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        if platform.system() == "Windows":
            self.menu_table.setMinimumSize(800, 450)
        elif platform.system() == "Linux":
            self.menu_table.setMinimumSize(600, 450)

        # ### ACG
        self.acg_separator = QTableWidgetItem("ACG")
        self.menu_table.setItem(0, 0, self.acg_separator)
        self.menu_table.setSpan(0, 0, 1, 3)
        self.acg_separator.setBackground(QColor(Qt.GlobalColor.lightGray))
        # 01-01
        self.acg_fast_menu_number = QTableWidgetItem("01-01")
        self.acg_fast_parm_name = QTableWidgetItem("ACG FAST DELAY")

        self.acg_fast_spin = QSpinBox()
        self.acg_fast_spin.setAlignment(Qt.AlignCenter)
        self.acg_fast_spin.setMaximum(4000)
        self.acg_fast_spin.setMinimum(20)
        self.acg_fast_spin.setValue(300)
        self.acg_fast_spin.setSingleStep(20)
        self.acg_fast_spin.setSuffix(" msec")
        self.acg_fast_spin.valueChanged.connect(self.set_acg_fast_delay)

        self.menu_table.setItem(1, 0, self.acg_fast_menu_number)
        self.menu_table.setItem(1, 1, self.acg_fast_parm_name)
        self.menu_table.setCellWidget(1, 2, self.acg_fast_spin)

        # 01-02
        self.acg_mid_menu_number = QTableWidgetItem("01-02")
        self.acg_mid_parm_name = QTableWidgetItem("ACG MID DELAY")

        self.acg_mid_spin = QSpinBox()
        self.acg_mid_spin.setAlignment(Qt.AlignCenter)
        self.acg_mid_spin.setMaximum(4000)
        self.acg_mid_spin.setMinimum(20)
        self.acg_mid_spin.setValue(700)
        self.acg_mid_spin.setSingleStep(20)
        self.acg_mid_spin.setSuffix(" msec")
        self.acg_mid_spin.valueChanged.connect(self.set_acg_mid_delay)

        self.menu_table.setItem(2, 0, self.acg_mid_menu_number)
        self.menu_table.setItem(2, 1, self.acg_mid_parm_name)
        self.menu_table.setCellWidget(2, 2, self.acg_mid_spin)

        # 01-03
        self.acg_slow_menu_number = QTableWidgetItem("01-03")
        self.acg_slow_parm_name = QTableWidgetItem("ACG SLOW DELAY")

        self.acg_slow_spin = QSpinBox()
        self.acg_slow_spin.setAlignment(Qt.AlignCenter)
        self.acg_slow_spin.setMaximum(4000)
        self.acg_slow_spin.setMinimum(20)
        self.acg_slow_spin.setValue(3000)
        self.acg_slow_spin.setSingleStep(20)
        self.acg_slow_spin.setSuffix(" msec")
        self.acg_slow_spin.valueChanged.connect(self.set_acg_slow_delay)

        self.menu_table.setItem(3, 0, self.acg_slow_menu_number)
        self.menu_table.setItem(3, 1, self.acg_slow_parm_name)
        self.menu_table.setCellWidget(3, 2, self.acg_slow_spin)

        # ### DISPLAY
        self.display_separator = QTableWidgetItem("DISPLAY")
        self.display_separator.setBackground(QColor(Qt.GlobalColor.lightGray))
        self.menu_table.setItem(4, 0, self.display_separator)
        self.menu_table.setSpan(4, 0, 1, 3)
        # 02-01
        self.lcd_contrast_menu_nb = QTableWidgetItem("02-01")
        self.lcd_contrast_parm_name = QTableWidgetItem("LCD CONTRAST")

        self.lcd_contrast_spin = QSpinBox()
        self.lcd_contrast_spin.setAlignment(Qt.AlignCenter)
        self.lcd_contrast_spin.setMaximum(15)
        self.lcd_contrast_spin.setMinimum(1)
        self.lcd_contrast_spin.setValue(8)
        self.lcd_contrast_spin.valueChanged.connect(self.set_lcd_contrast)

        self.menu_table.setItem(5, 0, self.lcd_contrast_menu_nb)
        self.menu_table.setItem(5, 1, self.lcd_contrast_parm_name)
        self.menu_table.setCellWidget(5, 2, self.lcd_contrast_spin)

        # 02-02
        self.dimmer_backlit_menu_nb = QTableWidgetItem("02-02")
        self.dimmer_backlit_parm_name = QTableWidgetItem("DIMMER BACKLIT")

        self.dimmer_backlit_spin = QSpinBox()
        self.dimmer_backlit_spin.setAlignment(Qt.AlignCenter)
        self.dimmer_backlit_spin.setMaximum(15)
        self.dimmer_backlit_spin.setMinimum(1)
        self.dimmer_backlit_spin.setValue(8)
        self.dimmer_backlit_spin.valueChanged.connect(self.set_dimmer_backlit)

        self.menu_table.setItem(6, 0, self.dimmer_backlit_menu_nb)
        self.menu_table.setItem(6, 1, self.dimmer_backlit_parm_name)
        self.menu_table.setCellWidget(6, 2, self.dimmer_backlit_spin)

        # 02-03
        self.dimmer_lcd_menu_nb = QTableWidgetItem("02-03")
        self.dimmer_lcd_parm_name = QTableWidgetItem("DIMMER LCD")

        self.dimmer_lcd_spin = QSpinBox()
        self.dimmer_lcd_spin.setAlignment(Qt.AlignCenter)
        self.dimmer_lcd_spin.setMaximum(15)
        self.dimmer_lcd_spin.setMinimum(1)
        self.dimmer_lcd_spin.setValue(8)
        self.dimmer_lcd_spin.valueChanged.connect(self.set_dimmer_lcd)

        self.menu_table.setItem(7, 0, self.dimmer_lcd_menu_nb)
        self.menu_table.setItem(7, 1, self.dimmer_lcd_parm_name)
        self.menu_table.setCellWidget(7, 2, self.dimmer_lcd_spin)

        # 02-04
        self.dimmer_tx_busy_menu_nb = QTableWidgetItem("02-04")
        self.dimmer_tx_busy_parm_name = QTableWidgetItem("DIMMER TX/BUSY")

        self.dimmer_tx_busy_spin = QSpinBox()
        self.dimmer_tx_busy_spin.setAlignment(Qt.AlignCenter)
        self.dimmer_tx_busy_spin.setMaximum(15)
        self.dimmer_tx_busy_spin.setMinimum(1)
        self.dimmer_tx_busy_spin.setValue(8)
        self.dimmer_tx_busy_spin.valueChanged.connect(self.set_dimmer_tx_busy)

        self.menu_table.setItem(8, 0, self.dimmer_tx_busy_menu_nb)
        self.menu_table.setItem(8, 1, self.dimmer_tx_busy_parm_name)
        self.menu_table.setCellWidget(8, 2, self.dimmer_tx_busy_spin)

        # 02-05
        self.peak_hold_menu_nb = QTableWidgetItem("02-05")
        self.peak_hold_parm_name = QTableWidgetItem("PEAK HOLD")

        self.peak_hold_combo = QComboBox()
        self.peak_hold_combo.setEditable(True)
        self.peak_hold_combo.lineEdit().setReadOnly(True)
        self.peak_hold_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.peak_hold_combo.addItems([i for i in PEAK_HOLD.keys()])
        format_combo(self.peak_hold_combo)
        self.peak_hold_combo.setCurrentIndex(0)
        self.peak_hold_combo.currentTextChanged.connect(self.set_peak_hold)

        self.menu_table.setItem(9, 0, self.peak_hold_menu_nb)
        self.menu_table.setItem(9, 1, self.peak_hold_parm_name)
        self.menu_table.setCellWidget(9, 2, self.peak_hold_combo)

        # 02-06
        self.zin_led_menu_nb = QTableWidgetItem("02-06")
        self.zin_led_parm_name = QTableWidgetItem("ZIN LED")

        self.zin_led_combo = QComboBox()
        self.zin_led_combo.setEditable(True)
        self.zin_led_combo.lineEdit().setReadOnly(True)
        self.zin_led_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.zin_led_combo.addItems([i for i in ZIN_LED.keys()])
        format_combo(self.zin_led_combo)
        self.zin_led_combo.setCurrentIndex(0)
        self.zin_led_combo.currentTextChanged.connect(self.set_zin_led)

        self.menu_table.setItem(10, 0, self.zin_led_menu_nb)
        self.menu_table.setItem(10, 1, self.zin_led_parm_name)
        self.menu_table.setCellWidget(10, 2, self.zin_led_combo)

        # 02-07
        self.pop_up_menu_nb = QTableWidgetItem("02-07")
        self.pop_up_parm_name = QTableWidgetItem("POP-UP MENU")

        self.pop_up_combo = QComboBox()
        self.pop_up_combo.setEditable(True)
        self.pop_up_combo.lineEdit().setReadOnly(True)
        self.pop_up_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.pop_up_combo.addItems([i for i in POPUP_MENU.keys()])
        format_combo(self.pop_up_combo)
        self.pop_up_combo.setCurrentIndex(1)
        self.pop_up_combo.currentTextChanged.connect(self.set_pop_up_menu)

        self.menu_table.setItem(11, 0, self.pop_up_menu_nb)
        self.menu_table.setItem(11, 1, self.pop_up_parm_name)
        self.menu_table.setCellWidget(11, 2, self.pop_up_combo)

        # ### DVS
        self.dvs_separator = QTableWidgetItem("DVS")
        self.dvs_separator.setBackground(QColor(Qt.GlobalColor.lightGray))
        self.menu_table.setItem(12, 0, self.dvs_separator)
        self.menu_table.setSpan(12, 0, 1, 3)
        # 03-01
        self.dvs_rx_out_lvl_menu_nb = QTableWidgetItem("03-01")
        self.dvs_rx_out_lvl_parm_name = QTableWidgetItem("DVS RX OUT LVL")

        self.dvs_rx_out_lvl_spin = QSpinBox()
        self.dvs_rx_out_lvl_spin.setAlignment(Qt.AlignCenter)
        self.dvs_rx_out_lvl_spin.setMaximum(100)
        self.dvs_rx_out_lvl_spin.setMinimum(0)
        self.dvs_rx_out_lvl_spin.setValue(50)
        self.dvs_rx_out_lvl_spin.valueChanged.connect(self.set_dvs_rx_out_lvl)

        self.menu_table.setItem(13, 0, self.dvs_rx_out_lvl_menu_nb)
        self.menu_table.setItem(13, 1, self.dvs_rx_out_lvl_parm_name)
        self.menu_table.setCellWidget(13, 2, self.dvs_rx_out_lvl_spin)

        # 03-02
        self.dvs_tx_out_lvl_menu_nb = QTableWidgetItem("03-02")
        self.dvs_tx_out_lvl_parm_name = QTableWidgetItem("DVS TX OUT LVL")

        self.dvs_tx_out_lvl_spin = QSpinBox()
        self.dvs_tx_out_lvl_spin.setAlignment(Qt.AlignCenter)
        self.dvs_tx_out_lvl_spin.setMaximum(100)
        self.dvs_tx_out_lvl_spin.setMinimum(0)
        self.dvs_tx_out_lvl_spin.setValue(50)
        self.dvs_tx_out_lvl_spin.valueChanged.connect(self.set_dvs_tx_out_lvl)

        self.menu_table.setItem(14, 0, self.dvs_tx_out_lvl_menu_nb)
        self.menu_table.setItem(14, 1, self.dvs_tx_out_lvl_parm_name)
        self.menu_table.setCellWidget(14, 2, self.dvs_tx_out_lvl_spin)

        # ### Keyer
        self.keyer_separator = QTableWidgetItem("KEYER")
        self.keyer_separator.setBackground(QColor(Qt.GlobalColor.lightGray))
        self.menu_table.setItem(15, 0, self.keyer_separator)
        self.menu_table.setSpan(15, 0, 1, 3)
        # 04-01
        self.keyer_type_menu_nb = QTableWidgetItem("04-01")
        self.keyer_type_parm_name = QTableWidgetItem("KEYER TYPE")

        self.keyer_type_combo = QComboBox()
        self.keyer_type_combo.setEditable(True)
        self.keyer_type_combo.lineEdit().setReadOnly(True)
        self.keyer_type_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.keyer_type_combo.addItems([i for i in KEYER_TYPE.keys()])
        format_combo(self.keyer_type_combo)
        self.keyer_type_combo.setCurrentIndex(3)
        self.keyer_type_combo.currentTextChanged.connect(self.set_keyer_type)

        self.menu_table.setItem(16, 0, self.keyer_type_menu_nb)
        self.menu_table.setItem(16, 1, self.keyer_type_parm_name)
        self.menu_table.setCellWidget(16, 2, self.keyer_type_combo)

        # 04-02
        self.keyer_dot_dash_menu_nb = QTableWidgetItem("04-02")
        self.keyer_dot_dash_parm_name = QTableWidgetItem("KEYER DOT/DASH")

        self.keyer_dot_dash_combo = QComboBox()
        self.keyer_dot_dash_combo.setEditable(True)
        self.keyer_dot_dash_combo.lineEdit().setReadOnly(True)
        self.keyer_dot_dash_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.keyer_dot_dash_combo.addItems([i for i in KEYER_DOT_DASH.keys()])
        format_combo(self.keyer_dot_dash_combo)
        self.keyer_dot_dash_combo.setCurrentIndex(0)
        self.keyer_dot_dash_combo.currentTextChanged.connect(self.set_keyer_dot_dash)

        self.menu_table.setItem(17, 0, self.keyer_dot_dash_menu_nb)
        self.menu_table.setItem(17, 1, self.keyer_dot_dash_parm_name)
        self.menu_table.setCellWidget(17, 2, self.keyer_dot_dash_combo)

        # 04-03
        self.cw_weight_menu_nb = QTableWidgetItem("04-03")
        self.cw_weight_parm_name = QTableWidgetItem("CW WEIGHT")

        self.cw_weight_spin = QDoubleSpinBox()
        self.cw_weight_spin.setSingleStep(0.1)
        self.cw_weight_spin.setDecimals(1)
        self.cw_weight_spin.setAlignment(Qt.AlignCenter)
        self.cw_weight_spin.setMaximum(4.5)
        self.cw_weight_spin.setMinimum(2.5)
        self.cw_weight_spin.setValue(3.0)
        self.cw_weight_spin.valueChanged.connect(self.set_cw_weight)

        self.menu_table.setItem(18, 0, self.cw_weight_menu_nb)
        self.menu_table.setItem(18, 1, self.cw_weight_parm_name)
        self.menu_table.setCellWidget(18, 2, self.cw_weight_spin)

        # 04-04
        self.beacon_interval_menu_nb = QTableWidgetItem("04-04")
        self.beacon_interval_parm_name = QTableWidgetItem("BEACON INTERVAL")

        self.beacon_interval_spin = QSpinBox()
        self.beacon_interval_spin.setAlignment(Qt.AlignCenter)
        self.beacon_interval_spin.setMaximum(690)
        self.beacon_interval_spin.setMinimum(0)
        self.beacon_interval_spin.setSingleStep(1)
        self.beacon_interval_spin.setSpecialValueText("OFF")
        self.beacon_interval_spin.setSuffix(" sec")
        self.beacon_interval_spin.valueChanged.connect(self.set_beacon_interval)

        self.menu_table.setItem(19, 0, self.beacon_interval_menu_nb)
        self.menu_table.setItem(19, 1, self.beacon_interval_parm_name)
        self.menu_table.setCellWidget(19, 2, self.beacon_interval_spin)

        # 04-05
        self.number_style_menu_nb = QTableWidgetItem("04-05")
        self.number_style_parm_name = QTableWidgetItem("NUMBER STYLE")

        self.number_style_combo = QComboBox()
        self.number_style_combo.setEditable(True)
        self.number_style_combo.lineEdit().setReadOnly(True)
        self.number_style_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.number_style_combo.addItems([i for i in NUMBER_STYLE.keys()])
        format_combo(self.number_style_combo)
        self.number_style_combo.setCurrentIndex(0)
        self.number_style_combo.currentTextChanged.connect(self.set_number_style)

        self.menu_table.setItem(20, 0, self.number_style_menu_nb)
        self.menu_table.setItem(20, 1, self.number_style_parm_name)
        self.menu_table.setCellWidget(20, 2, self.number_style_combo)

        # 04-06
        self.contest_number_menu_nb = QTableWidgetItem("04-06")
        self.contest_number_parm_name = QTableWidgetItem("CONTEST NUMBER")

        self.contest_number_spin = QSpinBox()
        self.contest_number_spin.setAlignment(Qt.AlignCenter)
        self.contest_number_spin.setMaximum(9999)
        self.contest_number_spin.setMinimum(0)
        self.contest_number_spin.setSingleStep(1)
        self.contest_number_spin.setValue(1)
        self.contest_number_spin.valueChanged.connect(self.set_contest_number)

        self.menu_table.setItem(21, 0, self.contest_number_menu_nb)
        self.menu_table.setItem(21, 1, self.contest_number_parm_name)
        self.menu_table.setCellWidget(21, 2, self.contest_number_spin)

        # 04-07
        self.cw_memory_1_menu_nb = QTableWidgetItem("04-07")
        self.cw_memory_1_parm_name = QTableWidgetItem("CW MEMORY 1")

        self.cw_memory_1_combo = QComboBox()
        self.cw_memory_1_combo.setEditable(True)
        self.cw_memory_1_combo.lineEdit().setReadOnly(True)
        self.cw_memory_1_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.cw_memory_1_combo.addItems([i for i in CW_MEMORY.keys()])
        format_combo(self.cw_memory_1_combo)
        self.cw_memory_1_combo.setCurrentIndex(0)
        self.cw_memory_1_combo.currentTextChanged.connect(self.set_cw_memory_1)

        self.menu_table.setItem(22, 0, self.cw_memory_1_menu_nb)
        self.menu_table.setItem(22, 1, self.cw_memory_1_parm_name)
        self.menu_table.setCellWidget(22, 2, self.cw_memory_1_combo)

        # 04-08
        self.cw_memory_2_menu_nb = QTableWidgetItem("04-08")
        self.cw_memory_2_parm_name = QTableWidgetItem("CW MEMORY 2")

        self.cw_memory_2_combo = QComboBox()
        self.cw_memory_2_combo.setEditable(True)
        self.cw_memory_2_combo.lineEdit().setReadOnly(True)
        self.cw_memory_2_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.cw_memory_2_combo.addItems([i for i in CW_MEMORY.keys()])
        format_combo(self.cw_memory_2_combo)
        self.cw_memory_2_combo.setCurrentIndex(0)
        self.cw_memory_2_combo.currentTextChanged.connect(self.set_cw_memory_2)

        self.menu_table.setItem(23, 0, self.cw_memory_2_menu_nb)
        self.menu_table.setItem(23, 1, self.cw_memory_2_parm_name)
        self.menu_table.setCellWidget(23, 2, self.cw_memory_2_combo)

        # 04-09
        self.cw_memory_3_menu_nb = QTableWidgetItem("04-09")
        self.cw_memory_3_parm_name = QTableWidgetItem("CW MEMORY 3")

        self.cw_memory_3_combo = QComboBox()
        self.cw_memory_3_combo.setEditable(True)
        self.cw_memory_3_combo.lineEdit().setReadOnly(True)
        self.cw_memory_3_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.cw_memory_3_combo.addItems([i for i in CW_MEMORY.keys()])
        format_combo(self.cw_memory_3_combo)
        self.cw_memory_3_combo.setCurrentIndex(0)
        self.cw_memory_3_combo.currentTextChanged.connect(self.set_cw_memory_3)

        self.menu_table.setItem(24, 0, self.cw_memory_3_menu_nb)
        self.menu_table.setItem(24, 1, self.cw_memory_3_parm_name)
        self.menu_table.setCellWidget(24, 2, self.cw_memory_3_combo)

        # 04-10
        self.cw_memory_4_menu_nb = QTableWidgetItem("04-10")
        self.cw_memory_4_parm_name = QTableWidgetItem("CW MEMORY 4")

        self.cw_memory_4_combo = QComboBox()
        self.cw_memory_4_combo.setEditable(True)
        self.cw_memory_4_combo.lineEdit().setReadOnly(True)
        self.cw_memory_4_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.cw_memory_4_combo.addItems([i for i in CW_MEMORY.keys()])
        format_combo(self.cw_memory_4_combo)
        self.cw_memory_4_combo.setCurrentIndex(0)
        self.cw_memory_4_combo.currentTextChanged.connect(self.set_cw_memory_4)

        self.menu_table.setItem(25, 0, self.cw_memory_4_menu_nb)
        self.menu_table.setItem(25, 1, self.cw_memory_4_parm_name)
        self.menu_table.setCellWidget(25, 2, self.cw_memory_4_combo)

        # 04-11
        self.cw_memory_5_menu_nb = QTableWidgetItem("04-11")
        self.cw_memory_5_parm_name = QTableWidgetItem("CW MEMORY 5")

        self.cw_memory_5_combo = QComboBox()
        self.cw_memory_5_combo.setEditable(True)
        self.cw_memory_5_combo.lineEdit().setReadOnly(True)
        self.cw_memory_5_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.cw_memory_5_combo.addItems([i for i in CW_MEMORY.keys()])
        format_combo(self.cw_memory_5_combo)
        self.cw_memory_5_combo.setCurrentIndex(0)
        self.cw_memory_5_combo.currentTextChanged.connect(self.set_cw_memory_5)

        self.menu_table.setItem(26, 0, self.cw_memory_5_menu_nb)
        self.menu_table.setItem(26, 1, self.cw_memory_5_parm_name)
        self.menu_table.setCellWidget(26, 2, self.cw_memory_5_combo)

        # ### General
        self.general_separator = QTableWidgetItem("GENERAL")
        self.general_separator.setBackground(QColor(Qt.GlobalColor.lightGray))
        self.menu_table.setItem(27, 0, self.general_separator)
        self.menu_table.setSpan(27, 0, 1, 3)
        # 05-01
        self.nb_width_menu_nb = QTableWidgetItem("05-01")
        self.nb_width_parm_name = QTableWidgetItem("NB WIDTH")

        self.nb_width_combo = QComboBox()
        self.nb_width_combo.setEditable(True)
        self.nb_width_combo.lineEdit().setReadOnly(True)
        self.nb_width_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.nb_width_combo.addItems([i for i in NB_WIDHT.keys()])
        format_combo(self.nb_width_combo)
        self.nb_width_combo.setCurrentIndex(1)
        self.nb_width_combo.currentTextChanged.connect(self.set_nb_width)

        self.menu_table.setItem(28, 0, self.nb_width_menu_nb)
        self.menu_table.setItem(28, 1, self.nb_width_parm_name)
        self.menu_table.setCellWidget(28, 2, self.nb_width_combo)

        # 05-02
        self.nb_rejection_menu_nb = QTableWidgetItem("05-02")
        self.nb_rejection_parm_name = QTableWidgetItem("NB REJECTION")

        self.nb_rejection_combo = QComboBox()
        self.nb_rejection_combo.setEditable(True)
        self.nb_rejection_combo.lineEdit().setReadOnly(True)
        self.nb_rejection_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.nb_rejection_combo.addItems([i for i in NB_REJECTION.keys()])
        format_combo(self.nb_rejection_combo)
        self.nb_rejection_combo.setCurrentIndex(1)
        self.nb_rejection_combo.currentTextChanged.connect(self.set_nb_rejection)

        self.menu_table.setItem(29, 0, self.nb_rejection_menu_nb)
        self.menu_table.setItem(29, 1, self.nb_rejection_parm_name)
        self.menu_table.setCellWidget(29, 2, self.nb_rejection_combo)

        # 05-03
        self.nb_level_menu_nb = QTableWidgetItem("05-03")
        self.nb_level_parm_name = QTableWidgetItem("NB LEVEL")

        self.nb_level_spin = QSpinBox()
        self.nb_level_spin.setAlignment(Qt.AlignCenter)
        self.nb_level_spin.setMaximum(10)
        self.nb_level_spin.setMinimum(0)
        self.nb_level_spin.setSingleStep(1)
        self.nb_level_spin.setValue(5)
        self.nb_level_spin.valueChanged.connect(self.set_nb_level)

        self.menu_table.setItem(30, 0, self.nb_level_menu_nb)
        self.menu_table.setItem(30, 1, self.nb_level_parm_name)
        self.menu_table.setCellWidget(30, 2, self.nb_level_spin)

        # 05-04
        self.beep_level_menu_nb = QTableWidgetItem("05-04")
        self.beep_level_parm_name = QTableWidgetItem("BEEP LEVEL")

        self.beep_level_spin = QSpinBox()
        self.beep_level_spin.setAlignment(Qt.AlignCenter)
        self.beep_level_spin.setMaximum(100)
        self.beep_level_spin.setMinimum(0)
        self.beep_level_spin.setSingleStep(1)
        self.beep_level_spin.setValue(30)
        self.beep_level_spin.valueChanged.connect(self.set_beep_level)

        self.menu_table.setItem(31, 0, self.beep_level_menu_nb)
        self.menu_table.setItem(31, 1, self.beep_level_parm_name)
        self.menu_table.setCellWidget(31, 2, self.beep_level_spin)

        # 05-05
        self.rf_sql_vr_menu_nb = QTableWidgetItem("05-05")
        self.rf_sql_vr_parm_name = QTableWidgetItem("RF/SQL VR")

        self.rf_sql_vr_combo = QComboBox()
        self.rf_sql_vr_combo.setEditable(True)
        self.rf_sql_vr_combo.lineEdit().setReadOnly(True)
        self.rf_sql_vr_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.rf_sql_vr_combo.addItems([i for i in RF_SQL_VR.keys()])
        format_combo(self.rf_sql_vr_combo)
        self.rf_sql_vr_combo.setCurrentIndex(0)
        self.rf_sql_vr_combo.currentTextChanged.connect(self.set_rf_sql_vr)

        self.menu_table.setItem(32, 0, self.rf_sql_vr_menu_nb)
        self.menu_table.setItem(32, 1, self.rf_sql_vr_parm_name)
        self.menu_table.setCellWidget(32, 2, self.rf_sql_vr_combo)

        # 05-06
        self.cat_rate_menu_nb = QTableWidgetItem("05-06")
        self.cat_rate_parm_name = QTableWidgetItem("CAT RATE")

        self.cat_rate_combo = QComboBox()
        self.cat_rate_combo.setEditable(True)
        self.cat_rate_combo.lineEdit().setReadOnly(True)
        self.cat_rate_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.cat_rate_combo.addItems([i for i in CAT_RATE.keys()])
        format_combo(self.cat_rate_combo)
        self.cat_rate_combo.setCurrentIndex(0)
        self.cat_rate_combo.currentTextChanged.connect(self.set_cat_rate)

        self.menu_table.setItem(33, 0, self.cat_rate_menu_nb)
        self.menu_table.setItem(33, 1, self.cat_rate_parm_name)
        self.menu_table.setCellWidget(33, 2, self.cat_rate_combo)

        # 05-07
        self.cat_tot_menu_nb = QTableWidgetItem("05-07")
        self.cat_tot_parm_name = QTableWidgetItem("CAT TOT")

        self.cat_tot_combo = QComboBox()
        self.cat_tot_combo.setEditable(True)
        self.cat_tot_combo.lineEdit().setReadOnly(True)
        self.cat_tot_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.cat_tot_combo.addItems([i for i in CAT_TOT.keys()])
        format_combo(self.cat_tot_combo)
        self.cat_tot_combo.setCurrentIndex(0)
        self.cat_tot_combo.currentTextChanged.connect(self.set_cat_tot)

        self.menu_table.setItem(34, 0, self.cat_tot_menu_nb)
        self.menu_table.setItem(34, 1, self.cat_tot_parm_name)
        self.menu_table.setCellWidget(34, 2, self.cat_tot_combo)

        # 05-08
        self.cat_rts_menu_nb = QTableWidgetItem("05-08")
        self.cat_rts_parm_name = QTableWidgetItem("CAT RTS")

        self.cat_rts_combo = QComboBox()
        self.cat_rts_combo.setEditable(True)
        self.cat_rts_combo.lineEdit().setReadOnly(True)
        self.cat_rts_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.cat_rts_combo.addItems([i for i in CAT_RTS.keys()])
        format_combo(self.cat_rts_combo)
        self.cat_rts_combo.setCurrentIndex(1)
        self.cat_rts_combo.currentTextChanged.connect(self.set_cat_rts)

        self.menu_table.setItem(35, 0, self.cat_rts_menu_nb)
        self.menu_table.setItem(35, 1, self.cat_rts_parm_name)
        self.menu_table.setCellWidget(35, 2, self.cat_rts_combo)

        # 05-09
        self.meme_group_menu_nb = QTableWidgetItem("05-09")
        self.meme_group_parm_name = QTableWidgetItem("MEMORY GROUP")

        self.meme_group_combo = QComboBox()
        self.meme_group_combo.setEditable(True)
        self.meme_group_combo.lineEdit().setReadOnly(True)
        self.meme_group_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.meme_group_combo.addItems([i for i in MEMORY_GROUP.keys()])
        format_combo(self.meme_group_combo)
        self.meme_group_combo.setCurrentIndex(0)
        self.meme_group_combo.currentTextChanged.connect(self.set_mem_group)

        self.menu_table.setItem(36, 0, self.meme_group_menu_nb)
        self.menu_table.setItem(36, 1, self.meme_group_parm_name)
        self.menu_table.setCellWidget(36, 2, self.meme_group_combo)

        # 05-10
        self.fm_setting_menu_nb = QTableWidgetItem("05-10")
        self.fm_setting_parm_name = QTableWidgetItem("FM SETTING")

        self.fm_setting_combo = QComboBox()
        self.fm_setting_combo.setEditable(True)
        self.fm_setting_combo.lineEdit().setReadOnly(True)
        self.fm_setting_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.fm_setting_combo.addItems([i for i in FM_SETTING.keys()])
        format_combo(self.fm_setting_combo)
        self.fm_setting_combo.setCurrentIndex(0)
        self.fm_setting_combo.currentTextChanged.connect(self.set_fm_setting)

        self.menu_table.setItem(37, 0, self.fm_setting_menu_nb)
        self.menu_table.setItem(37, 1, self.fm_setting_parm_name)
        self.menu_table.setCellWidget(37, 2, self.fm_setting_combo)

        # 05-11
        self.rec_setting_menu_nb = QTableWidgetItem("05-11")
        self.rec_setting_parm_name = QTableWidgetItem("REC SETTING")

        self.rec_setting_combo = QComboBox()
        self.rec_setting_combo.setEditable(True)
        self.rec_setting_combo.lineEdit().setReadOnly(True)
        self.rec_setting_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.rec_setting_combo.addItems([i for i in REC_SETTING.keys()])
        format_combo(self.rec_setting_combo)
        self.rec_setting_combo.setCurrentIndex(0)
        self.rec_setting_combo.currentTextChanged.connect(self.set_rec_setting)

        self.menu_table.setItem(38, 0, self.rec_setting_menu_nb)
        self.menu_table.setItem(38, 1, self.rec_setting_parm_name)
        self.menu_table.setCellWidget(38, 2, self.rec_setting_combo)

        # 05-12
        self.atas_setting_menu_nb = QTableWidgetItem("05-12")
        self.atas_setting_parm_name = QTableWidgetItem("ATAS SETTING")

        self.atas_setting_combo = QComboBox()
        self.atas_setting_combo.setEditable(True)
        self.atas_setting_combo.lineEdit().setReadOnly(True)
        self.atas_setting_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.atas_setting_combo.addItems([i for i in ATAS_SETTING.keys()])
        format_combo(self.atas_setting_combo)
        self.atas_setting_combo.setCurrentIndex(0)
        self.atas_setting_combo.currentTextChanged.connect(self.set_atas_setting)

        self.menu_table.setItem(39, 0, self.atas_setting_menu_nb)
        self.menu_table.setItem(39, 1, self.atas_setting_parm_name)
        self.menu_table.setCellWidget(39, 2, self.atas_setting_combo)

        # 05-13
        self.quick_spl_freq_menu_nb = QTableWidgetItem("05-13")
        self.quick_spl_freq_parm_name = QTableWidgetItem("QUICK SPL FREQ")

        self.quick_spl_freq_spin = QSpinBox()
        self.quick_spl_freq_spin.setAlignment(Qt.AlignCenter)
        self.quick_spl_freq_spin.setMaximum(20)
        self.quick_spl_freq_spin.setMinimum(-20)
        self.quick_spl_freq_spin.setSingleStep(1)
        self.quick_spl_freq_spin.setValue(5)
        self.quick_spl_freq_spin.setSuffix(" kHz")
        self.quick_spl_freq_spin.valueChanged.connect(self.set_quick_spl_freq)

        self.menu_table.setItem(40, 0, self.quick_spl_freq_menu_nb)
        self.menu_table.setItem(40, 1, self.quick_spl_freq_parm_name)
        self.menu_table.setCellWidget(40, 2, self.quick_spl_freq_spin)

        # 05-14
        self.tx_tot_menu_nb = QTableWidgetItem("05-14")
        self.tx_tot_parm_name = QTableWidgetItem("TX TOT")

        self.tx_tot_spin = QSpinBox()
        self.tx_tot_spin.setAlignment(Qt.AlignCenter)
        self.tx_tot_spin.setMaximum(30)
        self.tx_tot_spin.setMinimum(0)
        self.tx_tot_spin.setSingleStep(1)
        self.tx_tot_spin.setValue(10)
        self.tx_tot_spin.setSuffix(" min")
        self.tx_tot_spin.setSpecialValueText("OFF")
        self.tx_tot_spin.valueChanged.connect(self.set_tx_tot)

        self.menu_table.setItem(41, 0, self.tx_tot_menu_nb)
        self.menu_table.setItem(41, 1, self.tx_tot_parm_name)
        self.menu_table.setCellWidget(41, 2, self.tx_tot_spin)

        # 05-15
        self.mic_scan_menu_nb = QTableWidgetItem("05-15")
        self.mic_scan_parm_name = QTableWidgetItem("MIC SCAN")

        self.mic_scan_combo = QComboBox()
        self.mic_scan_combo.setEditable(True)
        self.mic_scan_combo.lineEdit().setReadOnly(True)
        self.mic_scan_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.mic_scan_combo.addItems([i for i in MIC_SCAN.keys()])
        format_combo(self.mic_scan_combo)
        self.mic_scan_combo.setCurrentIndex(1)
        self.mic_scan_combo.currentTextChanged.connect(self.set_mic_scan)

        self.menu_table.setItem(42, 0, self.mic_scan_menu_nb)
        self.menu_table.setItem(42, 1, self.mic_scan_parm_name)
        self.menu_table.setCellWidget(42, 2, self.mic_scan_combo)

        # 05-16
        self.mic_scan_resume_menu_nb = QTableWidgetItem("05-16")
        self.mic_scan_resume_parm_name = QTableWidgetItem("MIC SCAN RESUME")

        self.mic_scan_resume_combo = QComboBox()
        self.mic_scan_resume_combo.setEditable(True)
        self.mic_scan_resume_combo.lineEdit().setReadOnly(True)
        self.mic_scan_resume_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.mic_scan_resume_combo.addItems([i for i in MIC_SCAN_RESUME.keys()])
        format_combo(self.mic_scan_resume_combo)
        self.mic_scan_resume_combo.setCurrentIndex(1)
        self.mic_scan_resume_combo.currentTextChanged.connect(self.set_mic_scan_resume)

        self.menu_table.setItem(43, 0, self.mic_scan_resume_menu_nb)
        self.menu_table.setItem(43, 1, self.mic_scan_resume_parm_name)
        self.menu_table.setCellWidget(43, 2, self.mic_scan_resume_combo)

        # 05-17
        self.ref_freq_adj_menu_nb = QTableWidgetItem("05-17")
        self.ref_freq_adj_parm_name = QTableWidgetItem("REF FREQ ADJ")

        self.ref_freq_adj_spin = QSpinBox()
        self.ref_freq_adj_spin.setAlignment(Qt.AlignCenter)
        self.ref_freq_adj_spin.setMaximum(25)
        self.ref_freq_adj_spin.setMinimum(-25)
        self.ref_freq_adj_spin.setSingleStep(1)
        self.ref_freq_adj_spin.setValue(0)
        self.ref_freq_adj_spin.valueChanged.connect(self.set_ref_freq_adj)

        self.menu_table.setItem(44, 0, self.ref_freq_adj_menu_nb)
        self.menu_table.setItem(44, 1, self.ref_freq_adj_parm_name)
        self.menu_table.setCellWidget(44, 2, self.ref_freq_adj_spin)

        # 05-18
        self.clar_select_menu_nb = QTableWidgetItem("05-18")
        self.clar_select_parm_name = QTableWidgetItem("CLAR SELECT")

        self.clar_select_combo = QComboBox()
        self.clar_select_combo.setEditable(True)
        self.clar_select_combo.lineEdit().setReadOnly(True)
        self.clar_select_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.clar_select_combo.addItems([i for i in CLAR_SELECT.keys()])
        format_combo(self.clar_select_combo)
        self.clar_select_combo.setCurrentIndex(0)
        self.clar_select_combo.currentTextChanged.connect(self.set_clar_select)

        self.menu_table.setItem(45, 0, self.clar_select_menu_nb)
        self.menu_table.setItem(45, 1, self.clar_select_parm_name)
        self.menu_table.setCellWidget(45, 2, self.clar_select_combo)

        # 05-19
        self.apo_menu_nb = QTableWidgetItem("05-19")
        self.apo_parm_name = QTableWidgetItem("APO")

        self.apo_combo = QComboBox()
        self.apo_combo.setEditable(True)
        self.apo_combo.lineEdit().setReadOnly(True)
        self.apo_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.apo_combo.addItems([i for i in APO.keys()])
        format_combo(self.apo_combo)
        self.apo_combo.setCurrentIndex(0)
        self.apo_combo.currentTextChanged.connect(self.set_apo)

        self.menu_table.setItem(46, 0, self.apo_menu_nb)
        self.menu_table.setItem(46, 1, self.apo_parm_name)
        self.menu_table.setCellWidget(46, 2, self.apo_combo)

        # 05-20
        self.fan_control_menu_nb = QTableWidgetItem("05-20")
        self.fan_control_parm_name = QTableWidgetItem("FAN CONTROL")

        self.fan_control_combo = QComboBox()
        self.fan_control_combo.setEditable(True)
        self.fan_control_combo.lineEdit().setReadOnly(True)
        self.fan_control_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.fan_control_combo.addItems([i for i in FAN_CONTROL.keys()])
        format_combo(self.fan_control_combo)
        self.fan_control_combo.setCurrentIndex(0)
        self.fan_control_combo.currentTextChanged.connect(self.set_fan_control)

        self.menu_table.setItem(47, 0, self.fan_control_menu_nb)
        self.menu_table.setItem(47, 1, self.fan_control_parm_name)
        self.menu_table.setCellWidget(47, 2, self.fan_control_combo)

        # AM
        self.mode_am_separator = QTableWidgetItem("MODE AM")
        self.mode_am_separator.setBackground(QColor(Qt.GlobalColor.lightGray))
        self.menu_table.setItem(48, 0, self.mode_am_separator)
        self.menu_table.setSpan(48, 0, 1, 3)
        # 06-01
        self.am_lcut_freq_menu_nb = QTableWidgetItem("06-01")
        self.am_lcut_freq_parm_name = QTableWidgetItem("AM LCUT FREQ")

        self.am_lcut_freq_combo = QComboBox()
        self.am_lcut_freq_combo.setEditable(True)
        self.am_lcut_freq_combo.lineEdit().setReadOnly(True)
        self.am_lcut_freq_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.am_lcut_freq_combo.addItems([i for i in LCUT_FREQ.keys()])
        format_combo(self.am_lcut_freq_combo)
        self.am_lcut_freq_combo.setCurrentIndex(0)
        self.am_lcut_freq_combo.currentTextChanged.connect(self.set_am_lcut_freq)

        self.menu_table.setItem(49, 0, self.am_lcut_freq_menu_nb)
        self.menu_table.setItem(49, 1, self.am_lcut_freq_parm_name)
        self.menu_table.setCellWidget(49, 2, self.am_lcut_freq_combo)

        # 06-02
        self.am_lcut_slope_menu_nb = QTableWidgetItem("06-02")
        self.am_lcut_slope_parm_name = QTableWidgetItem("AM LCUT SLOPE")

        self.am_lcut_slope_combo = QComboBox()
        self.am_lcut_slope_combo.setEditable(True)
        self.am_lcut_slope_combo.lineEdit().setReadOnly(True)
        self.am_lcut_slope_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.am_lcut_slope_combo.addItems([i for i in SLOPE.keys()])
        format_combo(self.am_lcut_slope_combo)
        self.am_lcut_slope_combo.setCurrentIndex(0)
        self.am_lcut_slope_combo.currentTextChanged.connect(self.set_am_lcut_slope)

        self.menu_table.setItem(50, 0, self.am_lcut_slope_menu_nb)
        self.menu_table.setItem(50, 1, self.am_lcut_slope_parm_name)
        self.menu_table.setCellWidget(50, 2, self.am_lcut_slope_combo)

        # 06-03
        self.am_hcut_freq_menu_nb = QTableWidgetItem("06-03")
        self.am_hcut_freq_parm_name = QTableWidgetItem("AM HCUT FREQ")

        self.am_hcut_freq_combo = QComboBox()
        self.am_hcut_freq_combo.setEditable(True)
        self.am_hcut_freq_combo.lineEdit().setReadOnly(True)
        self.am_hcut_freq_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.am_hcut_freq_combo.addItems([i for i in HCUT_FREQ.keys()])
        format_combo(self.am_hcut_freq_combo)
        self.am_hcut_freq_combo.setCurrentIndex(0)
        self.am_hcut_freq_combo.currentTextChanged.connect(self.set_am_hcut_freq)

        self.menu_table.setItem(51, 0, self.am_hcut_freq_menu_nb)
        self.menu_table.setItem(51, 1, self.am_hcut_freq_parm_name)
        self.menu_table.setCellWidget(51, 2, self.am_hcut_freq_combo)

        # 06-04
        self.am_hcut_slope_menu_nb = QTableWidgetItem("06-04")
        self.am_hcut_slope_parm_name = QTableWidgetItem("AM HCUT SLOPE")

        self.am_hcut_slope_combo = QComboBox()
        self.am_hcut_slope_combo.setEditable(True)
        self.am_hcut_slope_combo.lineEdit().setReadOnly(True)
        self.am_hcut_slope_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.am_hcut_slope_combo.addItems([i for i in SLOPE.keys()])
        format_combo(self.am_hcut_slope_combo)
        self.am_hcut_slope_combo.setCurrentIndex(0)
        self.am_hcut_slope_combo.currentTextChanged.connect(self.set_am_hcut_slope)

        self.menu_table.setItem(52, 0, self.am_hcut_slope_menu_nb)
        self.menu_table.setItem(52, 1, self.am_hcut_slope_parm_name)
        self.menu_table.setCellWidget(52, 2, self.am_hcut_slope_combo)

        # 06-05
        self.am_mic_select_menu_nb = QTableWidgetItem("06-05")
        self.am_mic_select_parm_name = QTableWidgetItem("AM MIC SELECT")

        self.am_mic_select_combo = QComboBox()
        self.am_mic_select_combo.setEditable(True)
        self.am_mic_select_combo.lineEdit().setReadOnly(True)
        self.am_mic_select_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.am_mic_select_combo.addItems([i for i in AM_MIC_SELECT.keys()])
        format_combo(self.am_mic_select_combo)
        self.am_mic_select_combo.setCurrentIndex(0)
        self.am_mic_select_combo.currentTextChanged.connect(self.set_am_mic_select)

        self.menu_table.setItem(53, 0, self.am_mic_select_menu_nb)
        self.menu_table.setItem(53, 1, self.am_mic_select_parm_name)
        self.menu_table.setCellWidget(53, 2, self.am_mic_select_combo)

        # 06-06
        self.am_out_level_menu_nb = QTableWidgetItem("06-06")
        self.am_out_level_parm_name = QTableWidgetItem("AM OUT LEVEL")

        self.am_out_level_spin = QSpinBox()
        self.am_out_level_spin.setAlignment(Qt.AlignCenter)
        self.am_out_level_spin.setMaximum(100)
        self.am_out_level_spin.setMinimum(0)
        self.am_out_level_spin.setSingleStep(1)
        self.am_out_level_spin.setValue(50)
        self.am_out_level_spin.valueChanged.connect(self.set_am_out_level)

        self.menu_table.setItem(54, 0, self.am_out_level_menu_nb)
        self.menu_table.setItem(54, 1, self.am_out_level_parm_name)
        self.menu_table.setCellWidget(54, 2, self.am_out_level_spin)

        # 06-07
        self.am_ptt_select_menu_nb = QTableWidgetItem("06-07")
        self.am_ptt_select_parm_name = QTableWidgetItem("AM PTT SELECT")

        self.am_ptt_select_combo = QComboBox()
        self.am_ptt_select_combo.setEditable(True)
        self.am_ptt_select_combo.lineEdit().setReadOnly(True)
        self.am_ptt_select_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.am_ptt_select_combo.addItems([i for i in AM_PTT_SELECT.keys()])
        format_combo(self.am_ptt_select_combo)
        self.am_ptt_select_combo.setCurrentIndex(0)
        self.am_ptt_select_combo.currentTextChanged.connect(self.set_am_ptt_select)

        self.menu_table.setItem(55, 0, self.am_ptt_select_menu_nb)
        self.menu_table.setItem(55, 1, self.am_ptt_select_parm_name)
        self.menu_table.setCellWidget(55, 2, self.am_ptt_select_combo)

        # CW
        self.mode_cw_separator = QTableWidgetItem("MODE CW")
        self.mode_cw_separator.setBackground(QColor(Qt.GlobalColor.lightGray))
        self.menu_table.setItem(56, 0, self.mode_cw_separator)
        self.menu_table.setSpan(56, 0, 1, 3)
        # 07-01
        self.cw_lcut_freq_menu_nb = QTableWidgetItem("07-01")
        self.cw_lcut_freq_parm_name = QTableWidgetItem("CW LCUT FREQ")

        self.cw_lcut_freq_combo = QComboBox()
        self.cw_lcut_freq_combo.setEditable(True)
        self.cw_lcut_freq_combo.lineEdit().setReadOnly(True)
        self.cw_lcut_freq_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.cw_lcut_freq_combo.addItems([i for i in LCUT_FREQ.keys()])
        format_combo(self.cw_lcut_freq_combo)
        self.cw_lcut_freq_combo.setCurrentIndex(4)
        self.cw_lcut_freq_combo.currentTextChanged.connect(self.set_cw_lcut_freq)

        self.menu_table.setItem(57, 0, self.cw_lcut_freq_menu_nb)
        self.menu_table.setItem(57, 1, self.cw_lcut_freq_parm_name)
        self.menu_table.setCellWidget(57, 2, self.cw_lcut_freq_combo)

        # 07-02
        self.cw_lcut_slope_menu_nb = QTableWidgetItem("07-02")
        self.cw_lcut_slope_parm_name = QTableWidgetItem("CW LCUT SLOPE")

        self.cw_lcut_slope_combo = QComboBox()
        self.cw_lcut_slope_combo.setEditable(True)
        self.cw_lcut_slope_combo.lineEdit().setReadOnly(True)
        self.cw_lcut_slope_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.cw_lcut_slope_combo.addItems([i for i in SLOPE.keys()])
        format_combo(self.cw_lcut_slope_combo)
        self.cw_lcut_slope_combo.setCurrentIndex(1)
        self.cw_lcut_slope_combo.currentTextChanged.connect(self.set_cw_lcut_slope)

        self.menu_table.setItem(58, 0, self.cw_lcut_slope_menu_nb)
        self.menu_table.setItem(58, 1, self.cw_lcut_slope_parm_name)
        self.menu_table.setCellWidget(58, 2, self.cw_lcut_slope_combo)

        # 07-03
        self.cw_hcut_freq_menu_nb = QTableWidgetItem("07-03")
        self.cw_hcut_freq_parm_name = QTableWidgetItem("CW HCUT FREQ")

        self.cw_hcut_freq_combo = QComboBox()
        self.cw_hcut_freq_combo.setEditable(True)
        self.cw_hcut_freq_combo.lineEdit().setReadOnly(True)
        self.cw_hcut_freq_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.cw_hcut_freq_combo.addItems([i for i in HCUT_FREQ.keys()])
        format_combo(self.cw_hcut_freq_combo)
        self.cw_hcut_freq_combo.setCurrentIndex(11)
        self.cw_hcut_freq_combo.currentTextChanged.connect(self.set_cw_hcut_freq)

        self.menu_table.setItem(59, 0, self.cw_hcut_freq_menu_nb)
        self.menu_table.setItem(59, 1, self.cw_hcut_freq_parm_name)
        self.menu_table.setCellWidget(59, 2, self.cw_hcut_freq_combo)

        # 07-04
        self.cw_hcut_slope_menu_nb = QTableWidgetItem("07-04")
        self.cw_hcut_slope_parm_name = QTableWidgetItem("CW HCUT SLOPE")

        self.cw_hcut_slope_combo = QComboBox()
        self.cw_hcut_slope_combo.setEditable(True)
        self.cw_hcut_slope_combo.lineEdit().setReadOnly(True)
        self.cw_hcut_slope_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.cw_hcut_slope_combo.addItems([i for i in SLOPE.keys()])
        format_combo(self.cw_hcut_slope_combo)
        self.cw_hcut_slope_combo.setCurrentIndex(1)
        self.cw_hcut_slope_combo.currentTextChanged.connect(self.set_cw_hcut_slope)

        self.menu_table.setItem(60, 0, self.cw_hcut_slope_menu_nb)
        self.menu_table.setItem(60, 1, self.cw_hcut_slope_parm_name)
        self.menu_table.setCellWidget(60, 2, self.cw_hcut_slope_combo)

        # 07-05
        self.cw_out_level_menu_nb = QTableWidgetItem("07-05")
        self.cw_out_level_parm_name = QTableWidgetItem("CW OUT LEVEL")

        self.cw_out_level_spin = QSpinBox()
        self.cw_out_level_spin.setAlignment(Qt.AlignCenter)
        self.cw_out_level_spin.setMaximum(100)
        self.cw_out_level_spin.setMinimum(0)
        self.cw_out_level_spin.setSingleStep(1)
        self.cw_out_level_spin.setValue(50)
        self.cw_out_level_spin.valueChanged.connect(self.set_cw_out_level)

        self.menu_table.setItem(61, 0, self.cw_out_level_menu_nb)
        self.menu_table.setItem(61, 1, self.cw_out_level_parm_name)
        self.menu_table.setCellWidget(61, 2, self.cw_out_level_spin)

        # 07-06
        self.cw_auto_mode_menu_nb = QTableWidgetItem("07-06")
        self.cw_auto_mode_parm_name = QTableWidgetItem("CW AUTO MODE")

        self.cw_auto_mode_combo = QComboBox()
        self.cw_auto_mode_combo.setEditable(True)
        self.cw_auto_mode_combo.lineEdit().setReadOnly(True)
        self.cw_auto_mode_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.cw_auto_mode_combo.addItems([i for i in CW_AUTO_MODE.keys()])
        format_combo(self.cw_auto_mode_combo)
        self.cw_auto_mode_combo.setCurrentIndex(0)
        self.cw_auto_mode_combo.currentTextChanged.connect(self.set_cw_auto_mode)

        self.menu_table.setItem(62, 0, self.cw_auto_mode_menu_nb)
        self.menu_table.setItem(62, 1, self.cw_auto_mode_parm_name)
        self.menu_table.setCellWidget(62, 2, self.cw_auto_mode_combo)

        # 07-07
        self.cw_bfo_menu_nb = QTableWidgetItem("07-07")
        self.cw_bfo_parm_name = QTableWidgetItem("CW BFO")

        self.cw_bfo_combo = QComboBox()
        self.cw_bfo_combo.setEditable(True)
        self.cw_bfo_combo.lineEdit().setReadOnly(True)
        self.cw_bfo_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.cw_bfo_combo.addItems([i for i in CW_BFO.keys()])
        format_combo(self.cw_bfo_combo)
        self.cw_bfo_combo.setCurrentIndex(0)
        self.cw_bfo_combo.currentTextChanged.connect(self.set_cw_bfo)

        self.menu_table.setItem(63, 0, self.cw_bfo_menu_nb)
        self.menu_table.setItem(63, 1, self.cw_bfo_parm_name)
        self.menu_table.setCellWidget(63, 2, self.cw_bfo_combo)

        # 07-08
        self.cw_bk_in_type_menu_nb = QTableWidgetItem("07-08")
        self.cw_bk_in_type_parm_name = QTableWidgetItem("CW BK-IN TYPE")

        self.cw_bk_in_type_combo = QComboBox()
        self.cw_bk_in_type_combo.setEditable(True)
        self.cw_bk_in_type_combo.lineEdit().setReadOnly(True)
        self.cw_bk_in_type_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.cw_bk_in_type_combo.addItems([i for i in CW_BK_IN_TYPE.keys()])
        format_combo(self.cw_bk_in_type_combo)
        self.cw_bk_in_type_combo.setCurrentIndex(0)
        self.cw_bk_in_type_combo.currentTextChanged.connect(self.set_cw_bk_in_type)

        self.menu_table.setItem(64, 0, self.cw_bk_in_type_menu_nb)
        self.menu_table.setItem(64, 1, self.cw_bk_in_type_parm_name)
        self.menu_table.setCellWidget(64, 2, self.cw_bk_in_type_combo)

        # 07-09
        self.cw_bk_in_delay_menu_nb = QTableWidgetItem("07-09")
        self.cw_bk_in_delay_parm_name = QTableWidgetItem("CW BK-IN DELAY")

        self.cw_bk_in_delay_spin = QSpinBox()
        self.cw_bk_in_delay_spin.setAlignment(Qt.AlignCenter)
        self.cw_bk_in_delay_spin.setMaximum(3000)
        self.cw_bk_in_delay_spin.setMinimum(30)
        self.cw_bk_in_delay_spin.setSingleStep(10)
        self.cw_bk_in_delay_spin.setValue(200)
        self.cw_bk_in_delay_spin.setSuffix(" msec")
        self.cw_bk_in_delay_spin.valueChanged.connect(self.set_cw_bk_in_delay)

        self.menu_table.setItem(65, 0, self.cw_bk_in_delay_menu_nb)
        self.menu_table.setItem(65, 1, self.cw_bk_in_delay_parm_name)
        self.menu_table.setCellWidget(65, 2, self.cw_bk_in_delay_spin)

        # 07-10
        self.cw_wav_shape_menu_nb = QTableWidgetItem("07-10")
        self.cw_wav_shape_parm_name = QTableWidgetItem("CW WAVE SHAPE")

        self.cw_wav_shape_combo = QComboBox()
        self.cw_wav_shape_combo.setEditable(True)
        self.cw_wav_shape_combo.lineEdit().setReadOnly(True)
        self.cw_wav_shape_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.cw_wav_shape_combo.addItems([i for i in CW_WAVE_SHAPE.keys()])
        format_combo(self.cw_wav_shape_combo)
        self.cw_wav_shape_combo.setCurrentIndex(1)
        self.cw_wav_shape_combo.currentTextChanged.connect(self.set_cw_wave_shape)

        self.menu_table.setItem(66, 0, self.cw_wav_shape_menu_nb)
        self.menu_table.setItem(66, 1, self.cw_wav_shape_parm_name)
        self.menu_table.setCellWidget(66, 2, self.cw_wav_shape_combo)

        # 07-11
        self.cw_freq_display_menu_nb = QTableWidgetItem("07-11")
        self.cw_freq_display_parm_name = QTableWidgetItem("CW FREQ DISPLAY")

        self.cw_freq_display_combo = QComboBox()
        self.cw_freq_display_combo.setEditable(True)
        self.cw_freq_display_combo.lineEdit().setReadOnly(True)
        self.cw_freq_display_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.cw_freq_display_combo.addItems([i for i in CW_FREQ_DISPLAY.keys()])
        format_combo(self.cw_freq_display_combo)
        self.cw_freq_display_combo.setCurrentIndex(1)
        self.cw_freq_display_combo.currentTextChanged.connect(self.set_cw_freq_display)

        self.menu_table.setItem(67, 0, self.cw_freq_display_menu_nb)
        self.menu_table.setItem(67, 1, self.cw_freq_display_parm_name)
        self.menu_table.setCellWidget(67, 2, self.cw_freq_display_combo)

        # 07-12
        self.pc_keying_menu_nb = QTableWidgetItem("07-12")
        self.pc_keying_parm_name = QTableWidgetItem("PC KEYING")

        self.pc_keying_combo = QComboBox()
        self.pc_keying_combo.setEditable(True)
        self.pc_keying_combo.lineEdit().setReadOnly(True)
        self.pc_keying_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.pc_keying_combo.addItems([i for i in PC_KEYING.keys()])
        format_combo(self.pc_keying_combo)
        self.pc_keying_combo.setCurrentIndex(0)
        self.pc_keying_combo.currentTextChanged.connect(self.set_pc_keying)

        self.menu_table.setItem(68, 0, self.pc_keying_menu_nb)
        self.menu_table.setItem(68, 1, self.pc_keying_parm_name)
        self.menu_table.setCellWidget(68, 2, self.pc_keying_combo)

        # 07-13
        self.qsk_delay_time_menu_nb = QTableWidgetItem("07-13")
        self.qsk_delay_time_parm_name = QTableWidgetItem("QSK DELAY TIME")

        self.qsk_delay_time_combo = QComboBox()
        self.qsk_delay_time_combo.setEditable(True)
        self.qsk_delay_time_combo.lineEdit().setReadOnly(True)
        self.qsk_delay_time_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.qsk_delay_time_combo.addItems([i for i in QSK_DELAY_TIME.keys()])
        format_combo(self.qsk_delay_time_combo)
        self.qsk_delay_time_combo.setCurrentIndex(0)
        self.qsk_delay_time_combo.currentTextChanged.connect(self.set_qsk_delay_time)

        self.menu_table.setItem(69, 0, self.qsk_delay_time_menu_nb)
        self.menu_table.setItem(69, 1, self.qsk_delay_time_parm_name)
        self.menu_table.setCellWidget(69, 2, self.qsk_delay_time_combo)

        # MODE DAT
        self.mode_dat_separator = QTableWidgetItem("MODE DAT")
        self.mode_dat_separator.setBackground(QColor(Qt.GlobalColor.lightGray))
        self.menu_table.setItem(70, 0, self.mode_dat_separator)
        self.menu_table.setSpan(70, 0, 1, 3)
        # 08-01
        self.data_mode_menu_nb = QTableWidgetItem("08-01")
        self.data_mode_parm_name = QTableWidgetItem("DATA MODE")

        self.data_mode_combo = QComboBox()
        self.data_mode_combo.setEditable(True)
        self.data_mode_combo.lineEdit().setReadOnly(True)
        self.data_mode_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.data_mode_combo.addItems([i for i in DATA_MODE.keys()])
        format_combo(self.data_mode_combo)
        self.data_mode_combo.setCurrentIndex(0)
        self.data_mode_combo.currentTextChanged.connect(self.set_data_mode)

        self.menu_table.setItem(71, 0, self.data_mode_menu_nb)
        self.menu_table.setItem(71, 1, self.data_mode_parm_name)
        self.menu_table.setCellWidget(71, 2, self.data_mode_combo)

        # 08-02
        self.psk_tone_menu_nb = QTableWidgetItem("08-02")
        self.psk_tone_parm_name = QTableWidgetItem("PSK TONE")

        self.psk_tone_combo = QComboBox()
        self.psk_tone_combo.setEditable(True)
        self.psk_tone_combo.lineEdit().setReadOnly(True)
        self.psk_tone_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.psk_tone_combo.addItems([i for i in PSK_TONE.keys()])
        format_combo(self.psk_tone_combo)
        self.psk_tone_combo.setCurrentIndex(0)
        self.psk_tone_combo.currentTextChanged.connect(self.set_psk_tone)

        self.menu_table.setItem(72, 0, self.psk_tone_menu_nb)
        self.menu_table.setItem(72, 1, self.psk_tone_parm_name)
        self.menu_table.setCellWidget(72, 2, self.psk_tone_combo)

        # 08-03
        self.other_disp_menu_nb = QTableWidgetItem("08-03")
        self.other_disp_parm_name = QTableWidgetItem("OTHER DISP")

        self.other_disp_spin = QSpinBox()
        self.other_disp_spin.setAlignment(Qt.AlignCenter)
        self.other_disp_spin.setMaximum(3000)
        self.other_disp_spin.setMinimum(-3000)
        self.other_disp_spin.setSingleStep(10)
        self.other_disp_spin.setValue(0)
        self.other_disp_spin.setSuffix(" Hz")
        self.other_disp_spin.valueChanged.connect(self.set_other_disp)

        self.menu_table.setItem(73, 0, self.other_disp_menu_nb)
        self.menu_table.setItem(73, 1, self.other_disp_parm_name)
        self.menu_table.setCellWidget(73, 2, self.other_disp_spin)

        # 08-04
        self.other_shift_menu_nb = QTableWidgetItem("08-04")
        self.other_shift_parm_name = QTableWidgetItem("OTHER SHIFT")

        self.other_shift_spin = QSpinBox()
        self.other_shift_spin.setAlignment(Qt.AlignCenter)
        self.other_shift_spin.setMaximum(3000)
        self.other_shift_spin.setMinimum(-3000)
        self.other_shift_spin.setSingleStep(10)
        self.other_shift_spin.setValue(0)
        self.other_shift_spin.setSuffix(" Hz")
        self.other_shift_spin.valueChanged.connect(self.set_other_shift)

        self.menu_table.setItem(74, 0, self.other_shift_menu_nb)
        self.menu_table.setItem(74, 1, self.other_shift_parm_name)
        self.menu_table.setCellWidget(74, 2, self.other_shift_spin)

        # 08-05
        self.data_lcut_freq_menu_nb = QTableWidgetItem("08-05")
        self.data_lcut_freq_parm_name = QTableWidgetItem("DATA LCUT FREQ")

        self.data_lcut_freq_combo = QComboBox()
        self.data_lcut_freq_combo.setEditable(True)
        self.data_lcut_freq_combo.lineEdit().setReadOnly(True)
        self.data_lcut_freq_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.data_lcut_freq_combo.addItems([i for i in LCUT_FREQ.keys()])
        format_combo(self.data_lcut_freq_combo)
        self.data_lcut_freq_combo.setCurrentIndex(5)
        self.data_lcut_freq_combo.currentTextChanged.connect(self.set_data_lcut_freq)

        self.menu_table.setItem(75, 0, self.data_lcut_freq_menu_nb)
        self.menu_table.setItem(75, 1, self.data_lcut_freq_parm_name)
        self.menu_table.setCellWidget(75, 2, self.data_lcut_freq_combo)

        # 08-06
        self.data_lcut_slope_menu_nb = QTableWidgetItem("08-06")
        self.data_lcut_slope_parm_name = QTableWidgetItem("DATA LCUT SLOPE")

        self.data_lcut_slope_combo = QComboBox()
        self.data_lcut_slope_combo.setEditable(True)
        self.data_lcut_slope_combo.lineEdit().setReadOnly(True)
        self.data_lcut_slope_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.data_lcut_slope_combo.addItems([i for i in SLOPE.keys()])
        format_combo(self.data_lcut_slope_combo)
        self.data_lcut_slope_combo.setCurrentIndex(1)
        self.data_lcut_slope_combo.currentTextChanged.connect(self.set_data_lcut_slope)

        self.menu_table.setItem(76, 0, self.data_lcut_slope_menu_nb)
        self.menu_table.setItem(76, 1, self.data_lcut_slope_parm_name)
        self.menu_table.setCellWidget(76, 2, self.data_lcut_slope_combo)

        # 08-07
        self.data_hcut_freq_menu_nb = QTableWidgetItem("08-07")
        self.data_hcut_freq_parm_name = QTableWidgetItem("DATA HCUT FREQ")

        self.data_hcut_freq_combo = QComboBox()
        self.data_hcut_freq_combo.setEditable(True)
        self.data_hcut_freq_combo.lineEdit().setReadOnly(True)
        self.data_hcut_freq_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.data_hcut_freq_combo.addItems([i for i in HCUT_FREQ.keys()])
        format_combo(self.data_hcut_freq_combo)
        self.data_hcut_freq_combo.setCurrentIndex(47)
        self.data_hcut_freq_combo.currentTextChanged.connect(self.set_data_hcut_freq)

        self.menu_table.setItem(77, 0, self.data_hcut_freq_menu_nb)
        self.menu_table.setItem(77, 1, self.data_hcut_freq_parm_name)
        self.menu_table.setCellWidget(77, 2, self.data_hcut_freq_combo)

        # 08-08
        self.data_hcut_slope_menu_nb = QTableWidgetItem("08-08")
        self.data_hcut_slope_parm_name = QTableWidgetItem("DATA HCUT SLOPE")

        self.data_hcut_slope_combo = QComboBox()
        self.data_hcut_slope_combo.setEditable(True)
        self.data_hcut_slope_combo.lineEdit().setReadOnly(True)
        self.data_hcut_slope_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.data_hcut_slope_combo.addItems([i for i in SLOPE.keys()])
        format_combo(self.data_hcut_slope_combo)
        self.data_hcut_slope_combo.setCurrentIndex(1)
        self.data_hcut_slope_combo.currentTextChanged.connect(self.set_data_hcut_slope)

        self.menu_table.setItem(78, 0, self.data_hcut_slope_menu_nb)
        self.menu_table.setItem(78, 1, self.data_hcut_slope_parm_name)
        self.menu_table.setCellWidget(78, 2, self.data_hcut_slope_combo)

        # 08-09
        self.data_in_select_menu_nb = QTableWidgetItem("08-09")
        self.data_in_select_parm_name = QTableWidgetItem("DATA IN SELECT")

        self.data_in_select_combo = QComboBox()
        self.data_in_select_combo.setEditable(True)
        self.data_in_select_combo.lineEdit().setReadOnly(True)
        self.data_in_select_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.data_in_select_combo.addItems([i for i in DATA_IN_SELECT.keys()])
        format_combo(self.data_in_select_combo)
        self.data_in_select_combo.setCurrentIndex(1)
        self.data_in_select_combo.currentTextChanged.connect(self.set_data_in_select)

        self.menu_table.setItem(79, 0, self.data_in_select_menu_nb)
        self.menu_table.setItem(79, 1, self.data_in_select_parm_name)
        self.menu_table.setCellWidget(79, 2, self.data_in_select_combo)

        # 08-10
        self.data_ptt_select_menu_nb = QTableWidgetItem("08-10")
        self.data_ptt_select_parm_name = QTableWidgetItem("DATA PTT SELECT")

        self.data_ptt_select_combo = QComboBox()
        self.data_ptt_select_combo.setEditable(True)
        self.data_ptt_select_combo.lineEdit().setReadOnly(True)
        self.data_ptt_select_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.data_ptt_select_combo.addItems([i for i in DATA_PTT_SELECT.keys()])
        format_combo(self.data_ptt_select_combo)
        self.data_ptt_select_combo.setCurrentIndex(0)
        self.data_ptt_select_combo.currentTextChanged.connect(self.set_data_ptt_select)

        self.menu_table.setItem(80, 0, self.data_ptt_select_menu_nb)
        self.menu_table.setItem(80, 1, self.data_ptt_select_parm_name)
        self.menu_table.setCellWidget(80, 2, self.data_ptt_select_combo)

        # 08-11
        self.data_out_level_menu_nb = QTableWidgetItem("08-11")
        self.data_out_level_parm_name = QTableWidgetItem("DATA OUT LEVEL")

        self.data_out_level_spin = QSpinBox()
        self.data_out_level_spin.setAlignment(Qt.AlignCenter)
        self.data_out_level_spin.setMaximum(100)
        self.data_out_level_spin.setMinimum(0)
        self.data_out_level_spin.setSingleStep(1)
        self.data_out_level_spin.setValue(50)
        self.data_out_level_spin.valueChanged.connect(self.set_data_out_level)

        self.menu_table.setItem(81, 0, self.data_out_level_menu_nb)
        self.menu_table.setItem(81, 1, self.data_out_level_parm_name)
        self.menu_table.setCellWidget(81, 2, self.data_out_level_spin)

        # 08-12
        self.data_bfo_menu_nb = QTableWidgetItem("08-12")
        self.data_bfo_parm_name = QTableWidgetItem("DATA BFO")

        self.data_bfo_combo = QComboBox()
        self.data_bfo_combo.setEditable(True)
        self.data_bfo_combo.lineEdit().setReadOnly(True)
        self.data_bfo_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.data_bfo_combo.addItems([i for i in DATA_BFO.keys()])
        format_combo(self.data_bfo_combo)
        self.data_bfo_combo.setCurrentIndex(1)
        self.data_bfo_combo.currentTextChanged.connect(self.set_data_bfo)

        self.menu_table.setItem(82, 0, self.data_bfo_menu_nb)
        self.menu_table.setItem(82, 1, self.data_bfo_parm_name)
        self.menu_table.setCellWidget(82, 2, self.data_bfo_combo)

        # MODE FM
        self.mode_fm_separator = QTableWidgetItem("MODE FM")
        self.mode_fm_separator.setBackground(QColor(Qt.GlobalColor.lightGray))
        self.menu_table.setItem(83, 0, self.mode_fm_separator)
        self.menu_table.setSpan(83, 0, 1, 3)

        # 09-01
        self.fm_mic_select_menu_nb = QTableWidgetItem("09-01")
        self.fm_mic_select_parm_name = QTableWidgetItem("FM MIC SELECT")

        self.fm_mic_select_combo = QComboBox()
        self.fm_mic_select_combo.setEditable(True)
        self.fm_mic_select_combo.lineEdit().setReadOnly(True)
        self.fm_mic_select_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.fm_mic_select_combo.addItems([i for i in FM_MIC_SELECT.keys()])
        format_combo(self.fm_mic_select_combo)
        self.fm_mic_select_combo.setCurrentIndex(0)
        self.fm_mic_select_combo.currentTextChanged.connect(self.set_fm_mic_select)

        self.menu_table.setItem(84, 0, self.fm_mic_select_menu_nb)
        self.menu_table.setItem(84, 1, self.fm_mic_select_parm_name)
        self.menu_table.setCellWidget(84, 2, self.fm_mic_select_combo)

        # 09-02
        self.fm_out_level_menu_nb = QTableWidgetItem("09-02")
        self.fm_out_level_parm_name = QTableWidgetItem("FM OUT LEVEL")

        self.fm_out_level_spin = QSpinBox()
        self.fm_out_level_spin.setAlignment(Qt.AlignCenter)
        self.fm_out_level_spin.setMaximum(100)
        self.fm_out_level_spin.setMinimum(0)
        self.fm_out_level_spin.setSingleStep(1)
        self.fm_out_level_spin.setValue(50)
        self.fm_out_level_spin.valueChanged.connect(self.set_fm_out_level)

        self.menu_table.setItem(85, 0, self.fm_out_level_menu_nb)
        self.menu_table.setItem(85, 1, self.fm_out_level_parm_name)
        self.menu_table.setCellWidget(85, 2, self.fm_out_level_spin)

        # 09-03
        self.pkt_ptt_select_menu_nb = QTableWidgetItem("09-03")
        self.pkt_ptt_select_parm_name = QTableWidgetItem("PKT PTT SELECT")

        self.pkt_ptt_select_combo = QComboBox()
        self.pkt_ptt_select_combo.setEditable(True)
        self.pkt_ptt_select_combo.lineEdit().setReadOnly(True)
        self.pkt_ptt_select_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.pkt_ptt_select_combo.addItems([i for i in PKT_PTT_SELECT.keys()])
        format_combo(self.pkt_ptt_select_combo)
        self.pkt_ptt_select_combo.setCurrentIndex(0)
        self.pkt_ptt_select_combo.currentTextChanged.connect(self.set_pkt_ptt_select)

        self.menu_table.setItem(86, 0, self.pkt_ptt_select_menu_nb)
        self.menu_table.setItem(86, 1, self.pkt_ptt_select_parm_name)
        self.menu_table.setCellWidget(86, 2, self.pkt_ptt_select_combo)

        # 09-04
        self.rpt_shift_28_menu_nb = QTableWidgetItem("09-04")
        self.rpt_shift_28_parm_name = QTableWidgetItem("RPT SHIFT 28 MHz")

        self.rpt_shift_28_spin = QSpinBox()
        self.rpt_shift_28_spin.setAlignment(Qt.AlignCenter)
        self.rpt_shift_28_spin.setMaximum(1000)
        self.rpt_shift_28_spin.setMinimum(0)
        self.rpt_shift_28_spin.setSingleStep(10)
        self.rpt_shift_28_spin.setValue(100)
        self.rpt_shift_28_spin.setSuffix(" kHz")
        self.rpt_shift_28_spin.valueChanged.connect(self.set_rpt_shift_28)

        self.menu_table.setItem(87, 0, self.rpt_shift_28_menu_nb)
        self.menu_table.setItem(87, 1, self.rpt_shift_28_parm_name)
        self.menu_table.setCellWidget(87, 2, self.rpt_shift_28_spin)

        # 09-05
        self.rpt_shift_50_menu_nb = QTableWidgetItem("09-05")
        self.rpt_shift_50_parm_name = QTableWidgetItem("RPT SHIFT 50 MHz")

        self.rpt_shift_50_spin = QSpinBox()
        self.rpt_shift_50_spin.setAlignment(Qt.AlignCenter)
        self.rpt_shift_50_spin.setMaximum(4000)
        self.rpt_shift_50_spin.setMinimum(0)
        self.rpt_shift_50_spin.setSingleStep(10)
        self.rpt_shift_50_spin.setValue(1000)
        self.rpt_shift_50_spin.setSuffix(" kHz")
        self.rpt_shift_50_spin.valueChanged.connect(self.set_rpt_shift_50)

        self.menu_table.setItem(88, 0, self.rpt_shift_50_menu_nb)
        self.menu_table.setItem(88, 1, self.rpt_shift_50_parm_name)
        self.menu_table.setCellWidget(88, 2, self.rpt_shift_50_spin)

        # 09-06
        self.dcs_polarity_menu_nb = QTableWidgetItem("09-06")
        self.dcs_polarity_parm_name = QTableWidgetItem("DCS POLARITY")

        self.dcs_polarity_combo = QComboBox()
        self.dcs_polarity_combo.setEditable(True)
        self.dcs_polarity_combo.lineEdit().setReadOnly(True)
        self.dcs_polarity_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.dcs_polarity_combo.addItems([i for i in DCS_POLARITY.keys()])
        format_combo(self.dcs_polarity_combo)
        self.dcs_polarity_combo.setCurrentIndex(0)
        self.dcs_polarity_combo.currentTextChanged.connect(self.set_dcs_polarity)

        self.menu_table.setItem(89, 0, self.dcs_polarity_menu_nb)
        self.menu_table.setItem(89, 1, self.dcs_polarity_parm_name)
        self.menu_table.setCellWidget(89, 2, self.dcs_polarity_combo)

        # Mode RTTY
        self.mode_rtty_separator = QTableWidgetItem("MODE RTY")
        self.mode_rtty_separator.setBackground(QColor(Qt.GlobalColor.lightGray))
        self.menu_table.setItem(90, 0, self.mode_rtty_separator)
        self.menu_table.setSpan(90, 0, 1, 3)

        # 10-01
        self.rtty_lcut_freq_menu_nb = QTableWidgetItem("10-01")
        self.rtty_lcut_freq_parm_name = QTableWidgetItem("RTTY LCUT FREQ")

        self.rtty_lcut_freq_combo = QComboBox()
        self.rtty_lcut_freq_combo.setEditable(True)
        self.rtty_lcut_freq_combo.lineEdit().setReadOnly(True)
        self.rtty_lcut_freq_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.rtty_lcut_freq_combo.addItems([i for i in LCUT_FREQ.keys()])
        format_combo(self.rtty_lcut_freq_combo)
        self.rtty_lcut_freq_combo.setCurrentIndex(5)
        self.rtty_lcut_freq_combo.currentTextChanged.connect(self.set_rtty_lcut_freq)

        self.menu_table.setItem(91, 0, self.rtty_lcut_freq_menu_nb)
        self.menu_table.setItem(91, 1, self.rtty_lcut_freq_parm_name)
        self.menu_table.setCellWidget(91, 2, self.rtty_lcut_freq_combo)

        # 10-02
        self.rtty_lcut_slope_menu_nb = QTableWidgetItem("10-02")
        self.rtty_lcut_slope_parm_name = QTableWidgetItem("RTTY LCUT SLOPE")

        self.rtty_lcut_slope_combo = QComboBox()
        self.rtty_lcut_slope_combo.setEditable(True)
        self.rtty_lcut_slope_combo.lineEdit().setReadOnly(True)
        self.rtty_lcut_slope_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.rtty_lcut_slope_combo.addItems([i for i in SLOPE.keys()])
        format_combo(self.rtty_lcut_slope_combo)
        self.rtty_lcut_slope_combo.setCurrentIndex(1)
        self.rtty_lcut_slope_combo.currentTextChanged.connect(self.set_rtty_lcut_slope)

        self.menu_table.setItem(92, 0, self.rtty_lcut_slope_menu_nb)
        self.menu_table.setItem(92, 1, self.rtty_lcut_slope_parm_name)
        self.menu_table.setCellWidget(92, 2, self.rtty_lcut_slope_combo)

        # 10-03
        self.rtty_hcut_freq_menu_nb = QTableWidgetItem("10-03")
        self.rtty_hcut_freq_parm_name = QTableWidgetItem("RTTY HCUT FREQ")

        self.rtty_hcut_freq_combo = QComboBox()
        self.rtty_hcut_freq_combo.setEditable(True)
        self.rtty_hcut_freq_combo.lineEdit().setReadOnly(True)
        self.rtty_hcut_freq_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.rtty_hcut_freq_combo.addItems([i for i in HCUT_FREQ.keys()])
        format_combo(self.rtty_hcut_freq_combo)
        self.rtty_hcut_freq_combo.setCurrentIndex(47)
        self.rtty_hcut_freq_combo.currentTextChanged.connect(self.set_rtty_hcut_freq)

        self.menu_table.setItem(93, 0, self.rtty_hcut_freq_menu_nb)
        self.menu_table.setItem(93, 1, self.rtty_hcut_freq_parm_name)
        self.menu_table.setCellWidget(93, 2, self.rtty_hcut_freq_combo)

        # 10-04
        self.rtty_hcut_slope_menu_nb = QTableWidgetItem("10-04")
        self.rtty_hcut_slope_parm_name = QTableWidgetItem("RTTY HCUT SLOPE")

        self.rtty_hcut_slope_combo = QComboBox()
        self.rtty_hcut_slope_combo.setEditable(True)
        self.rtty_hcut_slope_combo.lineEdit().setReadOnly(True)
        self.rtty_hcut_slope_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.rtty_hcut_slope_combo.addItems([i for i in SLOPE.keys()])
        format_combo(self.rtty_hcut_slope_combo)
        self.rtty_hcut_slope_combo.setCurrentIndex(1)
        self.rtty_hcut_slope_combo.currentTextChanged.connect(self.set_rtty_hcut_slope)

        self.menu_table.setItem(94, 0, self.rtty_hcut_slope_menu_nb)
        self.menu_table.setItem(94, 1, self.rtty_hcut_slope_parm_name)
        self.menu_table.setCellWidget(94, 2, self.rtty_hcut_slope_combo)

        # 10-05
        self.rtty_shift_port_menu_nb = QTableWidgetItem("10-05")
        self.rtty_shift_port_parm_name = QTableWidgetItem("RTTY SHIFT PORT")

        self.rtty_shift_port_combo = QComboBox()
        self.rtty_shift_port_combo.setEditable(True)
        self.rtty_shift_port_combo.lineEdit().setReadOnly(True)
        self.rtty_shift_port_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.rtty_shift_port_combo.addItems([i for i in RTTY_SHIT_PORT.keys()])
        format_combo(self.rtty_shift_port_combo)
        self.rtty_shift_port_combo.setCurrentIndex(0)
        self.rtty_shift_port_combo.currentTextChanged.connect(self.set_rtty_shift_port)

        self.menu_table.setItem(95, 0, self.rtty_shift_port_menu_nb)
        self.menu_table.setItem(95, 1, self.rtty_shift_port_parm_name)
        self.menu_table.setCellWidget(95, 2, self.rtty_shift_port_combo)

        # 10-06
        self.rtty_polarity_r_menu_nb = QTableWidgetItem("10-06")
        self.rtty_polarity_r_parm_name = QTableWidgetItem("RTTY POLARITY-R")

        self.rtty_polarity_r_combo = QComboBox()
        self.rtty_polarity_r_combo.setEditable(True)
        self.rtty_polarity_r_combo.lineEdit().setReadOnly(True)
        self.rtty_polarity_r_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.rtty_polarity_r_combo.addItems([i for i in RTTY_POLARITY.keys()])
        format_combo(self.rtty_polarity_r_combo)
        self.rtty_polarity_r_combo.setCurrentIndex(0)
        self.rtty_polarity_r_combo.currentTextChanged.connect(self.set_rtty_polarity_r)

        self.menu_table.setItem(96, 0, self.rtty_polarity_r_menu_nb)
        self.menu_table.setItem(96, 1, self.rtty_polarity_r_parm_name)
        self.menu_table.setCellWidget(96, 2, self.rtty_polarity_r_combo)

        # 10-07
        self.rtty_polarity_t_menu_nb = QTableWidgetItem("10-07")
        self.rtty_polarity_t_parm_name = QTableWidgetItem("RTTY POLARITY-T")

        self.rtty_polarity_t_combo = QComboBox()
        self.rtty_polarity_t_combo.setEditable(True)
        self.rtty_polarity_t_combo.lineEdit().setReadOnly(True)
        self.rtty_polarity_t_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.rtty_polarity_t_combo.addItems([i for i in RTTY_POLARITY.keys()])
        format_combo(self.rtty_polarity_t_combo)
        self.rtty_polarity_t_combo.setCurrentIndex(0)
        self.rtty_polarity_t_combo.currentTextChanged.connect(self.set_rtty_polarity_t)

        self.menu_table.setItem(97, 0, self.rtty_polarity_t_menu_nb)
        self.menu_table.setItem(97, 1, self.rtty_polarity_t_parm_name)
        self.menu_table.setCellWidget(97, 2, self.rtty_polarity_t_combo)

        # 10-08
        self.rtty_out_level_menu_nb = QTableWidgetItem("10-08")
        self.rtty_out_level_parm_name = QTableWidgetItem("RTTY OUT LEVEL")

        self.rtty_out_level_spin = QSpinBox()
        self.rtty_out_level_spin.setAlignment(Qt.AlignCenter)
        self.rtty_out_level_spin.setMaximum(100)
        self.rtty_out_level_spin.setMinimum(0)
        self.rtty_out_level_spin.setSingleStep(1)
        self.rtty_out_level_spin.setValue(50)
        self.rtty_out_level_spin.valueChanged.connect(self.set_rtty_out_level)

        self.menu_table.setItem(98, 0, self.rtty_out_level_menu_nb)
        self.menu_table.setItem(98, 1, self.rtty_out_level_parm_name)
        self.menu_table.setCellWidget(98, 2, self.rtty_out_level_spin)

        # 10-09
        self.rtty_shift_freq_menu_nb = QTableWidgetItem("10-09")
        self.rtty_shift_freq_parm_name = QTableWidgetItem("RTTY SHIFT FREQ")

        self.rtty_shift_freq_combo = QComboBox()
        self.rtty_shift_freq_combo.setEditable(True)
        self.rtty_shift_freq_combo.lineEdit().setReadOnly(True)
        self.rtty_shift_freq_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.rtty_shift_freq_combo.addItems([i for i in RTTY_SHIFT_FREQ.keys()])
        format_combo(self.rtty_shift_freq_combo)
        self.rtty_shift_freq_combo.setCurrentIndex(0)
        self.rtty_shift_freq_combo.currentTextChanged.connect(self.set_rtty_shift_freq)

        self.menu_table.setItem(99, 0, self.rtty_shift_freq_menu_nb)
        self.menu_table.setItem(99, 1, self.rtty_shift_freq_parm_name)
        self.menu_table.setCellWidget(99, 2, self.rtty_shift_freq_combo)

        # 10-10
        self.rtty_mark_freq_menu_nb = QTableWidgetItem("10-10")
        self.rtty_mark_freq_parm_name = QTableWidgetItem("RTTY MARK FREQ")

        self.rtty_mark_freq_combo = QComboBox()
        self.rtty_mark_freq_combo.setEditable(True)
        self.rtty_mark_freq_combo.lineEdit().setReadOnly(True)
        self.rtty_mark_freq_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.rtty_mark_freq_combo.addItems([i for i in RTTY_MARK_FREQ.keys()])
        format_combo(self.rtty_mark_freq_combo)
        self.rtty_mark_freq_combo.setCurrentIndex(1)
        self.rtty_mark_freq_combo.currentTextChanged.connect(self.set_rtty_mark_freq)

        self.menu_table.setItem(100, 0, self.rtty_mark_freq_menu_nb)
        self.menu_table.setItem(100, 1, self.rtty_mark_freq_parm_name)
        self.menu_table.setCellWidget(100, 2, self.rtty_mark_freq_combo)

        # 10-11
        self.rtty_bfo_menu_nb = QTableWidgetItem("10-11")
        self.rtty_bfo_parm_name = QTableWidgetItem("RTTY BFO")

        self.rtty_bfo_combo = QComboBox()
        self.rtty_bfo_combo.setEditable(True)
        self.rtty_bfo_combo.lineEdit().setReadOnly(True)
        self.rtty_bfo_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.rtty_bfo_combo.addItems([i for i in RTTY_BFO.keys()])
        format_combo(self.rtty_bfo_combo)
        self.rtty_bfo_combo.setCurrentIndex(1)
        self.rtty_bfo_combo.currentTextChanged.connect(self.set_rtty_bfo)

        self.menu_table.setItem(101, 0, self.rtty_bfo_menu_nb)
        self.menu_table.setItem(101, 1, self.rtty_bfo_parm_name)
        self.menu_table.setCellWidget(101, 2, self.rtty_bfo_combo)

        # Mode SSB
        self.mode_ssb_separator = QTableWidgetItem("MODE SSB")
        self.mode_ssb_separator.setBackground(QColor(Qt.GlobalColor.lightGray))
        self.menu_table.setItem(102, 0, self.mode_ssb_separator)
        self.menu_table.setSpan(102, 0, 1, 3)

        # 11-01
        self.ssb_lcut_freq_menu_nb = QTableWidgetItem("11-01")
        self.ssb_lcut_freq_parm_name = QTableWidgetItem("SSB LCUT FREQ")

        self.ssb_lcut_freq_combo = QComboBox()
        self.ssb_lcut_freq_combo.setEditable(True)
        self.ssb_lcut_freq_combo.lineEdit().setReadOnly(True)
        self.ssb_lcut_freq_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.ssb_lcut_freq_combo.addItems([i for i in LCUT_FREQ.keys()])
        format_combo(self.ssb_lcut_freq_combo)
        self.ssb_lcut_freq_combo.setCurrentIndex(1)
        self.ssb_lcut_freq_combo.currentTextChanged.connect(self.set_ssb_lcut_freq)

        self.menu_table.setItem(103, 0, self.ssb_lcut_freq_menu_nb)
        self.menu_table.setItem(103, 1, self.ssb_lcut_freq_parm_name)
        self.menu_table.setCellWidget(103, 2, self.ssb_lcut_freq_combo)

        # 11-02
        self.ssb_lcut_slope_menu_nb = QTableWidgetItem("11-02")
        self.ssb_lcut_slope_parm_name = QTableWidgetItem("SSB LCUT SLOPE")

        self.ssb_lcut_slope_combo = QComboBox()
        self.ssb_lcut_slope_combo.setEditable(True)
        self.ssb_lcut_slope_combo.lineEdit().setReadOnly(True)
        self.ssb_lcut_slope_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.ssb_lcut_slope_combo.addItems([i for i in SLOPE.keys()])
        format_combo(self.ssb_lcut_slope_combo)
        self.ssb_lcut_slope_combo.setCurrentIndex(0)
        self.ssb_lcut_slope_combo.currentTextChanged.connect(self.set_ssb_lcut_slope)

        self.menu_table.setItem(104, 0, self.ssb_lcut_slope_menu_nb)
        self.menu_table.setItem(104, 1, self.ssb_lcut_slope_parm_name)
        self.menu_table.setCellWidget(104, 2, self.ssb_lcut_slope_combo)

        # 11-03
        self.ssb_hcut_freq_menu_nb = QTableWidgetItem("11-03")
        self.ssb_hcut_freq_parm_name = QTableWidgetItem("SSB HCUT FREQ")

        self.ssb_hcut_freq_combo = QComboBox()
        self.ssb_hcut_freq_combo.setEditable(True)
        self.ssb_hcut_freq_combo.lineEdit().setReadOnly(True)
        self.ssb_hcut_freq_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.ssb_hcut_freq_combo.addItems([i for i in HCUT_FREQ.keys()])
        format_combo(self.ssb_hcut_freq_combo)
        self.ssb_hcut_freq_combo.setCurrentIndex(47)
        self.ssb_hcut_freq_combo.currentTextChanged.connect(self.set_ssb_hcut_freq)

        self.menu_table.setItem(105, 0, self.ssb_hcut_freq_menu_nb)
        self.menu_table.setItem(105, 1, self.ssb_hcut_freq_parm_name)
        self.menu_table.setCellWidget(105, 2, self.ssb_hcut_freq_combo)

        # 11-04
        self.ssb_hcut_slope_menu_nb = QTableWidgetItem("11-04")
        self.ssb_hcut_slope_parm_name = QTableWidgetItem("SSB HCUT SLOPE")

        self.ssb_hcut_slope_combo = QComboBox()
        self.ssb_hcut_slope_combo.setEditable(True)
        self.ssb_hcut_slope_combo.lineEdit().setReadOnly(True)
        self.ssb_hcut_slope_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.ssb_hcut_slope_combo.addItems([i for i in SLOPE.keys()])
        format_combo(self.ssb_hcut_slope_combo)
        self.ssb_hcut_slope_combo.setCurrentIndex(0)
        self.ssb_hcut_slope_combo.currentTextChanged.connect(self.set_ssb_hcut_slope)

        self.menu_table.setItem(106, 0, self.ssb_hcut_slope_menu_nb)
        self.menu_table.setItem(106, 1, self.ssb_hcut_slope_parm_name)
        self.menu_table.setCellWidget(106, 2, self.ssb_hcut_slope_combo)

        # 11-05
        self.ssb_mic_select_menu_nb = QTableWidgetItem("11-05")
        self.ssb_mic_select_parm_name = QTableWidgetItem("SSB MIC SELECT")

        self.ssb_mic_select_combo = QComboBox()
        self.ssb_mic_select_combo.setEditable(True)
        self.ssb_mic_select_combo.lineEdit().setReadOnly(True)
        self.ssb_mic_select_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.ssb_mic_select_combo.addItems([i for i in SSB_MIC_SELECT.keys()])
        format_combo(self.ssb_mic_select_combo)
        self.ssb_mic_select_combo.setCurrentIndex(0)
        self.ssb_mic_select_combo.currentTextChanged.connect(self.set_ssb_mic_select)

        self.menu_table.setItem(107, 0, self.ssb_mic_select_menu_nb)
        self.menu_table.setItem(107, 1, self.ssb_mic_select_parm_name)
        self.menu_table.setCellWidget(107, 2, self.ssb_mic_select_combo)

        # 11-06
        self.ssb_out_level_menu_nb = QTableWidgetItem("11-06")
        self.ssb_out_level_parm_name = QTableWidgetItem("SSB OUT LEVEL")

        self.ssb_out_level_spin = QSpinBox()
        self.ssb_out_level_spin.setAlignment(Qt.AlignCenter)
        self.ssb_out_level_spin.setMaximum(100)
        self.ssb_out_level_spin.setMinimum(0)
        self.ssb_out_level_spin.setSingleStep(1)
        self.ssb_out_level_spin.setValue(50)
        self.ssb_out_level_spin.valueChanged.connect(self.set_ssb_out_level)

        self.menu_table.setItem(108, 0, self.ssb_out_level_menu_nb)
        self.menu_table.setItem(108, 1, self.ssb_out_level_parm_name)
        self.menu_table.setCellWidget(108, 2, self.ssb_out_level_spin)

        # 11-07
        self.ssb_bfo_menu_nb = QTableWidgetItem("11-07")
        self.ssb_bfo_parm_name = QTableWidgetItem("SSB BFO")

        self.ssb_bfo_combo = QComboBox()
        self.ssb_bfo_combo.setEditable(True)
        self.ssb_bfo_combo.lineEdit().setReadOnly(True)
        self.ssb_bfo_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.ssb_bfo_combo.addItems([i for i in SSB_BFO.keys()])
        format_combo(self.ssb_bfo_combo)
        self.ssb_bfo_combo.setCurrentIndex(2)
        self.ssb_bfo_combo.currentTextChanged.connect(self.set_ssb_bfo)

        self.menu_table.setItem(109, 0, self.ssb_bfo_menu_nb)
        self.menu_table.setItem(109, 1, self.ssb_bfo_parm_name)
        self.menu_table.setCellWidget(109, 2, self.ssb_bfo_combo)

        # 11-08
        self.ssb_ptt_select_menu_nb = QTableWidgetItem("11-08")
        self.ssb_ptt_select_parm_name = QTableWidgetItem("SSB PTT SELECT")

        self.ssb_ptt_select_combo = QComboBox()
        self.ssb_ptt_select_combo.setEditable(True)
        self.ssb_ptt_select_combo.lineEdit().setReadOnly(True)
        self.ssb_ptt_select_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.ssb_ptt_select_combo.addItems([i for i in SSB_PTT_SELECT.keys()])
        format_combo(self.ssb_ptt_select_combo)
        self.ssb_ptt_select_combo.setCurrentIndex(0)
        self.ssb_ptt_select_combo.currentTextChanged.connect(self.set_ssb_ptt_select)

        self.menu_table.setItem(110, 0, self.ssb_ptt_select_menu_nb)
        self.menu_table.setItem(110, 1, self.ssb_ptt_select_parm_name)
        self.menu_table.setCellWidget(110, 2, self.ssb_ptt_select_combo)

        # 11-09
        self.ssb_tx_bpf_menu_nb = QTableWidgetItem("11-09")
        self.ssb_tx_bpf_parm_name = QTableWidgetItem("SSB TX BPF")

        self.ssb_tx_bpf_combo = QComboBox()
        self.ssb_tx_bpf_combo.setEditable(True)
        self.ssb_tx_bpf_combo.lineEdit().setReadOnly(True)
        self.ssb_tx_bpf_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.ssb_tx_bpf_combo.addItems([i for i in SSB_TX_BPF.keys()])
        format_combo(self.ssb_tx_bpf_combo)
        self.ssb_tx_bpf_combo.setCurrentIndex(3)
        self.ssb_tx_bpf_combo.currentTextChanged.connect(self.set_ssb_tx_bpf)

        self.menu_table.setItem(111, 0, self.ssb_tx_bpf_menu_nb)
        self.menu_table.setItem(111, 1, self.ssb_tx_bpf_parm_name)
        self.menu_table.setCellWidget(111, 2, self.ssb_tx_bpf_combo)

        # RX DSP
        self.rx_dsp_separator = QTableWidgetItem("RX DSP")
        self.rx_dsp_separator.setBackground(QColor(Qt.GlobalColor.lightGray))
        self.menu_table.setItem(112, 0, self.rx_dsp_separator)
        self.menu_table.setSpan(112, 0, 1, 3)

        # 12-01
        self.apf_width_menu_nb = QTableWidgetItem("12-01")
        self.apf_width_parm_name = QTableWidgetItem("APF WIDTH")

        self.apf_width_combo = QComboBox()
        self.apf_width_combo.setEditable(True)
        self.apf_width_combo.lineEdit().setReadOnly(True)
        self.apf_width_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.apf_width_combo.addItems([i for i in APF_WIDTH.keys()])
        format_combo(self.apf_width_combo)
        self.apf_width_combo.setCurrentIndex(1)
        self.apf_width_combo.currentTextChanged.connect(self.set_apf_width)

        self.menu_table.setItem(113, 0, self.apf_width_menu_nb)
        self.menu_table.setItem(113, 1, self.apf_width_parm_name)
        self.menu_table.setCellWidget(113, 2, self.apf_width_combo)

        # 12-02
        self.contour_level_menu_nb = QTableWidgetItem("12-02")
        self.contour_level_parm_name = QTableWidgetItem("CONTOUR LEVEL")

        self.contour_level_spin = QSpinBox()
        self.contour_level_spin.setAlignment(Qt.AlignCenter)
        self.contour_level_spin.setMaximum(20)
        self.contour_level_spin.setMinimum(-40)
        self.contour_level_spin.setSingleStep(1)
        self.contour_level_spin.setValue(-15)
        self.contour_level_spin.valueChanged.connect(self.set_contour_level)

        self.menu_table.setItem(114, 0, self.contour_level_menu_nb)
        self.menu_table.setItem(114, 1, self.contour_level_parm_name)
        self.menu_table.setCellWidget(114, 2, self.contour_level_spin)

        # 12-03
        self.contour_width_menu_nb = QTableWidgetItem("12-03")
        self.contour_width_parm_name = QTableWidgetItem("CONTOUR WIDTH")

        self.contour_width_spin = QSpinBox()
        self.contour_width_spin.setAlignment(Qt.AlignCenter)
        self.contour_width_spin.setMaximum(11)
        self.contour_width_spin.setMinimum(1)
        self.contour_width_spin.setSingleStep(1)
        self.contour_width_spin.setValue(10)
        self.contour_width_spin.valueChanged.connect(self.set_contour_width)

        self.menu_table.setItem(115, 0, self.contour_width_menu_nb)
        self.menu_table.setItem(115, 1, self.contour_width_parm_name)
        self.menu_table.setCellWidget(115, 2, self.contour_width_spin)

        # 12-04
        self.if_notch_width_menu_nb = QTableWidgetItem("12-04")
        self.if_notch_width_parm_name = QTableWidgetItem("IF NOTCH WIDTH")

        self.if_notch_width_combo = QComboBox()
        self.if_notch_width_combo.setEditable(True)
        self.if_notch_width_combo.lineEdit().setReadOnly(True)
        self.if_notch_width_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.if_notch_width_combo.addItems([i for i in IF_NOTCH_WIDTH.keys()])
        format_combo(self.if_notch_width_combo)
        self.if_notch_width_combo.setCurrentIndex(1)
        self.if_notch_width_combo.currentTextChanged.connect(self.set_if_notch_width)

        self.menu_table.setItem(116, 0, self.if_notch_width_menu_nb)
        self.menu_table.setItem(116, 1, self.if_notch_width_parm_name)
        self.menu_table.setCellWidget(116, 2, self.if_notch_width_combo)

        # SCOPE
        self.scope_separator = QTableWidgetItem("SCOPE")
        self.scope_separator.setBackground(QColor(Qt.GlobalColor.lightGray))
        self.menu_table.setItem(117, 0, self.scope_separator)
        self.menu_table.setSpan(117, 0, 1, 3)

        # 13-01
        self.scp_start_cycle_menu_nb = QTableWidgetItem("13-01")
        self.scp_start_cycle_parm_name = QTableWidgetItem("SCP START CYCLE")

        self.scp_start_cycle_combo = QComboBox()
        self.scp_start_cycle_combo.setEditable(True)
        self.scp_start_cycle_combo.lineEdit().setReadOnly(True)
        self.scp_start_cycle_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.scp_start_cycle_combo.addItems([i for i in SCP_START_CYCLE.keys()])
        format_combo(self.scp_start_cycle_combo)
        self.scp_start_cycle_combo.setCurrentIndex(0)
        self.scp_start_cycle_combo.currentTextChanged.connect(self.set_scp_start_cycle)

        self.menu_table.setItem(118, 0, self.scp_start_cycle_menu_nb)
        self.menu_table.setItem(118, 1, self.scp_start_cycle_parm_name)
        self.menu_table.setCellWidget(118, 2, self.scp_start_cycle_combo)

        # 13-02
        self.scp_span_freq_menu_nb = QTableWidgetItem("13-02")
        self.scp_span_freq_parm_name = QTableWidgetItem("SCP SPAN FREQ")

        self.scp_span_freq_combo = QComboBox()
        self.scp_span_freq_combo.setEditable(True)
        self.scp_span_freq_combo.lineEdit().setReadOnly(True)
        self.scp_span_freq_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.scp_span_freq_combo.addItems([i for i in SCP_SPAN_FREQ.keys()])
        format_combo(self.scp_span_freq_combo)
        self.scp_span_freq_combo.setCurrentIndex(4)
        self.scp_span_freq_combo.currentTextChanged.connect(self.set_scp_span_freq)

        self.menu_table.setItem(119, 0, self.scp_span_freq_menu_nb)
        self.menu_table.setItem(119, 1, self.scp_span_freq_parm_name)
        self.menu_table.setCellWidget(119, 2, self.scp_span_freq_combo)

        # TUNING
        self.tuning_separator = QTableWidgetItem("TUNING")
        self.tuning_separator.setBackground(QColor(Qt.GlobalColor.lightGray))
        self.menu_table.setItem(120, 0, self.tuning_separator)
        self.menu_table.setSpan(120, 0, 1, 3)

        # 14-01
        self.quick_dial_menu_nb = QTableWidgetItem("14-01")
        self.quick_dial_parm_name = QTableWidgetItem("QUICK DIAL")

        self.quick_dial_combo = QComboBox()
        self.quick_dial_combo.setEditable(True)
        self.quick_dial_combo.lineEdit().setReadOnly(True)
        self.quick_dial_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.quick_dial_combo.addItems([i for i in QUICK_DIAL.keys()])
        format_combo(self.quick_dial_combo)
        self.quick_dial_combo.setCurrentIndex(2)
        self.quick_dial_combo.currentTextChanged.connect(self.set_quick_dial)

        self.menu_table.setItem(121, 0, self.quick_dial_menu_nb)
        self.menu_table.setItem(121, 1, self.quick_dial_parm_name)
        self.menu_table.setCellWidget(121, 2, self.quick_dial_combo)

        # 14-02
        self.ssb_dial_step_menu_nb = QTableWidgetItem("14-02")
        self.ssb_dial_step_parm_name = QTableWidgetItem("SSB DIAL STEP")

        self.ssb_dial_step_combo = QComboBox()
        self.ssb_dial_step_combo.setEditable(True)
        self.ssb_dial_step_combo.lineEdit().setReadOnly(True)
        self.ssb_dial_step_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.ssb_dial_step_combo.addItems([i for i in SSB_DIAL_STEP.keys()])
        format_combo(self.ssb_dial_step_combo)
        self.ssb_dial_step_combo.setCurrentIndex(2)
        self.ssb_dial_step_combo.currentTextChanged.connect(self.set_ssb_dial_step)

        self.menu_table.setItem(122, 0, self.ssb_dial_step_menu_nb)
        self.menu_table.setItem(122, 1, self.ssb_dial_step_parm_name)
        self.menu_table.setCellWidget(122, 2, self.ssb_dial_step_combo)

        # 14-03
        self.am_dial_step_menu_nb = QTableWidgetItem("14-03")
        self.am_dial_step_parm_name = QTableWidgetItem("AM DIAL STEP")

        self.am_dial_step_combo = QComboBox()
        self.am_dial_step_combo.setEditable(True)
        self.am_dial_step_combo.lineEdit().setReadOnly(True)
        self.am_dial_step_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.am_dial_step_combo.addItems([i for i in AM_DIAL_STEP.keys()])
        format_combo(self.am_dial_step_combo)
        self.am_dial_step_combo.setCurrentIndex(0)
        self.am_dial_step_combo.currentTextChanged.connect(self.set_am_dial_step)

        self.menu_table.setItem(123, 0, self.am_dial_step_menu_nb)
        self.menu_table.setItem(123, 1, self.am_dial_step_parm_name)
        self.menu_table.setCellWidget(123, 2, self.am_dial_step_combo)

        # 14-04
        self.fm_dial_step_menu_nb = QTableWidgetItem("14-04")
        self.fm_dial_step_parm_name = QTableWidgetItem("FM DIAL STEP")

        self.fm_dial_step_combo = QComboBox()
        self.fm_dial_step_combo.setEditable(True)
        self.fm_dial_step_combo.lineEdit().setReadOnly(True)
        self.fm_dial_step_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.fm_dial_step_combo.addItems([i for i in FM_DIAL_STEP.keys()])
        format_combo(self.fm_dial_step_combo)
        self.fm_dial_step_combo.setCurrentIndex(1)
        self.fm_dial_step_combo.currentTextChanged.connect(self.set_fm_dial_step)

        self.menu_table.setItem(124, 0, self.fm_dial_step_menu_nb)
        self.menu_table.setItem(124, 1, self.fm_dial_step_parm_name)
        self.menu_table.setCellWidget(124, 2, self.fm_dial_step_combo)

        # 14-05
        self.dial_step_menu_nb = QTableWidgetItem("14-05")
        self.dial_step_parm_name = QTableWidgetItem("DIAL STEP")

        self.dial_step_combo = QComboBox()
        self.dial_step_combo.setEditable(True)
        self.dial_step_combo.lineEdit().setReadOnly(True)
        self.dial_step_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.dial_step_combo.addItems([i for i in DIAL_STEP.keys()])
        format_combo(self.dial_step_combo)
        self.dial_step_combo.setCurrentIndex(1)
        self.dial_step_combo.currentTextChanged.connect(self.set_dial_step)

        self.menu_table.setItem(125, 0, self.dial_step_menu_nb)
        self.menu_table.setItem(125, 1, self.dial_step_parm_name)
        self.menu_table.setCellWidget(125, 2, self.dial_step_combo)

        # 14-06
        self.am_ch_step_menu_nb = QTableWidgetItem("14-06")
        self.am_ch_step_parm_name = QTableWidgetItem("AM CH STEP")

        self.am_ch_step_combo = QComboBox()
        self.am_ch_step_combo.setEditable(True)
        self.am_ch_step_combo.lineEdit().setReadOnly(True)
        self.am_ch_step_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.am_ch_step_combo.addItems([i for i in AM_CH_STEP.keys()])
        format_combo(self.am_ch_step_combo)
        self.am_ch_step_combo.setCurrentIndex(1)
        self.am_ch_step_combo.currentTextChanged.connect(self.set_am_ch_step)

        self.menu_table.setItem(126, 0, self.am_ch_step_menu_nb)
        self.menu_table.setItem(126, 1, self.am_ch_step_parm_name)
        self.menu_table.setCellWidget(126, 2, self.am_ch_step_combo)

        # 14-07
        self.fm_ch_step_menu_nb = QTableWidgetItem("14-07")
        self.fm_ch_step_parm_name = QTableWidgetItem("FM CH STEP")

        self.fm_ch_step_combo = QComboBox()
        self.fm_ch_step_combo.setEditable(True)
        self.fm_ch_step_combo.lineEdit().setReadOnly(True)
        self.fm_ch_step_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.fm_ch_step_combo.addItems([i for i in FM_CH_STEP.keys()])
        format_combo(self.fm_ch_step_combo)
        self.fm_ch_step_combo.setCurrentIndex(0)
        self.fm_ch_step_combo.currentTextChanged.connect(self.set_fm_ch_step)

        self.menu_table.setItem(127, 0, self.fm_ch_step_menu_nb)
        self.menu_table.setItem(127, 1, self.fm_ch_step_parm_name)
        self.menu_table.setCellWidget(127, 2, self.fm_ch_step_combo)

        # TX AUDIO
        self.tx_audio_separator = QTableWidgetItem("TX AUDIO")
        self.tx_audio_separator.setBackground(QColor(Qt.GlobalColor.lightGray))
        self.menu_table.setItem(128, 0, self.tx_audio_separator)
        self.menu_table.setSpan(128, 0, 1, 3)

        # 15-01
        self.eq_1_freq_menu_nb = QTableWidgetItem("15-01")
        self.eq_1_freq_parm_name = QTableWidgetItem("EQ1 FREQ")

        self.eq_1_freq_combo = QComboBox()
        self.eq_1_freq_combo.setEditable(True)
        self.eq_1_freq_combo.lineEdit().setReadOnly(True)
        self.eq_1_freq_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.eq_1_freq_combo.addItems([i for i in EQ_1_FREQ.keys()])
        format_combo(self.eq_1_freq_combo)
        self.eq_1_freq_combo.setCurrentIndex(0)
        self.eq_1_freq_combo.currentTextChanged.connect(self.set_eq_1_freq)

        self.menu_table.setItem(129, 0, self.eq_1_freq_menu_nb)
        self.menu_table.setItem(129, 1, self.eq_1_freq_parm_name)
        self.menu_table.setCellWidget(129, 2, self.eq_1_freq_combo)

        # 15-02
        self.eq_1_level_menu_nb = QTableWidgetItem("15-02")
        self.eq_1_level_parm_name = QTableWidgetItem("EQ1 LEVEL")

        self.eq_1_level_spin = QSpinBox()
        self.eq_1_level_spin.setAlignment(Qt.AlignCenter)
        self.eq_1_level_spin.setMaximum(10)
        self.eq_1_level_spin.setMinimum(-20)
        self.eq_1_level_spin.setSingleStep(1)
        self.eq_1_level_spin.setValue(5)
        self.eq_1_level_spin.valueChanged.connect(self.set_eq_1_level)

        self.menu_table.setItem(130, 0, self.eq_1_level_menu_nb)
        self.menu_table.setItem(130, 1, self.eq_1_level_parm_name)
        self.menu_table.setCellWidget(130, 2, self.eq_1_level_spin)

        # 15-03
        self.eq_1_bwth_menu_nb = QTableWidgetItem("15-03")
        self.eq_1_bwth_parm_name = QTableWidgetItem("EQ1 BWTH")

        self.eq_1_bwth_spin = QSpinBox()
        self.eq_1_bwth_spin.setAlignment(Qt.AlignCenter)
        self.eq_1_bwth_spin.setMaximum(10)
        self.eq_1_bwth_spin.setMinimum(1)
        self.eq_1_bwth_spin.setSingleStep(1)
        self.eq_1_bwth_spin.setValue(10)
        self.eq_1_bwth_spin.valueChanged.connect(self.set_eq_1_bwth)

        self.menu_table.setItem(131, 0, self.eq_1_bwth_menu_nb)
        self.menu_table.setItem(131, 1, self.eq_1_bwth_parm_name)
        self.menu_table.setCellWidget(131, 2, self.eq_1_bwth_spin)

        # 15-04
        self.eq_2_freq_menu_nb = QTableWidgetItem("15-04")
        self.eq_2_freq_parm_name = QTableWidgetItem("EQ2 FREQ")

        self.eq_2_freq_combo = QComboBox()
        self.eq_2_freq_combo.setEditable(True)
        self.eq_2_freq_combo.lineEdit().setReadOnly(True)
        self.eq_2_freq_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.eq_2_freq_combo.addItems([i for i in EQ_2_FREQ.keys()])
        format_combo(self.eq_2_freq_combo)
        self.eq_2_freq_combo.setCurrentIndex(0)
        self.eq_2_freq_combo.currentTextChanged.connect(self.set_eq_2_freq)

        self.menu_table.setItem(132, 0, self.eq_2_freq_menu_nb)
        self.menu_table.setItem(132, 1, self.eq_2_freq_parm_name)
        self.menu_table.setCellWidget(132, 2, self.eq_2_freq_combo)

        # 15-05
        self.eq_2_level_menu_nb = QTableWidgetItem("15-05")
        self.eq_2_level_parm_name = QTableWidgetItem("EQ2 LEVEL")

        self.eq_2_level_spin = QSpinBox()
        self.eq_2_level_spin.setAlignment(Qt.AlignCenter)
        self.eq_2_level_spin.setMaximum(10)
        self.eq_2_level_spin.setMinimum(-20)
        self.eq_2_level_spin.setSingleStep(1)
        self.eq_2_level_spin.setValue(5)
        self.eq_2_level_spin.valueChanged.connect(self.set_eq_2_level)

        self.menu_table.setItem(133, 0, self.eq_2_level_menu_nb)
        self.menu_table.setItem(133, 1, self.eq_2_level_parm_name)
        self.menu_table.setCellWidget(133, 2, self.eq_2_level_spin)

        # 15-06
        self.eq_2_bwth_menu_nb = QTableWidgetItem("15-06")
        self.eq_2_bwth_parm_name = QTableWidgetItem("EQ2 BWTH")

        self.eq_2_bwth_spin = QSpinBox()
        self.eq_2_bwth_spin.setAlignment(Qt.AlignCenter)
        self.eq_2_bwth_spin.setMaximum(10)
        self.eq_2_bwth_spin.setMinimum(1)
        self.eq_2_bwth_spin.setSingleStep(1)
        self.eq_2_bwth_spin.setValue(10)
        self.eq_2_bwth_spin.valueChanged.connect(self.set_eq_2_bwth)

        self.menu_table.setItem(134, 0, self.eq_2_bwth_menu_nb)
        self.menu_table.setItem(134, 1, self.eq_2_bwth_parm_name)
        self.menu_table.setCellWidget(134, 2, self.eq_2_bwth_spin)

        # 15-07
        self.eq_3_freq_menu_nb = QTableWidgetItem("15-07")
        self.eq_3_freq_parm_name = QTableWidgetItem("EQ3 FREQ")

        self.eq_3_freq_combo = QComboBox()
        self.eq_3_freq_combo.setEditable(True)
        self.eq_3_freq_combo.lineEdit().setReadOnly(True)
        self.eq_3_freq_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.eq_3_freq_combo.addItems([i for i in EQ_3_FREQ.keys()])
        format_combo(self.eq_3_freq_combo)
        self.eq_3_freq_combo.setCurrentIndex(0)
        self.eq_3_freq_combo.currentTextChanged.connect(self.set_eq_3_freq)

        self.menu_table.setItem(135, 0, self.eq_3_freq_menu_nb)
        self.menu_table.setItem(135, 1, self.eq_3_freq_parm_name)
        self.menu_table.setCellWidget(135, 2, self.eq_3_freq_combo)

        # 15-08
        self.eq_3_level_menu_nb = QTableWidgetItem("15-08")
        self.eq_3_level_parm_name = QTableWidgetItem("EQ3 LEVEL")

        self.eq_3_level_spin = QSpinBox()
        self.eq_3_level_spin.setAlignment(Qt.AlignCenter)
        self.eq_3_level_spin.setMaximum(10)
        self.eq_3_level_spin.setMinimum(-20)
        self.eq_3_level_spin.setSingleStep(1)
        self.eq_3_level_spin.setValue(5)
        self.eq_3_level_spin.valueChanged.connect(self.set_eq_3_level)

        self.menu_table.setItem(136, 0, self.eq_3_level_menu_nb)
        self.menu_table.setItem(136, 1, self.eq_3_level_parm_name)
        self.menu_table.setCellWidget(136, 2, self.eq_3_level_spin)

        # 15-09
        self.eq_3_bwth_menu_nb = QTableWidgetItem("15-09")
        self.eq_3_bwth_parm_name = QTableWidgetItem("EQ3 BWTH")

        self.eq_3_bwth_spin = QSpinBox()
        self.eq_3_bwth_spin.setAlignment(Qt.AlignCenter)
        self.eq_3_bwth_spin.setMaximum(10)
        self.eq_3_bwth_spin.setMinimum(1)
        self.eq_3_bwth_spin.setSingleStep(1)
        self.eq_3_bwth_spin.setValue(10)
        self.eq_3_bwth_spin.valueChanged.connect(self.set_eq_3_bwth)

        self.menu_table.setItem(137, 0, self.eq_3_bwth_menu_nb)
        self.menu_table.setItem(137, 1, self.eq_3_bwth_parm_name)
        self.menu_table.setCellWidget(137, 2, self.eq_3_bwth_spin)

        # 15-10
        self.p_eq_1_freq_menu_nb = QTableWidgetItem("15-10")
        self.p_eq_1_freq_parm_name = QTableWidgetItem("P-EQ1 FREQ")

        self.p_eq_1_freq_combo = QComboBox()
        self.p_eq_1_freq_combo.setEditable(True)
        self.p_eq_1_freq_combo.lineEdit().setReadOnly(True)
        self.p_eq_1_freq_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.p_eq_1_freq_combo.addItems([i for i in EQ_1_FREQ.keys()])
        format_combo(self.p_eq_1_freq_combo)
        self.p_eq_1_freq_combo.setCurrentIndex(2)
        self.p_eq_1_freq_combo.currentTextChanged.connect(self.set_p_eq_1_freq)

        self.menu_table.setItem(138, 0, self.p_eq_1_freq_menu_nb)
        self.menu_table.setItem(138, 1, self.p_eq_1_freq_parm_name)
        self.menu_table.setCellWidget(138, 2, self.p_eq_1_freq_combo)

        # 15-11
        self.p_eq_1_level_menu_nb = QTableWidgetItem("15-11")
        self.p_eq_1_level_parm_name = QTableWidgetItem("P-EQ1 LEVEL")

        self.p_eq_1_level_spin = QSpinBox()
        self.p_eq_1_level_spin.setAlignment(Qt.AlignCenter)
        self.p_eq_1_level_spin.setMaximum(10)
        self.p_eq_1_level_spin.setMinimum(-20)
        self.p_eq_1_level_spin.setSingleStep(1)
        self.p_eq_1_level_spin.setValue(0)
        self.p_eq_1_level_spin.valueChanged.connect(self.set_p_eq_1_level)

        self.menu_table.setItem(139, 0, self.p_eq_1_level_menu_nb)
        self.menu_table.setItem(139, 1, self.p_eq_1_level_parm_name)
        self.menu_table.setCellWidget(139, 2, self.p_eq_1_level_spin)

        # 15-12
        self.p_eq_1_bwth_menu_nb = QTableWidgetItem("15-12")
        self.p_eq_1_bwth_parm_name = QTableWidgetItem("P-EQ1 BWTH")

        self.p_eq_1_bwth_spin = QSpinBox()
        self.p_eq_1_bwth_spin.setAlignment(Qt.AlignCenter)
        self.p_eq_1_bwth_spin.setMaximum(10)
        self.p_eq_1_bwth_spin.setMinimum(1)
        self.p_eq_1_bwth_spin.setSingleStep(1)
        self.p_eq_1_bwth_spin.setValue(2)
        self.p_eq_1_bwth_spin.valueChanged.connect(self.set_p_eq_1_bwth)

        self.menu_table.setItem(140, 0, self.p_eq_1_bwth_menu_nb)
        self.menu_table.setItem(140, 1, self.p_eq_1_bwth_parm_name)
        self.menu_table.setCellWidget(140, 2, self.p_eq_1_bwth_spin)

        # 15-13
        self.p_eq_2_freq_menu_nb = QTableWidgetItem("15-13")
        self.p_eq_2_freq_parm_name = QTableWidgetItem("P-EQ2 FREQ")

        self.p_eq_2_freq_combo = QComboBox()
        self.p_eq_2_freq_combo.setEditable(True)
        self.p_eq_2_freq_combo.lineEdit().setReadOnly(True)
        self.p_eq_2_freq_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.p_eq_2_freq_combo.addItems([i for i in EQ_2_FREQ.keys()])
        format_combo(self.p_eq_2_freq_combo)
        self.p_eq_2_freq_combo.setCurrentIndex(2)
        self.p_eq_2_freq_combo.currentTextChanged.connect(self.set_p_eq_2_freq)

        self.menu_table.setItem(141, 0, self.p_eq_2_freq_menu_nb)
        self.menu_table.setItem(141, 1, self.p_eq_2_freq_parm_name)
        self.menu_table.setCellWidget(141, 2, self.p_eq_2_freq_combo)

        # 15-14
        self.p_eq_2_level_menu_nb = QTableWidgetItem("15-14")
        self.p_eq_2_level_parm_name = QTableWidgetItem("P-EQ2 LEVEL")

        self.p_eq_2_level_spin = QSpinBox()
        self.p_eq_2_level_spin.setAlignment(Qt.AlignCenter)
        self.p_eq_2_level_spin.setMaximum(10)
        self.p_eq_2_level_spin.setMinimum(-20)
        self.p_eq_2_level_spin.setSingleStep(1)
        self.p_eq_2_level_spin.setValue(0)
        self.p_eq_2_level_spin.valueChanged.connect(self.set_p_eq_2_level)

        self.menu_table.setItem(142, 0, self.p_eq_2_level_menu_nb)
        self.menu_table.setItem(142, 1, self.p_eq_2_level_parm_name)
        self.menu_table.setCellWidget(142, 2, self.p_eq_2_level_spin)

        # 15-15
        self.p_eq_2_bwth_menu_nb = QTableWidgetItem("15-15")
        self.p_eq_2_bwth_parm_name = QTableWidgetItem("P-EQ2 BWTH")

        self.p_eq_2_bwth_spin = QSpinBox()
        self.p_eq_2_bwth_spin.setAlignment(Qt.AlignCenter)
        self.p_eq_2_bwth_spin.setMaximum(10)
        self.p_eq_2_bwth_spin.setMinimum(1)
        self.p_eq_2_bwth_spin.setSingleStep(1)
        self.p_eq_2_bwth_spin.setValue(1)
        self.p_eq_2_bwth_spin.valueChanged.connect(self.set_p_eq_2_bwth)

        self.menu_table.setItem(143, 0, self.p_eq_2_bwth_menu_nb)
        self.menu_table.setItem(143, 1, self.p_eq_2_bwth_parm_name)
        self.menu_table.setCellWidget(143, 2, self.p_eq_2_bwth_spin)

        # 15-16
        self.p_eq_3_freq_menu_nb = QTableWidgetItem("15-16")
        self.p_eq_3_freq_parm_name = QTableWidgetItem("P-EQ3 FREQ")

        self.p_eq_3_freq_combo = QComboBox()
        self.p_eq_3_freq_combo.setEditable(True)
        self.p_eq_3_freq_combo.lineEdit().setReadOnly(True)
        self.p_eq_3_freq_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.p_eq_3_freq_combo.addItems([i for i in EQ_3_FREQ.keys()])
        format_combo(self.p_eq_3_freq_combo)
        self.p_eq_3_freq_combo.setCurrentIndex(7)
        self.p_eq_3_freq_combo.currentTextChanged.connect(self.set_p_eq_3_freq)

        self.menu_table.setItem(144, 0, self.p_eq_3_freq_menu_nb)
        self.menu_table.setItem(144, 1, self.p_eq_3_freq_parm_name)
        self.menu_table.setCellWidget(144, 2, self.p_eq_3_freq_combo)

        # 15-17
        self.p_eq_3_level_menu_nb = QTableWidgetItem("15-17")
        self.p_eq_3_level_parm_name = QTableWidgetItem("P-EQ3 LEVEL")

        self.p_eq_3_level_spin = QSpinBox()
        self.p_eq_3_level_spin.setAlignment(Qt.AlignCenter)
        self.p_eq_3_level_spin.setMaximum(10)
        self.p_eq_3_level_spin.setMinimum(-20)
        self.p_eq_3_level_spin.setSingleStep(1)
        self.p_eq_3_level_spin.setValue(0)
        self.p_eq_3_level_spin.valueChanged.connect(self.set_p_eq_3_level)

        self.menu_table.setItem(145, 0, self.p_eq_3_level_menu_nb)
        self.menu_table.setItem(145, 1, self.p_eq_3_level_parm_name)
        self.menu_table.setCellWidget(145, 2, self.p_eq_3_level_spin)

        # 15-18
        self.p_eq_3_bwth_menu_nb = QTableWidgetItem("15-18")
        self.p_eq_3_bwth_parm_name = QTableWidgetItem("P-EQ3 BWTH")

        self.p_eq_3_bwth_spin = QSpinBox()
        self.p_eq_3_bwth_spin.setAlignment(Qt.AlignCenter)
        self.p_eq_3_bwth_spin.setMaximum(10)
        self.p_eq_3_bwth_spin.setMinimum(1)
        self.p_eq_3_bwth_spin.setSingleStep(1)
        self.p_eq_3_bwth_spin.setValue(1)
        self.p_eq_3_bwth_spin.valueChanged.connect(self.set_p_eq_3_bwth)

        self.menu_table.setItem(146, 0, self.p_eq_3_bwth_menu_nb)
        self.menu_table.setItem(146, 1, self.p_eq_3_bwth_parm_name)
        self.menu_table.setCellWidget(146, 2, self.p_eq_3_bwth_spin)

        # TX GNRL
        self.tx_gnrl_separator = QTableWidgetItem("TX GNRL")
        self.tx_gnrl_separator.setBackground(QColor(Qt.GlobalColor.lightGray))
        self.menu_table.setItem(147, 0, self.tx_gnrl_separator)
        self.menu_table.setSpan(147, 0, 1, 3)

        # 16-01
        self.hf_ssb_pwr_menu_nb = QTableWidgetItem("16-01")
        self.hf_ssb_pwr_parm_name = QTableWidgetItem("HF SSB PWR")

        self.hf_ssb_pwr_spin = QSpinBox()
        self.hf_ssb_pwr_spin.setAlignment(Qt.AlignCenter)
        self.hf_ssb_pwr_spin.setMaximum(100)
        self.hf_ssb_pwr_spin.setMinimum(5)
        self.hf_ssb_pwr_spin.setSingleStep(1)
        self.hf_ssb_pwr_spin.setValue(100)
        self.hf_ssb_pwr_spin.valueChanged.connect(self.set_hf_ssb_pwr)

        self.menu_table.setItem(148, 0, self.hf_ssb_pwr_menu_nb)
        self.menu_table.setItem(148, 1, self.hf_ssb_pwr_parm_name)
        self.menu_table.setCellWidget(148, 2, self.hf_ssb_pwr_spin)

        # 16-02
        self.hf_am_pwr_menu_nb = QTableWidgetItem("16-02")
        self.hf_am_pwr_parm_name = QTableWidgetItem("HF AM PWR")

        self.hf_am_pwr_spin = QSpinBox()
        self.hf_am_pwr_spin.setAlignment(Qt.AlignCenter)
        self.hf_am_pwr_spin.setMaximum(40)
        self.hf_am_pwr_spin.setMinimum(5)
        self.hf_am_pwr_spin.setSingleStep(1)
        self.hf_am_pwr_spin.setValue(25)
        self.hf_am_pwr_spin.setValue(25)
        self.hf_am_pwr_spin.valueChanged.connect(self.set_hf_am_pwr)

        self.menu_table.setItem(149, 0, self.hf_am_pwr_menu_nb)
        self.menu_table.setItem(149, 1, self.hf_am_pwr_parm_name)
        self.menu_table.setCellWidget(149, 2, self.hf_am_pwr_spin)

        # 16-03
        self.hf_pwr_menu_nb = QTableWidgetItem("16-03")
        self.hf_pwr_parm_name = QTableWidgetItem("HF PWR")

        self.hf_pwr_spin = QSpinBox()
        self.hf_pwr_spin.setAlignment(Qt.AlignCenter)
        self.hf_pwr_spin.setMaximum(100)
        self.hf_pwr_spin.setMinimum(5)
        self.hf_pwr_spin.setSingleStep(1)
        self.hf_pwr_spin.setValue(100)
        self.hf_pwr_spin.valueChanged.connect(self.set_hf_pwr)

        self.menu_table.setItem(150, 0, self.hf_pwr_menu_nb)
        self.menu_table.setItem(150, 1, self.hf_pwr_parm_name)
        self.menu_table.setCellWidget(150, 2, self.hf_pwr_spin)

        # 16-04
        self.ssb_50m_pwr_menu_nb = QTableWidgetItem("16-04")
        self.ssb_50m_pwr_parm_name = QTableWidgetItem("50M SSB PWR")

        self.ssb_50m_pwr_spin = QSpinBox()
        self.ssb_50m_pwr_spin.setAlignment(Qt.AlignCenter)
        self.ssb_50m_pwr_spin.setMaximum(100)
        self.ssb_50m_pwr_spin.setMinimum(5)
        self.ssb_50m_pwr_spin.setSingleStep(1)
        self.ssb_50m_pwr_spin.setValue(100)
        self.ssb_50m_pwr_spin.valueChanged.connect(self.set_50m_ssb_pwr)

        self.menu_table.setItem(151, 0, self.ssb_50m_pwr_menu_nb)
        self.menu_table.setItem(151, 1, self.ssb_50m_pwr_parm_name)
        self.menu_table.setCellWidget(151, 2, self.ssb_50m_pwr_spin)

        # 16-05
        self.am_50m_pwr_menu_nb = QTableWidgetItem("16-05")
        self.am_50m_pwr_parm_name = QTableWidgetItem("50M AM PWR")

        self.am_50m_pwr_spin = QSpinBox()
        self.am_50m_pwr_spin.setAlignment(Qt.AlignCenter)
        self.am_50m_pwr_spin.setMaximum(40)
        self.am_50m_pwr_spin.setMinimum(5)
        self.am_50m_pwr_spin.setSingleStep(1)
        self.am_50m_pwr_spin.setValue(25)
        self.am_50m_pwr_spin.valueChanged.connect(self.set_50m_am_pwr)

        self.menu_table.setItem(152, 0, self.am_50m_pwr_menu_nb)
        self.menu_table.setItem(152, 1, self.am_50m_pwr_parm_name)
        self.menu_table.setCellWidget(152, 2, self.am_50m_pwr_spin)

        # 16-06
        self.pwr_50m_menu_nb = QTableWidgetItem("16-06")
        self.pwr_50m_parm_name = QTableWidgetItem("50M PWR")

        self.pwr_50m_spin = QSpinBox()
        self.pwr_50m_spin.setAlignment(Qt.AlignCenter)
        self.pwr_50m_spin.setMaximum(100)
        self.pwr_50m_spin.setMinimum(5)
        self.pwr_50m_spin.setSingleStep(1)
        self.pwr_50m_spin.setValue(100)
        self.pwr_50m_spin.valueChanged.connect(self.set_50m_pwr)

        self.menu_table.setItem(153, 0, self.pwr_50m_menu_nb)
        self.menu_table.setItem(153, 1, self.pwr_50m_parm_name)
        self.menu_table.setCellWidget(153, 2, self.pwr_50m_spin)

        # 16-07
        self.ssb_mic_gain_menu_nb = QTableWidgetItem("16-07")
        self.ssb_mic_gain_parm_name = QTableWidgetItem("SSB MIC GAIN")

        self.ssb_mic_gain_spin = QSpinBox()
        self.ssb_mic_gain_spin.setAlignment(Qt.AlignCenter)
        self.ssb_mic_gain_spin.setMaximum(100)
        self.ssb_mic_gain_spin.setMinimum(0)
        self.ssb_mic_gain_spin.setSingleStep(1)
        self.ssb_mic_gain_spin.setValue(50)
        self.ssb_mic_gain_spin.valueChanged.connect(self.set_ssb_mic_gain)

        self.menu_table.setItem(154, 0, self.ssb_mic_gain_menu_nb)
        self.menu_table.setItem(154, 1, self.ssb_mic_gain_parm_name)
        self.menu_table.setCellWidget(154, 2, self.ssb_mic_gain_spin)

        # 16-08
        self.am_mic_gain_menu_nb = QTableWidgetItem("16-08")
        self.am_mic_gain_parm_name = QTableWidgetItem("AM MIC GAIN")

        self.am_mic_gain_spin = QSpinBox()
        self.am_mic_gain_spin.setAlignment(Qt.AlignCenter)
        self.am_mic_gain_spin.setMaximum(100)
        self.am_mic_gain_spin.setMinimum(0)
        self.am_mic_gain_spin.setSingleStep(1)
        self.am_mic_gain_spin.setValue(50)
        self.am_mic_gain_spin.valueChanged.connect(self.set_am_mic_gain)

        self.menu_table.setItem(155, 0, self.am_mic_gain_menu_nb)
        self.menu_table.setItem(155, 1, self.am_mic_gain_parm_name)
        self.menu_table.setCellWidget(155, 2, self.am_mic_gain_spin)

        # 16-09
        self.fm_mic_gain_menu_nb = QTableWidgetItem("16-09")
        self.fm_mic_gain_parm_name = QTableWidgetItem("FM MIC GAIN")

        self.fm_mic_gain_spin = QSpinBox()
        self.fm_mic_gain_spin.setAlignment(Qt.AlignCenter)
        self.fm_mic_gain_spin.setMaximum(100)
        self.fm_mic_gain_spin.setMinimum(0)
        self.fm_mic_gain_spin.setSingleStep(1)
        self.fm_mic_gain_spin.setValue(50)
        self.fm_mic_gain_spin.valueChanged.connect(self.set_fm_mic_gain)

        self.menu_table.setItem(156, 0, self.fm_mic_gain_menu_nb)
        self.menu_table.setItem(156, 1, self.fm_mic_gain_parm_name)
        self.menu_table.setCellWidget(156, 2, self.fm_mic_gain_spin)

        # 16-10
        self.data_mic_gain_menu_nb = QTableWidgetItem("16-10")
        self.data_mic_gain_parm_name = QTableWidgetItem("DATA MIC GAIN")

        self.data_mic_gain_spin = QSpinBox()
        self.data_mic_gain_spin.setAlignment(Qt.AlignCenter)
        self.data_mic_gain_spin.setMaximum(100)
        self.data_mic_gain_spin.setMinimum(0)
        self.data_mic_gain_spin.setSingleStep(1)
        self.data_mic_gain_spin.setValue(50)
        self.data_mic_gain_spin.valueChanged.connect(self.set_data_mic_gain)

        self.menu_table.setItem(157, 0, self.data_mic_gain_menu_nb)
        self.menu_table.setItem(157, 1, self.data_mic_gain_parm_name)
        self.menu_table.setCellWidget(157, 2, self.data_mic_gain_spin)

        # 16-11
        self.ssb_data_gain_menu_nb = QTableWidgetItem("16-11")
        self.ssb_data_gain_parm_name = QTableWidgetItem("SSB DATA GAIN")

        self.ssb_data_gain_spin = QSpinBox()
        self.ssb_data_gain_spin.setAlignment(Qt.AlignCenter)
        self.ssb_data_gain_spin.setMaximum(100)
        self.ssb_data_gain_spin.setMinimum(0)
        self.ssb_data_gain_spin.setSingleStep(1)
        self.ssb_data_gain_spin.setValue(50)
        self.ssb_data_gain_spin.valueChanged.connect(self.set_ssb_data_gain)

        self.menu_table.setItem(158, 0, self.ssb_data_gain_menu_nb)
        self.menu_table.setItem(158, 1, self.ssb_data_gain_parm_name)
        self.menu_table.setCellWidget(158, 2, self.ssb_data_gain_spin)

        # 16-12
        self.am_data_gain_menu_nb = QTableWidgetItem("16-12")
        self.am_data_gain_parm_name = QTableWidgetItem("AM DATA GAIN")

        self.am_data_gain_spin = QSpinBox()
        self.am_data_gain_spin.setAlignment(Qt.AlignCenter)
        self.am_data_gain_spin.setMaximum(100)
        self.am_data_gain_spin.setMinimum(0)
        self.am_data_gain_spin.setSingleStep(1)
        self.am_data_gain_spin.setValue(50)
        self.am_data_gain_spin.valueChanged.connect(self.set_am_data_gain)

        self.menu_table.setItem(159, 0, self.am_data_gain_menu_nb)
        self.menu_table.setItem(159, 1, self.am_data_gain_parm_name)
        self.menu_table.setCellWidget(159, 2, self.am_data_gain_spin)

        # 16-13
        self.fm_data_gain_menu_nb = QTableWidgetItem("16-13")
        self.fm_data_gain_parm_name = QTableWidgetItem("FM DATA GAIN")

        self.fm_data_gain_spin = QSpinBox()
        self.fm_data_gain_spin.setAlignment(Qt.AlignCenter)
        self.fm_data_gain_spin.setMaximum(100)
        self.fm_data_gain_spin.setMinimum(0)
        self.fm_data_gain_spin.setSingleStep(1)
        self.fm_data_gain_spin.setValue(50)
        self.fm_data_gain_spin.valueChanged.connect(self.set_fm_data_gain)

        self.menu_table.setItem(160, 0, self.fm_data_gain_menu_nb)
        self.menu_table.setItem(160, 1, self.fm_data_gain_parm_name)
        self.menu_table.setCellWidget(160, 2, self.fm_data_gain_spin)

        # 16-14
        self.data_data_gain_menu_nb = QTableWidgetItem("16-14")
        self.data_data_gain_parm_name = QTableWidgetItem("DATA DATA GAIN")

        self.data_data_gain_spin = QSpinBox()
        self.data_data_gain_spin.setAlignment(Qt.AlignCenter)
        self.data_data_gain_spin.setMaximum(100)
        self.data_data_gain_spin.setMinimum(0)
        self.data_data_gain_spin.setSingleStep(1)
        self.data_data_gain_spin.setValue(50)
        self.data_data_gain_spin.valueChanged.connect(self.set_data_data_gain)

        self.menu_table.setItem(161, 0, self.data_data_gain_menu_nb)
        self.menu_table.setItem(161, 1, self.data_data_gain_parm_name)
        self.menu_table.setCellWidget(161, 2, self.data_data_gain_spin)

        # 16-15
        self.tuner_select_menu_nb = QTableWidgetItem("16-15")
        self.tuner_select_parm_name = QTableWidgetItem("TUNER SELECT")

        self.tuner_select_combo = QComboBox()
        self.tuner_select_combo.setEditable(True)
        self.tuner_select_combo.lineEdit().setReadOnly(True)
        self.tuner_select_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.tuner_select_combo.addItems([i for i in TUNER_SELECT.keys()])
        format_combo(self.tuner_select_combo)
        self.tuner_select_combo.setCurrentIndex(0)
        self.tuner_select_combo.currentTextChanged.connect(self.set_tuner_select)

        self.menu_table.setItem(162, 0, self.tuner_select_menu_nb)
        self.menu_table.setItem(162, 1, self.tuner_select_parm_name)
        self.menu_table.setCellWidget(162, 2, self.tuner_select_combo)

        # 16-16
        self.vox_select_menu_nb = QTableWidgetItem("16-16")
        self.vox_select_parm_name = QTableWidgetItem("VOX SELECT")

        self.vox_select_combo = QComboBox()
        self.vox_select_combo.setEditable(True)
        self.vox_select_combo.lineEdit().setReadOnly(True)
        self.vox_select_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.vox_select_combo.addItems([i for i in VOX_SELECT.keys()])
        format_combo(self.vox_select_combo)
        self.vox_select_combo.setCurrentIndex(0)
        self.vox_select_combo.currentTextChanged.connect(self.set_vox_select)

        self.menu_table.setItem(163, 0, self.vox_select_menu_nb)
        self.menu_table.setItem(163, 1, self.vox_select_parm_name)
        self.menu_table.setCellWidget(163, 2, self.vox_select_combo)

        # 16-17
        self.vox_gain_menu_nb = QTableWidgetItem("16-17")
        self.vox_gain_parm_name = QTableWidgetItem("VOX GAIN")

        self.vox_gain_spin = QSpinBox()
        self.vox_gain_spin.setAlignment(Qt.AlignCenter)
        self.vox_gain_spin.setMaximum(100)
        self.vox_gain_spin.setMinimum(0)
        self.vox_gain_spin.setSingleStep(1)
        self.vox_gain_spin.setValue(50)
        self.vox_gain_spin.valueChanged.connect(self.set_vox_gain)

        self.menu_table.setItem(164, 0, self.vox_gain_menu_nb)
        self.menu_table.setItem(164, 1, self.vox_gain_parm_name)
        self.menu_table.setCellWidget(164, 2, self.vox_gain_spin)

        # 16-18
        self.vox_delay_menu_nb = QTableWidgetItem("16-18")
        self.vox_delay_parm_name = QTableWidgetItem("VOX DELAY")

        self.vox_delay_spin = QSpinBox()
        self.vox_delay_spin.setAlignment(Qt.AlignCenter)
        self.vox_delay_spin.setMaximum(3000)
        self.vox_delay_spin.setMinimum(30)
        self.vox_delay_spin.setSingleStep(10)
        self.vox_delay_spin.setValue(500)
        self.vox_delay_spin.setSuffix(" msec")
        self.vox_delay_spin.valueChanged.connect(self.set_vox_delay)

        self.menu_table.setItem(165, 0, self.vox_delay_menu_nb)
        self.menu_table.setItem(165, 1, self.vox_delay_parm_name)
        self.menu_table.setCellWidget(165, 2, self.vox_delay_spin)

        # 16-19
        self.anti_vox_gain_menu_nb = QTableWidgetItem("16-19")
        self.anti_vox_gain_parm_name = QTableWidgetItem("ANTI VOX GAIN")

        self.anti_vox_gain_spin = QSpinBox()
        self.anti_vox_gain_spin.setAlignment(Qt.AlignCenter)
        self.anti_vox_gain_spin.setMaximum(100)
        self.anti_vox_gain_spin.setMinimum(0)
        self.anti_vox_gain_spin.setSingleStep(1)
        self.anti_vox_gain_spin.setValue(50)
        self.anti_vox_gain_spin.valueChanged.connect(self.set_anti_vox_gain)

        self.menu_table.setItem(166, 0, self.anti_vox_gain_menu_nb)
        self.menu_table.setItem(166, 1, self.anti_vox_gain_parm_name)
        self.menu_table.setCellWidget(166, 2, self.anti_vox_gain_spin)

        # 16-20
        self.data_vox_gain_menu_nb = QTableWidgetItem("16-20")
        self.data_vox_gain_parm_name = QTableWidgetItem("DATA VOX GAIN")

        self.data_vox_gain_spin = QSpinBox()
        self.data_vox_gain_spin.setAlignment(Qt.AlignCenter)
        self.data_vox_gain_spin.setMaximum(100)
        self.data_vox_gain_spin.setMinimum(0)
        self.data_vox_gain_spin.setSingleStep(1)
        self.data_vox_gain_spin.setValue(50)
        self.data_vox_gain_spin.valueChanged.connect(self.set_data_vox_gain)

        self.menu_table.setItem(167, 0, self.data_vox_gain_menu_nb)
        self.menu_table.setItem(167, 1, self.data_vox_gain_parm_name)
        self.menu_table.setCellWidget(167, 2, self.data_vox_gain_spin)

        # 16-21
        self.data_vox_delay_menu_nb = QTableWidgetItem("16-21")
        self.data_vox_delay_parm_name = QTableWidgetItem("DATA VOX DELAY")

        self.data_vox_delay_spin = QSpinBox()
        self.data_vox_delay_spin.setAlignment(Qt.AlignCenter)
        self.data_vox_delay_spin.setMaximum(3000)
        self.data_vox_delay_spin.setMinimum(30)
        self.data_vox_delay_spin.setSingleStep(10)
        self.data_vox_delay_spin.setValue(100)
        self.data_vox_delay_spin.setSuffix(" msec")
        self.data_vox_delay_spin.valueChanged.connect(self.set_data_vox_delay)

        self.menu_table.setItem(168, 0, self.data_vox_delay_menu_nb)
        self.menu_table.setItem(168, 1, self.data_vox_delay_parm_name)
        self.menu_table.setCellWidget(168, 2, self.data_vox_delay_spin)

        # 16-22
        self.anti_dvox_gain_menu_nb = QTableWidgetItem("16-22")
        self.anti_dvox_gain_parm_name = QTableWidgetItem("ANTI DVOX GAIN")

        self.anti_dvox_gain_spin = QSpinBox()
        self.anti_dvox_gain_spin.setAlignment(Qt.AlignCenter)
        self.anti_dvox_gain_spin.setMaximum(100)
        self.anti_dvox_gain_spin.setMinimum(0)
        self.anti_dvox_gain_spin.setSingleStep(1)
        self.anti_dvox_gain_spin.setValue(0)
        self.anti_dvox_gain_spin.valueChanged.connect(self.set_anti_dvox_gain)

        self.menu_table.setItem(169, 0, self.anti_dvox_gain_menu_nb)
        self.menu_table.setItem(169, 1, self.anti_dvox_gain_parm_name)
        self.menu_table.setCellWidget(169, 2, self.anti_dvox_gain_spin)

        # 16-23
        self.emergency_freq_menu_nb = QTableWidgetItem("16-23")
        self.emergency_freq_parm_name = QTableWidgetItem("EMERGENCY FREQ")

        self.emergency_freq_combo = QComboBox()
        self.emergency_freq_combo.setEditable(True)
        self.emergency_freq_combo.lineEdit().setReadOnly(True)
        self.emergency_freq_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.emergency_freq_combo.addItems([i for i in EMERGENCY_FREQ.keys()])
        format_combo(self.emergency_freq_combo)
        self.emergency_freq_combo.setCurrentIndex(0)
        self.emergency_freq_combo.currentTextChanged.connect(self.set_emergency_freq)

        self.menu_table.setItem(170, 0, self.emergency_freq_menu_nb)
        self.menu_table.setItem(170, 1, self.emergency_freq_parm_name)
        self.menu_table.setCellWidget(170, 2, self.emergency_freq_combo)

        # Table config
        for row in range(0, self.menu_table.rowCount()):
            try:
                self.menu_table.item(row, 0).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.menu_table.item(row, 0).setTextAlignment(Qt.AlignCenter)
                self.menu_table.item(row, 0).setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)

                self.menu_table.item(row, 1).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.menu_table.item(row, 1).setTextAlignment(Qt.AlignCenter)
                self.menu_table.item(row, 1).setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)

                self.menu_table.item(row, 2).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.menu_table.item(row, 2).setTextAlignment(Qt.AlignCenter)
                self.menu_table.item(row, 2).setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)

            except AttributeError:
                pass

        # ###### Memory tab
        self.memory_layout = QVBoxLayout()
        self.memory_tab.setLayout(self.memory_layout)

        self.memory_table = QTableWidget(99, 8)
        self.memory_layout.addWidget(self.memory_table)

        self.memory_table.verticalHeader().setVisible(True)
        self.memory_table.horizontalHeader().setVisible(True)
        self.memory_table.setSortingEnabled(False)
        self.memory_table.setAlternatingRowColors(True)
        self.memory_table.setHorizontalHeaderLabels(["Frequency", "Clarifier offset",
                                                     "CLAR state", "Mode", "CTCSS/DCS",
                                                     "RPT shift direction", "TAG state",
                                                     "TAG Name (max 12 chars ASCII)"])
        self.memory_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.memory_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.memory_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        self.memory_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        self.memory_table.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)
        self.memory_table.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeMode.Stretch)
        self.memory_table.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeMode.Stretch)
        self.memory_table.horizontalHeader().setSectionResizeMode(7, QHeaderView.ResizeMode.Stretch)

        regexp_freq = QRegExp(r"^\d{7,9}$")
        regexp_tag = QRegExp(r"^[ -~]{1,12}$")

        # Mem 001
        self.mem_1_freq_entry = QLineEdit("7000000")
        self.mem_1_freq_entry.setValidator(QRegExpValidator(regexp_freq))
        self.mem_1_freq_entry.setAlignment(Qt.AlignCenter)
        self.mem_1_clar_dir_spin = QSpinBox()
        self.mem_1_clar_dir_spin.setAlignment(Qt.AlignCenter)
        self.mem_1_clar_dir_spin.setMaximum(9999)
        self.mem_1_clar_dir_spin.setMinimum(-9999)
        self.mem_1_clar_state_combo = QComboBox()
        self.mem_1_clar_state_combo.setEditable(True)
        self.mem_1_clar_state_combo.lineEdit().setReadOnly(True)
        self.mem_1_clar_state_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.mem_1_clar_state_combo.addItems([i for i in CLAR_STATE.keys()])
        format_combo(self.mem_1_clar_state_combo)
        self.mem_1_mode_combo = QComboBox()
        self.mem_1_mode_combo.setEditable(True)
        self.mem_1_mode_combo.lineEdit().setReadOnly(True)
        self.mem_1_mode_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.mem_1_mode_combo.addItems(i for i in MODES.keys())
        format_combo(self.mem_1_mode_combo)
        self.mem_1_ctcss_dcs_state_combo = QComboBox()
        self.mem_1_ctcss_dcs_state_combo.setEditable(True)
        self.mem_1_ctcss_dcs_state_combo.lineEdit().setReadOnly(True)
        self.mem_1_ctcss_dcs_state_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.mem_1_ctcss_dcs_state_combo.addItems([i for i in CTCSS_STATE.keys()])
        format_combo(self.mem_1_ctcss_dcs_state_combo)
        self.mem_1_rpt_shift_dir_combo = QComboBox()
        self.mem_1_rpt_shift_dir_combo.setEditable(True)
        self.mem_1_rpt_shift_dir_combo.lineEdit().setReadOnly(True)
        self.mem_1_rpt_shift_dir_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.mem_1_rpt_shift_dir_combo.addItems([i for i in RPT_SHIFT_DIR.keys()])
        format_combo(self.mem_1_rpt_shift_dir_combo)
        self.mem_1_tag_state_combo = QComboBox()
        self.mem_1_tag_state_combo.setEditable(True)
        self.mem_1_tag_state_combo.lineEdit().setReadOnly(True)
        self.mem_1_tag_state_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.mem_1_tag_state_combo.addItems([i for i in TAG_STATE.keys()])
        format_combo(self.mem_1_tag_state_combo)
        self.mem_1_tag_entry = QLineEdit()
        self.mem_1_tag_entry.setValidator(QRegExpValidator(regexp_tag))
        self.mem_1_tag_entry.setAlignment(Qt.AlignCenter)

        self.memory_table.setCellWidget(0, 0, self.mem_1_freq_entry)
        self.memory_table.setCellWidget(0, 1, self.mem_1_clar_dir_spin)
        self.memory_table.setCellWidget(0, 2, self.mem_1_clar_state_combo)
        self.memory_table.setCellWidget(0, 3, self.mem_1_mode_combo)
        self.memory_table.setCellWidget(0, 4, self.mem_1_ctcss_dcs_state_combo)
        self.memory_table.setCellWidget(0, 5, self.mem_1_rpt_shift_dir_combo)
        self.memory_table.setCellWidget(0, 6, self.mem_1_tag_state_combo)
        self.memory_table.setCellWidget(0, 7, self.mem_1_tag_entry)

        # Mem 002
        self.mem_2_freq_entry = QLineEdit("")
        self.mem_2_freq_entry.setValidator(QRegExpValidator(regexp_freq))
        self.mem_2_freq_entry.setAlignment(Qt.AlignCenter)
        self.mem_2_clar_dir_spin = QSpinBox()
        self.mem_2_clar_dir_spin.setAlignment(Qt.AlignCenter)
        self.mem_2_clar_dir_spin.setMaximum(9999)
        self.mem_2_clar_dir_spin.setMinimum(-9999)
        self.mem_2_clar_state_combo = QComboBox()
        self.mem_2_clar_state_combo.setEditable(True)
        self.mem_2_clar_state_combo.lineEdit().setReadOnly(True)
        self.mem_2_clar_state_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.mem_2_clar_state_combo.addItems([i for i in CLAR_STATE.keys()])
        format_combo(self.mem_2_clar_state_combo)
        self.mem_2_mode_combo = QComboBox()
        self.mem_2_mode_combo.setEditable(True)
        self.mem_2_mode_combo.lineEdit().setReadOnly(True)
        self.mem_2_mode_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.mem_2_mode_combo.addItems(i for i in MODES.keys())
        format_combo(self.mem_2_mode_combo)
        self.mem_2_ctcss_dcs_state_combo = QComboBox()
        self.mem_2_ctcss_dcs_state_combo.setEditable(True)
        self.mem_2_ctcss_dcs_state_combo.lineEdit().setReadOnly(True)
        self.mem_2_ctcss_dcs_state_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.mem_2_ctcss_dcs_state_combo.addItems([i for i in CTCSS_STATE.keys()])
        format_combo(self.mem_2_ctcss_dcs_state_combo)
        self.mem_2_rpt_shift_dir_combo = QComboBox()
        self.mem_2_rpt_shift_dir_combo.setEditable(True)
        self.mem_2_rpt_shift_dir_combo.lineEdit().setReadOnly(True)
        self.mem_2_rpt_shift_dir_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.mem_2_rpt_shift_dir_combo.addItems([i for i in RPT_SHIFT_DIR.keys()])
        format_combo(self.mem_2_rpt_shift_dir_combo)
        self.mem_2_tag_state_combo = QComboBox()
        self.mem_2_tag_state_combo.setEditable(True)
        self.mem_2_tag_state_combo.lineEdit().setReadOnly(True)
        self.mem_2_tag_state_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.mem_2_tag_state_combo.addItems([i for i in TAG_STATE.keys()])
        format_combo(self.mem_2_tag_state_combo)
        self.mem_2_tag_entry = QLineEdit()
        self.mem_2_tag_entry.setValidator(QRegExpValidator(regexp_tag))
        self.mem_2_tag_entry.setAlignment(Qt.AlignCenter)

        self.memory_table.setCellWidget(1, 0, self.mem_2_freq_entry)
        self.memory_table.setCellWidget(1, 1, self.mem_2_clar_dir_spin)
        self.memory_table.setCellWidget(1, 2, self.mem_2_clar_state_combo)
        self.memory_table.setCellWidget(1, 3, self.mem_2_mode_combo)
        self.memory_table.setCellWidget(1, 4, self.mem_2_ctcss_dcs_state_combo)
        self.memory_table.setCellWidget(1, 5, self.mem_2_rpt_shift_dir_combo)
        self.memory_table.setCellWidget(1, 6, self.mem_2_tag_state_combo)
        self.memory_table.setCellWidget(1, 7, self.mem_2_tag_entry)

        # ###### PMS
        self.pms_layout = QVBoxLayout()
        self.pms_tab.setLayout(self.pms_layout)

        self.pms_table = QTableWidget(18, 8)
        self.pms_layout.addWidget(self.pms_table)

        self.pms_table.verticalHeader().setVisible(True)
        self.pms_table.horizontalHeader().setVisible(True)
        self.pms_table.setSortingEnabled(False)
        self.pms_table.setAlternatingRowColors(True)
        self.pms_table.setHorizontalHeaderLabels(["Frequency", "Clarifier offset",
                                                  "CLAR state", "Mode", "CTCSS/DCS",
                                                  "RPT shift direction", "TAG state",
                                                  "TAG Name (max 12 chars ASCII)"])
        self.pms_table.setVerticalHeaderLabels(["P1L", "P1U",
                                                "P2L", "P2U",
                                                "P3L", "P3U",
                                                "P4L", "P4U",
                                                "P5L", "P5U",
                                                "P6L", "P6U",
                                                "P7L", "P7U",
                                                "P8L", "P8U",
                                                "P9L", "P9U",])
        self.pms_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.pms_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.pms_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        self.pms_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        self.pms_table.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)
        self.pms_table.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeMode.Stretch)
        self.pms_table.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeMode.Stretch)
        self.pms_table.horizontalHeader().setSectionResizeMode(7, QHeaderView.ResizeMode.Stretch)

        regexp_freq = QRegExp(r"^\d{7,9}$")
        regexp_tag = QRegExp(r"^[ -~]{1,12}$")

        # Mem 001
        self.pms_1_freq_entry = QLineEdit("")
        self.pms_1_freq_entry.setValidator(QRegExpValidator(regexp_freq))
        self.pms_1_freq_entry.setAlignment(Qt.AlignCenter)
        self.pms_1_clar_dir_spin = QSpinBox()
        self.pms_1_clar_dir_spin.setAlignment(Qt.AlignCenter)
        self.pms_1_clar_dir_spin.setMaximum(9999)
        self.pms_1_clar_dir_spin.setMinimum(-9999)
        self.pms_1_clar_state_combo = QComboBox()
        self.pms_1_clar_state_combo.setEditable(True)
        self.pms_1_clar_state_combo.lineEdit().setReadOnly(True)
        self.pms_1_clar_state_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.pms_1_clar_state_combo.addItems([i for i in CLAR_STATE.keys()])
        format_combo(self.pms_1_clar_state_combo)
        self.pms_1_mode_combo = QComboBox()
        self.pms_1_mode_combo.setEditable(True)
        self.pms_1_mode_combo.lineEdit().setReadOnly(True)
        self.pms_1_mode_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.pms_1_mode_combo.addItems(i for i in MODES.keys())
        format_combo(self.pms_1_mode_combo)
        self.pms_1_ctcss_dcs_state_combo = QComboBox()
        self.pms_1_ctcss_dcs_state_combo.setEditable(True)
        self.pms_1_ctcss_dcs_state_combo.lineEdit().setReadOnly(True)
        self.pms_1_ctcss_dcs_state_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.pms_1_ctcss_dcs_state_combo.addItems([i for i in CTCSS_STATE.keys()])
        format_combo(self.pms_1_ctcss_dcs_state_combo)
        self.pms_1_rpt_shift_dir_combo = QComboBox()
        self.pms_1_rpt_shift_dir_combo.setEditable(True)
        self.pms_1_rpt_shift_dir_combo.lineEdit().setReadOnly(True)
        self.pms_1_rpt_shift_dir_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.pms_1_rpt_shift_dir_combo.addItems([i for i in RPT_SHIFT_DIR.keys()])
        format_combo(self.pms_1_rpt_shift_dir_combo)
        self.pms_1_tag_state_combo = QComboBox()
        self.pms_1_tag_state_combo.setEditable(True)
        self.pms_1_tag_state_combo.lineEdit().setReadOnly(True)
        self.pms_1_tag_state_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.pms_1_tag_state_combo.addItems([i for i in TAG_STATE.keys()])
        format_combo(self.pms_1_tag_state_combo)
        self.pms_1_tag_entry = QLineEdit()
        self.pms_1_tag_entry.setValidator(QRegExpValidator(regexp_tag))
        self.pms_1_tag_entry.setAlignment(Qt.AlignCenter)

        self.pms_table.setCellWidget(0, 0, self.pms_1_freq_entry)
        self.pms_table.setCellWidget(0, 1, self.pms_1_clar_dir_spin)
        self.pms_table.setCellWidget(0, 2, self.pms_1_clar_state_combo)
        self.pms_table.setCellWidget(0, 3, self.pms_1_mode_combo)
        self.pms_table.setCellWidget(0, 4, self.pms_1_ctcss_dcs_state_combo)
        self.pms_table.setCellWidget(0, 5, self.pms_1_rpt_shift_dir_combo)
        self.pms_table.setCellWidget(0, 6, self.pms_1_tag_state_combo)
        self.pms_table.setCellWidget(0, 7, self.pms_1_tag_entry)

    def send_config_2_radio(self):
        """Send the config to the Radio"""
        self.transfert = True

        self.progressbar = QProgressBar(self)
        self.status_bar.addWidget(self.progressbar, 1)
        self.progressbar.setMaximum(155)
        self.progressbar.setValue(0)

        self.set_acg_fast_delay()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_acg_mid_delay()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_acg_slow_delay()
        self.progressbar.setValue(self.progressbar.value() + 1)

        self.set_lcd_contrast()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_dimmer_backlit()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_dimmer_lcd()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_dimmer_tx_busy()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_peak_hold()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_zin_led()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_pop_up_menu()
        self.progressbar.setValue(self.progressbar.value() + 1)

        self.set_dvs_rx_out_lvl()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_dvs_tx_out_lvl()
        self.progressbar.setValue(self.progressbar.value() + 1)

        self.set_keyer_type()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_keyer_dot_dash()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_cw_weight()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_beacon_interval()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_number_style()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_contest_number()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_cw_memory_1()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_cw_memory_2()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_cw_memory_3()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_cw_memory_4()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_cw_memory_5()
        self.progressbar.setValue(self.progressbar.value() + 1)

        self.set_nb_width()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_nb_rejection()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_nb_level()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_beep_level()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_rf_sql_vr()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_cat_rate()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_cat_tot()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_cat_rts()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_mem_group()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_fm_setting()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_rec_setting()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_atas_setting()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_quick_spl_freq()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_tx_tot()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_mic_scan()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_mic_scan_resume()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_ref_freq_adj()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_clar_select()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_apo()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_fan_control()
        self.progressbar.setValue(self.progressbar.value() + 1)

        self.set_am_lcut_freq()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_am_lcut_slope()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_am_hcut_freq()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_am_hcut_slope()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_am_mic_select()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_am_out_level()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_am_ptt_select()
        self.progressbar.setValue(self.progressbar.value() + 1)

        self.set_cw_lcut_freq()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_cw_lcut_slope()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_cw_hcut_freq()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_cw_hcut_slope()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_cw_out_level()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_cw_auto_mode()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_cw_bfo()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_cw_bk_in_type()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_cw_bk_in_delay()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_cw_wave_shape()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_cw_freq_display()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_pc_keying()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_qsk_delay_time()
        self.progressbar.setValue(self.progressbar.value() + 1)

        self.set_data_mode()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_psk_tone()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_other_disp()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_other_shift()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_data_lcut_freq()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_data_lcut_slope()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_data_hcut_freq()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_data_hcut_slope()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_data_in_select()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_data_ptt_select()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_data_out_level()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_data_bfo()
        self.progressbar.setValue(self.progressbar.value() + 1)

        self.set_fm_mic_select()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_fm_out_level()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_pkt_ptt_select()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_rpt_shift_28()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_rpt_shift_50()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_dcs_polarity()
        self.progressbar.setValue(self.progressbar.value() + 1)

        self.set_rtty_lcut_freq()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_rtty_lcut_slope()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_rtty_hcut_freq()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_rtty_hcut_slope()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_rtty_shift_port()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_rtty_polarity_r()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_rtty_polarity_t()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_rtty_out_level()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_rtty_shift_freq()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_rtty_mark_freq()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_rtty_bfo()
        self.progressbar.setValue(self.progressbar.value() + 1)

        self.set_ssb_lcut_freq()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_ssb_lcut_slope()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_ssb_hcut_freq()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_ssb_hcut_slope()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_ssb_mic_select()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_ssb_out_level()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_ssb_bfo()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_ssb_ptt_select()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_ssb_tx_bpf()
        self.progressbar.setValue(self.progressbar.value() + 1)

        self.set_apf_width()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_contour_level()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_contour_width()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_if_notch_width()
        self.progressbar.setValue(self.progressbar.value() + 1)

        self.set_scp_start_cycle()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_scp_span_freq()
        self.progressbar.setValue(self.progressbar.value() + 1)

        self.set_quick_dial()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_ssb_dial_step()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_am_dial_step()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_fm_dial_step()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_dial_step()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_am_ch_step()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_fm_ch_step()
        self.progressbar.setValue(self.progressbar.value() + 1)

        self.set_eq_1_freq()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_eq_1_level()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_eq_1_bwth()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_eq_2_freq()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_eq_2_level()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_eq_2_bwth()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_eq_3_freq()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_eq_3_level()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_eq_3_bwth()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_p_eq_1_freq()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_p_eq_1_level()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_p_eq_1_bwth()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_p_eq_2_freq()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_p_eq_2_level()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_p_eq_2_bwth()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_p_eq_3_freq()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_p_eq_3_level()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_p_eq_3_bwth()
        self.progressbar.setValue(self.progressbar.value() + 1)

        self.set_hf_ssb_pwr()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_hf_am_pwr()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_hf_pwr()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_50m_ssb_pwr()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_50m_am_pwr()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_50m_pwr()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_ssb_mic_gain()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_am_mic_gain()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_fm_mic_gain()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_data_mic_gain()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_ssb_data_gain()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_am_data_gain()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_fm_data_gain()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_data_data_gain()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_tuner_select()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_vox_select()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_vox_gain()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_vox_delay()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_anti_vox_gain()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_data_vox_gain()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_data_vox_delay()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_anti_dvox_gain()
        self.progressbar.setValue(self.progressbar.value() + 1)
        self.set_emergency_freq()
        self.progressbar.setValue(self.progressbar.value() + 1)

        self.status_bar.removeWidget(self.progressbar)
        self.status_bar.showMessage("Done")
        self.transfert = False

    def get_config_from_radio(self):
        self.transfert = True

        self.progressbar = QProgressBar(self)
        self.status_bar.addWidget(self.progressbar, 1)
        self.progressbar.setMaximum(155)
        self.progressbar.setValue(0)

        self.get_acg_fast_delay()
        self.progressbar.setValue(1)
        self.get_acg_mid_delay()
        self.progressbar.setValue(2)
        self.get_acg_slow_delay()
        self.progressbar.setValue(3)

        self.get_lcd_contrast()
        self.progressbar.setValue(4)
        self.get_dimmer_backlit()
        self.progressbar.setValue(5)
        self.get_dimmer_lcd()
        self.progressbar.setValue(6)
        self.get_dimmer_tx_busy()
        self.progressbar.setValue(7)
        self.get_peak_hold()
        self.progressbar.setValue(8)
        self.get_zin_led()
        self.progressbar.setValue(9)
        self.get_pop_up_menu()
        self.progressbar.setValue(10)

        self.get_dvs_rx_out_lvl()
        self.progressbar.setValue(11)
        self.get_dvs_tx_out_lvl()
        self.progressbar.setValue(12)

        self.get_keyer_type()
        self.progressbar.setValue(13)
        self.get_keyer_dot_dash()
        self.progressbar.setValue(14)
        self.get_cw_weight()
        self.progressbar.setValue(15)
        self.get_beacon_interval()
        self.progressbar.setValue(16)
        self.get_number_style()
        self.progressbar.setValue(17)
        self.get_contest_number()
        self.progressbar.setValue(18)
        self.get_cw_memory_1()
        self.progressbar.setValue(19)
        self.get_cw_memory_2()
        self.progressbar.setValue(20)
        self.get_cw_memory_3()
        self.progressbar.setValue(21)
        self.get_cw_memory_4()
        self.progressbar.setValue(22)
        self.get_cw_memory_5()
        self.progressbar.setValue(23)

        self.get_nb_width()
        self.progressbar.setValue(24)
        self.get_nb_rejection()
        self.progressbar.setValue(25)
        self.get_nb_level()
        self.progressbar.setValue(26)
        self.get_beep_level()
        self.progressbar.setValue(27)
        self.get_rf_sql_vr()
        self.progressbar.setValue(28)
        self.get_cat_rate()
        self.progressbar.setValue(29)
        self.get_cat_tot()
        self.progressbar.setValue(30)
        self.get_cat_rts()
        self.progressbar.setValue(31)
        self.get_mem_group()
        self.progressbar.setValue(32)
        self.get_fm_setting()
        self.progressbar.setValue(33)
        self.get_rec_setting()
        self.progressbar.setValue(34)
        self.get_atas_setting()
        self.progressbar.setValue(35)
        self.get_quick_spl_freq()
        self.progressbar.setValue(36)
        self.get_tx_tot()
        self.progressbar.setValue(37)
        self.get_mic_scan()
        self.progressbar.setValue(38)
        self.get_mic_scan_resume()
        self.progressbar.setValue(39)
        self.get_ref_freq_adj()
        self.progressbar.setValue(40)
        self.get_clar_select()
        self.progressbar.setValue(41)
        self.get_apo()
        self.progressbar.setValue(42)
        self.get_fan_control()
        self.progressbar.setValue(43)

        self.get_am_lcut_freq()
        self.progressbar.setValue(44)
        self.get_am_lcut_slope()
        self.progressbar.setValue(45)
        self.get_am_hcut_freq()
        self.progressbar.setValue(46)
        self.get_am_hcut_slope()
        self.progressbar.setValue(47)
        self.get_am_mic_select()
        self.progressbar.setValue(48)
        self.get_am_out_level()
        self.progressbar.setValue(49)
        self.get_am_ptt_select()
        self.progressbar.setValue(50)

        self.get_cw_lcut_freq()
        self.progressbar.setValue(51)
        self.get_cw_lcut_slope()
        self.progressbar.setValue(52)
        self.get_cw_hcut_freq()
        self.progressbar.setValue(53)
        self.get_cw_hcut_slope()
        self.progressbar.setValue(54)
        self.get_cw_out_level()
        self.progressbar.setValue(55)
        self.get_cw_auto_mode()
        self.progressbar.setValue(56)
        self.get_cw_bfo()
        self.progressbar.setValue(57)
        self.get_cw_bk_in_type()
        self.progressbar.setValue(58)
        self.get_cw_bk_in_delay()
        self.progressbar.setValue(59)
        self.get_cw_wave_shape()
        self.progressbar.setValue(60)
        self.get_cw_freq_display()
        self.progressbar.setValue(61)
        self.get_pc_keying()
        self.progressbar.setValue(62)
        self.get_qsk_delay_time()
        self.progressbar.setValue(63)

        self.get_data_mode()
        self.progressbar.setValue(64)
        self.get_psk_tone()
        self.progressbar.setValue(65)
        self.get_other_disp()
        self.progressbar.setValue(66)
        self.get_other_shift()
        self.progressbar.setValue(67)
        self.get_data_lcut_freq()
        self.progressbar.setValue(68)
        self.get_data_lcut_slope()
        self.progressbar.setValue(69)
        self.get_data_hcut_freq()
        self.progressbar.setValue(70)
        self.get_data_hcut_slope()
        self.progressbar.setValue(71)
        self.get_data_in_select()
        self.progressbar.setValue(72)
        self.get_data_ptt_select()
        self.progressbar.setValue(73)
        self.get_data_out_level()
        self.progressbar.setValue(74)
        self.get_data_bfo()
        self.progressbar.setValue(75)

        self.get_fm_mic_select()
        self.progressbar.setValue(76)
        self.get_fm_out_level()
        self.progressbar.setValue(77)
        self.get_pkt_ptt_select()
        self.progressbar.setValue(78)
        self.get_rpt_shift_28()
        self.progressbar.setValue(79)
        self.get_rpt_shift_50()
        self.progressbar.setValue(80)
        self.get_dcs_polarity()
        self.progressbar.setValue(81)

        self.get_rtty_lcut_freq()
        self.progressbar.setValue(82)
        self.get_rtty_lcut_slope()
        self.progressbar.setValue(83)
        self.get_rtty_hcut_freq()
        self.progressbar.setValue(84)
        self.get_rtty_hcut_slope()
        self.progressbar.setValue(85)
        self.get_rtty_shift_port()
        self.progressbar.setValue(86)
        self.get_rtty_polarity_r()
        self.progressbar.setValue(87)
        self.get_rtty_polarity_t()
        self.progressbar.setValue(88)
        self.get_rtty_out_level()
        self.progressbar.setValue(89)
        self.get_rtty_shift_freq()
        self.progressbar.setValue(90)
        self.get_rtty_mark_freq()
        self.progressbar.setValue(91)
        self.get_rtty_bfo()
        self.progressbar.setValue(92)

        self.get_ssb_lcut_freq()
        self.progressbar.setValue(93)
        self.get_ssb_lcut_slope()
        self.progressbar.setValue(94)
        self.get_ssb_hcut_freq()
        self.progressbar.setValue(95)
        self.get_ssb_hcut_slope()
        self.progressbar.setValue(96)
        self.get_ssb_mic_select()
        self.progressbar.setValue(97)
        self.get_ssb_out_level()
        self.progressbar.setValue(98)
        self.get_ssb_bfo()
        self.progressbar.setValue(99)
        self.get_ssb_ptt_select()
        self.progressbar.setValue(100)
        self.get_ssb_tx_bpf()
        self.progressbar.setValue(101)

        self.get_apf_width()
        self.progressbar.setValue(102)
        self.get_contour_level()
        self.progressbar.setValue(103)
        self.get_contour_width()
        self.progressbar.setValue(104)
        self.get_if_notch_width()
        self.progressbar.setValue(105)

        self.get_scp_start_cycle()
        self.progressbar.setValue(106)
        self.get_scp_span_freq()
        self.progressbar.setValue(107)

        self.get_quick_dial()
        self.progressbar.setValue(108)
        self.get_ssb_dial_step()
        self.progressbar.setValue(109)
        self.get_am_dial_step()
        self.progressbar.setValue(110)
        self.get_fm_dial_step()
        self.progressbar.setValue(111)
        self.get_dial_step()
        self.progressbar.setValue(112)
        self.get_am_ch_step()
        self.progressbar.setValue(113)
        self.get_fm_ch_step()
        self.progressbar.setValue(114)

        self.get_eq_1_freq()
        self.progressbar.setValue(115)
        self.get_eq_1_level()
        self.progressbar.setValue(116)
        self.get_eq_1_bwth()
        self.progressbar.setValue(117)
        self.get_eq_2_freq()
        self.progressbar.setValue(118)
        self.get_eq_2_level()
        self.progressbar.setValue(119)
        self.get_eq_2_bwth()
        self.progressbar.setValue(120)
        self.get_eq_3_freq()
        self.progressbar.setValue(121)
        self.get_eq_3_level()
        self.progressbar.setValue(122)
        self.get_eq_3_bwth()
        self.progressbar.setValue(123)
        self.get_p_eq_1_freq()
        self.progressbar.setValue(124)
        self.get_p_eq_1_level()
        self.progressbar.setValue(125)
        self.get_p_eq_1_bwth()
        self.progressbar.setValue(126)
        self.get_p_eq_2_freq()
        self.progressbar.setValue(127)
        self.get_p_eq_2_level()
        self.progressbar.setValue(128)
        self.get_p_eq_2_bwth()
        self.progressbar.setValue(129)
        self.get_p_eq_3_freq()
        self.progressbar.setValue(130)
        self.get_p_eq_3_level()
        self.progressbar.setValue(131)
        self.get_p_eq_3_bwth()
        self.progressbar.setValue(132)

        self.get_hf_ssb_pwr()
        self.progressbar.setValue(133)
        self.get_hf_am_pwr()
        self.progressbar.setValue(134)
        self.get_hf_pwr()
        self.progressbar.setValue(135)
        self.get_50m_ssb_pwr()
        self.progressbar.setValue(136)
        self.get_50m_am_pwr()
        self.progressbar.setValue(137)
        self.get_50m_pwr()
        self.progressbar.setValue(138)
        self.get_ssb_mic_gain()
        self.progressbar.setValue(139)
        self.get_am_mic_gain()
        self.progressbar.setValue(140)
        self.get_fm_mic_gain()
        self.progressbar.setValue(141)
        self.get_data_mic_gain()
        self.progressbar.setValue(142)
        self.get_ssb_data_gain()
        self.progressbar.setValue(143)
        self.get_am_data_gain()
        self.progressbar.setValue(144)
        self.get_fm_data_gain()
        self.progressbar.setValue(145)
        self.get_data_data_gain()
        self.progressbar.setValue(146)
        self.get_tuner_select()
        self.progressbar.setValue(147)
        self.get_vox_select()
        self.progressbar.setValue(148)
        self.get_vox_gain()
        self.progressbar.setValue(149)
        self.get_vox_delay()
        self.progressbar.setValue(150)
        self.get_anti_vox_gain()
        self.progressbar.setValue(151)
        self.get_data_vox_gain()
        self.progressbar.setValue(152)
        self.get_data_vox_delay()
        self.progressbar.setValue(153)
        self.get_anti_dvox_gain()
        self.progressbar.setValue(154)
        self.get_emergency_freq()
        self.progressbar.setValue(155)

        self.status_bar.removeWidget(self.progressbar)
        self.status_bar.showMessage("Done")
        if not self.live_mode_action.isChecked():
            self.transfert = False

    def toggle_live_mode(self):
        """Toggle Live Mode"""
        if self.transfert:
            self.live_mode_action.setChecked(False)
            self.transfert = False
            self.send_to_radio_action.setEnabled(True)
        else:
            self.live_mode_action.setChecked(True)
            self.transfert = True
            self.send_to_radio_action.setDisabled(True)

    def set_acg_fast_delay(self):
        """Set ACG FAST DELAY"""
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.acg_fast_spin.value())
                while len(value) < 4:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0101" + value + b";"
                self.rig.write(cmd)

    def get_acg_fast_delay(self):
        """Get ACG FAST DELAY"""
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0101;")
                resp = self.rig.read_until(b";")
                resp = resp.decode(ENCODER)
                resp = resp.replace(";", "")
                self.acg_fast_spin.setValue(int(resp[6:]))

    def set_acg_mid_delay(self):
        """Set ACG MID DELAY"""
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.acg_mid_spin.value())
                while len(value) < 4:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0102" + value + b";"
                self.rig.write(cmd)

    def get_acg_mid_delay(self):
        """Get ACG MID DELAY"""
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0102;")
                resp = self.rig.read_until(b";")
                resp = resp.decode(ENCODER)
                resp = resp.replace(";", "")
                self.acg_mid_spin.setValue(int(resp[6:]))

    def set_acg_slow_delay(self):
        """Set ACG SLOW DELAY"""
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.acg_slow_spin.value())
                while len(value) < 4:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0103" + value + b";"
                self.rig.write(cmd)

    def get_acg_slow_delay(self):
        """Get ACG MID DELAY"""
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0103;")
                resp = self.rig.read_until(b";")
                resp = resp.decode(ENCODER)
                resp = resp.replace(";", "")
                self.acg_slow_spin.setValue(int(resp[6:]))

    def set_lcd_contrast(self):
        """Set LCD CONTRAST"""
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.lcd_contrast_spin.value())
                while len(value) < 2:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0201" + value + b";"
                self.rig.write(cmd)

    def get_lcd_contrast(self):
        """Get ACG MID DELAY"""
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0201;")
                resp = self.rig.read_until(b";")
                resp = resp.decode(ENCODER)
                resp = resp.replace(";", "")
                self.lcd_contrast_spin.setValue(int(resp[6:]))

    def set_dimmer_backlit(self):
        """Set DIMMER BACKLIT"""
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.dimmer_backlit_spin.value())
                while len(value) < 2:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0202" + value + b";"
                self.rig.write(cmd)

    def get_dimmer_backlit(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0202;")
                resp = self.rig.read_until(b";")
                resp = resp.decode(ENCODER)
                resp = resp.replace(";", "")
                self.dimmer_backlit_spin.setValue(int(resp[6:]))

    def set_dimmer_lcd(self):
        """Set DIMMER LCD"""
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.dimmer_lcd_spin.value())
                while len(value) < 2:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0203" + value + b";"
                self.rig.write(cmd)

    def get_dimmer_lcd(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0203;")
                resp = self.rig.read_until(b";")
                resp = resp.decode(ENCODER)
                resp = resp.replace(";", "")
                self.dimmer_lcd_spin.setValue(int(resp[6:]))

    def set_dimmer_tx_busy(self):
        """Set DIMMER TX/BUSY"""
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.dimmer_tx_busy_spin.value())
                while len(value) < 2:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0204" + value + b";"
                self.rig.write(cmd)

    def get_dimmer_tx_busy(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0204;")
                resp = self.rig.read_until(b";")
                resp = resp.decode(ENCODER)
                resp = resp.replace(";", "")
                self.dimmer_tx_busy_spin.setValue(int(resp[6:]))

    def set_peak_hold(self):
        """Set PEAK HOLD"""
        if self.rig.isOpen():
            if self.transfert:
                value = PEAK_HOLD[self.peak_hold_combo.currentText()]
                cmd = b"EX0205" + value + b";"
                self.rig.write(cmd)

    def get_peak_hold(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0205;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_peak_old = {value: key for key, value in PEAK_HOLD.items()}
                self.peak_hold_combo.setCurrentText(rev_peak_old[resp[6:]])

    def set_zin_led(self):
        """Set ZIN LED"""
        if self.rig.isOpen():
            if self.transfert:
                value = ZIN_LED[self.zin_led_combo.currentText()]
                cmd = b"EX0206" + value + b";"
                self.rig.write(cmd)

    def get_zin_led(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0206;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_zin_led = {value: key for key, value in ZIN_LED.items()}
                self.zin_led_combo.setCurrentText(rev_zin_led[resp[6:]])

    def set_pop_up_menu(self):
        """Set POP-UP MENU"""
        if self.rig.isOpen():
            if self.transfert:
                value = POPUP_MENU[self.pop_up_combo.currentText()]
                cmd = b"EX0207" + value + b";"
                self.rig.write(cmd)

    def get_pop_up_menu(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0207;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_pop_up_menu = {value: key for key, value in POPUP_MENU.items()}
                self.pop_up_combo.setCurrentText(rev_pop_up_menu[resp[6:]])

    def set_dvs_rx_out_lvl(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.dvs_rx_out_lvl_spin.value())
                while len(value) < 3:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0301" + value + b";"
                self.rig.write(cmd)

    def get_dvs_rx_out_lvl(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0301;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.dvs_rx_out_lvl_spin.setValue(int(resp[6:]))

    def set_dvs_tx_out_lvl(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.dvs_tx_out_lvl_spin.value())
                while len(value) < 3:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0302" + value + b";"
                self.rig.write(cmd)

    def get_dvs_tx_out_lvl(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0302;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.dvs_tx_out_lvl_spin.setValue(int(resp[6:]))

    def set_keyer_type(self):
        if self.rig.isOpen():
            if self.transfert:
                value = KEYER_TYPE[self.keyer_type_combo.currentText()]
                cmd = b"EX0401" + value + b";"
                self.rig.write(cmd)

    def get_keyer_type(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0401;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_keyer_type = {value: key for key, value in KEYER_TYPE.items()}
                self.keyer_type_combo.setCurrentText(rev_keyer_type[resp[6:]])

    def set_keyer_dot_dash(self):
        if self.rig.isOpen():
            if self.transfert:
                value = KEYER_DOT_DASH[self.keyer_dot_dash_combo.currentText()]
                cmd = b"EX0402" + value + b";"
                self.rig.write(cmd)

    def get_keyer_dot_dash(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0402;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_keyer_dot_dat = {value: key for key, value in KEYER_DOT_DASH.items()}
                self.keyer_dot_dash_combo.setCurrentText(rev_keyer_dot_dat[resp[6:]])

    def set_cw_weight(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(round(self.cw_weight_spin.value(), 1))
                value = value.replace(".", "")
                value = bytes(value, ENCODER)
                cmd = b"EX0403" + value + b";"
                self.rig.write(cmd)

    def get_cw_weight(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0403;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                resp = resp[6:]
                resp = resp[0] + "." + resp[1]
                self.cw_weight_spin.setValue(float(resp))

    def set_beacon_interval(self):
        """Set BEACON INTERVAL"""
        if self.old_beacon_interval == 240 and self.beacon_interval_spin.value() == 241:
            self.beacon_interval_spin.setSingleStep(30)
            self.beacon_interval_spin.setValue(270)
        elif self.old_beacon_interval == 240 and self.beacon_interval_spin.value() == 210:
            self.beacon_interval_spin.setSingleStep(1)
            self.beacon_interval_spin.setValue(239)

        self.old_beacon_interval = self.beacon_interval_spin.value()

        if self.rig.isOpen():
            if self.transfert:
                value = str(self.beacon_interval_spin.value())

                if value == "270":
                    value = "241"
                elif value == "300":
                    value = "242"
                elif value == "330":
                    value = "243"
                elif value == "360":
                    value = "244"
                elif value == "390":
                    value = "245"
                elif value == "420":
                    value = "246"
                elif value == "450":
                    value = "247"
                elif value == "480":
                    value = "248"
                elif value == "510":
                    value = "249"
                elif value == "540":
                    value = "250"
                elif value == "570":
                    value = "251"
                elif value == "600":
                    value = "252"
                elif value == "630":
                    value = "253"
                elif value == "660":
                    value = "254"
                elif value == "690":
                    value = "255"

                while len(value) < 3:
                    value = "0" + value
                cmd = b"EX0404" + bytes(value, ENCODER) + b";"
                self.rig.write(cmd)

    def get_beacon_interval(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0404;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                resp = resp[6:]

                if resp == "241":
                    resp = "270"
                elif resp == "242":
                    resp = "300"
                elif resp == "243":
                    resp = "330"
                elif resp == "244":
                    resp = "360"
                elif resp == "245":
                    resp = "390"
                elif resp == "246":
                    resp = "420"
                elif resp == "247":
                    resp = "450"
                elif resp == "248":
                    resp = "480"
                elif resp == "249":
                    resp = "510"
                elif resp == "250":
                    resp = "540"
                elif resp == "251":
                    resp = "570"
                elif resp == "252":
                    resp = "600"
                elif resp == "253":
                    resp = "630"
                elif resp == "254":
                    resp = "660"
                elif resp == "255":
                    resp = "690"

                self.beacon_interval_spin.setValue(int(resp))

    def set_number_style(self):
        if self.rig.isOpen():
            if self.transfert:
                value = NUMBER_STYLE[self.number_style_combo.currentText()]
                cmd = b"EX0405" + value + b";"
                self.rig.write(cmd)

    def get_number_style(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0405;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_number_style = {value: key for key, value in NUMBER_STYLE.items()}
                self.number_style_combo.setCurrentText(rev_number_style[resp[6:]])

    def set_contest_number(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.contest_number_spin.value())
                while len(value) < 4:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0406" + value + b";"
                self.rig.write(cmd)

    def get_contest_number(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0406;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.contest_number_spin.setValue(int(resp[6:]))

    def set_cw_memory_1(self):
        if self.rig.isOpen():
            if self.transfert:
                value = CW_MEMORY[self.cw_memory_1_combo.currentText()]
                cmd = b"EX0407" + value + b";"
                self.rig.write(cmd)

    def get_cw_memory_1(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0407;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_cw_memory = {value: key for key, value in CW_MEMORY.items()}
                self.cw_memory_1_combo.setCurrentText(rev_cw_memory[resp[6:]])

    def set_cw_memory_2(self):
        if self.rig.isOpen():
            if self.transfert:
                value = CW_MEMORY[self.cw_memory_2_combo.currentText()]
                cmd = b"EX0408" + value + b";"
                self.rig.write(cmd)

    def get_cw_memory_2(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0408;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_cw_memory = {value: key for key, value in CW_MEMORY.items()}
                self.cw_memory_2_combo.setCurrentText(rev_cw_memory[resp[6:]])

    def set_cw_memory_3(self):
        if self.rig.isOpen():
            if self.transfert:
                value = CW_MEMORY[self.cw_memory_3_combo.currentText()]
                cmd = b"EX0409" + value + b";"
                self.rig.write(cmd)

    def get_cw_memory_3(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0409;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_cw_memory = {value: key for key, value in CW_MEMORY.items()}
                self.cw_memory_3_combo.setCurrentText(rev_cw_memory[resp[6:]])

    def set_cw_memory_4(self):
        if self.rig.isOpen():
            if self.transfert:
                value = CW_MEMORY[self.cw_memory_4_combo.currentText()]
                cmd = b"EX0410" + value + b";"
                self.rig.write(cmd)

    def get_cw_memory_4(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0410;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_cw_memory = {value: key for key, value in CW_MEMORY.items()}
                self.cw_memory_4_combo.setCurrentText(rev_cw_memory[resp[6:]])

    def set_cw_memory_5(self):
        if self.rig.isOpen():
            if self.transfert:
                value = CW_MEMORY[self.cw_memory_5_combo.currentText()]
                cmd = b"EX0411" + value + b";"
                self.rig.write(cmd)

    def get_cw_memory_5(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0411;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_cw_memory = {value: key for key, value in CW_MEMORY.items()}
                self.cw_memory_5_combo.setCurrentText(rev_cw_memory[resp[6:]])

    def set_nb_width(self):
        if self.rig.isOpen():
            if self.transfert:
                value = NB_WIDHT[self.nb_width_combo.currentText()]
                cmd = b"EX0501" + value + b";"
                self.rig.write(cmd)

    def get_nb_width(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0501;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_nb_width = {value: key for key, value in NB_WIDHT.items()}
                self.nb_width_combo.setCurrentText(rev_nb_width[resp[6:]])

    def set_nb_rejection(self):
        if self.rig.isOpen():
            if self.transfert:
                value = NB_REJECTION[self.nb_rejection_combo.currentText()]
                cmd = b"EX0502" + value + b";"
                self.rig.write(cmd)

    def get_nb_rejection(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0502;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_nb_rejection = {value: key for key, value in NB_REJECTION.items()}
                self.nb_rejection_combo.setCurrentText(rev_nb_rejection[resp[6:]])

    def set_nb_level(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.nb_level_spin.value())
                while len(value) < 2:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0503" + value + b";"
                self.rig.write(cmd)

    def get_nb_level(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0503;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.nb_level_spin.setValue(int(resp[6:]))

    def set_beep_level(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.beep_level_spin.value())
                while len(value) < 3:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0504" + value + b";"
                self.rig.write(cmd)

    def get_beep_level(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0504;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.beep_level_spin.setValue(int(resp[6:]))

    def set_rf_sql_vr(self):
        if self.rig.isOpen():
            if self.transfert:
                value = RF_SQL_VR[self.rf_sql_vr_combo.currentText()]
                cmd = b"EX0505" + value + b";"
                self.rig.write(cmd)

    def get_rf_sql_vr(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0505;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_rf_sql_vr = {value: key for key, value in RF_SQL_VR.items()}
                self.rf_sql_vr_combo.setCurrentText(rev_rf_sql_vr[resp[6:]])

    def set_cat_rate(self):
        if self.rig.isOpen():
            if self.transfert:
                """value = CAT_RATE[self.cat_rate_combo.currentText()]
                cmd = b"EX0506" + value + b";"
                self.rig.write(cmd)"""
                pass

    def get_cat_rate(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0506;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_cat_rate = {value: key for key, value in CAT_RATE.items()}
                self.cat_rate_combo.setCurrentText(rev_cat_rate[resp[6:]])

    def set_cat_tot(self):
        if self.rig.isOpen():
            if self.transfert:
                value = CAT_TOT[self.cat_tot_combo.currentText()]
                cmd = b"EX0507" + value + b";"
                self.rig.write(cmd)

    def get_cat_tot(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0507;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_cat_tot = {value: key for key, value in CAT_TOT.items()}
                self.cat_tot_combo.setCurrentText(rev_cat_tot[resp[6:]])

    def set_cat_rts(self):
        if self.rig.isOpen():
            if self.transfert:
                value = CAT_RTS[self.cat_rts_combo.currentText()]
                cmd = b"EX0508" + value + b";"
                self.rig.write(cmd)

    def get_cat_rts(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0508;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_cat_rts = {value: key for key, value in CAT_RTS.items()}
                self.cat_rts_combo.setCurrentText(rev_cat_rts[resp[6:]])

    def set_mem_group(self):
        if self.rig.isOpen():
            if self.transfert:
                value = MEMORY_GROUP[self.meme_group_combo.currentText()]
                cmd = b"EX0509" + value + b";"
                self.rig.write(cmd)

    def get_mem_group(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0509;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_mem_group = {value: key for key, value in MEMORY_GROUP.items()}
                self.meme_group_combo.setCurrentText(rev_mem_group[resp[6:]])

    def set_fm_setting(self):
        if self.rig.isOpen():
            if self.transfert:
                value = FM_SETTING[self.fm_setting_combo.currentText()]
                cmd = b"EX0510" + value + b";"
                self.rig.write(cmd)

    def get_fm_setting(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0510;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_fm_setting = {value: key for key, value in FM_SETTING.items()}
                self.fm_setting_combo.setCurrentText(rev_fm_setting[resp[6:]])

    def set_rec_setting(self):
        if self.rig.isOpen():
            if self.transfert:
                value = REC_SETTING[self.rec_setting_combo.currentText()]
                cmd = b"EX0511" + value + b";"
                self.rig.write(cmd)

    def get_rec_setting(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0511;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_rec_setting = {value: key for key, value in REC_SETTING.items()}
                self.rec_setting_combo.setCurrentText(rev_rec_setting[resp[6:]])

    def set_atas_setting(self):
        if self.rig.isOpen():
            if self.transfert:
                value = ATAS_SETTING[self.atas_setting_combo.currentText()]
                cmd = b"EX0512" + value + b";"
                self.rig.write(cmd)

    def get_atas_setting(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0512;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_atas_setting = {value: key for key, value in ATAS_SETTING.items()}
                self.atas_setting_combo.setCurrentText(rev_atas_setting[resp[6:]])

    def set_quick_spl_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.quick_spl_freq_spin.value())

                if -10 < self.quick_spl_freq_spin.value() < 0:
                    value = value[0] + "0" + value[1]
                elif 0 <= self.quick_spl_freq_spin.value() < 10:
                    value = "+0" + value[0]
                elif self.quick_spl_freq_spin.value() >= 10:
                    value = "+" + value

                value = bytes(value, ENCODER)
                cmd = b"EX0513" + value + b";"
                self.rig.write(cmd)

    def get_quick_spl_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0513;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.quick_spl_freq_spin.setValue(int(resp[6:]))

    def set_tx_tot(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.tx_tot_spin.value())
                while len(value) < 2:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0514" + value + b";"
                self.rig.write(cmd)

    def get_tx_tot(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0514;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.tx_tot_spin.setValue(int(resp[6:]))

    def set_mic_scan(self):
        if self.rig.isOpen():
            if self.transfert:
                value = MIC_SCAN[self.mic_scan_combo.currentText()]
                cmd = b"EX0515" + value + b";"
                self.rig.write(cmd)

    def get_mic_scan(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0515;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_mic_scan = {value: key for key, value in MIC_SCAN.items()}
                self.mic_scan_combo.setCurrentText(rev_mic_scan[resp[6:]])

    def set_mic_scan_resume(self):
        if self.rig.isOpen():
            if self.transfert:
                value = MIC_SCAN_RESUME[self.mic_scan_resume_combo.currentText()]
                cmd = b"EX0516" + value + b";"
                self.rig.write(cmd)

    def get_mic_scan_resume(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0516;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_mic_scan_resume = {value: key for key, value in MIC_SCAN_RESUME.items()}
                self.mic_scan_resume_combo.setCurrentText(rev_mic_scan_resume[resp[6:]])

    def set_ref_freq_adj(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.ref_freq_adj_spin.value())

                if -10 < self.ref_freq_adj_spin.value() < 0:
                    value = value[0] + "0" + value[1]
                elif 0 <= self.ref_freq_adj_spin.value() < 10:
                    value = "+0" + value[0]
                elif self.ref_freq_adj_spin.value() >= 10:
                    value = "+" + value

                value = bytes(value, ENCODER)
                cmd = b"EX0517" + value + b";"
                self.rig.write(cmd)

    def get_ref_freq_adj(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0517;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.ref_freq_adj_spin.setValue(int(resp[6:]))

    def set_clar_select(self):
        if self.rig.isOpen():
            if self.transfert:
                value = CLAR_SELECT[self.clar_select_combo.currentText()]
                cmd = b"EX0518" + value + b";"
                self.rig.write(cmd)

    def get_clar_select(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0518;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_clar_select = {value: key for key, value in CLAR_SELECT.items()}
                self.clar_select_combo.setCurrentText(rev_clar_select[resp[6:]])

    def set_apo(self):
        if self.rig.isOpen():
            if self.transfert:
                value = APO[self.apo_combo.currentText()]
                cmd = b"EX0519" + value + b";"
                self.rig.write(cmd)

    def get_apo(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0519;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_apo = {value: key for key, value in APO.items()}
                self.apo_combo.setCurrentText(rev_apo[resp[6:]])

    def set_fan_control(self):
        if self.rig.isOpen():
            if self.transfert:
                value = FAN_CONTROL[self.fan_control_combo.currentText()]
                cmd = b"EX0520" + value + b";"
                self.rig.write(cmd)

    def get_fan_control(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0520;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_fan_control = {value: key for key, value in FAN_CONTROL.items()}
                self.fan_control_combo.setCurrentText(rev_fan_control[resp[6:]])

    def set_am_lcut_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                value = LCUT_FREQ[self.am_lcut_freq_combo.currentText()]
                cmd = b"EX0601" + value + b";"
                self.rig.write(cmd)

    def get_am_lcut_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0601;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_am_lcut_freq = {value: key for key, value in LCUT_FREQ.items()}
                self.am_lcut_freq_combo.setCurrentText(rev_am_lcut_freq[resp[6:]])

    def set_am_lcut_slope(self):
        if self.rig.isOpen():
            if self.transfert:
                value = SLOPE[self.am_lcut_slope_combo.currentText()]
                cmd = b"EX0602" + value + b";"
                self.rig.write(cmd)

    def get_am_lcut_slope(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0602;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_am_lcut_slope = {value: key for key, value in SLOPE.items()}
                self.am_lcut_slope_combo.setCurrentText(rev_am_lcut_slope[resp[6:]])

    def set_am_hcut_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                value = HCUT_FREQ[self.am_hcut_freq_combo.currentText()]
                cmd = b"EX0603" + value + b";"
                self.rig.write(cmd)

    def get_am_hcut_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0603;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_am_hcut_freq = {value: key for key, value in HCUT_FREQ.items()}
                self.am_hcut_freq_combo.setCurrentText(rev_am_hcut_freq[resp[6:]])

    def set_am_hcut_slope(self):
        if self.rig.isOpen():
            if self.transfert:
                value = SLOPE[self.am_hcut_slope_combo.currentText()]
                cmd = b"EX0604" + value + b";"
                self.rig.write(cmd)

    def get_am_hcut_slope(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0604;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_am_hcut_slope = {value: key for key, value in SLOPE.items()}
                self.am_hcut_slope_combo.setCurrentText(rev_am_hcut_slope[resp[6:]])

    def set_am_mic_select(self):
        if self.rig.isOpen():
            if self.transfert:
                value = AM_MIC_SELECT[self.am_mic_select_combo.currentText()]
                cmd = b"EX0605" + value + b";"
                self.rig.write(cmd)

    def get_am_mic_select(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0605;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_am_mic_select = {value: key for key, value in AM_MIC_SELECT.items()}
                self.am_mic_select_combo.setCurrentText(rev_am_mic_select[resp[6:]])

    def set_am_out_level(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.am_out_level_spin.value())
                while len(value) < 3:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0606" + value + b";"
                self.rig.write(cmd)

    def get_am_out_level(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0606;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.am_out_level_spin.setValue(int(resp[6:]))

    def set_am_ptt_select(self):
        if self.rig.isOpen():
            if self.transfert:
                value = AM_PTT_SELECT[self.am_ptt_select_combo.currentText()]
                cmd = b"EX0607" + value + b";"
                self.rig.write(cmd)

    def get_am_ptt_select(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0607;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_am_ptt_select = {value: key for key, value in AM_PTT_SELECT.items()}
                self.am_ptt_select_combo.setCurrentText(rev_am_ptt_select[resp[6:]])

    def set_cw_lcut_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                value = LCUT_FREQ[self.cw_lcut_freq_combo.currentText()]
                cmd = b"EX0701" + value + b";"
                self.rig.write(cmd)

    def get_cw_lcut_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0701;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_cw_lcut_freq = {value: key for key, value in LCUT_FREQ.items()}
                self.cw_lcut_freq_combo.setCurrentText(rev_cw_lcut_freq[resp[6:]])

    def set_cw_lcut_slope(self):
        if self.rig.isOpen():
            if self.transfert:
                value = SLOPE[self.cw_lcut_slope_combo.currentText()]
                cmd = b"EX0702" + value + b";"
                self.rig.write(cmd)

    def get_cw_lcut_slope(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0702;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_cw_lcut_slope = {value: key for key, value in SLOPE.items()}
                self.cw_lcut_slope_combo.setCurrentText(rev_cw_lcut_slope[resp[6:]])

    def set_cw_hcut_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                value = HCUT_FREQ[self.cw_hcut_freq_combo.currentText()]
                cmd = b"EX0703" + value + b";"
                self.rig.write(cmd)

    def get_cw_hcut_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0703;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_cw_hcut_freq = {value: key for key, value in HCUT_FREQ.items()}
                self.cw_hcut_freq_combo.setCurrentText(rev_cw_hcut_freq[resp[6:]])

    def set_cw_hcut_slope(self):
        if self.rig.isOpen():
            if self.transfert:
                value = SLOPE[self.cw_hcut_slope_combo.currentText()]
                cmd = b"EX0704" + value + b";"
                self.rig.write(cmd)

    def get_cw_hcut_slope(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0704;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_cw_hcut_slope = {value: key for key, value in SLOPE.items()}
                self.cw_hcut_slope_combo.setCurrentText(rev_cw_hcut_slope[resp[6:]])

    def set_cw_out_level(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.cw_out_level_spin.value())
                while len(value) < 3:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0705" + value + b";"
                self.rig.write(cmd)

    def get_cw_out_level(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0705;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.cw_out_level_spin.setValue(int(resp[6:]))

    def set_cw_auto_mode(self):
        if self.rig.isOpen():
            if self.transfert:
                value = CW_AUTO_MODE[self.cw_auto_mode_combo.currentText()]
                cmd = b"EX0706" + value + b";"
                self.rig.write(cmd)

    def get_cw_auto_mode(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0706;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_cw_auto_mode = {value: key for key, value in CW_AUTO_MODE.items()}
                self.cw_auto_mode_combo.setCurrentText(rev_cw_auto_mode[resp[6:]])

    def set_cw_bfo(self):
        if self.rig.isOpen():
            if self.transfert:
                value = CW_BFO[self.cw_bfo_combo.currentText()]
                cmd = b"EX0707" + value + b";"
                self.rig.write(cmd)

    def get_cw_bfo(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0707;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_cw_bfo = {value: key for key, value in CW_BFO.items()}
                self.cw_bfo_combo.setCurrentText(rev_cw_bfo[resp[6:]])

    def set_cw_bk_in_type(self):
        if self.rig.isOpen():
            if self.transfert:
                value = CW_BK_IN_TYPE[self.cw_bk_in_type_combo.currentText()]
                cmd = b"EX0708" + value + b";"
                self.rig.write(cmd)

    def get_cw_bk_in_type(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0708;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_cw_bk_in_type = {value: key for key, value in CW_BK_IN_TYPE.items()}
                self.cw_bk_in_type_combo.setCurrentText(rev_cw_bk_in_type[resp[6:]])

    def set_cw_bk_in_delay(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.cw_bk_in_delay_spin.value())
                while len(value) < 4:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0709" + value + b";"
                self.rig.write(cmd)

    def get_cw_bk_in_delay(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0709;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.cw_bk_in_delay_spin.setValue(int(resp[6:]))

    def set_cw_wave_shape(self):
        if self.rig.isOpen():
            if self.transfert:
                value = CW_WAVE_SHAPE[self.cw_wav_shape_combo.currentText()]
                cmd = b"EX0710" + value + b";"
                self.rig.write(cmd)

    def get_cw_wave_shape(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0710;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_cw_wave_shape = {value: key for key, value in CW_WAVE_SHAPE.items()}
                self.cw_wav_shape_combo.setCurrentText(rev_cw_wave_shape[resp[6:]])

    def set_cw_freq_display(self):
        if self.rig.isOpen():
            if self.transfert:
                value = CW_FREQ_DISPLAY[self.cw_freq_display_combo.currentText()]
                cmd = b"EX0711" + value + b";"
                self.rig.write(cmd)

    def get_cw_freq_display(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0711;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_cw_freq_display = {value: key for key, value in CW_FREQ_DISPLAY.items()}
                self.cw_freq_display_combo.setCurrentText(rev_cw_freq_display[resp[6:]])

    def set_pc_keying(self):
        if self.rig.isOpen():
            if self.transfert:
                value = PC_KEYING[self.pc_keying_combo.currentText()]
                cmd = b"EX0712" + value + b";"
                self.rig.write(cmd)

    def get_pc_keying(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0712;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_pc_keying = {value: key for key, value in PC_KEYING.items()}
                self.pc_keying_combo.setCurrentText(rev_pc_keying[resp[6:]])

    def set_qsk_delay_time(self):
        if self.rig.isOpen():
            if self.transfert:
                value = QSK_DELAY_TIME[self.qsk_delay_time_combo.currentText()]
                cmd = b"EX0713" + value + b";"
                self.rig.write(cmd)

    def get_qsk_delay_time(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0713;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_qsk_delay_time = {value: key for key, value in QSK_DELAY_TIME.items()}
                self.qsk_delay_time_combo.setCurrentText(rev_qsk_delay_time[resp[6:]])

    def set_data_mode(self):
        if self.rig.isOpen():
            if self.transfert:
                value = DATA_MODE[self.data_mode_combo.currentText()]
                cmd = b"EX0801" + value + b";"
                self.rig.write(cmd)

    def get_data_mode(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0801;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_data_mode = {value: key for key, value in DATA_MODE.items()}
                self.data_mode_combo.setCurrentText(rev_data_mode[resp[6:]])

    def set_psk_tone(self):
        if self.rig.isOpen():
            if self.transfert:
                value = PSK_TONE[self.psk_tone_combo.currentText()]
                cmd = b"EX0802" + value + b";"
                self.rig.write(cmd)

    def get_psk_tone(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0802;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_psk_tone = {value: key for key, value in PSK_TONE.items()}
                self.psk_tone_combo.setCurrentText(rev_psk_tone[resp[6:]])

    def set_other_disp(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.other_disp_spin.value())
                val = self.other_disp_spin.value()

                if -1000 < val <= -100:
                    value = value[0] + "0" + value[1] + value[2] + value[3]
                elif -100 < val <= -10:
                    value = value[0] + "00" + value[1] + value[2]
                elif -10 < val < 0:
                    value = value[0] + "000" + value[1]
                elif 0 <= val < 10:
                    value = "+000" + value[0]
                elif 10 <= val < 100:
                    value = "+00" + value
                elif 100 <= val < 1000:
                    value = "+0" + value
                elif 1000 <= val < 4000:
                    value = "+" + value

                value = bytes(value, ENCODER)
                cmd = b"EX0803" + value + b";"
                self.rig.write(cmd)

    def get_other_disp(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0803;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.other_disp_spin.setValue(int(resp[6:]))

    def set_other_shift(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.other_shift_spin.value())
                val = self.other_shift_spin.value()

                if -1000 < val <= -100:
                    value = value[0] + "0" + value[1] + value[2] + value[3]
                elif -100 < val <= -10:
                    value = value[0] + "00" + value[1] + value[2]
                elif -10 < val < 0:
                    value = value[0] + "000" + value[1]
                elif 0 <= val < 10:
                    value = "+000" + value[0]
                elif 10 <= val < 100:
                    value = "+00" + value
                elif 100 <= val < 1000:
                    value = "+0" + value
                elif 1000 <= val < 4000:
                    value = "+" + value

                value = bytes(value, ENCODER)
                cmd = b"EX0804" + value + b";"
                self.rig.write(cmd)

    def get_other_shift(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0804;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.other_shift_spin.setValue(int(resp[6:]))

    def set_data_lcut_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                value = LCUT_FREQ[self.data_lcut_freq_combo.currentText()]
                cmd = b"EX0805" + value + b";"
                self.rig.write(cmd)

    def get_data_lcut_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0805;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_data_lcut_freq = {value: key for key, value in LCUT_FREQ.items()}
                self.data_lcut_freq_combo.setCurrentText(rev_data_lcut_freq[resp[6:]])

    def set_data_lcut_slope(self):
        if self.rig.isOpen():
            if self.transfert:
                value = SLOPE[self.data_lcut_slope_combo.currentText()]
                cmd = b"EX0806" + value + b";"
                self.rig.write(cmd)

    def get_data_lcut_slope(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0806;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_data_lcut_slope = {value: key for key, value in SLOPE.items()}
                self.data_lcut_slope_combo.setCurrentText(rev_data_lcut_slope[resp[6:]])

    def set_data_hcut_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                value = HCUT_FREQ[self.data_hcut_freq_combo.currentText()]
                cmd = b"EX0807" + value + b";"
                self.rig.write(cmd)

    def get_data_hcut_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0807;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_data_hcut_freq = {value: key for key, value in HCUT_FREQ.items()}
                self.data_hcut_freq_combo.setCurrentText(rev_data_hcut_freq[resp[6:]])

    def set_data_hcut_slope(self):
        if self.rig.isOpen():
            if self.transfert:
                value = SLOPE[self.data_hcut_slope_combo.currentText()]
                cmd = b"EX0808" + value + b";"
                self.rig.write(cmd)

    def get_data_hcut_slope(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0808;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_data_hcut_slope = {value: key for key, value in SLOPE.items()}
                self.data_hcut_slope_combo.setCurrentText(rev_data_hcut_slope[resp[6:]])

    def set_data_in_select(self):
        if self.rig.isOpen():
            if self.transfert:
                value = DATA_IN_SELECT[self.data_in_select_combo.currentText()]
                cmd = b"EX0809" + value + b";"
                self.rig.write(cmd)

    def get_data_in_select(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0809;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_data_in_select = {value: key for key, value in DATA_IN_SELECT.items()}
                self.data_in_select_combo.setCurrentText(rev_data_in_select[resp[6:]])

    def set_data_ptt_select(self):
        if self.rig.isOpen():
            if self.transfert:
                value = DATA_PTT_SELECT[self.data_ptt_select_combo.currentText()]
                cmd = b"EX0810" + value + b";"
                self.rig.write(cmd)

    def get_data_ptt_select(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0810;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_data_ptt_select = {value: key for key, value in DATA_PTT_SELECT.items()}
                self.data_ptt_select_combo.setCurrentText(rev_data_ptt_select[resp[6:]])

    def set_data_out_level(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.data_out_level_spin.value())
                while len(value) < 3:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0811" + value + b";"
                self.rig.write(cmd)

    def get_data_out_level(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0811;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.cw_out_level_spin.setValue(int(resp[6:]))

    def set_data_bfo(self):
        if self.rig.isOpen():
            if self.transfert:
                value = DATA_BFO[self.data_bfo_combo.currentText()]
                cmd = b"EX0812" + value + b";"
                self.rig.write(cmd)

    def get_data_bfo(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0812;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_data_bfo = {value: key for key, value in DATA_BFO.items()}
                self.data_bfo_combo.setCurrentText(rev_data_bfo[resp[6:]])

    def set_fm_mic_select(self):
        if self.rig.isOpen():
            if self.transfert:
                value = FM_MIC_SELECT[self.fm_mic_select_combo.currentText()]
                cmd = b"EX0901" + value + b";"
                self.rig.write(cmd)

    def get_fm_mic_select(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0901;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_fm_mic_select = {value: key for key, value in FM_MIC_SELECT.items()}
                self.fm_mic_select_combo.setCurrentText(rev_fm_mic_select[resp[6:]])

    def set_fm_out_level(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.fm_out_level_spin.value())
                while len(value) < 3:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0902" + value + b";"
                self.rig.write(cmd)

    def get_fm_out_level(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0902;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.fm_out_level_spin.setValue(int(resp[6:]))

    def set_pkt_ptt_select(self):
        if self.rig.isOpen():
            if self.transfert:
                value = PKT_PTT_SELECT[self.pkt_ptt_select_combo.currentText()]
                cmd = b"EX0903" + value + b";"
                self.rig.write(cmd)

    def get_pkt_ptt_select(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0903;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_pkt_ptt_select = {value: key for key, value in PKT_PTT_SELECT.items()}
                self.pkt_ptt_select_combo.setCurrentText(rev_pkt_ptt_select[resp[6:]])

    def set_rpt_shift_28(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.rpt_shift_28_spin.value())
                while len(value) < 4:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0904" + value + b";"
                self.rig.write(cmd)

    def get_rpt_shift_28(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0904;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.rpt_shift_28_spin.setValue(int(resp[6:]))

    def set_rpt_shift_50(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.rpt_shift_50_spin.value())
                while len(value) < 4:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0905" + value + b";"
                self.rig.write(cmd)

    def get_rpt_shift_50(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0905;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.rpt_shift_50_spin.setValue(int(resp[6:]))

    def set_dcs_polarity(self):
        if self.rig.isOpen():
            if self.transfert:
                value = DCS_POLARITY[self.dcs_polarity_combo.currentText()]
                cmd = b"EX0906" + value + b";"
                self.rig.write(cmd)

    def get_dcs_polarity(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX0906;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_dcs_polarity = {value: key for key, value in DCS_POLARITY.items()}
                self.dcs_polarity_combo.setCurrentText(rev_dcs_polarity[resp[6:]])

    def set_rtty_lcut_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                value = LCUT_FREQ[self.rtty_lcut_freq_combo.currentText()]
                cmd = b"EX1001" + value + b";"
                self.rig.write(cmd)

    def get_rtty_lcut_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1001;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_rtty_lcut_freq = {value: key for key, value in LCUT_FREQ.items()}
                self.rtty_lcut_freq_combo.setCurrentText(rev_rtty_lcut_freq[resp[6:]])

    def set_rtty_lcut_slope(self):
        if self.rig.isOpen():
            if self.transfert:
                value = SLOPE[self.rtty_lcut_slope_combo.currentText()]
                cmd = b"EX1002" + value + b";"
                self.rig.write(cmd)

    def get_rtty_lcut_slope(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1002;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_rtty_lcut_slope = {value: key for key, value in SLOPE.items()}
                self.rtty_lcut_slope_combo.setCurrentText(rev_rtty_lcut_slope[resp[6:]])

    def set_rtty_hcut_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                value = HCUT_FREQ[self.rtty_hcut_freq_combo.currentText()]
                cmd = b"EX1003" + value + b";"
                self.rig.write(cmd)

    def get_rtty_hcut_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1003;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_rtty_hcut_freq = {value: key for key, value in HCUT_FREQ.items()}
                self.rtty_hcut_freq_combo.setCurrentText(rev_rtty_hcut_freq[resp[6:]])

    def set_rtty_hcut_slope(self):
        if self.rig.isOpen():
            if self.transfert:
                value = SLOPE[self.rtty_hcut_slope_combo.currentText()]
                cmd = b"EX1004" + value + b";"
                self.rig.write(cmd)

    def get_rtty_hcut_slope(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1004;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_rtty_hcut_slope = {value: key for key, value in SLOPE.items()}
                self.rtty_hcut_slope_combo.setCurrentText(rev_rtty_hcut_slope[resp[6:]])

    def set_rtty_shift_port(self):
        if self.rig.isOpen():
            if self.transfert:
                value = RTTY_SHIT_PORT[self.rtty_shift_port_combo.currentText()]
                cmd = b"EX1005" + value + b";"
                self.rig.write(cmd)

    def get_rtty_shift_port(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1005;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_rtty_shift_port = {value: key for key, value in RTTY_SHIT_PORT.items()}
                self.rtty_shift_port_combo.setCurrentText(rev_rtty_shift_port[resp[6:]])

    def set_rtty_polarity_r(self):
        if self.rig.isOpen():
            if self.transfert:
                value = RTTY_POLARITY[self.rtty_polarity_r_combo.currentText()]
                cmd = b"EX1006" + value + b";"
                self.rig.write(cmd)

    def get_rtty_polarity_r(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1006;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_rtty_polarity_r = {value: key for key, value in RTTY_POLARITY.items()}
                self.rtty_polarity_r_combo.setCurrentText(rev_rtty_polarity_r[resp[6:]])

    def set_rtty_polarity_t(self):
        if self.rig.isOpen():
            if self.transfert:
                value = RTTY_POLARITY[self.rtty_polarity_t_combo.currentText()]
                cmd = b"EX1007" + value + b";"
                self.rig.write(cmd)

    def get_rtty_polarity_t(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1007;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_rtty_polarity_t = {value: key for key, value in RTTY_POLARITY.items()}
                self.rtty_polarity_t_combo.setCurrentText(rev_rtty_polarity_t[resp[6:]])

    def set_rtty_out_level(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.rtty_out_level_spin.value())
                while len(value) < 3:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX1008" + value + b";"
                self.rig.write(cmd)

    def get_rtty_out_level(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1008;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.rtty_out_level_spin.setValue(int(resp[6:]))

    def set_rtty_shift_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                value = RTTY_SHIFT_FREQ[self.rtty_shift_freq_combo.currentText()]
                cmd = b"EX1009" + value + b";"
                self.rig.write(cmd)

    def get_rtty_shift_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1009;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_rtty_shift_freq = {value: key for key, value in RTTY_SHIFT_FREQ.items()}
                self.rtty_shift_freq_combo.setCurrentText(rev_rtty_shift_freq[resp[6:]])

    def set_rtty_mark_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                value = RTTY_MARK_FREQ[self.rtty_mark_freq_combo.currentText()]
                cmd = b"EX1010" + value + b";"
                self.rig.write(cmd)

    def get_rtty_mark_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1010;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_rtty_mark_freq = {value: key for key, value in RTTY_MARK_FREQ.items()}
                self.rtty_mark_freq_combo.setCurrentText(rev_rtty_mark_freq[resp[6:]])

    def set_rtty_bfo(self):
        if self.rig.isOpen():
            if self.transfert:
                value = RTTY_BFO[self.rtty_bfo_combo.currentText()]
                cmd = b"EX1011" + value + b";"
                self.rig.write(cmd)

    def get_rtty_bfo(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1011;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_rtty_bfo = {value: key for key, value in RTTY_BFO.items()}
                self.rtty_bfo_combo.setCurrentText(rev_rtty_bfo[resp[6:]])

    def set_ssb_lcut_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                value = LCUT_FREQ[self.ssb_lcut_freq_combo.currentText()]
                cmd = b"EX1101" + value + b";"
                self.rig.write(cmd)

    def get_ssb_lcut_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1101;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_ssb_lcut_freq = {value: key for key, value in LCUT_FREQ.items()}
                self.ssb_lcut_freq_combo.setCurrentText(rev_ssb_lcut_freq[resp[6:]])

    def set_ssb_lcut_slope(self):
        if self.rig.isOpen():
            if self.transfert:
                value = SLOPE[self.ssb_lcut_slope_combo.currentText()]
                cmd = b"EX1102" + value + b";"
                self.rig.write(cmd)

    def get_ssb_lcut_slope(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1102;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_ssb_lcut_slope = {value: key for key, value in SLOPE.items()}
                self.ssb_lcut_slope_combo.setCurrentText(rev_ssb_lcut_slope[resp[6:]])

    def set_ssb_hcut_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                value = HCUT_FREQ[self.ssb_hcut_freq_combo.currentText()]
                cmd = b"EX1103" + value + b";"
                self.rig.write(cmd)

    def get_ssb_hcut_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1103;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_ssb_hcut_freq = {value: key for key, value in HCUT_FREQ.items()}
                self.ssb_hcut_freq_combo.setCurrentText(rev_ssb_hcut_freq[resp[6:]])

    def set_ssb_hcut_slope(self):
        if self.rig.isOpen():
            if self.transfert:
                value = SLOPE[self.ssb_hcut_slope_combo.currentText()]
                cmd = b"EX1104" + value + b";"
                self.rig.write(cmd)

    def get_ssb_hcut_slope(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1104;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_ssb_hcut_slope = {value: key for key, value in SLOPE.items()}
                self.ssb_hcut_slope_combo.setCurrentText(rev_ssb_hcut_slope[resp[6:]])

    def set_ssb_mic_select(self):
        if self.rig.isOpen():
            if self.transfert:
                value = SSB_MIC_SELECT[self.ssb_mic_select_combo.currentText()]
                cmd = b"EX1105" + value + b";"
                self.rig.write(cmd)

    def get_ssb_mic_select(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1105;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_ssb_mic_select = {value: key for key, value in SSB_MIC_SELECT.items()}
                self.ssb_mic_select_combo.setCurrentText(rev_ssb_mic_select[resp[6:]])

    def set_ssb_out_level(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.ssb_out_level_spin.value())
                while len(value) < 3:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX1106" + value + b";"
                self.rig.write(cmd)

    def get_ssb_out_level(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1106;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.ssb_out_level_spin.setValue(int(resp[6:]))

    def set_ssb_bfo(self):
        if self.rig.isOpen():
            if self.transfert:
                value = SSB_BFO[self.ssb_bfo_combo.currentText()]
                cmd = b"EX1107" + value + b";"
                self.rig.write(cmd)

    def get_ssb_bfo(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1107;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_ssb_bfo = {value: key for key, value in SSB_BFO.items()}
                self.ssb_bfo_combo.setCurrentText(rev_ssb_bfo[resp[6:]])

    def set_ssb_ptt_select(self):
        if self.rig.isOpen():
            if self.transfert:
                value = SSB_PTT_SELECT[self.ssb_ptt_select_combo.currentText()]
                cmd = b"EX1108" + value + b";"
                self.rig.write(cmd)

    def get_ssb_ptt_select(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1108;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_ssb_ptt_select = {value: key for key, value in SSB_PTT_SELECT.items()}
                self.ssb_ptt_select_combo.setCurrentText(rev_ssb_ptt_select[resp[6:]])

    def set_ssb_tx_bpf(self):
        if self.rig.isOpen():
            if self.transfert:
                value = SSB_TX_BPF[self.ssb_tx_bpf_combo.currentText()]
                cmd = b"EX1109" + value + b";"
                self.rig.write(cmd)

    def get_ssb_tx_bpf(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1109;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_ssb_tx_bpf = {value: key for key, value in SSB_TX_BPF.items()}
                self.ssb_tx_bpf_combo.setCurrentText(rev_ssb_tx_bpf[resp[6:]])

    def set_apf_width(self):
        if self.rig.isOpen():
            if self.transfert:
                value = APF_WIDTH[self.apf_width_combo.currentText()]
                cmd = b"EX1201" + value + b";"
                self.rig.write(cmd)

    def get_apf_width(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1201;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_apf_width = {value: key for key, value in APF_WIDTH.items()}
                self.apf_width_combo.setCurrentText(rev_apf_width[resp[6:]])

    def set_contour_level(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.contour_level_spin.value())
                val = self.contour_level_spin.value()

                if -10 < val < 0:
                    value = value[0] + "0" + value[1]
                elif 0 <= val < 10:
                    value = "+0" + value[0]
                elif val >= 10:
                    value = "+" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1202" + value + b";"
                self.rig.write(cmd)

    def get_contour_level(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1202;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.contour_level_spin.setValue(int(resp[6:]))

    def set_contour_width(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.contour_width_spin.value())

                while len(value) < 2:
                    value = "0" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1203" + value + b";"
                self.rig.write(cmd)

    def get_contour_width(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1203;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.contour_width_spin.setValue(int(resp[6:]))

    def set_if_notch_width(self):
        if self.rig.isOpen():
            if self.transfert:
                value = IF_NOTCH_WIDTH[self.if_notch_width_combo.currentText()]
                cmd = b"EX1204" + value + b";"
                self.rig.write(cmd)

    def get_if_notch_width(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1204;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_if_notch_width = {value: key for key, value in IF_NOTCH_WIDTH.items()}
                self.if_notch_width_combo.setCurrentText(rev_if_notch_width[resp[6:]])

    def set_scp_start_cycle(self):
        if self.rig.isOpen():
            if self.transfert:
                value = SCP_START_CYCLE[self.scp_start_cycle_combo.currentText()]
                cmd = b"EX1301" + value + b";"
                self.rig.write(cmd)

    def get_scp_start_cycle(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1301;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_scp_start_cycle = {value: key for key, value in SCP_START_CYCLE.items()}
                self.scp_start_cycle_combo.setCurrentText(rev_scp_start_cycle[resp[6:]])

    def set_scp_span_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                value = SCP_SPAN_FREQ[self.scp_span_freq_combo.currentText()]
                cmd = b"EX1302" + value + b";"
                self.rig.write(cmd)

    def get_scp_span_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1302;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_scp_span_freq = {value: key for key, value in SCP_SPAN_FREQ.items()}
                self.scp_span_freq_combo.setCurrentText(rev_scp_span_freq[resp[6:]])

    def set_quick_dial(self):
        if self.rig.isOpen():
            if self.transfert:
                value = QUICK_DIAL[self.quick_dial_combo.currentText()]
                cmd = b"EX1401" + value + b";"
                self.rig.write(cmd)

    def get_quick_dial(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1401;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_quick_dial = {value: key for key, value in QUICK_DIAL.items()}
                self.quick_dial_combo.setCurrentText(rev_quick_dial[resp[6:]])

    def set_ssb_dial_step(self):
        if self.rig.isOpen():
            if self.transfert:
                value = SSB_DIAL_STEP[self.ssb_dial_step_combo.currentText()]
                cmd = b"EX1402" + value + b";"
                self.rig.write(cmd)

    def get_ssb_dial_step(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1402;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_ssb_dial_step = {value: key for key, value in SSB_DIAL_STEP.items()}
                self.ssb_dial_step_combo.setCurrentText(rev_ssb_dial_step[resp[6:]])

    def set_am_dial_step(self):
        if self.rig.isOpen():
            if self.transfert:
                value = AM_DIAL_STEP[self.am_dial_step_combo.currentText()]
                cmd = b"EX1403" + value + b";"
                self.rig.write(cmd)

    def get_am_dial_step(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1403;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_am_dial_step = {value: key for key, value in AM_DIAL_STEP.items()}
                self.am_dial_step_combo.setCurrentText(rev_am_dial_step[resp[6:]])

    def set_fm_dial_step(self):
        if self.rig.isOpen():
            if self.transfert:
                value = FM_DIAL_STEP[self.fm_dial_step_combo.currentText()]
                cmd = b"EX1404" + value + b";"
                self.rig.write(cmd)

    def get_fm_dial_step(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1404;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_fm_dial_step = {value: key for key, value in FM_DIAL_STEP.items()}
                self.fm_dial_step_combo.setCurrentText(rev_fm_dial_step[resp[6:]])

    def set_dial_step(self):
        if self.rig.isOpen():
            if self.transfert:
                value = DIAL_STEP[self.dial_step_combo.currentText()]
                cmd = b"EX1405" + value + b";"
                self.rig.write(cmd)

    def get_dial_step(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1405;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_dial_step = {value: key for key, value in DIAL_STEP.items()}
                self.dial_step_combo.setCurrentText(rev_dial_step[resp[6:]])

    def set_am_ch_step(self):
        if self.rig.isOpen():
            if self.transfert:
                value = AM_CH_STEP[self.am_ch_step_combo.currentText()]
                cmd = b"EX1406" + value + b";"
                self.rig.write(cmd)

    def get_am_ch_step(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1406;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_am_ch_step = {value: key for key, value in AM_CH_STEP.items()}
                self.am_ch_step_combo.setCurrentText(rev_am_ch_step[resp[6:]])

    def set_fm_ch_step(self):
        if self.rig.isOpen():
            if self.transfert:
                value = FM_CH_STEP[self.fm_ch_step_combo.currentText()]
                cmd = b"EX1407" + value + b";"
                self.rig.write(cmd)

    def get_fm_ch_step(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1407;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_fm_ch_step = {value: key for key, value in FM_CH_STEP.items()}
                self.fm_ch_step_combo.setCurrentText(rev_fm_ch_step[resp[6:]])

    def set_eq_1_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                value = EQ_1_FREQ[self.eq_1_freq_combo.currentText()]
                cmd = b"EX1501" + value + b";"
                self.rig.write(cmd)

    def get_eq_1_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1501;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_eq_1_freq = {value: key for key, value in EQ_1_FREQ.items()}
                self.eq_1_freq_combo.setCurrentText(rev_eq_1_freq[resp[6:]])

    def set_eq_1_level(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.eq_1_level_spin.value())

                if -10 < self.eq_1_level_spin.value() < 0:
                    value = value[0] + "0" + value[1]
                elif 0 <= self.eq_1_level_spin.value() < 10:
                    value = "+0" + value[0]
                elif self.eq_1_level_spin.value() >= 10:
                    value = "+" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1502" + value + b";"
                self.rig.write(cmd)

    def get_eq_1_level(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1502;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.eq_1_level_spin.setValue(int(resp[6:]))

    def set_eq_1_bwth(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.eq_1_bwth_spin.value())

                while len(value) < 2:
                    value = "0" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1503" + value + b";"
                self.rig.write(cmd)

    def get_eq_1_bwth(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1503;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.eq_1_bwth_spin.setValue(int(resp[6:]))

    def set_eq_2_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                value = EQ_2_FREQ[self.eq_2_freq_combo.currentText()]
                cmd = b"EX1504" + value + b";"
                self.rig.write(cmd)

    def get_eq_2_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1504;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_eq_2_freq = {value: key for key, value in EQ_2_FREQ.items()}
                self.eq_2_freq_combo.setCurrentText(rev_eq_2_freq[resp[6:]])

    def set_eq_2_level(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.eq_2_level_spin.value())

                if -10 < self.eq_2_level_spin.value() < 0:
                    value = value[0] + "0" + value[1]
                elif 0 <= self.eq_2_level_spin.value() < 10:
                    value = "+0" + value[0]
                elif self.eq_2_level_spin.value() >= 10:
                    value = "+" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1505" + value + b";"
                self.rig.write(cmd)

    def get_eq_2_level(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1505;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.eq_2_level_spin.setValue(int(resp[6:]))

    def set_eq_2_bwth(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.eq_2_bwth_spin.value())

                while len(value) < 2:
                    value = "0" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1506" + value + b";"
                self.rig.write(cmd)

    def get_eq_2_bwth(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1506;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.eq_2_bwth_spin.setValue(int(resp[6:]))

    def set_eq_3_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                value = EQ_3_FREQ[self.eq_3_freq_combo.currentText()]
                cmd = b"EX1507" + value + b";"
                self.rig.write(cmd)

    def get_eq_3_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1507;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_eq_3_freq = {value: key for key, value in EQ_3_FREQ.items()}
                self.eq_3_freq_combo.setCurrentText(rev_eq_3_freq[resp[6:]])

    def set_eq_3_level(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.eq_3_level_spin.value())

                if -10 < self.eq_3_level_spin.value() < 0:
                    value = value[0] + "0" + value[1]
                elif 0 <= self.eq_3_level_spin.value() < 10:
                    value = "+0" + value[0]
                elif self.eq_3_level_spin.value() >= 10:
                    value = "+" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1508" + value + b";"
                self.rig.write(cmd)

    def get_eq_3_level(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1508;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.eq_3_level_spin.setValue(int(resp[6:]))

    def set_eq_3_bwth(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.eq_3_bwth_spin.value())

                while len(value) < 2:
                    value = "0" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1509" + value + b";"
                self.rig.write(cmd)

    def get_eq_3_bwth(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1509;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.eq_3_bwth_spin.setValue(int(resp[6:]))

    def set_p_eq_1_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                value = EQ_1_FREQ[self.p_eq_1_freq_combo.currentText()]
                cmd = b"EX1510" + value + b";"
                self.rig.write(cmd)

    def get_p_eq_1_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1510;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_p_eq_1_freq = {value: key for key, value in EQ_1_FREQ.items()}
                self.p_eq_1_freq_combo.setCurrentText(rev_p_eq_1_freq[resp[6:]])

    def set_p_eq_1_level(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.p_eq_1_level_spin.value())

                if -10 < self.p_eq_1_level_spin.value() < 0:
                    value = value[0] + "0" + value[1]
                elif 0 <= self.p_eq_1_level_spin.value() < 10:
                    value = "+0" + value[0]
                elif self.p_eq_1_level_spin.value() >= 10:
                    value = "+" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1511" + value + b";"
                self.rig.write(cmd)

    def get_p_eq_1_level(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1511;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.p_eq_1_level_spin.setValue(int(resp[6:]))

    def set_p_eq_1_bwth(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.p_eq_1_bwth_spin.value())

                while len(value) < 2:
                    value = "0" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1512" + value + b";"
                self.rig.write(cmd)

    def get_p_eq_1_bwth(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1512;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.p_eq_1_bwth_spin.setValue(int(resp[6:]))

    def set_p_eq_2_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                value = EQ_2_FREQ[self.p_eq_2_freq_combo.currentText()]
                cmd = b"EX1513" + value + b";"
                self.rig.write(cmd)

    def get_p_eq_2_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1513;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_p_eq_2_freq = {value: key for key, value in EQ_2_FREQ.items()}
                self.p_eq_2_freq_combo.setCurrentText(rev_p_eq_2_freq[resp[6:]])

    def set_p_eq_2_level(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.p_eq_2_level_spin.value())

                if -10 < self.p_eq_2_level_spin.value() < 0:
                    value = value[0] + "0" + value[1]
                elif 0 <= self.p_eq_2_level_spin.value() < 10:
                    value = "+0" + value[0]
                elif self.p_eq_2_level_spin.value() >= 10:
                    value = "+" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1514" + value + b";"
                self.rig.write(cmd)

    def get_p_eq_2_level(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1514;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.p_eq_2_level_spin.setValue(int(resp[6:]))

    def set_p_eq_2_bwth(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.p_eq_2_bwth_spin.value())

                while len(value) < 2:
                    value = "0" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1515" + value + b";"
                self.rig.write(cmd)

    def get_p_eq_2_bwth(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1515;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.p_eq_2_bwth_spin.setValue(int(resp[6:]))

    def set_p_eq_3_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                value = EQ_3_FREQ[self.p_eq_3_freq_combo.currentText()]
                cmd = b"EX1516" + value + b";"
                self.rig.write(cmd)

    def get_p_eq_3_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1516;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_p_eq_3_freq = {value: key for key, value in EQ_3_FREQ.items()}
                self.p_eq_3_freq_combo.setCurrentText(rev_p_eq_3_freq[resp[6:]])

    def set_p_eq_3_level(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.p_eq_3_level_spin.value())

                if -10 < self.p_eq_3_level_spin.value() < 0:
                    value = value[0] + "0" + value[1]
                elif 0 <= self.p_eq_3_level_spin.value() < 10:
                    value = "+0" + value[0]
                elif self.p_eq_3_level_spin.value() >= 10:
                    value = "+" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1517" + value + b";"
                self.rig.write(cmd)

    def get_p_eq_3_level(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1517;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.p_eq_3_level_spin.setValue(int(resp[6:]))

    def set_p_eq_3_bwth(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.p_eq_3_bwth_spin.value())

                while len(value) < 2:
                    value = "0" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1518" + value + b";"
                self.rig.write(cmd)

    def get_p_eq_3_bwth(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1518;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.p_eq_3_bwth_spin.setValue(int(resp[6:]))

    def set_hf_ssb_pwr(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.hf_ssb_pwr_spin.value())

                while len(value) < 3:
                    value = "0" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1601" + value + b";"
                self.rig.write(cmd)

    def get_hf_ssb_pwr(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1601;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.hf_ssb_pwr_spin.setValue(int(resp[6:]))

    def set_hf_am_pwr(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.hf_am_pwr_spin.value())

                while len(value) < 3:
                    value = "0" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1602" + value + b";"
                self.rig.write(cmd)

    def get_hf_am_pwr(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1602;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.hf_am_pwr_spin.setValue(int(resp[6:]))

    def set_hf_pwr(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.hf_pwr_spin.value())

                while len(value) < 3:
                    value = "0" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1603" + value + b";"
                self.rig.write(cmd)

    def get_hf_pwr(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1603;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.hf_pwr_spin.setValue(int(resp[6:]))

    def set_50m_ssb_pwr(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.ssb_50m_pwr_spin.value())

                while len(value) < 3:
                    value = "0" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1604" + value + b";"
                self.rig.write(cmd)

    def get_50m_ssb_pwr(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1604;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.ssb_50m_pwr_spin.setValue(int(resp[6:]))

    def set_50m_am_pwr(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.am_50m_pwr_spin.value())

                while len(value) < 3:
                    value = "0" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1605" + value + b";"
                self.rig.write(cmd)

    def get_50m_am_pwr(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1605;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.am_50m_pwr_spin.setValue(int(resp[6:]))

    def set_50m_pwr(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.pwr_50m_spin.value())

                while len(value) < 3:
                    value = "0" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1606" + value + b";"
                self.rig.write(cmd)

    def get_50m_pwr(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1606;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.pwr_50m_spin.setValue(int(resp[6:]))

    def set_ssb_mic_gain(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.ssb_mic_gain_spin.value())

                while len(value) < 3:
                    value = "0" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1607" + value + b";"
                self.rig.write(cmd)

    def get_ssb_mic_gain(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1607;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.ssb_mic_gain_spin.setValue(int(resp[6:]))

    def set_am_mic_gain(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.am_mic_gain_spin.value())

                while len(value) < 3:
                    value = "0" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1608" + value + b";"
                self.rig.write(cmd)

    def get_am_mic_gain(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1608;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.am_mic_gain_spin.setValue(int(resp[6:]))

    def set_fm_mic_gain(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.fm_mic_gain_spin.value())

                while len(value) < 3:
                    value = "0" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1609" + value + b";"
                self.rig.write(cmd)

    def get_fm_mic_gain(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1609;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.fm_mic_gain_spin.setValue(int(resp[6:]))

    def set_data_mic_gain(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.data_mic_gain_spin.value())

                while len(value) < 3:
                    value = "0" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1610" + value + b";"
                self.rig.write(cmd)

    def get_data_mic_gain(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1610;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.data_mic_gain_spin.setValue(int(resp[6:]))

    def set_ssb_data_gain(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.ssb_data_gain_spin.value())

                while len(value) < 3:
                    value = "0" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1611" + value + b";"
                self.rig.write(cmd)

    def get_ssb_data_gain(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1611;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.ssb_data_gain_spin.setValue(int(resp[6:]))

    def set_am_data_gain(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.am_data_gain_spin.value())

                while len(value) < 3:
                    value = "0" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1612" + value + b";"
                self.rig.write(cmd)

    def get_am_data_gain(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1612;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.am_data_gain_spin.setValue(int(resp[6:]))

    def set_fm_data_gain(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.fm_data_gain_spin.value())

                while len(value) < 3:
                    value = "0" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1613" + value + b";"
                self.rig.write(cmd)

    def get_fm_data_gain(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1613;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.fm_data_gain_spin.setValue(int(resp[6:]))

    def set_data_data_gain(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.data_data_gain_spin.value())

                while len(value) < 3:
                    value = "0" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1614" + value + b";"
                self.rig.write(cmd)

    def get_data_data_gain(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1614;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.data_data_gain_spin.setValue(int(resp[6:]))

    def set_tuner_select(self):
        if self.rig.isOpen():
            if self.transfert:
                value = TUNER_SELECT[self.tuner_select_combo.currentText()]
                cmd = b"EX1615" + value + b";"
                self.rig.write(cmd)

    def get_tuner_select(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1615;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_tuner_select = {value: key for key, value in TUNER_SELECT.items()}
                self.tuner_select_combo.setCurrentText(rev_tuner_select[resp[6:]])

    def set_vox_select(self):
        if self.rig.isOpen():
            if self.transfert:
                value = VOX_SELECT[self.vox_select_combo.currentText()]
                cmd = b"EX1616" + value + b";"
                self.rig.write(cmd)

    def get_vox_select(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1616;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_vox_select = {value: key for key, value in VOX_SELECT.items()}
                self.vox_select_combo.setCurrentText(rev_vox_select[resp[6:]])

    def set_vox_gain(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.vox_gain_spin.value())

                while len(value) < 3:
                    value = "0" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1617" + value + b";"
                self.rig.write(cmd)

    def get_vox_gain(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1617;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.vox_gain_spin.setValue(int(resp[6:]))

    def set_vox_delay(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.vox_delay_spin.value())

                while len(value) < 4:
                    value = "0" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1618" + value + b";"
                self.rig.write(cmd)

    def get_vox_delay(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1618;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.vox_delay_spin.setValue(int(resp[6:]))

    def set_anti_vox_gain(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.anti_vox_gain_spin.value())

                while len(value) < 3:
                    value = "0" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1619" + value + b";"
                self.rig.write(cmd)

    def get_anti_vox_gain(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1619;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.anti_vox_gain_spin.setValue(int(resp[6:]))

    def set_data_vox_gain(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.data_vox_gain_spin.value())

                while len(value) < 3:
                    value = "0" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1620" + value + b";"
                self.rig.write(cmd)

    def get_data_vox_gain(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1620;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.data_vox_gain_spin.setValue(int(resp[6:]))

    def set_data_vox_delay(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.data_vox_delay_spin.value())

                while len(value) < 4:
                    value = "0" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1621" + value + b";"
                self.rig.write(cmd)

    def get_data_vox_delay(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1621;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.data_vox_delay_spin.setValue(int(resp[6:]))

    def set_anti_dvox_gain(self):
        if self.rig.isOpen():
            if self.transfert:
                value = str(self.anti_dvox_gain_spin.value())

                while len(value) < 3:
                    value = "0" + value

                value = bytes(value, ENCODER)
                cmd = b"EX1622" + value + b";"
                self.rig.write(cmd)

    def get_anti_dvox_gain(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1622;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                resp = resp.decode(ENCODER)
                self.anti_dvox_gain_spin.setValue(int(resp[6:]))

    def set_emergency_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                value = EMERGENCY_FREQ[self.emergency_freq_combo.currentText()]
                cmd = b"EX1623" + value + b";"
                self.rig.write(cmd)

    def get_emergency_freq(self):
        if self.rig.isOpen():
            if self.transfert:
                self.rig.write(b"EX1623;")
                resp = self.rig.read_until(b";")
                resp = resp.replace(b";", b"")
                rev_emergency_freq = {value: key for key, value in EMERGENCY_FREQ.items()}
                self.emergency_freq_combo.setCurrentText(rev_emergency_freq[resp[6:]])

    def closeEvent(self, event):
        """Close event"""
        dialog = QMessageBox()
        rep = dialog.question(self,
                              "Exit",
                              "Close CPyS-891 ?",
                              dialog.Yes | dialog.No)
        if rep == dialog.Yes:
            pass

        elif rep == dialog.No:
            QCloseEvent.ignore(event)
            return

        if self.rig.isOpen():
            self.rig.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # ###### Font
    QFontDatabase.addApplicationFont(FONT)
    app.setFont(QFont(FONT_FAMILY, FONT_SIZE))

    # ###### Splash Screen
    splash = QSplashScreen(QPixmap(ICON))
    splash.show()
    splash.showMessage(APP_TITLE, Qt.AlignmentFlag.AlignHCenter |
                       Qt.AlignmentFlag.AlignBottom, Qt.GlobalColor.white)

    app.processEvents()
    window = MainWindow(app)
    splash.finish(window)
    # window.showMaximized()
    window.show()
    window.resize(window.minimumSizeHint())
    sys.exit(app.exec_())
