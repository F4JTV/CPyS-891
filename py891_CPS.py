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
        self.setMouseTracking(True)

        self.central_Widget = QWidget()
        self.setCentralWidget(self.central_Widget)

        self.main_layout = QVBoxLayout()
        self.central_Widget.setLayout(self.main_layout)

        # Rig
        self.rig = Serial(baudrate=38400, write_timeout=1)
        self.rig.setPort("/dev/ttyUSB0")
        self.rig.open()

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
        self.menu_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.menu_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.menu_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        self.menu_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)

        # ### ACG
        # 01-01
        self.acg_fast_menu_name = QTableWidgetItem("ACG")
        self.acg_fast_menu_number = QTableWidgetItem("01-01")
        self.acg_fast_parm_name = QTableWidgetItem("ACG FAST DELAY")

        self.acg_fast_menu_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.acg_fast_menu_name.setTextAlignment(Qt.AlignCenter)
        self.acg_fast_menu_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.acg_fast_menu_number.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.acg_fast_menu_number.setTextAlignment(Qt.AlignCenter)
        self.acg_fast_menu_number.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.acg_fast_parm_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.acg_fast_parm_name.setTextAlignment(Qt.AlignCenter)
        self.acg_fast_parm_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)

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

        self.acg_mid_menu_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.acg_mid_menu_name.setTextAlignment(Qt.AlignCenter)
        self.acg_mid_menu_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.acg_mid_menu_number.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.acg_mid_menu_number.setTextAlignment(Qt.AlignCenter)
        self.acg_mid_menu_number.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.acg_mid_parm_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.acg_mid_parm_name.setTextAlignment(Qt.AlignCenter)
        self.acg_mid_parm_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)

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

        self.acg_slow_menu_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.acg_slow_menu_name.setTextAlignment(Qt.AlignCenter)
        self.acg_slow_menu_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.acg_slow_menu_number.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.acg_slow_menu_number.setTextAlignment(Qt.AlignCenter)
        self.acg_slow_menu_number.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.acg_slow_parm_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.acg_slow_parm_name.setTextAlignment(Qt.AlignCenter)
        self.acg_slow_parm_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)

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

        self.display_lcd_contrast_menu_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.display_lcd_contrast_menu_name.setTextAlignment(Qt.AlignCenter)
        self.display_lcd_contrast_menu_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.display_lcd_contrast_menu_nb.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.display_lcd_contrast_menu_nb.setTextAlignment(Qt.AlignCenter)
        self.display_lcd_contrast_menu_nb.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.display_lcd_contrast_parm_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.display_lcd_contrast_parm_name.setTextAlignment(Qt.AlignCenter)
        self.display_lcd_contrast_parm_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)

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

        self.display_dimmer_backlit_menu_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.display_dimmer_backlit_menu_name.setTextAlignment(Qt.AlignCenter)
        self.display_dimmer_backlit_menu_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.display_dimmer_backlit_menu_nb.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.display_dimmer_backlit_menu_nb.setTextAlignment(Qt.AlignCenter)
        self.display_dimmer_backlit_menu_nb.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.display_dimmer_backlit_parm_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.display_dimmer_backlit_parm_name.setTextAlignment(Qt.AlignCenter)
        self.display_dimmer_backlit_parm_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)

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

        self.display_dimmer_lcd_menu_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.display_dimmer_lcd_menu_name.setTextAlignment(Qt.AlignCenter)
        self.display_dimmer_lcd_menu_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.display_dimmer_lcd_menu_nb.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.display_dimmer_lcd_menu_nb.setTextAlignment(Qt.AlignCenter)
        self.display_dimmer_lcd_menu_nb.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.display_dimmer_lcd_parm_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.display_dimmer_lcd_parm_name.setTextAlignment(Qt.AlignCenter)
        self.display_dimmer_lcd_parm_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)

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

        self.display_dimmer_tx_busy_menu_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.display_dimmer_tx_busy_menu_name.setTextAlignment(Qt.AlignCenter)
        self.display_dimmer_tx_busy_menu_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.display_dimmer_tx_busy_menu_nb.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.display_dimmer_tx_busy_menu_nb.setTextAlignment(Qt.AlignCenter)
        self.display_dimmer_tx_busy_menu_nb.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.display_dimmer_tx_busy_parm_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.display_dimmer_tx_busy_parm_name.setTextAlignment(Qt.AlignCenter)
        self.display_dimmer_tx_busy_parm_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)

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

        self.peak_hold_menu_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.peak_hold_menu_name.setTextAlignment(Qt.AlignCenter)
        self.peak_hold_menu_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.peak_hold_menu_nb.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.peak_hold_menu_nb.setTextAlignment(Qt.AlignCenter)
        self.peak_hold_menu_nb.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.peak_hold_parm_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.peak_hold_parm_name.setTextAlignment(Qt.AlignCenter)
        self.peak_hold_parm_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)

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

        self.zin_led_menu_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.zin_led_menu_name.setTextAlignment(Qt.AlignCenter)
        self.zin_led_menu_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.zin_led_menu_nb.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.zin_led_menu_nb.setTextAlignment(Qt.AlignCenter)
        self.zin_led_menu_nb.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.zin_led_parm_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.zin_led_parm_name.setTextAlignment(Qt.AlignCenter)
        self.zin_led_parm_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)

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

        self.pop_up_menu_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.pop_up_menu_name.setTextAlignment(Qt.AlignCenter)
        self.pop_up_menu_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.pop_up_menu_nb.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.pop_up_menu_nb.setTextAlignment(Qt.AlignCenter)
        self.pop_up_menu_nb.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.pop_up_parm_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.pop_up_parm_name.setTextAlignment(Qt.AlignCenter)
        self.pop_up_parm_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)

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

        self.dvs_rx_out_lvl_menu_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.dvs_rx_out_lvl_menu_name.setTextAlignment(Qt.AlignCenter)
        self.dvs_rx_out_lvl_menu_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.dvs_rx_out_lvl_menu_nb.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.dvs_rx_out_lvl_menu_nb.setTextAlignment(Qt.AlignCenter)
        self.dvs_rx_out_lvl_menu_nb.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.dvs_rx_out_lvl_parm_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.dvs_rx_out_lvl_parm_name.setTextAlignment(Qt.AlignCenter)
        self.dvs_rx_out_lvl_parm_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)

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

        self.dvs_tx_out_lvl_menu_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.dvs_tx_out_lvl_menu_name.setTextAlignment(Qt.AlignCenter)
        self.dvs_tx_out_lvl_menu_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.dvs_tx_out_lvl_menu_nb.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.dvs_tx_out_lvl_menu_nb.setTextAlignment(Qt.AlignCenter)
        self.dvs_tx_out_lvl_menu_nb.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.dvs_tx_out_lvl_parm_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.dvs_tx_out_lvl_parm_name.setTextAlignment(Qt.AlignCenter)
        self.dvs_tx_out_lvl_parm_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)

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

        self.keyer_type_menu_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.keyer_type_menu_name.setTextAlignment(Qt.AlignCenter)
        self.keyer_type_menu_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.keyer_type_menu_nb.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.keyer_type_menu_nb.setTextAlignment(Qt.AlignCenter)
        self.keyer_type_menu_nb.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.keyer_type_parm_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.keyer_type_parm_name.setTextAlignment(Qt.AlignCenter)
        self.keyer_type_parm_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)

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

        self.keyer_dot_dash_menu_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.keyer_dot_dash_menu_name.setTextAlignment(Qt.AlignCenter)
        self.keyer_dot_dash_menu_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.keyer_dot_dash_menu_nb.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.keyer_dot_dash_menu_nb.setTextAlignment(Qt.AlignCenter)
        self.keyer_dot_dash_menu_nb.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.keyer_dot_dash_parm_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.keyer_dot_dash_parm_name.setTextAlignment(Qt.AlignCenter)
        self.keyer_dot_dash_parm_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)

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

        self.cw_weight_menu_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.cw_weight_menu_name.setTextAlignment(Qt.AlignCenter)
        self.cw_weight_menu_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.cw_weight_menu_nb.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.cw_weight_menu_nb.setTextAlignment(Qt.AlignCenter)
        self.cw_weight_menu_nb.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.cw_weight_parm_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.cw_weight_parm_name.setTextAlignment(Qt.AlignCenter)
        self.cw_weight_parm_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)

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

        self.beacon_interval_menu_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.beacon_interval_menu_name.setTextAlignment(Qt.AlignCenter)
        self.beacon_interval_menu_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.beacon_interval_menu_nb.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.beacon_interval_menu_nb.setTextAlignment(Qt.AlignCenter)
        self.beacon_interval_menu_nb.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)
        self.beacon_interval_parm_name.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.beacon_interval_parm_name.setTextAlignment(Qt.AlignCenter)
        self.beacon_interval_parm_name.setFlags(Qt.NoItemFlags | Qt.ItemIsEnabled)

        self.beacon_interval_spin = QSpinBox()
        self.beacon_interval_spin.setAlignment(Qt.AlignCenter)
        self.beacon_interval_spin.setMaximum(690)
        self.beacon_interval_spin.setMinimum(0)
        self.beacon_interval_spin.setSingleStep(1)
        self.beacon_interval_spin.setValue(0)
        self.beacon_interval_spin.setSuffix(" sec")
        self.beacon_interval_spin.valueChanged.connect(self.set_beacon_interval)

        self.menu_table.setItem(15, 0, self.beacon_interval_menu_name)
        self.menu_table.setItem(15, 1, self.beacon_interval_menu_nb)
        self.menu_table.setItem(15, 2, self.beacon_interval_parm_name)
        self.menu_table.setCellWidget(15, 3, self.beacon_interval_spin)

        # ###### Memory tab
        self.memory_layout = QVBoxLayout()
        self.memory_tab.setLayout(self.memory_layout)

        # ###### Menu Bar
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        self.file_menu = QMenu("Files")
        self.menu_bar.addMenu(self.file_menu)

        # ###### Status Bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

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
        if self.old_beacon_interval == 239 and self.beacon_interval_spin.value() == 240:
            self.beacon_interval_spin.setSingleStep(30)
        elif self.old_beacon_interval == 270 and self.beacon_interval_spin.value() == 240:
            self.beacon_interval_spin.setSingleStep(1)

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
