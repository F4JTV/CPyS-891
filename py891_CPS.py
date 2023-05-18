#!/usr/bin/python3
##########################################################################
#   CPyS-891 is a CPS for the Yaesu FT-891 made with Python3 and PyQt5   #
# It doesn't use Hamlib, it uses serial module with CAT protocol instead #
##########################################################################
import sys
from datetime import datetime

from serial import Serial
from PyQt5.Qt import *

APP_NAME = "CPyS-891"
APP_VERSION = datetime.strftime(datetime.now(), "%y%m%d")
APP_TITLE = f"{APP_NAME} - v{APP_VERSION}"
ICON = "../images/icon.png"
FONT = "../fonts/Quicksand-Regular.ttf"
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
APO = {"OFF": 0, "1 h": 1, "2 h": 2, "4 h": 3,
       "6 h": 4, "8 h": 5, "10 h": 6, "12 h": 7}
FAN_CONTROL = {"NORMAL": b"0", "CONTEST": b"1"}
AM_LCUT_SLOPE = {"6 dB/oct": b"0", "18 dB/oct": b"1"}


def format_combo(combobox):
    for i in range(0, combobox.count()):
        combobox.setItemData(i, Qt.AlignCenter, Qt.TextAlignmentRole)


class MainWindow(QMainWindow):
    """ Main Window """

    def __init__(self, appli, **kwargs):
        super().__init__(**kwargs)

        # ######
        self.app = appli
        self.live_mode = True
        self.old_beacon_interval = int()

        # ###### Main Window config
        self.setWindowTitle(APP_TITLE)
        self.setWindowIcon(QIcon(ICON))
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setMouseTracking(True)

        self.central_Widget = QWidget()
        self.setCentralWidget(self.central_Widget)

        self.main_layout = QVBoxLayout()
        self.central_Widget.setLayout(self.main_layout)

        # Rig
        self.rig = Serial(baudrate=38400, write_timeout=1)
        self.rig.setPort("/dev/ttyUSB0")
        # self.rig.open()

        # ###### Tab
        self.tab = QTabWidget()
        self.main_layout.addWidget(self.tab)

        self.menu_tab = QWidget()
        self.memory_tab = QWidget()

        self.tab.addTab(self.menu_tab, "Menu")
        self.tab.addTab(self.memory_tab, "Memory")

        # ###### Menu tab
        self.menu_layout = QVBoxLayout()
        self.menu_tab.setLayout(self.menu_layout)

        self.menu_table = QTableWidget(159, 4)
        self.menu_layout.addWidget(self.menu_table)

        # Menu Table
        self.menu_table.verticalHeader().setVisible(False)
        self.menu_table.horizontalHeader().setVisible(False)
        self.menu_table.setSortingEnabled(False)
        self.menu_table.setMinimumSize(600, 450)
        self.menu_table.setAlternatingRowColors(True)
        self.menu_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.menu_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.menu_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        self.menu_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)

        # ### ACG
        # 01-01
        self.acg_fast_menu_name = QTableWidgetItem("ACG")
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

        self.menu_table.setItem(0, 0, self.acg_fast_menu_name)
        self.menu_table.setItem(0, 1, self.acg_fast_menu_number)
        self.menu_table.setItem(0, 2, self.acg_fast_parm_name)
        self.menu_table.setCellWidget(0, 3, self.acg_fast_spin)

        # 01-02
        self.acg_mid_menu_name = QTableWidgetItem("ACG")
        self.acg_mid_menu_number = QTableWidgetItem("01-02")
        self.acg_mid_parm_name = QTableWidgetItem("ACG MID DELAY")

        self.acg_mid_spin = QSpinBox()
        self.acg_mid_spin.setAlignment(Qt.AlignCenter)
        self.acg_mid_spin.setMaximum(4000)
        self.acg_mid_spin.setMinimum(20)
        self.acg_mid_spin.setValue(700)
        self.acg_mid_spin.setSuffix(" msec")

        self.menu_table.setItem(1, 0, self.acg_mid_menu_name)
        self.menu_table.setItem(1, 1, self.acg_mid_menu_number)
        self.menu_table.setItem(1, 2, self.acg_mid_parm_name)
        self.menu_table.setCellWidget(1, 3, self.acg_mid_spin)

        # 01-03
        self.acg_slow_menu_name = QTableWidgetItem("ACG")
        self.acg_slow_menu_number = QTableWidgetItem("01-03")
        self.acg_slow_parm_name = QTableWidgetItem("ACG SLOW DELAY")

        self.acg_slow_spin = QSpinBox()
        self.acg_slow_spin.setAlignment(Qt.AlignCenter)
        self.acg_slow_spin.setMaximum(4000)
        self.acg_slow_spin.setMinimum(20)
        self.acg_slow_spin.setValue(3000)
        self.acg_slow_spin.setSuffix(" msec")

        self.menu_table.setItem(2, 0, self.acg_slow_menu_name)
        self.menu_table.setItem(2, 1, self.acg_slow_menu_number)
        self.menu_table.setItem(2, 2, self.acg_slow_parm_name)
        self.menu_table.setCellWidget(2, 3, self.acg_slow_spin)

        # ### DISPLAY
        # 02-01
        self.display_lcd_contrast_menu_name = QTableWidgetItem("DISPLAY")
        self.display_lcd_contrast_menu_nb = QTableWidgetItem("02-01")
        self.display_lcd_contrast_parm_name = QTableWidgetItem("LCD CONTRAST")

        self.display_lcd_contrast_spin = QSpinBox()
        self.display_lcd_contrast_spin.setAlignment(Qt.AlignCenter)
        self.display_lcd_contrast_spin.setMaximum(15)
        self.display_lcd_contrast_spin.setMinimum(1)
        self.display_lcd_contrast_spin.setValue(8)

        self.menu_table.setItem(3, 0, self.display_lcd_contrast_menu_name)
        self.menu_table.setItem(3, 1, self.display_lcd_contrast_menu_nb)
        self.menu_table.setItem(3, 2, self.display_lcd_contrast_parm_name)
        self.menu_table.setCellWidget(3, 3, self.display_lcd_contrast_spin)

        # 02-02
        self.display_dimmer_backlit_menu_name = QTableWidgetItem("DISPLAY")
        self.display_dimmer_backlit_menu_nb = QTableWidgetItem("02-02")
        self.display_dimmer_backlit_parm_name = QTableWidgetItem("DIMMER BACKLIT")

        self.display_dimmer_backlit_spin = QSpinBox()
        self.display_dimmer_backlit_spin.setAlignment(Qt.AlignCenter)
        self.display_dimmer_backlit_spin.setMaximum(15)
        self.display_dimmer_backlit_spin.setMinimum(1)
        self.display_dimmer_backlit_spin.setValue(8)
        self.display_dimmer_backlit_spin.valueChanged.connect(self.set_dimmer_backlit)

        self.menu_table.setItem(4, 0, self.display_dimmer_backlit_menu_name)
        self.menu_table.setItem(4, 1, self.display_dimmer_backlit_menu_nb)
        self.menu_table.setItem(4, 2, self.display_dimmer_backlit_parm_name)
        self.menu_table.setCellWidget(4, 3, self.display_dimmer_backlit_spin)

        # 02-03
        self.display_dimmer_lcd_menu_name = QTableWidgetItem("DISPLAY")
        self.display_dimmer_lcd_menu_nb = QTableWidgetItem("02-03")
        self.display_dimmer_lcd_parm_name = QTableWidgetItem("DIMMER LCD")

        self.display_dimmer_lcd_spin = QSpinBox()
        self.display_dimmer_lcd_spin.setAlignment(Qt.AlignCenter)
        self.display_dimmer_lcd_spin.setMaximum(15)
        self.display_dimmer_lcd_spin.setMinimum(1)
        self.display_dimmer_lcd_spin.setValue(8)
        self.display_dimmer_lcd_spin.valueChanged.connect(self.set_dimmer_lcd)

        self.menu_table.setItem(5, 0, self.display_dimmer_lcd_menu_name)
        self.menu_table.setItem(5, 1, self.display_dimmer_lcd_menu_nb)
        self.menu_table.setItem(5, 2, self.display_dimmer_lcd_parm_name)
        self.menu_table.setCellWidget(5, 3, self.display_dimmer_lcd_spin)

        # 02-04
        self.display_dimmer_tx_busy_menu_name = QTableWidgetItem("DISPLAY")
        self.display_dimmer_tx_busy_menu_nb = QTableWidgetItem("02-04")
        self.display_dimmer_tx_busy_parm_name = QTableWidgetItem("DIMMER TX/BUSY")

        self.display_dimmer_tx_busy_spin = QSpinBox()
        self.display_dimmer_tx_busy_spin.setAlignment(Qt.AlignCenter)
        self.display_dimmer_tx_busy_spin.setMaximum(15)
        self.display_dimmer_tx_busy_spin.setMinimum(1)
        self.display_dimmer_tx_busy_spin.setValue(8)

        self.menu_table.setItem(6, 0, self.display_dimmer_tx_busy_menu_name)
        self.menu_table.setItem(6, 1, self.display_dimmer_tx_busy_menu_nb)
        self.menu_table.setItem(6, 2, self.display_dimmer_tx_busy_parm_name)
        self.menu_table.setCellWidget(6, 3, self.display_dimmer_tx_busy_spin)

        # 02-05
        self.peak_hold_menu_name = QTableWidgetItem("DISPLAY")
        self.peak_hold_menu_nb = QTableWidgetItem("02-05")
        self.peak_hold_parm_name = QTableWidgetItem("PEAK HOLD")

        self.peak_hold_combo = QComboBox()
        self.peak_hold_combo.setEditable(True)
        self.peak_hold_combo.lineEdit().setReadOnly(True)
        self.peak_hold_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.peak_hold_combo.addItems([i for i in PEAK_HOLD.keys()])
        format_combo(self.peak_hold_combo)
        self.peak_hold_combo.setCurrentIndex(0)

        self.menu_table.setItem(7, 0, self.peak_hold_menu_name)
        self.menu_table.setItem(7, 1, self.peak_hold_menu_nb)
        self.menu_table.setItem(7, 2, self.peak_hold_parm_name)
        self.menu_table.setCellWidget(7, 3, self.peak_hold_combo)

        # 02-06
        self.zin_led_menu_name = QTableWidgetItem("DISPLAY")
        self.zin_led_menu_nb = QTableWidgetItem("02-06")
        self.zin_led_parm_name = QTableWidgetItem("ZIN LED")

        self.zin_led_combo = QComboBox()
        self.zin_led_combo.setEditable(True)
        self.zin_led_combo.lineEdit().setReadOnly(True)
        self.zin_led_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.zin_led_combo.addItems([i for i in ZIN_LED.keys()])
        format_combo(self.zin_led_combo)
        self.zin_led_combo.setCurrentIndex(0)

        self.menu_table.setItem(8, 0, self.zin_led_menu_name)
        self.menu_table.setItem(8, 1, self.zin_led_menu_nb)
        self.menu_table.setItem(8, 2, self.zin_led_parm_name)
        self.menu_table.setCellWidget(8, 3, self.zin_led_combo)

        # 02-07
        self.pop_up_menu_name = QTableWidgetItem("DISPLAY")
        self.pop_up_menu_nb = QTableWidgetItem("02-07")
        self.pop_up_parm_name = QTableWidgetItem("POP-UP MENU")

        self.pop_up_combo = QComboBox()
        self.pop_up_combo.setEditable(True)
        self.pop_up_combo.lineEdit().setReadOnly(True)
        self.pop_up_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.pop_up_combo.addItems([i for i in POPUP_MENU.keys()])
        format_combo(self.pop_up_combo)
        self.pop_up_combo.setCurrentIndex(1)

        self.menu_table.setItem(9, 0, self.pop_up_menu_name)
        self.menu_table.setItem(9, 1, self.pop_up_menu_nb)
        self.menu_table.setItem(9, 2, self.pop_up_parm_name)
        self.menu_table.setCellWidget(9, 3, self.pop_up_combo)

        # ### DVS
        # 03-01
        self.dvs_rx_out_lvl_menu_name = QTableWidgetItem("DVS")
        self.dvs_rx_out_lvl_menu_nb = QTableWidgetItem("03-01")
        self.dvs_rx_out_lvl_parm_name = QTableWidgetItem("DVS RX OUT LVL")

        self.dvs_rx_out_lvl_spin = QSpinBox()
        self.dvs_rx_out_lvl_spin.setAlignment(Qt.AlignCenter)
        self.dvs_rx_out_lvl_spin.setMaximum(100)
        self.dvs_rx_out_lvl_spin.setMinimum(0)
        self.dvs_rx_out_lvl_spin.setValue(50)

        self.menu_table.setItem(10, 0, self.dvs_rx_out_lvl_menu_name)
        self.menu_table.setItem(10, 1, self.dvs_rx_out_lvl_menu_nb)
        self.menu_table.setItem(10, 2, self.dvs_rx_out_lvl_parm_name)
        self.menu_table.setCellWidget(10, 3, self.dvs_rx_out_lvl_spin)

        # 03-02
        self.dvs_tx_out_lvl_menu_name = QTableWidgetItem("DVS")
        self.dvs_tx_out_lvl_menu_nb = QTableWidgetItem("03-02")
        self.dvs_tx_out_lvl_parm_name = QTableWidgetItem("DVS TX OUT LVL")

        self.dvs_tx_out_lvl_spin = QSpinBox()
        self.dvs_tx_out_lvl_spin.setAlignment(Qt.AlignCenter)
        self.dvs_tx_out_lvl_spin.setMaximum(100)
        self.dvs_tx_out_lvl_spin.setMinimum(0)
        self.dvs_tx_out_lvl_spin.setValue(50)

        self.menu_table.setItem(11, 0, self.dvs_tx_out_lvl_menu_name)
        self.menu_table.setItem(11, 1, self.dvs_tx_out_lvl_menu_nb)
        self.menu_table.setItem(11, 2, self.dvs_tx_out_lvl_parm_name)
        self.menu_table.setCellWidget(11, 3, self.dvs_tx_out_lvl_spin)

        # ### Keyer
        # 04-01
        self.keyer_type_menu_name = QTableWidgetItem("KEYER")
        self.keyer_type_menu_nb = QTableWidgetItem("04-01")
        self.keyer_type_parm_name = QTableWidgetItem("KEYER TYPE")

        self.keyer_type_combo = QComboBox()
        self.keyer_type_combo.setEditable(True)
        self.keyer_type_combo.lineEdit().setReadOnly(True)
        self.keyer_type_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.keyer_type_combo.addItems([i for i in KEYER_TYPE.keys()])
        format_combo(self.keyer_type_combo)
        self.keyer_type_combo.setCurrentIndex(3)

        self.menu_table.setItem(12, 0, self.keyer_type_menu_name)
        self.menu_table.setItem(12, 1, self.keyer_type_menu_nb)
        self.menu_table.setItem(12, 2, self.keyer_type_parm_name)
        self.menu_table.setCellWidget(12, 3, self.keyer_type_combo)

        # 04-02
        self.keyer_dot_dash_menu_name = QTableWidgetItem("KEYER")
        self.keyer_dot_dash_menu_nb = QTableWidgetItem("04-02")
        self.keyer_dot_dash_parm_name = QTableWidgetItem("KEYER DOT/DASH")

        self.keyer_dot_dash_combo = QComboBox()
        self.keyer_dot_dash_combo.setEditable(True)
        self.keyer_dot_dash_combo.lineEdit().setReadOnly(True)
        self.keyer_dot_dash_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.keyer_dot_dash_combo.addItems([i for i in KEYER_DOT_DASH.keys()])
        format_combo(self.keyer_dot_dash_combo)
        self.keyer_dot_dash_combo.setCurrentIndex(0)

        self.menu_table.setItem(13, 0, self.keyer_dot_dash_menu_name)
        self.menu_table.setItem(13, 1, self.keyer_dot_dash_menu_nb)
        self.menu_table.setItem(13, 2, self.keyer_dot_dash_parm_name)
        self.menu_table.setCellWidget(13, 3, self.keyer_dot_dash_combo)

        # 04-03
        self.cw_weight_menu_name = QTableWidgetItem("KEYER")
        self.cw_weight_menu_nb = QTableWidgetItem("04-03")
        self.cw_weight_parm_name = QTableWidgetItem("CW WEIGHT")

        self.cw_weight_spin = QDoubleSpinBox()
        self.cw_weight_spin.setSingleStep(0.1)
        self.cw_weight_spin.setDecimals(1)
        self.cw_weight_spin.setAlignment(Qt.AlignCenter)
        self.cw_weight_spin.setMaximum(4.5)
        self.cw_weight_spin.setMinimum(2.5)
        self.cw_weight_spin.setValue(3.0)

        self.menu_table.setItem(14, 0, self.cw_weight_menu_name)
        self.menu_table.setItem(14, 1, self.cw_weight_menu_nb)
        self.menu_table.setItem(14, 2, self.cw_weight_parm_name)
        self.menu_table.setCellWidget(14, 3, self.cw_weight_spin)

        # 04-04
        self.beacon_interval_menu_name = QTableWidgetItem("KEYER")
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

        self.menu_table.setItem(15, 0, self.beacon_interval_menu_name)
        self.menu_table.setItem(15, 1, self.beacon_interval_menu_nb)
        self.menu_table.setItem(15, 2, self.beacon_interval_parm_name)
        self.menu_table.setCellWidget(15, 3, self.beacon_interval_spin)

        # 04-05
        self.number_style_menu_name = QTableWidgetItem("KEYER")
        self.number_style_menu_nb = QTableWidgetItem("04-05")
        self.number_style_parm_name = QTableWidgetItem("NUMBER STYLE")

        self.number_style_combo = QComboBox()
        self.number_style_combo.setEditable(True)
        self.number_style_combo.lineEdit().setReadOnly(True)
        self.number_style_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.number_style_combo.addItems([i for i in NUMBER_STYLE.keys()])
        format_combo(self.number_style_combo)
        self.number_style_combo.setCurrentIndex(0)

        self.menu_table.setItem(16, 0, self.number_style_menu_name)
        self.menu_table.setItem(16, 1, self.number_style_menu_nb)
        self.menu_table.setItem(16, 2, self.number_style_parm_name)
        self.menu_table.setCellWidget(16, 3, self.number_style_combo)

        # 04-06
        self.contest_number_menu_name = QTableWidgetItem("KEYER")
        self.contest_number_menu_nb = QTableWidgetItem("04-06")
        self.contest_number_parm_name = QTableWidgetItem("CONTEST NUMBER")

        self.contest_number_spin = QSpinBox()
        self.contest_number_spin.setAlignment(Qt.AlignCenter)
        self.contest_number_spin.setMaximum(9999)
        self.contest_number_spin.setMinimum(0)
        self.contest_number_spin.setSingleStep(1)
        self.contest_number_spin.setValue(1)

        self.menu_table.setItem(17, 0, self.contest_number_menu_name)
        self.menu_table.setItem(17, 1, self.contest_number_menu_nb)
        self.menu_table.setItem(17, 2, self.contest_number_parm_name)
        self.menu_table.setCellWidget(17, 3, self.contest_number_spin)

        # 04-07
        self.cw_memory_1_menu_name = QTableWidgetItem("KEYER")
        self.cw_memory_1_menu_nb = QTableWidgetItem("04-07")
        self.cw_memory_1_parm_name = QTableWidgetItem("CW MEMORY 1")

        self.cw_memory_1_combo = QComboBox()
        self.cw_memory_1_combo.setEditable(True)
        self.cw_memory_1_combo.lineEdit().setReadOnly(True)
        self.cw_memory_1_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.cw_memory_1_combo.addItems([i for i in CW_MEMORY.keys()])
        format_combo(self.cw_memory_1_combo)
        self.cw_memory_1_combo.setCurrentIndex(1)

        self.menu_table.setItem(18, 0, self.cw_memory_1_menu_name)
        self.menu_table.setItem(18, 1, self.cw_memory_1_menu_nb)
        self.menu_table.setItem(18, 2, self.cw_memory_1_parm_name)
        self.menu_table.setCellWidget(18, 3, self.cw_memory_1_combo)

        # 04-08
        self.cw_memory_2_menu_name = QTableWidgetItem("KEYER")
        self.cw_memory_2_menu_nb = QTableWidgetItem("04-08")
        self.cw_memory_2_parm_name = QTableWidgetItem("CW MEMORY 2")

        self.cw_memory_2_combo = QComboBox()
        self.cw_memory_2_combo.setEditable(True)
        self.cw_memory_2_combo.lineEdit().setReadOnly(True)
        self.cw_memory_2_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.cw_memory_2_combo.addItems([i for i in CW_MEMORY.keys()])
        format_combo(self.cw_memory_2_combo)
        self.cw_memory_2_combo.setCurrentIndex(1)

        self.menu_table.setItem(19, 0, self.cw_memory_2_menu_name)
        self.menu_table.setItem(19, 1, self.cw_memory_2_menu_nb)
        self.menu_table.setItem(19, 2, self.cw_memory_2_parm_name)
        self.menu_table.setCellWidget(19, 3, self.cw_memory_2_combo)

        # 04-09
        self.cw_memory_3_menu_name = QTableWidgetItem("KEYER")
        self.cw_memory_3_menu_nb = QTableWidgetItem("04-09")
        self.cw_memory_3_parm_name = QTableWidgetItem("CW MEMORY 3")

        self.cw_memory_3_combo = QComboBox()
        self.cw_memory_3_combo.setEditable(True)
        self.cw_memory_3_combo.lineEdit().setReadOnly(True)
        self.cw_memory_3_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.cw_memory_3_combo.addItems([i for i in CW_MEMORY.keys()])
        format_combo(self.cw_memory_3_combo)
        self.cw_memory_3_combo.setCurrentIndex(1)

        self.menu_table.setItem(20, 0, self.cw_memory_3_menu_name)
        self.menu_table.setItem(20, 1, self.cw_memory_3_menu_nb)
        self.menu_table.setItem(20, 2, self.cw_memory_3_parm_name)
        self.menu_table.setCellWidget(20, 3, self.cw_memory_3_combo)

        # 04-10
        self.cw_memory_4_menu_name = QTableWidgetItem("KEYER")
        self.cw_memory_4_menu_nb = QTableWidgetItem("04-10")
        self.cw_memory_4_parm_name = QTableWidgetItem("CW MEMORY 4")

        self.cw_memory_4_combo = QComboBox()
        self.cw_memory_4_combo.setEditable(True)
        self.cw_memory_4_combo.lineEdit().setReadOnly(True)
        self.cw_memory_4_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.cw_memory_4_combo.addItems([i for i in CW_MEMORY.keys()])
        format_combo(self.cw_memory_4_combo)
        self.cw_memory_4_combo.setCurrentIndex(1)

        self.menu_table.setItem(21, 0, self.cw_memory_4_menu_name)
        self.menu_table.setItem(21, 1, self.cw_memory_4_menu_nb)
        self.menu_table.setItem(21, 2, self.cw_memory_4_parm_name)
        self.menu_table.setCellWidget(21, 3, self.cw_memory_4_combo)

        # 04-11
        self.cw_memory_5_menu_name = QTableWidgetItem("KEYER")
        self.cw_memory_5_menu_nb = QTableWidgetItem("04-11")
        self.cw_memory_5_parm_name = QTableWidgetItem("CW MEMORY 5")

        self.cw_memory_5_combo = QComboBox()
        self.cw_memory_5_combo.setEditable(True)
        self.cw_memory_5_combo.lineEdit().setReadOnly(True)
        self.cw_memory_5_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.cw_memory_5_combo.addItems([i for i in CW_MEMORY.keys()])
        format_combo(self.cw_memory_5_combo)
        self.cw_memory_5_combo.setCurrentIndex(1)

        self.menu_table.setItem(22, 0, self.cw_memory_5_menu_name)
        self.menu_table.setItem(22, 1, self.cw_memory_5_menu_nb)
        self.menu_table.setItem(22, 2, self.cw_memory_5_parm_name)
        self.menu_table.setCellWidget(22, 3, self.cw_memory_5_combo)

        # ### General
        # 05-01
        self.nb_width_menu_name = QTableWidgetItem("GENERAL")
        self.nb_width_menu_nb = QTableWidgetItem("05-01")
        self.nb_width_parm_name = QTableWidgetItem("NB WIDTH")

        self.nb_width_combo = QComboBox()
        self.nb_width_combo.setEditable(True)
        self.nb_width_combo.lineEdit().setReadOnly(True)
        self.nb_width_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.nb_width_combo.addItems([i for i in NB_WIDHT.keys()])
        format_combo(self.nb_width_combo)
        self.nb_width_combo.setCurrentIndex(1)

        self.menu_table.setItem(23, 0, self.nb_width_menu_name)
        self.menu_table.setItem(23, 1, self.nb_width_menu_nb)
        self.menu_table.setItem(23, 2, self.nb_width_parm_name)
        self.menu_table.setCellWidget(23, 3, self.nb_width_combo)

        # 05-02
        self.nb_rejection_menu_name = QTableWidgetItem("GENERAL")
        self.nb_rejection_menu_nb = QTableWidgetItem("05-02")
        self.nb_rejection_parm_name = QTableWidgetItem("NB REJECTION")

        self.nb_rejection_combo = QComboBox()
        self.nb_rejection_combo.setEditable(True)
        self.nb_rejection_combo.lineEdit().setReadOnly(True)
        self.nb_rejection_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.nb_rejection_combo.addItems([i for i in NB_REJECTION.keys()])
        format_combo(self.nb_rejection_combo)
        self.nb_rejection_combo.setCurrentIndex(1)

        self.menu_table.setItem(24, 0, self.nb_rejection_menu_name)
        self.menu_table.setItem(24, 1, self.nb_rejection_menu_nb)
        self.menu_table.setItem(24, 2, self.nb_rejection_parm_name)
        self.menu_table.setCellWidget(24, 3, self.nb_rejection_combo)

        # 05-03
        self.nb_level_menu_name = QTableWidgetItem("GENERAL")
        self.nb_level_menu_nb = QTableWidgetItem("05-03")
        self.nb_level_parm_name = QTableWidgetItem("NB LEVEL")

        self.nb_level_spin = QSpinBox()
        self.nb_level_spin.setAlignment(Qt.AlignCenter)
        self.nb_level_spin.setMaximum(10)
        self.nb_level_spin.setMinimum(0)
        self.nb_level_spin.setSingleStep(1)
        self.nb_level_spin.setValue(5)

        self.menu_table.setItem(25, 0, self.nb_level_menu_name)
        self.menu_table.setItem(25, 1, self.nb_level_menu_nb)
        self.menu_table.setItem(25, 2, self.nb_level_parm_name)
        self.menu_table.setCellWidget(25, 3, self.nb_level_spin)

        # 05-04
        self.beep_level_menu_name = QTableWidgetItem("GENERAL")
        self.beep_level_menu_nb = QTableWidgetItem("05-04")
        self.beep_level_parm_name = QTableWidgetItem("BEEP LEVEL")

        self.beep_level_spin = QSpinBox()
        self.beep_level_spin.setAlignment(Qt.AlignCenter)
        self.beep_level_spin.setMaximum(100)
        self.beep_level_spin.setMinimum(0)
        self.beep_level_spin.setSingleStep(1)
        self.beep_level_spin.setValue(30)

        self.menu_table.setItem(26, 0, self.beep_level_menu_name)
        self.menu_table.setItem(26, 1, self.beep_level_menu_nb)
        self.menu_table.setItem(26, 2, self.beep_level_parm_name)
        self.menu_table.setCellWidget(26, 3, self.beep_level_spin)

        # 05-05
        self.rf_sql_vr_menu_name = QTableWidgetItem("GENERAL")
        self.rf_sql_vr_menu_nb = QTableWidgetItem("05-05")
        self.rf_sql_vr_parm_name = QTableWidgetItem("RF/SQL VR")

        self.rf_sql_vr_combo = QComboBox()
        self.rf_sql_vr_combo.setEditable(True)
        self.rf_sql_vr_combo.lineEdit().setReadOnly(True)
        self.rf_sql_vr_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.rf_sql_vr_combo.addItems([i for i in RF_SQL_VR.keys()])
        format_combo(self.rf_sql_vr_combo)
        self.rf_sql_vr_combo.setCurrentIndex(0)

        self.menu_table.setItem(27, 0, self.rf_sql_vr_menu_name)
        self.menu_table.setItem(27, 1, self.rf_sql_vr_menu_nb)
        self.menu_table.setItem(27, 2, self.rf_sql_vr_parm_name)
        self.menu_table.setCellWidget(27, 3, self.rf_sql_vr_combo)

        # 05-06
        self.cat_rate_menu_name = QTableWidgetItem("GENERAL")
        self.cat_rate_menu_nb = QTableWidgetItem("05-06")
        self.cat_rate_parm_name = QTableWidgetItem("CAT RATE")

        self.cat_rate_combo = QComboBox()
        self.cat_rate_combo.setEditable(True)
        self.cat_rate_combo.lineEdit().setReadOnly(True)
        self.cat_rate_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.cat_rate_combo.addItems([i for i in CAT_RATE.keys()])
        format_combo(self.cat_rate_combo)
        self.cat_rate_combo.setCurrentIndex(0)

        self.menu_table.setItem(28, 0, self.cat_rate_menu_name)
        self.menu_table.setItem(28, 1, self.cat_rate_menu_nb)
        self.menu_table.setItem(28, 2, self.cat_rate_parm_name)
        self.menu_table.setCellWidget(28, 3, self.cat_rate_combo)

        # 05-07
        self.cat_tot_menu_name = QTableWidgetItem("GENERAL")
        self.cat_tot_menu_nb = QTableWidgetItem("05-07")
        self.cat_tot_parm_name = QTableWidgetItem("CAT TOT")

        self.cat_tot_combo = QComboBox()
        self.cat_tot_combo.setEditable(True)
        self.cat_tot_combo.lineEdit().setReadOnly(True)
        self.cat_tot_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.cat_tot_combo.addItems([i for i in CAT_TOT.keys()])
        format_combo(self.cat_tot_combo)
        self.cat_tot_combo.setCurrentIndex(0)

        self.menu_table.setItem(29, 0, self.cat_tot_menu_name)
        self.menu_table.setItem(29, 1, self.cat_tot_menu_nb)
        self.menu_table.setItem(29, 2, self.cat_tot_parm_name)
        self.menu_table.setCellWidget(29, 3, self.cat_tot_combo)

        # 05-08
        self.cat_rts_menu_name = QTableWidgetItem("GENERAL")
        self.cat_rts_menu_nb = QTableWidgetItem("05-08")
        self.cat_rts_parm_name = QTableWidgetItem("CAT RTS")

        self.cat_rts_combo = QComboBox()
        self.cat_rts_combo.setEditable(True)
        self.cat_rts_combo.lineEdit().setReadOnly(True)
        self.cat_rts_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.cat_rts_combo.addItems([i for i in CAT_RTS.keys()])
        format_combo(self.cat_rts_combo)
        self.cat_rts_combo.setCurrentIndex(1)

        self.menu_table.setItem(30, 0, self.cat_rts_menu_name)
        self.menu_table.setItem(30, 1, self.cat_rts_menu_nb)
        self.menu_table.setItem(30, 2, self.cat_rts_parm_name)
        self.menu_table.setCellWidget(30, 3, self.cat_rts_combo)

        # 05-09
        self.meme_group_menu_name = QTableWidgetItem("GENERAL")
        self.meme_group_menu_nb = QTableWidgetItem("05-09")
        self.meme_group_parm_name = QTableWidgetItem("MEMORY GROUP")

        self.meme_group_combo = QComboBox()
        self.meme_group_combo.setEditable(True)
        self.meme_group_combo.lineEdit().setReadOnly(True)
        self.meme_group_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.meme_group_combo.addItems([i for i in MEMORY_GROUP.keys()])
        format_combo(self.meme_group_combo)
        self.meme_group_combo.setCurrentIndex(0)

        self.menu_table.setItem(31, 0, self.meme_group_menu_name)
        self.menu_table.setItem(31, 1, self.meme_group_menu_nb)
        self.menu_table.setItem(31, 2, self.meme_group_parm_name)
        self.menu_table.setCellWidget(31, 3, self.meme_group_combo)

        # 05-10
        self.fm_setting_menu_name = QTableWidgetItem("GENERAL")
        self.fm_setting_menu_nb = QTableWidgetItem("05-10")
        self.fm_setting_parm_name = QTableWidgetItem("FM SETTING")

        self.fm_setting_combo = QComboBox()
        self.fm_setting_combo.setEditable(True)
        self.fm_setting_combo.lineEdit().setReadOnly(True)
        self.fm_setting_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.fm_setting_combo.addItems([i for i in FM_SETTING.keys()])
        format_combo(self.fm_setting_combo)
        self.fm_setting_combo.setCurrentIndex(0)

        self.menu_table.setItem(32, 0, self.fm_setting_menu_name)
        self.menu_table.setItem(32, 1, self.fm_setting_menu_nb)
        self.menu_table.setItem(32, 2, self.fm_setting_parm_name)
        self.menu_table.setCellWidget(32, 3, self.fm_setting_combo)

        # 05-11
        self.rec_setting_menu_name = QTableWidgetItem("GENERAL")
        self.rec_setting_menu_nb = QTableWidgetItem("05-11")
        self.rec_setting_parm_name = QTableWidgetItem("REC SETTING")

        self.rec_setting_combo = QComboBox()
        self.rec_setting_combo.setEditable(True)
        self.rec_setting_combo.lineEdit().setReadOnly(True)
        self.rec_setting_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.rec_setting_combo.addItems([i for i in REC_SETTING.keys()])
        format_combo(self.rec_setting_combo)
        self.rec_setting_combo.setCurrentIndex(0)

        self.menu_table.setItem(33, 0, self.rec_setting_menu_name)
        self.menu_table.setItem(33, 1, self.rec_setting_menu_nb)
        self.menu_table.setItem(33, 2, self.rec_setting_parm_name)
        self.menu_table.setCellWidget(33, 3, self.rec_setting_combo)

        # 05-12
        self.atas_setting_menu_name = QTableWidgetItem("GENERAL")
        self.atas_setting_menu_nb = QTableWidgetItem("05-12")
        self.atas_setting_parm_name = QTableWidgetItem("ATAS SETTING")

        self.atas_setting_combo = QComboBox()
        self.atas_setting_combo.setEditable(True)
        self.atas_setting_combo.lineEdit().setReadOnly(True)
        self.atas_setting_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.atas_setting_combo.addItems([i for i in ATAS_SETTING.keys()])
        format_combo(self.atas_setting_combo)
        self.atas_setting_combo.setCurrentIndex(0)

        self.menu_table.setItem(34, 0, self.atas_setting_menu_name)
        self.menu_table.setItem(34, 1, self.atas_setting_menu_nb)
        self.menu_table.setItem(34, 2, self.atas_setting_parm_name)
        self.menu_table.setCellWidget(34, 3, self.atas_setting_combo)

        # 05-13
        self.quick_spl_freq_menu_name = QTableWidgetItem("GENERAL")
        self.quick_spl_freq_menu_nb = QTableWidgetItem("05-13")
        self.quick_spl_freq_parm_name = QTableWidgetItem("QUICK SPL FREQ")

        self.quick_spl_freq_spin = QSpinBox()
        self.quick_spl_freq_spin.setAlignment(Qt.AlignCenter)
        self.quick_spl_freq_spin.setMaximum(20)
        self.quick_spl_freq_spin.setMinimum(-20)
        self.quick_spl_freq_spin.setSingleStep(1)
        self.quick_spl_freq_spin.setValue(5)
        self.quick_spl_freq_spin.setSuffix(" kHz")

        self.menu_table.setItem(35, 0, self.quick_spl_freq_menu_name)
        self.menu_table.setItem(35, 1, self.quick_spl_freq_menu_nb)
        self.menu_table.setItem(35, 2, self.quick_spl_freq_parm_name)
        self.menu_table.setCellWidget(35, 3, self.quick_spl_freq_spin)

        # 05-14
        self.tx_tot_menu_name = QTableWidgetItem("GENERAL")
        self.tx_tot_menu_nb = QTableWidgetItem("05-14")
        self.tx_tot_parm_name = QTableWidgetItem("TX TOT")

        self.tx_tot_spin = QSpinBox()
        self.tx_tot_spin.setAlignment(Qt.AlignCenter)
        self.tx_tot_spin.setMaximum(30)
        self.tx_tot_spin.setMinimum(0)
        self.tx_tot_spin.setSingleStep(1)
        self.tx_tot_spin.setValue(10)
        self.tx_tot_spin.setSuffix(" min")

        self.menu_table.setItem(36, 0, self.tx_tot_menu_name)
        self.menu_table.setItem(36, 1, self.tx_tot_menu_nb)
        self.menu_table.setItem(36, 2, self.tx_tot_parm_name)
        self.menu_table.setCellWidget(36, 3, self.tx_tot_spin)

        # 05-15
        self.mic_scan_menu_name = QTableWidgetItem("GENERAL")
        self.mic_scan_menu_nb = QTableWidgetItem("05-15")
        self.mic_scan_parm_name = QTableWidgetItem("MIC SCAN")

        self.mic_scan_combo = QComboBox()
        self.mic_scan_combo.setEditable(True)
        self.mic_scan_combo.lineEdit().setReadOnly(True)
        self.mic_scan_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.mic_scan_combo.addItems([i for i in MIC_SCAN.keys()])
        format_combo(self.mic_scan_combo)
        self.mic_scan_combo.setCurrentIndex(1)

        self.menu_table.setItem(37, 0, self.mic_scan_menu_name)
        self.menu_table.setItem(37, 1, self.mic_scan_menu_nb)
        self.menu_table.setItem(37, 2, self.mic_scan_parm_name)
        self.menu_table.setCellWidget(37, 3, self.mic_scan_combo)

        # 05-16
        self.mic_scan_resume_menu_name = QTableWidgetItem("GENERAL")
        self.mic_scan_resume_menu_nb = QTableWidgetItem("05-16")
        self.mic_scan_resume_parm_name = QTableWidgetItem("MIC SCAN RESUME")

        self.mic_scan_resume_combo = QComboBox()
        self.mic_scan_resume_combo.setEditable(True)
        self.mic_scan_resume_combo.lineEdit().setReadOnly(True)
        self.mic_scan_resume_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.mic_scan_resume_combo.addItems([i for i in MIC_SCAN_RESUME.keys()])
        format_combo(self.mic_scan_resume_combo)
        self.mic_scan_resume_combo.setCurrentIndex(1)

        self.menu_table.setItem(38, 0, self.mic_scan_resume_menu_name)
        self.menu_table.setItem(38, 1, self.mic_scan_resume_menu_nb)
        self.menu_table.setItem(38, 2, self.mic_scan_resume_parm_name)
        self.menu_table.setCellWidget(38, 3, self.mic_scan_resume_combo)

        # 05-17
        self.ref_freq_adj_menu_name = QTableWidgetItem("GENERAL")
        self.ref_freq_adj_menu_nb = QTableWidgetItem("05-17")
        self.ref_freq_adj_parm_name = QTableWidgetItem("REF FREQ ADJ")

        self.ref_freq_adj_spin = QSpinBox()
        self.ref_freq_adj_spin.setAlignment(Qt.AlignCenter)
        self.ref_freq_adj_spin.setMaximum(25)
        self.ref_freq_adj_spin.setMinimum(-25)
        self.ref_freq_adj_spin.setSingleStep(1)
        self.ref_freq_adj_spin.setValue(0)

        self.menu_table.setItem(39, 0, self.ref_freq_adj_menu_name)
        self.menu_table.setItem(39, 1, self.ref_freq_adj_menu_nb)
        self.menu_table.setItem(39, 2, self.ref_freq_adj_parm_name)
        self.menu_table.setCellWidget(39, 3, self.ref_freq_adj_spin)

        # 05-18
        self.clar_select_menu_name = QTableWidgetItem("GENERAL")
        self.clar_select_menu_nb = QTableWidgetItem("05-18")
        self.clar_select_parm_name = QTableWidgetItem("CLAR SELECT")

        self.clar_select_combo = QComboBox()
        self.clar_select_combo.setEditable(True)
        self.clar_select_combo.lineEdit().setReadOnly(True)
        self.clar_select_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.clar_select_combo.addItems([i for i in CLAR_SELECT.keys()])
        format_combo(self.clar_select_combo)
        self.clar_select_combo.setCurrentIndex(0)

        self.menu_table.setItem(40, 0, self.clar_select_menu_name)
        self.menu_table.setItem(40, 1, self.clar_select_menu_nb)
        self.menu_table.setItem(40, 2, self.clar_select_parm_name)
        self.menu_table.setCellWidget(40, 3, self.clar_select_combo)

        # 05-19
        self.apo_menu_name = QTableWidgetItem("GENERAL")
        self.apo_menu_nb = QTableWidgetItem("05-19")
        self.apo_parm_name = QTableWidgetItem("APO")

        self.apo_combo = QComboBox()
        self.apo_combo.setEditable(True)
        self.apo_combo.lineEdit().setReadOnly(True)
        self.apo_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.apo_combo.addItems([i for i in APO.keys()])
        format_combo(self.apo_combo)
        self.apo_combo.setCurrentIndex(0)

        self.menu_table.setItem(41, 0, self.apo_menu_name)
        self.menu_table.setItem(41, 1, self.apo_menu_nb)
        self.menu_table.setItem(41, 2, self.apo_parm_name)
        self.menu_table.setCellWidget(41, 3, self.apo_combo)

        # 05-20
        self.fan_control_menu_name = QTableWidgetItem("GENERAL")
        self.fan_control_menu_nb = QTableWidgetItem("05-20")
        self.fan_control_parm_name = QTableWidgetItem("FAN CONTROL")

        self.fan_control_combo = QComboBox()
        self.fan_control_combo.setEditable(True)
        self.fan_control_combo.lineEdit().setReadOnly(True)
        self.fan_control_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.fan_control_combo.addItems([i for i in FAN_CONTROL.keys()])
        format_combo(self.fan_control_combo)
        self.fan_control_combo.setCurrentIndex(0)

        self.menu_table.setItem(42, 0, self.fan_control_menu_name)
        self.menu_table.setItem(42, 1, self.fan_control_menu_nb)
        self.menu_table.setItem(42, 2, self.fan_control_parm_name)
        self.menu_table.setCellWidget(42, 3, self.fan_control_combo)

        # 06-01
        self.am_lcut_freq_menu_name = QTableWidgetItem("MODE AM")
        self.am_lcut_freq_menu_nb = QTableWidgetItem("06-01")
        self.am_lcut_freq_parm_name = QTableWidgetItem("AM LCUT FREQ")

        self.am_lcut_freq_spin = QSpinBox()
        self.am_lcut_freq_spin.setAlignment(Qt.AlignCenter)
        self.am_lcut_freq_spin.setMaximum(1000)
        self.am_lcut_freq_spin.setMinimum(50)
        self.am_lcut_freq_spin.setSingleStep(50)
        self.am_lcut_freq_spin.setSpecialValueText("OFF")
        self.am_lcut_freq_spin.setSuffix(" Hz")

        self.menu_table.setItem(43, 0, self.am_lcut_freq_menu_name)
        self.menu_table.setItem(43, 1, self.am_lcut_freq_menu_nb)
        self.menu_table.setItem(43, 2, self.am_lcut_freq_parm_name)
        self.menu_table.setCellWidget(43, 3, self.am_lcut_freq_spin)

        # 06-02
        self.am_lcut_slope_menu_name = QTableWidgetItem("MODE AM")
        self.am_lcut_slope_menu_nb = QTableWidgetItem("06-02")
        self.am_lcut_slope_parm_name = QTableWidgetItem("AM LCUT SLOPE")

        self.am_lcut_slope_combo = QComboBox()
        self.am_lcut_slope_combo.setEditable(True)
        self.am_lcut_slope_combo.lineEdit().setReadOnly(True)
        self.am_lcut_slope_combo.lineEdit().setAlignment(Qt.AlignCenter)
        self.am_lcut_slope_combo.addItems([i for i in AM_LCUT_SLOPE.keys()])
        format_combo(self.am_lcut_slope_combo)
        self.am_lcut_slope_combo.setCurrentIndex(0)

        self.menu_table.setItem(44, 0, self.am_lcut_slope_menu_name)
        self.menu_table.setItem(44, 1, self.am_lcut_slope_menu_nb)
        self.menu_table.setItem(44, 2, self.am_lcut_slope_parm_name)
        self.menu_table.setCellWidget(44, 3, self.am_lcut_slope_combo)

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

        # ###### Menu Bar
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        self.file_menu = QMenu("Files")
        self.edit_menu = QMenu("Edit")
        self.menu_bar.addMenu(self.file_menu)
        self.menu_bar.addMenu(self.edit_menu)

        # Edit Actions
        self.live_mode_action = QAction("Live Mode")
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

    def send_config_2_radio(self):
        self.set_dimmer_lcd()
        self.set_dimmer_backlit()
        self.set_beacon_interval()
        self.set_acg_fast_delay()

    def toggle_live_mode(self):
        if self.live_mode:
            self.live_mode_action.setChecked(False)
            self.live_mode = False
            self.send_to_radio_action.setEnabled(True)
        else:
            self.live_mode_action.setChecked(True)
            self.live_mode = True
            self.send_to_radio_action.setDisabled(True)

    def set_dimmer_backlit(self):
        if self.rig.isOpen():
            if self.live_mode:
                value = str(self.display_dimmer_backlit_spin.value())
                while len(value) < 2:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0202" + value + b";"
                self.rig.write(cmd)

    def set_dimmer_lcd(self):
        if self.rig.isOpen():
            if self.live_mode:
                value = str(self.display_dimmer_lcd_spin.value())
                while len(value) < 2:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0203" + value + b";"
                self.rig.write(cmd)

    def set_beacon_interval(self):
        if self.old_beacon_interval == 240 and self.beacon_interval_spin.value() == 241:
            self.beacon_interval_spin.setSingleStep(30)
            self.beacon_interval_spin.setValue(270)
        elif self.old_beacon_interval == 240 and self.beacon_interval_spin.value() == 210:
            self.beacon_interval_spin.setSingleStep(1)
            self.beacon_interval_spin.setValue(239)

        self.old_beacon_interval = self.beacon_interval_spin.value()

        if self.rig.isOpen():
            if self.live_mode:
                pass

    def set_acg_fast_delay(self):
        if self.rig.isOpen():
            if self.live_mode:
                value = str(self.acg_fast_spin.value())
                while len(value) < 4:
                    value = "0" + value
                value = bytes(value, ENCODER)
                cmd = b"EX0101" + value + b";"
                self.rig.write(cmd)

    def closeEvent(self, a0: QCloseEvent):
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
    splash.showMessage(APP_NAME, Qt.AlignmentFlag.AlignHCenter |
                       Qt.AlignmentFlag.AlignBottom, Qt.GlobalColor.black)

    app.processEvents()
    window = MainWindow(app)
    splash.finish(window)
    # window.showMaximized()
    window.show()
    # window.resize(window.minimumSizeHint())
    sys.exit(app.exec_())
