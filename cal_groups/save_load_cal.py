#!/usr/bin/env python

from rohdeschwarz.instruments.vna import Vna

# Connect
vna = Vna()
vna.open_tcp()

# Applying example in channel 1
channel   = 1

# Load cal group
# Assuming cal group called "my_cal_group"
# cal group files have .cal extension
cal_group = "my_cal_group.cal";

scpi = ":MMEM:LOAD:CORR {0}, '{1}'"
scpi = scpi.format(channel, cal_group)
vna.write(scpi);
vna.pause()

# Saving a calibration to a cal group
new_cal_group = "my_new_cal.cal"

scpi = ":MMEM:STOR:CORR {0}, '{1}'"
scpi = scpi.format(channel, new_cal_group)
vna.write(scpi);
vna.pause()

vna.close()
