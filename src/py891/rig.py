from serial import Serial
import logging

ENCODER = "UTF-8"
CTCSS_TONES = {"67.0": b"000", "69.3": b"001", "71.9": b"002",
               "74.4": b"003", "77,0": b"004", "79.7": b"005"}
DCS_CODES = {}
TUNER_OFF = b"0"
TUNER_ON = b"1"
TUNING_START = b"2"


class FT891(Serial):
    def __init__(self, port, baudrate, write_timeout):
        super().__init__(port=port, baudrate=baudrate, write_timeout=write_timeout)

        self._port = port
        self._baudrate = baudrate
        self._write_timeout = write_timeout
        logging.basicConfig(filename="./debug.log", encoding=ENCODER, level=logging.DEBUG)

    def swap_vfo(self):
        """Swap VFO's"""
        self.write(b"SV;")

    def set_vfoa_2_vfob(self):
        """Set VFOA -> VFOB"""
        self.write(b"AB;")

    def set_tuner(self, state):
        """Set tuner state"""
        if state != TUNER_ON and state != TUNER_OFF and state != TUNING_START:
            return
        else:
            self.write(b"AC00" + state + b";")

    def set_tuning_start(self):
        """Set tuning start"""
        self.write(b"AC002;")

    def get_tuner_state(self):
        """Get the tuner state"""
        self.write(b"AC;")
        return self.read(6)

    def set_af_gain(self, level=str()):
        """Set the AF gain level"""
        lev = bytes(level, ENCODER)
        cmd = b"AG0" + lev + b";"
        self.write(cmd)

    def get_af_gain(self):
        """Get the AF gain"""
        self.write(b"AG0;")
        return self.read(7)

    def set_vfoa_2_mem(self):
        """Set VFOA -> MEM"""
        self.write(b"AM;")

    def set_vfob_2_vfoa(self):
        """Set VFOB -> VFOA"""
        self.write(b"BA;")

    def set_auto_notch(self, state):
        """Set auto notch"""
        if state:
            self.write(b"BC01;")
        else:
            self.write(b"BC00;")

    def get_auto_notch(self):
        """Get the auto notch state"""
        self.write(b"BC0;")
        return self.read(5)

    def set_band_down(self):
        """Set the band down"""
        self.write(b"BD0;")

    def set_band_up(self):
        """Set the band up"""
        self.write(b"BU0;")

    def set_break_in(self, state=bool()):
        """Set break-in state"""
        if state:
            self.write(b"BI1;")
        else:
            self.write(b"BI0;")

    def get_break_in(self):
        """Get the break-in state"""
        self.write(b"BI;")
        return self.read(4)

    def set_manual_notch(self, state=bool()):
        """Set the notch state"""
        if state:
            self.write(b"BP001;")
        else:
            self.write(b"BP00;")

    def set_manual_notch_level(self, level=str()):
        """Set the manual notch level"""
        lev = bytes(level, ENCODER)
        cmd = b"BP01" + lev + b";"
        self.write(cmd)

    def get_manual_notch_state(self):
        """Get the manual notch state"""
        self.write(b"BP00;")
        return self.read(8)

    def get_manual_notch_level(self):
        """Get the manual notch level"""
        self.write(b"BP01;")
        return self.read(8)

    def set_band(self, band):
        """Set the band"""
        b = bytes(band, ENCODER)
        cmd = b"BS" + b + b";"
        self.write(cmd)

    def get_busy(self):
        """Get the busy state"""
        self.write(b"BY;")
        return self.read()

    def set_clar(self, state):
        """Set the CLAR state"""
        if state:
            self.write(b"CF010;")
        else:
            self.write(b"CF000;")

    def get_clar(self):
        """Get the CLAR state"""
        self.write(b"CF0;")
        return self.read(6)

    def set_channel_up(self):
        """Set the channel up"""
        self.write(b"CH0;")

    def set_channel_down(self):
        """Set the channel down"""
        self.write(b"CH1;")

    def set_ctcss_tone(self, tone):
        """Set the CTCSS tone"""
        cmd = b"CN00" + CTCSS_TONES[tone] + b";"
        self.write(cmd)

    def set_dcs_code(self, code):
        """Set the DCS code"""
        cmd = b"CN01" + DCS_CODES[code] + b";"
        self.write(cmd)

    def get_ctcss_tone(self):
        """Get the CTCSS tone"""
        self.write(b"CN00;")
        return self.read(8)

    def get_dcs_code(self):
        """Get the DCS code"""
        self.write(b"CN01;")
        return self.read(8)

    def set_contour_state(self, state):
        """Set the contour state"""
        if state:
            self.write(b"CO000001;")
        else:
            self.write(b"CO000000;")

    def set_contour_freq(self, freq):
        """Set the contour freq"""
        f = bytes(freq, ENCODER)
        cmd = b"CO01" + f + b";"
        self.write(cmd)

    def set_contour_apf_state(self, state):
        """Set the contour APT state"""
        if state:
            self.write(b"CO020001;")
        else:
            self.write(b"CO020000;")

    def set_controur_apf_freq(self, freq):
        """Set the contour APT freq"""
        f = bytes(freq, ENCODER)
        cmd = b"CO03" + f + b";"
        self.write(cmd)

    def get_contour_state(self):
        """Get the contour state"""
        self.write(b"CO00;")
        return self.read(9)

    def get_contour_freq(self):
        """Get the contour freq"""
        self.write(b"CO01;")
        return self.read(9)

    def get_contour_apf_state(self):
        """Get the contour APT state"""
        self.write(b"CO02;")
        return self.read(9)

    def get_contour_apf_freq(self):
        """Get the contour APT freq"""
        self.write(b"CO03;")
        return self.read(9)

    def set_cw_spot(self, state):
        """Set the CW spot state"""
        if state:
            self.write(b"CS1;")
        else:
            self.write(b"CS0;")

    def get_cw_spot(self):
        """Get the CW spot state"""
        self.write(b"CS;")
        return self.read(4)

    def set_ctcss_off(self):
        """Set CTCSS OFF"""
        self.write(b"CT00;")

    def set_ctcss_enc_dec(self):
        """Set CTCSS TX/RX ON"""
        self.write(b"CT01;")

    def set_ctcss_enc(self):
        """Set CTCSS TX ON"""
        self.write(b"CT02;")

    def set_dcs_on(self):
        """Set DCS ON"""
        self.write(b"CT03;")

    def get_ctcss_dcs_state(self):
        """Set CTCSS/DCS state"""
        self.write(b"CT0;")
        return self.read(5)
