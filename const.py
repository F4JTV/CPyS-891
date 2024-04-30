from PyQt5.Qt import *

#########################################################################
#                             General
#########################################################################
APP_NAME = "CPyS-891"
APP_VERSION = "0.240430"
APP_TITLE = f"{APP_NAME} - v{APP_VERSION}"
ICON = "./images/icon.png"
FONT = "./fonts/Quicksand-Regular.ttf"
FONT_FAMILY = "Quicksand"
FONT_SIZE = 11
ENCODER = "ascii"

#########################################################################
#                               Menu
#########################################################################
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

#########################################################################
#                               Function
#########################################################################


def format_combo(combobox):
    """ Center text in Combobox """
    for i in range(0, combobox.count()):
        combobox.setItemData(i, Qt.AlignCenter, Qt.TextAlignmentRole)
