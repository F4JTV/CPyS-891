from serial import Serial

ENCODER = "UTF-8"
CTCSS_TONES = {"67.0": b"000", "69.3": b"001", "71.9": b"002",
               "74.4": b"003", "77,0": b"004", "79.7": b"005",
               "82.5": b"006", "85.4": b"007", "88.5": b"008",
               "91.5": b"009", "94.8": b"010", "97.4": b"011",
               "100.0": b"012", "103.5": b"013", "107.2": b"014",
               "110.9": b"015", "114.8": b"016", "118.8": b"017",
               "123.0": b"018", "127.3": b"019", "131.8": b"020",
               "136.5": b"021", "141.3": b"022", "146.2": b"023",
               "151.4": b"024", "156.7": b"025", "159.8": b"026",
               "162.2": b"027", "165.5": b"028", "167.9": b"029",
               "171.3": b"030", "173.8": b"031", "177.3": b"032",
               "179.9": b"033", "183.5": b"034", "186.2": b"035",
               "189.9": b"036", "192.8": b"037", "196.6": b"038",
               "199.5": b"039", "203.5": b"040", "206.5": b"041",
               "210.7": b"042", "218.1": b"043", "225.7": b"044",
               "229.1": b"045", "233.6": b"046", "241.8": b"047",
               "250.3": b"048", "254.1": b"049"}
DCS_CODES = {"023": b"000", "025": b"001", "026": b"002",
             "031": b"003", "032": b"004", "036": b"005",
             "043": b"006", "047": b"007", "051": b"008",
             "053": b"009", "054": b"010", "065": b"011",
             "071": b"012", "072": b"013", "073": b"014",
             "074": b"015", "114": b"016", "115": b"017",
             "116": b"018", "122": b"019", "125": b"020",
             "131": b"021", "132": b"022", "134": b"023",
             "143": b"024", "145": b"025", "152": b"026",
             "155": b"027", "156": b"028", "162": b"029",
             "165": b"030", "172": b"031", "174": b"032",
             "205": b"033", "212": b"034", "223": b"035",
             "225": b"036", "226": b"037", "243": b"038",
             "244": b"039", "245": b"040", "246": b"041",
             "251": b"042", "252": b"043", "255": b"044",
             "261": b"045", "263": b"046", "265": b"047",
             "266": b"048", "271": b"049", "274": b"050",
             "306": b"051", "311": b"052", "315": b"053",
             "325": b"054", "331": b"055", "332": b"056",
             "343": b"057", "346": b"058", "351": b"059",
             "356": b"060", "364": b"061", "365": b"062",
             "371": b"063", "411": b"064", "412": b"065",
             "413": b"066", "423": b"067", "431": b"068",
             "432": b"069", "445": b"070", "446": b"071",
             "452": b"072", "454": b"073", "455": b"074",
             "462": b"075", "464": b"076", "465": b"077",
             "466": b"078", "503": b"079", "506": b"080",
             "516": b"081", "523": b"082", "526": b"083",
             "532": b"084", "546": b"085", "565": b"086",
             "606": b"087", "612": b"088", "624": b"089",
             "627": b"090", "631": b"091", "632": b"092",
             "654": b"093", "662": b"094", "664": b"095",
             "703": b"096", "712": b"097", "723": b"098",
             "731": b"099", "732": b"100", "734": b"101",
             "743": b"102", "754": b"103"}
TUNER_OFF = b"0"
TUNER_ON = b"1"
TUNING_START = b"2"
ACG_OFF = b"0"
ACG_FAST = b"1"
ACG_MID = b"2"
ACG_SLOW = b"3"
ACG_AUTO = b"4"


class FT891(Serial):
    def __init__(self, port, baudrate, write_timeout):
        super().__init__(baudrate=baudrate, write_timeout=write_timeout)

        self.setPort(port)

    def swap_vfo(self):
        """
        Swap VFO's

        VFOA <-> VFOB

        Set:
        S V ;
        3
        """
        self.write(b"SV;")

    def set_vfoa_2_vfob(self):
        """
        Set VFOA to VFOB

        VFOA -> VFOB

        Set:
        A B ;
        3
        """
        self.write(b"AB;")

    def set_tuner(self, state):
        """
        Set the tuner state

        P1: 0 (Fixed)
        P2: 0 (Fixed)
        P3: 0 Tuner “OFF”, 1: Tuner “ON”, 2: Tuning Start

        Set & Answer:
        A C P1 P2 P3 ;
        6

        Read:
        A C P1 ;
        """
        if state not in [TUNER_ON, TUNER_OFF, TUNING_START]:
            return
        else:
            self.write(b"AC00" + state + b";")

    def get_tuner_state(self):
        """
        Get the tuner state

        P1: 0 (Fixed)
        P2: 0 (Fixed)
        P3: 0 Tuner “OFF”, 1: Tuner “ON”, 2: Tuning Start

        Set & Answer:
        A C P1 P2 P3 ;
        6

        Read:
        A C P1 ;
        """
        self.write(b"AC;")
        return self.read(6)

    def set_af_gain(self, level=str()):
        """
        Set the AF gain level

        P1: 0 (Fixed)
        P2: 000 - 255

        Set & Answer:
        A G P1 P2 P2 P2 ;
        7

        Read:
        A G P1 ;
        4
        """
        lev = bytes(level, ENCODER)
        cmd = b"AG0" + lev + b";"
        self.write(cmd)

    def get_af_gain(self):
        """
        Get the AF gain

        P1: 0 (Fixed)
        P2: 000 - 255

        Set & Answer:
        A G P1 P2 P2 P2 ;
        7

        Read:
        A G P1 ;
        4
        """
        self.write(b"AG0;")
        return self.read(7)

    def set_vfoa_2_mem(self):
        """
        Set VFOA -> MEM

        Set:
        A M ;
        3
        """
        self.write(b"AM;")

    def set_vfob_2_vfoa(self):
        """
        Set VFOB to VFOA

        Set:
        B A ;
        3
        """
        self.write(b"BA;")

    def set_auto_notch(self, state):
        """
        Set auto notch

        P1: 0 (Fixed)
        P2: 0 Auto Notch “OFF”, 1: Auto Notch “ON”

        Set & Answer: B C P1 P2 ;
        5

        Read: B C P1 ;
        4
        """
        if state:
            self.write(b"BC01;")
        else:
            self.write(b"BC00;")

    def get_auto_notch(self):
        """
        Get the auto notch state

        P1: 0 (Fixed)
        P2: 0 Auto Notch “OFF”, 1: Auto Notch “ON”

        Set & Answer: B C P1 P2 ;
        5

        Read: B C P1 ;
        4
        """
        self.write(b"BC0;")
        return self.read(5)

    def set_band_down(self):
        """
        Set the band down

        P1: 0 (Fixed)

        B D P1 ;
        4
        """
        self.write(b"BD0;")

    def set_band_up(self):
        """
        Set the band up

        P1: 0 (Fixed)

        B U P1 ;
        4
        """
        self.write(b"BU0;")

    def set_break_in(self, state=bool()):
        """
        Set break-in state

        P1: 0: Break-in “OFF", 1: Break-in “ON”

        Set & answer: B I P1 ;
        4

        Read: B I ;
        3
        """
        if state:
            self.write(b"BI1;")
        else:
            self.write(b"BI0;")

    def get_break_in(self):
        """
        Get the break-in state

        P1: 0: Break-in “OFF", 1: Break-in “ON”

        Set & answer: B I P1 ;
        4

        Read: B I ;
        3
        """
        self.write(b"BI;")
        return self.read(4)

    def set_manual_notch(self, state=bool()):
        """
        Set the notch state

        P1: 0 (Fixed)
        P2: 0: Manual NOTCH “ON/OFF, 1: Manual NOTCH LEVEL”
        P3 - P2=0: 000: OFF, 001: ON
        P3 - P2=1: 001 - 320 (NOTCH Frequency : x 10 Hz )

        Set & answer: B P P1 P2 P3 P3 P3 ;
        8

        Read: B P P1 P2 ;
        5
        """
        if state:
            self.write(b"BP00001;")
        else:
            self.write(b"BP00000;")

    def set_manual_notch_level(self, level=str()):
        """
        Set the manual notch level

        P1: 0 (Fixed)
        P2: 0: Manual NOTCH “ON/OFF, 1: Manual NOTCH LEVEL”
        P3 - P2=0: 000: OFF, 001: ON
        P3 - P2=1: 001 - 320 (NOTCH Frequency : x 10 Hz )

        Set & answer: B P P1 P2 P3 P3 P3 ;
        8

        Read: B P P1 P2 ;
        5
        """
        lev = bytes(level, ENCODER)
        cmd = b"BP01" + lev + b";"
        self.write(cmd)

    def get_manual_notch_state(self):
        """
        Get the manual notch state

        P1: 0 (Fixed)
        P2: 0: Manual NOTCH “ON/OFF, 1: Manual NOTCH LEVEL”
        P3 - P2=0: 000: OFF, 001: ON
        P3 - P2=1: 001 - 320 (NOTCH Frequency : x 10 Hz )

        Set & answer: B P P1 P2 P3 P3 P3 ;
        8

        Read: B P P1 P2 ;
        5
        """
        self.write(b"BP00;")
        return self.read(8)

    def get_manual_notch_level(self):
        """
        Get the manual notch level

        P1: 0 (Fixed)
        P2: 0: Manual NOTCH “ON/OFF, 1: Manual NOTCH LEVEL”
        P3 - P2=0: 000: OFF, 001: ON
        P3 - P2=1: 001 - 320 (NOTCH Frequency : x 10 Hz )

        Set & answer: B P P1 P2 P3 P3 P3 ;
        8

        Read: B P P1 P2 ;
        5
        """
        self.write(b"BP01;")
        return self.read(8)

    def set_band(self, band):
        """
        Set the band

        P1: 00 - 12

        00: 1.8 MHz
        01: 3.5 MHz
        02: -
        03: 7 MHz
        04: 10 MHz
        05: 14 MHz
        06: 18 MHz
        07: 21 MHz
        08: 24.5 MHz
        09: 28 MHz
        10: 50 MHz
        11: GEN
        12: MW

        Set: B S P1 P1 ;
        5
        """
        b = bytes(band, ENCODER)
        cmd = b"BS" + b + b";"
        self.write(cmd)

    def get_busy(self):
        """
        Get the busy state

        P1 0: RX BUSY “OFF”
           1: RX BUSY “ON”
        P2 0: (Fixed)

        Answer: B Y P1 P2 ;
        5

        Read: B Y ;
        3
        """
        self.write(b"BY;")
        return self.read(5)

    def set_clar(self, state):
        """
        Set the CLAR state

        P1 0: (Fixed)
        P2 0: CLAR “OFF”
           1: CLAR “ON”
        P3 0: (Fixed)

        Set & Answer: C F P1 P2 P3 ;
        6

        Read: C F P1 ;
        4
        """
        if state:
            self.write(b"CF010;")
        else:
            self.write(b"CF000;")

    def get_clar(self):
        """
        Get the CLAR state

        P1 0: (Fixed)
        P2 0: CLAR “OFF”
           1: CLAR “ON”
        P3 0: (Fixed)

        Set & Answer: C F P1 P2 P3 ;
        6

        Read: C F P1 ;
        4
        """
        self.write(b"CF0;")
        return self.read(6)

    def set_channel_up(self):
        """
        Set the channel up

        P1 0: Memory Channel “UP”
           1: Memory Channel “DOWN”

        Set: C H P1 ;
        4
        """
        self.write(b"CH0;")

    def set_channel_down(self):
        """
        Set the channel down

        P1 0: Memory Channel “UP”
           1: Memory Channel “DOWN”

        Set: C H P1 ;
        4
        """
        self.write(b"CH1;")

    def set_ctcss_tone(self, tone):
        """
        Set the CTCSS tone

        P1 0: (Fixed)
        P2 0: CTCSS
           1: DCS
        P3 P2=0 000 - 049: Tone Frequency Number
           P2=1 000 - 103: DCS Code Number

        Set & Answer: C N P1 P2 P3 P3 P3 ;
        8

        Read: C N P1 P2 ;
        5
        """
        cmd = b"CN00" + CTCSS_TONES[tone] + b";"
        self.write(cmd)

    def set_dcs_code(self, code):
        """
        Set the DCS code

        P1 0: (Fixed)
        P2 0: CTCSS
           1: DCS
        P3 P2=0 000 - 049: Tone Frequency Number
           P2=1 000 - 103: DCS Code Number

        Set & Answer: C N P1 P2 P3 P3 P3 ;
        8

        Read: C N P1 P2 ;
        5
        """
        cmd = b"CN01" + DCS_CODES[code] + b";"
        self.write(cmd)

    def get_ctcss_tone(self):
        """
        Get the CTCSS tone

        P1 0: (Fixed)
        P2 0: CTCSS
           1: DCS
        P3 P2=0 000 - 049: Tone Frequency Number
           P2=1 000 - 103: DCS Code Number

        Set & Answer: C N P1 P2 P3 P3 P3 ;
        8

        Read: C N P1 P2 ;
        5
        """
        self.write(b"CN00;")
        return self.read(8)

    def get_dcs_code(self):
        """
        Get the DCS code

        P1 0: (Fixed)
        P2 0: CTCSS
           1: DCS
        P3 P2=0 000 - 049: Tone Frequency Number
           P2=1 000 - 103: DCS Code Number

        Set & Answer: C N P1 P2 P3 P3 P3 ;
        8

        Read: C N P1 P2 ;
        5
        """
        self.write(b"CN01;")
        return self.read(8)

    def set_contour_state(self, state):
        """
        Set the contour state

        P1 0: (Fixed)
        P2 0: CONTOUR “ON/OFF”
           1: CONTOUR FREQ
           2: APF “ON/OFF”
           3: APF FREQ
        P3 P2=0 0000: CONTOUR “OFF”
                0001: CONTOUR “ON”
           P2=1 0010 - 3200 (CONTOUR Frequency:10 - 3200 Hz)
           P2=2 0000: APF “OFF”
                0001: APF “ON”
           P2=3 0000 - 0050 (APF Frequency: -250 - 250 Hz)

        Set & Anwser: C O P1 P2 P3 P3 P3 P3 ;
        9

        Read: C O P1 P2 ;
        5
        """
        if state:
            self.write(b"CO000001;")
        else:
            self.write(b"CO000000;")

    def set_contour_freq(self, freq):
        """
        Set the contour freq

        P1 0: (Fixed)
        P2 0: CONTOUR “ON/OFF”
           1: CONTOUR FREQ
           2: APF “ON/OFF”
           3: APF FREQ
        P3 P2=0 0000: CONTOUR “OFF”
                0001: CONTOUR “ON”
           P2=1 0010 - 3200 (CONTOUR Frequency:10 - 3200 Hz)
           P2=2 0000: APF “OFF”
                0001: APF “ON”
           P2=3 0000 - 0050 (APF Frequency: -250 - 250 Hz)

        Set & Anwser: C O P1 P2 P3 P3 P3 P3 ;
        9

        Read: C O P1 P2 ;
        5
        """
        f = bytes(freq, ENCODER)
        cmd = b"CO01" + f + b";"
        self.write(cmd)

    def set_contour_apf_state(self, state):
        """
        Set the contour APT state

        P1 0: (Fixed)
        P2 0: CONTOUR “ON/OFF”
           1: CONTOUR FREQ
           2: APF “ON/OFF”
           3: APF FREQ
        P3 P2=0 0000: CONTOUR “OFF”
                0001: CONTOUR “ON”
           P2=1 0010 - 3200 (CONTOUR Frequency:10 - 3200 Hz)
           P2=2 0000: APF “OFF”
                0001: APF “ON”
           P2=3 0000 - 0050 (APF Frequency: -250 - 250 Hz)

        Set & Anwser: C O P1 P2 P3 P3 P3 P3 ;
        9

        Read: C O P1 P2 ;
        5
        """
        if state:
            self.write(b"CO020001;")
        else:
            self.write(b"CO020000;")

    def set_controur_apf_freq(self, freq):
        """
        Set the contour APT freq

        P1 0: (Fixed)
        P2 0: CONTOUR “ON/OFF”
           1: CONTOUR FREQ
           2: APF “ON/OFF”
           3: APF FREQ
        P3 P2=0 0000: CONTOUR “OFF”
                0001: CONTOUR “ON”
           P2=1 0010 - 3200 (CONTOUR Frequency:10 - 3200 Hz)
           P2=2 0000: APF “OFF”
                0001: APF “ON”
           P2=3 0000 - 0050 (APF Frequency: -250 - 250 Hz)

        Set & Anwser: C O P1 P2 P3 P3 P3 P3 ;
        9

        Read: C O P1 P2 ;
        5
        """
        f = bytes(freq, ENCODER)
        cmd = b"CO03" + f + b";"
        self.write(cmd)

    def get_contour_state(self):
        """
        Get the contour state

        P1 0: (Fixed)
        P2 0: CONTOUR “ON/OFF”
           1: CONTOUR FREQ
           2: APF “ON/OFF”
           3: APF FREQ
        P3 P2=0 0000: CONTOUR “OFF”
                0001: CONTOUR “ON”
           P2=1 0010 - 3200 (CONTOUR Frequency:10 - 3200 Hz)
           P2=2 0000: APF “OFF”
                0001: APF “ON”
           P2=3 0000 - 0050 (APF Frequency: -250 - 250 Hz)

        Set & Anwser: C O P1 P2 P3 P3 P3 P3 ;
        9

        Read: C O P1 P2 ;
        5
        """
        self.write(b"CO00;")
        return self.read(9)

    def get_contour_freq(self):
        """
        Get the contour freq

        P1 0: (Fixed)
        P2 0: CONTOUR “ON/OFF”
           1: CONTOUR FREQ
           2: APF “ON/OFF”
           3: APF FREQ
        P3 P2=0 0000: CONTOUR “OFF”
                0001: CONTOUR “ON”
           P2=1 0010 - 3200 (CONTOUR Frequency:10 - 3200 Hz)
           P2=2 0000: APF “OFF”
                0001: APF “ON”
           P2=3 0000 - 0050 (APF Frequency: -250 - 250 Hz)

        Set & Anwser: C O P1 P2 P3 P3 P3 P3 ;
        9

        Read: C O P1 P2 ;
        5
        """
        self.write(b"CO01;")
        return self.read(9)

    def get_contour_apf_state(self):
        """
        Get the contour APT state

        P1 0: (Fixed)
        P2 0: CONTOUR “ON/OFF”
           1: CONTOUR FREQ
           2: APF “ON/OFF”
           3: APF FREQ
        P3 P2=0 0000: CONTOUR “OFF”
                0001: CONTOUR “ON”
           P2=1 0010 - 3200 (CONTOUR Frequency:10 - 3200 Hz)
           P2=2 0000: APF “OFF”
                0001: APF “ON”
           P2=3 0000 - 0050 (APF Frequency: -250 - 250 Hz)

        Set & Anwser: C O P1 P2 P3 P3 P3 P3 ;
        9

        Read: C O P1 P2 ;
        5
        """
        self.write(b"CO02;")
        return self.read(9)

    def get_contour_apf_freq(self):
        """
        Get the contour APT freq

        P1 0: (Fixed)
        P2 0: CONTOUR “ON/OFF”
           1: CONTOUR FREQ
           2: APF “ON/OFF”
           3: APF FREQ
        P3 P2=0 0000: CONTOUR “OFF”
                0001: CONTOUR “ON”
           P2=1 0010 - 3200 (CONTOUR Frequency:10 - 3200 Hz)
           P2=2 0000: APF “OFF”
                0001: APF “ON”
           P2=3 0000 - 0050 (APF Frequency: -250 - 250 Hz)

        Set & Anwser: C O P1 P2 P3 P3 P3 P3 ;
        9

        Read: C O P1 P2 ;
        5
        """
        self.write(b"CO03;")
        return self.read(9)

    def set_cw_spot(self, state):
        """
        Set the CW spot state

        P1 0: OFF
           1: ON

        Set & Answer: C S P1 ;
        4

        Read: C S ;
        3
        """
        if state:
            self.write(b"CS1;")
        else:
            self.write(b"CS0;")

    def get_cw_spot(self):
        """
        Get the CW spot state

        P1 0: OFF
           1: ON

        Set & Answer: C S P1 ;
        4

        Read: C S ;
        3
        """
        self.write(b"CS;")
        return self.read(4)

    def set_ctcss_off(self):
        """
        Set CTCSS OFF

        P1 0: (Fixed)
        P2 0: CTCSS “OFF”
           1: CTCSS ENC/DEC “ON”
           2: CTCSS ENC “ON”
           3: DCS “ON”

        Set & Answer: C T P1 P2 ;
        5

        Read: C T P1 ;
        4
        """
        self.write(b"CT00;")

    def set_ctcss_enc_dec(self):
        """
        Set CTCSS TX/RX ON

        P1 0: (Fixed)
        P2 0: CTCSS “OFF”
           1: CTCSS ENC/DEC “ON”
           2: CTCSS ENC “ON”
           3: DCS “ON”

        Set & Answer: C T P1 P2 ;
        5

        Read: C T P1 ;
        4
        """
        self.write(b"CT01;")

    def set_ctcss_enc(self):
        """
        Set CTCSS TX ON

        P1 0: (Fixed)
        P2 0: CTCSS “OFF”
           1: CTCSS ENC/DEC “ON”
           2: CTCSS ENC “ON”
           3: DCS “ON”

        Set & Answer: C T P1 P2 ;
        5

        Read: C T P1 ;
        4
        """
        self.write(b"CT02;")

    def set_dcs_on(self):
        """
        Set DCS ON

        P1 0: (Fixed)
        P2 0: CTCSS “OFF”
           1: CTCSS ENC/DEC “ON”
           2: CTCSS ENC “ON”
           3: DCS “ON”

        Set & Answer: C T P1 P2 ;
        5

        Read: C T P1 ;
        4
        """
        self.write(b"CT03;")

    def get_ctcss_dcs_state(self):
        """
        Set CTCSS/DCS state

        P1 0: (Fixed)
        P2 0: CTCSS “OFF”
           1: CTCSS ENC/DEC “ON”
           2: CTCSS ENC “ON”
           3: DCS “ON”

        Set & Answer: C T P1 P2 ;
        5

        Read: C T P1 ;
        4
        """
        self.write(b"CT0;")
        return self.read(5)

    def set_dimmer(self, contrast_level, backlight_level,
                   lcd_level, tx_busy_level):
        """
        Set the dimmer levels

        Set the dimmer levels for the LCD contrast, backlight,
        LCD and tx/busy

        P1 01 - 15: LCD Contrast Level
        P2 01 - 15: Dimmer Backlight Level
        P3 01 - 15: Dimmer LCD Level
        P4 01 - 15: Dimmer TX/BUSY Level

        Set & Answer: D A P1 P1 P2 P2 P3 P3 P4 P4 ;
        11

        Read: D A ;
        3
        """
        c_lvl = bytes(contrast_level, ENCODER)
        b_lvl = bytes(backlight_level, ENCODER)
        l_lvl = bytes(lcd_level, ENCODER)
        t_lvl = bytes(tx_busy_level, ENCODER)

        cmd = b"DA" + c_lvl + b_lvl + l_lvl + t_lvl + b";"
        self.write(cmd)

    def get_dimmer(self):
        """
        Get the dimmer levels

        Get the dimmer levels for the LCD contrast, backlight,
        LCD and tx/busy

        P1 01 - 15: LCD Contrast Level
        P2 01 - 15: Dimmer Backlight Level
        P3 01 - 15: Dimmer LCD Level
        P4 01 - 15: Dimmer TX/BUSY Level

        Set & Answer: D A P1 P1 P2 P2 P3 P3 P4 P4 ;
        11

        Read: D A ;
        3
        """
        self.write(b"DA;")
        return self.read(11)

    def set_mic_down(self):
        """
        Set the down key

        Set: D N ;
        3
        """
        self.write(b"DN;")

    def set_main_encoder_down(self, steps):
        """
        Set the main encoder down for nb steps

        P1 0: MAIN ENCORDER
           8: MULTI FUNCTION KNOB
        P2 01 - 99: Steps

        Set: E D P1 P2 P2 ;
        """
        step = bytes(steps, ENCODER)
        cmd = b"ED0" + step + b";"
        self.write(cmd)

    def set_multi_func_encoder_down(self, steps):
        """
        Set the multi function encoder down for nb steps

        P1 0: MAIN ENCORDER
           8: MULTI FUNCTION KNOB
        P2 01 - 99: Steps

        Set: E D P1 P2 P2 ;
        """
        step = bytes(steps, ENCODER)
        cmd = b"ED8" + step + b";"
        self.write(cmd)

    def set_main_encoder_up(self, steps):
        """
        Set the main encoder up for nb steps

        P1 0: MAIN ENCORDER
           8: MULTI FUNCTION KNOB
        P2 01 - 99: Steps

        Set: E U P1 P2 P2 ;
        """
        step = bytes(steps, ENCODER)
        cmd = b"EU0" + step + b";"
        self.write(cmd)

    def set_multi_func_encoder_up(self, steps):
        """
        Set the multi function encoder up for nb steps

        P1 0: MAIN ENCORDER
           8: MULTI FUNCTION KNOB
        P2 01 - 99: Steps

        Set: E U P1 P2 P2 ;
        """
        step = bytes(steps, ENCODER)
        cmd = b"EU8" + step + b";"
        self.write(cmd)

    def set_enter_key(self):
        """
        Toggle the Enter key

        Set: E K ;
        3
        """
        self.write(b"EK;")

    def set_vfoa_freq(self, frequency):
        """
        Set the frequency of VFOA

        P1 000030000 - 056000000 (Hz)

        Set & Answer: F A P1 P1 P1 P1 P1 P1 P1 P1 P1 ;
        12

        Read: F A ;
        3
        """
        freq = bytes(frequency, ENCODER)
        cmd = b"FA" + freq + b";"
        self.write(cmd)

    def set_vfob_freq(self, frequency):
        """
        Set the frequency of VFOB

        P1 000030000 - 056000000 (Hz)

        Set & Answer: F B P1 P1 P1 P1 P1 P1 P1 P1 P1 ;
        12

        Read: F B ;
        3
        """
        freq = bytes(frequency, ENCODER)
        cmd = b"FB" + freq + b";"
        self.write(cmd)

    def get_vfoa_freq(self):
        """
        Get the frequency of VFOA

        P1 000030000 - 056000000 (Hz)

        Set & Answer: F A P1 P1 P1 P1 P1 P1 P1 P1 P1 ;
        12

        Read: F A ;
        3
        """
        self.write(b"FA;")
        return self.read(12)

    def get_vfob_freq(self):
        """
        Get the frequency of VFOB

        P1 000030000 - 056000000 (Hz)

        Set & Answer: F B P1 P1 P1 P1 P1 P1 P1 P1 P1 ;
        12

        Read: F B ;
        3
        """
        self.write(b"FB;")
        return self.read(12)

    def set_fast_key(self, state=bool()):
        """
        Set the fast key state

        P1 0: VFO-A FAST Key “OFF”
           1: VFO-A FAST Key “ON”

        Set & Answer: F S P1 ;
        4

        Read: F S ;
        3
        :param state: True or False
        """
        if state:
            self.write(b"FS1;")
        else:
            self.write(b"FS0;")

    def get_fast_key(self):
        """
        Get the fast key state

        P1 0: VFO-A FAST Key “OFF”
           1: VFO-A FAST Key “ON”

        Set & Answer: F S P1 ;
        4

        Read: F S ;
        3
        """
        self.write(b"FS;")
        return self.read(4)

    def set_acg(self, state=bytes()):
        """
        Set the ACG function

        P1 0: (Fixed)
        P2 0: AGC “OFF”
           1: AGC “FAST”
           2: AGC “MID”
           3: AGC “SLOW”
           4: AGC “AUTO”
        P3 0: AGC “OFF”
           1: AGC “FAST”
           2: AGC “MID”
           3: AGC “SLOW”
           4: AGC “AUTO-FAST”
           5: AGC “AUTO-MID”
           6: AGC “AUTO-SLOW”

        Set: G T P1 P2 ;
        5

        Read: G T P1 ;
        4

        Answer: G T P1 P3 ;
        5
        """
        if state not in [ACG_OFF, ACG_FAST, ACG_MID, ACG_SLOW, ACG_AUTO]:
           return

        cmd = b"GT0" + state + b";"
        self.write(cmd)

    def get_acg(self):
        """
        Get the ACG function

        P1 0: (Fixed)
        P2 0: AGC “OFF”
           1: AGC “FAST”
           2: AGC “MID”
           3: AGC “SLOW”
           4: AGC “AUTO”
        P3 0: AGC “OFF”
           1: AGC “FAST”
           2: AGC “MID”
           3: AGC “SLOW”
           4: AGC “AUTO-FAST”
           5: AGC “AUTO-MID”
           6: AGC “AUTO-SLOW”

        Set: G T P1 P2 ;
        5

        Read: G T P1 ;
        4

        Answer: G T P1 P3 ;
        5
        """
        self.write(b"GT0;")
        return self.read(5)

    def get_identification(self):
        """
        Get the identification

        P1 0650: FT-891

        Read: I D ;
        3

        Answer: I D P1 P1 P1 P1 ;
        7
        """
        self.write(b"ID;")
        return self.read(7)

