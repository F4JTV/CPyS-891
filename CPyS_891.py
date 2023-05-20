#!/usr/bin/python3
##########################################################################
#   CPyS-891 is a CPS for the Yaesu FT-891 made with Python3 and PyQt5   #
#       It uses serial module for CAT protocol in place of Hamlib        #
#                                                                        #
#                  ___ ___      ___     ___ ___ _                        #
#                 / __| _ \_  _/ __|___( _ / _ / |                       #
#                | (__|  _| || \__ |___/ _ \_, | |                       #
#                 \___|_|  \_, |___/   \___//_/|_|                       #
#                          |__/                                          #
##########################################################################

import sys
from datetime import datetime

from serial import Serial
from PyQt5.Qt import *

APP_NAME = "CPyS-891"
APP_VERSION = datetime.strftime(datetime.now(), "%y%m%d")
APP_TITLE = f"{APP_NAME} - v{APP_VERSION}"
ICON = "./images/icon.png"
FONT = "./fonts/Quicksand-Regular.ttf"
FONT_FAMILY = "Quicksand"
FONT_SIZE = 11
ENCODER = "utf-8"
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
SCP_SPAN_FREQ = {"37.5 kHz": b"0", "75 kHz": b"1",
                 "150 kHz": b"2", "375 kHz": b"3",
                 "750 kHz": b"4"}


def format_combo(combobox):
    for i in range(0, combobox.count()):
        combobox.setItemData(i, Qt.AlignCenter, Qt.TextAlignmentRole)


class MainWindow(QMainWindow):
    """ Main Window """

    def __init__(self, appli, **kwargs):
        super().__init__(**kwargs)

        # ######
        self.app = appli
        self.trasnfert = True
        self.old_beacon_interval = int()
        self.settings = None

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
        self.menu_bar.addMenu(self.file_menu)
        self.menu_bar.addMenu(self.edit_menu)

        # Files Actions
        self.save_config_action = QAction("&Save config")
        self.file_menu.addAction(self.save_config_action)

        self.open_config_action = QAction("&Open config file")
        self.file_menu.addAction(self.open_config_action)
        self.file_menu.addSeparator()

        self.settings_action = QAction("Se&tting")
        self.settings_action.triggered.connect(self.display_settings_win)
        self.file_menu.addAction(self.settings_action)
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

        # ###### Status Bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        self.central_Widget = QWidget()
        self.setCentralWidget(self.central_Widget)

        self.main_layout = QVBoxLayout()
        self.central_Widget.setLayout(self.main_layout)

        # ###### Rig
        self.rig = Serial(baudrate=38400, write_timeout=1)
        self.rig.setPort("/dev/ttyUSB0")
        # self.rig.open()

        # ###### Tab
        self.tab = QTabWidget()
        self.main_layout.addWidget(self.tab)

        self.menu_tab = QWidget()
        self.memory_tab = QWidget()

        self.tab.addTab(self.menu_tab, "Menu / Functions")
        self.tab.addTab(self.memory_tab, "Memory")

        # ###### Menu tab
        self.menu_layout = QHBoxLayout()
        self.menu_tab.setLayout(self.menu_layout)

        self.menu_table = QTableWidget(200, 3)
        self.function_layout = QScrollArea()
        self.menu_layout.addWidget(self.menu_table, 1)
        self.menu_layout.addWidget(self.function_layout, 3)

        # Menu Table
        self.menu_table.verticalHeader().setVisible(False)
        self.menu_table.horizontalHeader().setVisible(False)
        self.menu_table.setSortingEnabled(False)
        self.menu_table.setMinimumSize(600, 450)
        # self.menu_table.setAlternatingRowColors(True)
        self.menu_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.menu_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.menu_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)

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
        self.cw_memory_1_combo.setCurrentIndex(1)

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
        self.cw_memory_2_combo.setCurrentIndex(1)

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
        self.cw_memory_3_combo.setCurrentIndex(1)

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
        self.cw_memory_4_combo.setCurrentIndex(1)

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
        self.cw_memory_5_combo.setCurrentIndex(1)

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
        self.rf_sql_vr_combo.currentTextChanged.connect(self.set_number_style)

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

        self.am_lcut_freq_spin = QSpinBox()
        self.am_lcut_freq_spin.setAlignment(Qt.AlignCenter)
        self.am_lcut_freq_spin.setMaximum(1000)
        self.am_lcut_freq_spin.setMinimum(50)
        self.am_lcut_freq_spin.setSingleStep(50)
        self.am_lcut_freq_spin.setSpecialValueText("OFF")
        self.am_lcut_freq_spin.setSuffix(" Hz")

        self.menu_table.setItem(49, 0, self.am_lcut_freq_menu_nb)
        self.menu_table.setItem(49, 1, self.am_lcut_freq_parm_name)
        self.menu_table.setCellWidget(49, 2, self.am_lcut_freq_spin)

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

        self.menu_table.setItem(50, 0, self.am_lcut_slope_menu_nb)
        self.menu_table.setItem(50, 1, self.am_lcut_slope_parm_name)
        self.menu_table.setCellWidget(50, 2, self.am_lcut_slope_combo)

        # 06-03
        self.am_hcut_freq_menu_nb = QTableWidgetItem("06-03")
        self.am_hcut_freq_parm_name = QTableWidgetItem("AM HCUT FREQ")

        self.am_hcut_freq_spin = QSpinBox()
        self.am_hcut_freq_spin.setAlignment(Qt.AlignCenter)
        self.am_hcut_freq_spin.setMaximum(4000)
        self.am_hcut_freq_spin.setMinimum(650)
        self.am_hcut_freq_spin.setSingleStep(50)
        self.am_hcut_freq_spin.setSpecialValueText("OFF")
        self.am_hcut_freq_spin.setSuffix(" Hz")

        self.menu_table.setItem(51, 0, self.am_hcut_freq_menu_nb)
        self.menu_table.setItem(51, 1, self.am_hcut_freq_parm_name)
        self.menu_table.setCellWidget(51, 2, self.am_hcut_freq_spin)

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

        self.cw_lcut_freq_spin = QSpinBox()
        self.cw_lcut_freq_spin.setAlignment(Qt.AlignCenter)
        self.cw_lcut_freq_spin.setMaximum(1000)
        self.cw_lcut_freq_spin.setMinimum(50)
        self.cw_lcut_freq_spin.setSingleStep(50)
        self.cw_lcut_freq_spin.setSpecialValueText("OFF")
        self.cw_lcut_freq_spin.setValue(250)
        self.cw_lcut_freq_spin.setSuffix(" Hz")

        self.menu_table.setItem(57, 0, self.cw_lcut_freq_menu_nb)
        self.menu_table.setItem(57, 1, self.cw_lcut_freq_parm_name)
        self.menu_table.setCellWidget(57, 2, self.cw_lcut_freq_spin)

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

        self.menu_table.setItem(58, 0, self.cw_lcut_slope_menu_nb)
        self.menu_table.setItem(58, 1, self.cw_lcut_slope_parm_name)
        self.menu_table.setCellWidget(58, 2, self.cw_lcut_slope_combo)

        # 07-03
        self.cw_hcut_freq_menu_nb = QTableWidgetItem("07-03")
        self.cw_hcut_freq_parm_name = QTableWidgetItem("CW HCUT FREQ")

        self.cw_hcut_freq_spin = QSpinBox()
        self.cw_hcut_freq_spin.setAlignment(Qt.AlignCenter)
        self.cw_hcut_freq_spin.setMaximum(4000)
        self.cw_hcut_freq_spin.setMinimum(650)
        self.cw_hcut_freq_spin.setSingleStep(50)
        self.cw_hcut_freq_spin.setSpecialValueText("OFF")
        self.cw_hcut_freq_spin.setValue(1200)
        self.cw_hcut_freq_spin.setSuffix(" Hz")

        self.menu_table.setItem(59, 0, self.cw_hcut_freq_menu_nb)
        self.menu_table.setItem(59, 1, self.cw_hcut_freq_parm_name)
        self.menu_table.setCellWidget(59, 2, self.cw_hcut_freq_spin)

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
        self.cw_bk_in_delay_spin.setSingleStep(1)
        self.cw_bk_in_delay_spin.setValue(200)
        self.cw_bk_in_delay_spin.setSuffix(" msec")

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

        self.menu_table.setItem(74, 0, self.other_shift_menu_nb)
        self.menu_table.setItem(74, 1, self.other_shift_parm_name)
        self.menu_table.setCellWidget(74, 2, self.other_shift_spin)

        # 08-05
        self.data_lcut_freq_menu_nb = QTableWidgetItem("08-05")
        self.data_lcut_freq_parm_name = QTableWidgetItem("DATA LCUT FREQ")

        self.data_lcut_freq_spin = QSpinBox()
        self.data_lcut_freq_spin.setAlignment(Qt.AlignCenter)
        self.data_lcut_freq_spin.setMaximum(1000)
        self.data_lcut_freq_spin.setMinimum(50)
        self.data_lcut_freq_spin.setSingleStep(50)
        self.data_lcut_freq_spin.setValue(300)
        self.data_lcut_freq_spin.setSpecialValueText("OFF")
        self.data_lcut_freq_spin.setSuffix(" Hz")

        self.menu_table.setItem(75, 0, self.data_lcut_freq_menu_nb)
        self.menu_table.setItem(75, 1, self.data_lcut_freq_parm_name)
        self.menu_table.setCellWidget(75, 2, self.data_lcut_freq_spin)

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

        self.menu_table.setItem(76, 0, self.data_lcut_slope_menu_nb)
        self.menu_table.setItem(76, 1, self.data_lcut_slope_parm_name)
        self.menu_table.setCellWidget(76, 2, self.data_lcut_slope_combo)

        # 08-07
        self.data_hcut_freq_menu_nb = QTableWidgetItem("08-07")
        self.data_hcut_freq_parm_name = QTableWidgetItem("DATA HCUT FREQ")

        self.data_hcut_freq_spin = QSpinBox()
        self.data_hcut_freq_spin.setAlignment(Qt.AlignCenter)
        self.data_hcut_freq_spin.setMaximum(4000)
        self.data_hcut_freq_spin.setMinimum(650)
        self.data_hcut_freq_spin.setSingleStep(50)
        self.data_hcut_freq_spin.setValue(3000)
        self.data_hcut_freq_spin.setSpecialValueText("OFF")
        self.data_hcut_freq_spin.setSuffix(" Hz")

        self.menu_table.setItem(77, 0, self.data_hcut_freq_menu_nb)
        self.menu_table.setItem(77, 1, self.data_hcut_freq_parm_name)
        self.menu_table.setCellWidget(77, 2, self.data_hcut_freq_spin)

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
        self.data_bfo_combo.setCurrentIndex(0)

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

        self.rtty_lcut_freq_spin = QSpinBox()
        self.rtty_lcut_freq_spin.setAlignment(Qt.AlignCenter)
        self.rtty_lcut_freq_spin.setMaximum(1000)
        self.rtty_lcut_freq_spin.setMinimum(50)
        self.rtty_lcut_freq_spin.setSingleStep(50)
        self.rtty_lcut_freq_spin.setValue(300)
        self.rtty_lcut_freq_spin.setSpecialValueText("OFF")
        self.rtty_lcut_freq_spin.setSuffix(" Hz")

        self.menu_table.setItem(91, 0, self.rtty_lcut_freq_menu_nb)
        self.menu_table.setItem(91, 1, self.rtty_lcut_freq_parm_name)
        self.menu_table.setCellWidget(91, 2, self.rtty_lcut_freq_spin)

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

        self.menu_table.setItem(92, 0, self.rtty_lcut_slope_menu_nb)
        self.menu_table.setItem(92, 1, self.rtty_lcut_slope_parm_name)
        self.menu_table.setCellWidget(92, 2, self.rtty_lcut_slope_combo)

        # 10-03
        self.rtty_hcut_freq_menu_nb = QTableWidgetItem("10-03")
        self.rtty_hcut_freq_parm_name = QTableWidgetItem("RTTY HCUT FREQ")

        self.rtty_hcut_freq_spin = QSpinBox()
        self.rtty_hcut_freq_spin.setAlignment(Qt.AlignCenter)
        self.rtty_hcut_freq_spin.setMaximum(4000)
        self.rtty_hcut_freq_spin.setMinimum(650)
        self.rtty_hcut_freq_spin.setSingleStep(50)
        self.rtty_hcut_freq_spin.setValue(3000)
        self.rtty_hcut_freq_spin.setSpecialValueText("OFF")
        self.rtty_hcut_freq_spin.setSuffix(" Hz")

        self.menu_table.setItem(93, 0, self.rtty_hcut_freq_menu_nb)
        self.menu_table.setItem(93, 1, self.rtty_hcut_freq_parm_name)
        self.menu_table.setCellWidget(93, 2, self.rtty_hcut_freq_spin)

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

        self.ssb_lcut_freq_spin = QSpinBox()
        self.ssb_lcut_freq_spin.setAlignment(Qt.AlignCenter)
        self.ssb_lcut_freq_spin.setMaximum(1000)
        self.ssb_lcut_freq_spin.setMinimum(50)
        self.ssb_lcut_freq_spin.setSingleStep(50)
        self.ssb_lcut_freq_spin.setValue(100)
        self.ssb_lcut_freq_spin.setSpecialValueText("OFF")
        self.ssb_lcut_freq_spin.setSuffix(" Hz")

        self.menu_table.setItem(103, 0, self.ssb_lcut_freq_menu_nb)
        self.menu_table.setItem(103, 1, self.ssb_lcut_freq_parm_name)
        self.menu_table.setCellWidget(103, 2, self.ssb_lcut_freq_spin)

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

        self.menu_table.setItem(104, 0, self.ssb_lcut_slope_menu_nb)
        self.menu_table.setItem(104, 1, self.ssb_lcut_slope_parm_name)
        self.menu_table.setCellWidget(104, 2, self.ssb_lcut_slope_combo)

        # 11-03
        self.ssb_hcut_freq_menu_nb = QTableWidgetItem("11-03")
        self.ssb_hcut_freq_parm_name = QTableWidgetItem("SSB HCUT FREQ")

        self.ssb_hcut_freq_spin = QSpinBox()
        self.ssb_hcut_freq_spin.setAlignment(Qt.AlignCenter)
        self.ssb_hcut_freq_spin.setMaximum(4000)
        self.ssb_hcut_freq_spin.setMinimum(650)
        self.ssb_hcut_freq_spin.setSingleStep(50)
        self.ssb_hcut_freq_spin.setValue(3000)
        self.ssb_hcut_freq_spin.setSpecialValueText("OFF")
        self.ssb_hcut_freq_spin.setSuffix(" Hz")

        self.menu_table.setItem(105, 0, self.ssb_hcut_freq_menu_nb)
        self.menu_table.setItem(105, 1, self.ssb_hcut_freq_parm_name)
        self.menu_table.setCellWidget(105, 2, self.ssb_hcut_freq_spin)

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

        self.menu_table.setItem(119, 0, self.scp_span_freq_menu_nb)
        self.menu_table.setItem(119, 1, self.scp_span_freq_parm_name)
        self.menu_table.setCellWidget(119, 2, self.scp_span_freq_combo)

        # TUNING
        self.tuning_separator = QTableWidgetItem("TUNING")
        self.tuning_separator.setBackground(QColor(Qt.GlobalColor.lightGray))
        self.menu_table.setItem(120, 0, self.tuning_separator)
        self.menu_table.setSpan(120, 0, 1, 3)

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

    def send_config_2_radio(self):
        """Send the config to the Radio"""
        self.trasnfert = True

        self.set_acg_fast_delay()
        self.set_acg_mid_delay()
        self.set_acg_slow_delay()
        self.set_lcd_contrast()
        self.set_dimmer_backlit()
        self.set_dimmer_lcd()

        self.set_beacon_interval()

        self.trasnfert = False

    def toggle_live_mode(self):
        """Toggle Live Mode"""
        if self.trasnfert:
            self.live_mode_action.setChecked(False)
            self.trasnfert = False
            self.send_to_radio_action.setEnabled(True)
        else:
            self.live_mode_action.setChecked(True)
            self.trasnfert = True
            self.send_to_radio_action.setDisabled(True)

    def display_settings_win(self):
        if self.settings is not None:
            pass
        else:
            self.settings = SettingsWindow(self)
            self.settings.show()

    def set_acg_fast_delay(self):
        """Set ACG FAST DELAY"""
        if self.rig.isOpen():
            if self.trasnfert:
                value = str(self.acg_fast_spin.value())
                while len(value) < 4:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0101" + value + b";"
                self.rig.write(cmd)

    def set_acg_mid_delay(self):
        """Set ACG MID DELAY"""
        if self.rig.isOpen():
            if self.trasnfert:
                value = str(self.acg_mid_spin.value())
                while len(value) < 4:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0102" + value + b";"
                self.rig.write(cmd)

    def set_acg_slow_delay(self):
        """Set ACG SLOW DELAY"""
        if self.rig.isOpen():
            if self.trasnfert:
                value = str(self.acg_slow_spin.value())
                while len(value) < 4:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0103" + value + b";"
                self.rig.write(cmd)

    def set_lcd_contrast(self):
        """Set LCD CONTRAST"""
        if self.rig.isOpen():
            if self.trasnfert:
                value = str(self.dimmer_lcd_spin.value())
                while len(value) < 2:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0201" + value + b";"
                self.rig.write(cmd)

    def set_dimmer_backlit(self):
        """Set DIMMER BACKLIT"""
        if self.rig.isOpen():
            if self.trasnfert:
                value = str(self.dimmer_backlit_spin.value())
                while len(value) < 2:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0202" + value + b";"
                self.rig.write(cmd)

    def set_dimmer_lcd(self):
        """Set DIMMER LCD"""
        if self.rig.isOpen():
            if self.trasnfert:
                value = str(self.dimmer_lcd_spin.value())
                while len(value) < 2:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0203" + value + b";"
                self.rig.write(cmd)

    def set_dimmer_tx_busy(self):
        """Set DIMMER TX/BUSY"""
        if self.rig.isOpen():
            if self.trasnfert:
                value = str(self.dimmer_tx_busy_spin.value())
                while len(value) < 2:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0204" + value + b";"
                self.rig.write(cmd)

    def set_peak_hold(self):
        """Set PEAK HOLD"""
        if self.rig.isOpen():
            if self.trasnfert:
                value = PEAK_HOLD[self.peak_hold_combo.currentText()]
                cmd = b"EX0205" + value + b";"
                self.rig.write(cmd)

    def set_zin_led(self):
        """Set ZIN LED"""
        if self.rig.isOpen():
            if self.trasnfert:
                value = ZIN_LED[self.zin_led_combo.currentText()]
                cmd = b"EX0206" + value + b";"
                self.rig.write(cmd)

    def set_pop_up_menu(self):
        """Set POP-UP MENU"""
        if self.rig.isOpen():
            if self.trasnfert:
                value = POPUP_MENU[self.pop_up_combo.currentText()]
                cmd = b"EX0207" + value + b";"
                self.rig.write(cmd)

    def set_dvs_rx_out_lvl(self):
        if self.rig.isOpen():
            if self.trasnfert:
                value = str(self.dvs_rx_out_lvl_spin.value())
                while len(value) < 3:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0301" + value + b";"
                self.rig.write(cmd)

    def set_dvs_tx_out_lvl(self):
        if self.rig.isOpen():
            if self.trasnfert:
                value = str(self.dvs_tx_out_lvl_spin.value())
                while len(value) < 3:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0302" + value + b";"
                self.rig.write(cmd)

    def set_keyer_type(self):
        if self.rig.isOpen():
            if self.trasnfert:
                value = KEYER_TYPE[self.keyer_type_combo.currentText()]
                cmd = b"EX0401" + value + b";"
                self.rig.write(cmd)

    def set_keyer_dot_dash(self):
        if self.rig.isOpen():
            if self.trasnfert:
                value = KEYER_DOT_DASH[self.keyer_dot_dash_combo.currentText()]
                cmd = b"EX0402" + value + b";"
                self.rig.write(cmd)

    def set_cw_weight(self):
        if self.rig.isOpen():
            if self.trasnfert:
                value = str(self.cw_weight_spin.value())
                value = value.replace(",", "")
                value = bytes(value, ENCODER)
                cmd = b"EX0403" + value + b";"
                self.rig.write(cmd)

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
            if self.trasnfert:
                value = str(self.beacon_interval_spin.value())
                while len(value) < 3:
                    value = "0" + value
                cmd = b"EX0404" + bytes(value) + b";"
                self.rig.write(cmd)

    def set_number_style(self):
        if self.rig.isOpen():
            if self.trasnfert:
                value = NUMBER_STYLE[self.number_style_combo.currentText()]
                cmd = b"EX0405" + value + b";"
                self.rig.write(cmd)

    def set_contest_number(self):
        if self.rig.isOpen():
            if self.trasnfert:
                value = str(self.contest_number_spin.value())
                while len(value) < 4:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0406" + value + b";"
                self.rig.write(cmd)

    def set_cw_memory_1(self):
        if self.rig.isOpen():
            if self.trasnfert:
                value = CW_MEMORY[self.cw_memory_1_combo.currentText()]
                cmd = b"EX0407" + value + b";"
                self.rig.write(cmd)

    def set_cw_memory_2(self):
        if self.rig.isOpen():
            if self.trasnfert:
                value = CW_MEMORY[self.cw_memory_2_combo.currentText()]
                cmd = b"EX0408" + value + b";"
                self.rig.write(cmd)

    def set_cw_memory_3(self):
        if self.rig.isOpen():
            if self.trasnfert:
                value = CW_MEMORY[self.cw_memory_3_combo.currentText()]
                cmd = b"EX0409" + value + b";"
                self.rig.write(cmd)

    def set_cw_memory_4(self):
        if self.rig.isOpen():
            if self.trasnfert:
                value = CW_MEMORY[self.cw_memory_4_combo.currentText()]
                cmd = b"EX0410" + value + b";"
                self.rig.write(cmd)

    def set_cw_memory_5(self):
        if self.rig.isOpen():
            if self.trasnfert:
                value = CW_MEMORY[self.cw_memory_5_combo.currentText()]
                cmd = b"EX0411" + value + b";"
                self.rig.write(cmd)

    def closeEvent(self, event):
        """Close event"""
        """dialog = QMessageBox()
        rep = dialog.question(self,
                              "Exit",
                              "Close CPyS-891 ?",
                              dialog.Yes | dialog.No)
        if rep == dialog.Yes:
            pass

        elif rep == dialog.No:
            QCloseEvent.ignore(event)
            return"""

        if self.rig.isOpen():
            self.rig.close()


class SettingsWindow(QDialog):
    """ Settings Windows """
    def __init__(self, master, **kwargs):
        super().__init__(**kwargs)

        self.master = master

        self.setModal(True)

    def closeEvent(self, event):
        self.master.settings = None


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # ###### Font
    QFontDatabase.addApplicationFont(FONT)
    app.setFont(QFont(FONT_FAMILY, FONT_SIZE))

    # ###### Splash Screen
    splash = QSplashScreen(QPixmap(ICON))
    splash.show()
    splash.showMessage(APP_NAME, Qt.AlignmentFlag.AlignHCenter |
                       Qt.AlignmentFlag.AlignBottom, Qt.GlobalColor.black)

    app.processEvents()
    window = MainWindow(app)
    splash.finish(window)
    # window.showMaximized()
    window.show()
    # window.resize(window.minimumSizeHint())
    sys.exit(app.exec_())