#!/usr/bin/python3
import time
import Hamlib

VFOA = Hamlib.RIG_VFO_A
VFOB = Hamlib.RIG_VFO_B

Hamlib.rig_set_debug(Hamlib.RIG_DEBUG_NONE)

rig = Hamlib.Rig(Hamlib.RIG_MODEL_FT891)
rig.set_conf("rig_pathname", "/dev/ttyUSB0")
rig.set_conf("retry", "5")
rig.set_conf("serial_speed", "38400")

rig.open()

rig.set_freq(VFOA, 7150000)
rig.set_freq(VFOB, 14250000)
rig.set_level(Hamlib.RIG_LEVEL_AF, 0.5)
rig.set_func(Hamlib.RIG_FUNC_NB, False)
rig.get_level_f(Hamlib.RIG_POWER_OFF)

print("\n")
print("Audio Level:\t\t%0.2f" % rig.get_level_f(Hamlib.RIG_LEVEL_AF))
print("Signal Strength:\t%s dB" % rig.get_level_i(Hamlib.RIG_LEVEL_STRENGTH))
print("Freq VFOA:\t\t%0.0f hz" % rig.get_freq(VFOA))
print("Freq VFOB:\t\t%0.0f hz" % rig.get_freq(VFOB))
print("Noise Blanker:\t\t%s" % rig.get_func(Hamlib.RIG_FUNC_NB))
print("Status(str):\t\t%s" % Hamlib.rigerror(rig.error_status))
print("\n")
print("_" * 25)
print("\n")

time.sleep(3)

rig.set_freq(VFOA, 14250000)
rig.set_freq(VFOB, 7150000)
rig.set_level(Hamlib.RIG_LEVEL_AF, 0.1)
rig.set_func(Hamlib.RIG_FUNC_NB, True)

print("Audio Level:\t\t%0.2f" % rig.get_level_f(Hamlib.RIG_LEVEL_AF))
print("Signal Strength:\t%s dB" % rig.get_level_i(Hamlib.RIG_LEVEL_STRENGTH))
print("Freq VFOA:\t\t%0.0f hz" % rig.get_freq(VFOA))
print("Freq VFOB:\t\t%0.0f hz" % rig.get_freq(VFOB))
print("Noise Blanker:\t\t%s" % rig.get_func(Hamlib.RIG_FUNC_NB))
print("Status(str):\t\t%s" % Hamlib.rigerror(rig.error_status))
print("\n")
print("_" * 25)
print("\n")

rig.close()