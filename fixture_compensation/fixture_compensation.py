#!/usr/bin/env python
from rohdeschwarz.instruments.vna import Vna

# Connect
vna = Vna()
vna.open_tcp()

channel      = 1;
ports_string = "1,2,3,4"
direct_comp  = "OFF"  # ON | OFF
include_loss = "ON"   # ON | OFF
standard     = "SHOR" # SHORt | OPEN

# Start fixture compensation
#   This clears previous offsets
scpi = "SENS{0}:CORR:COLL:FIXT:STAR"
scpi = scpi.format(channel)
vna.write(scpi)

# Direct compensation
#   corrections generated per frequency point
#   rather than with an overall electrical
#   length estimate.
scpi = "SENS{0}:CORR:COLL:FIXT:LMP {1}";
scpi = scpi.format(channel, direct_comp)
vna.write(scpi)

# include loss compensation
#   This setting is overridden if direct compensation
#   is on
scpi = "SENS{0}:CORR:COLL:FIXT:LMP:LOSS {1}";
scpi = scpi.format(channel, include_loss)
vna.write(scpi)

# Measure a standard (short) at all ports
scpi = "SENS{0}:CORR:COLL:FIXT:ACQ {1},{2}"
scpi = scpi.format(channel, standard, ports_string)
vna.write(scpi)
vna.pause(10000) # wait for 10 s

# Optional:
#   Can also measure another standard.
#   The VNA will use the average of both
#   results
standard = "OPEN"
scpi = "SENS{0}:CORR:COLL:FIXT:ACQ {1},{2}"
scpi = scpi.format(channel, standard, ports_string)
vna.write(scpi)
vna.pause(10000) # wait for 10 s

# Apply corrections
scpi = "SENS{0}:CORR:COLL:FIXT:SAVE"
scpi = scpi.format(channel)
vna.write(scpi)
vna.pause()

vna.close()
