#!/usr/bin/env python

# Handle python 2, 3 input
# differences
try:
	input = raw_input
except:
	pass

from cal_functions import connections
from cal_functions import get_cal_steps
from rohdeschwarz.instruments.vna import Vna

# Provide this information:
ip_address = '127.0.0.1'
timeout_ms = 5*60*1000 # 5 mins
ports      = range(1,21) # VNA Ports 1-20
cal_size   = 8           # Cal unit is 8 ports

# Assuming channel 1 ('SENS1')
# for simplicity's sake

# Connect to VNA
vna = Vna()
vna.open_tcp(ip_address)

# Delete any previously defined cal steps
vna.write("SENS1:CORR:COLL:AUTO:ASS:DEL:ALL")

# Setup for full N-Port calibration with cal unit
vna.write("SENS1:CORR:COLL:AUTO:CONF FNPort,''")

# get cal steps
steps     = get_cal_steps(ports, cal_size)
num_steps = len(steps)

# Define each cal step via SCPI
for i in range(1, num_steps+1):
	step  = [str(n) for n in steps[i]]
	step  = ",".join(step)
	scpi  = "SENS1:CORR:COLL:AUTO:ASS{0}:TPOR {1}".format(i, step)
	vna.write(scpi)

# For each cal step:
# - Make sure vna ports are connected
# - Start measurement
# - Wait until it completes
for i in range(1, num_steps+1):
	while connections(vna) != steps[i]:
		input('Connect ports {0}'.format(step))
	vna.write("SENS1:CORR:COLL:AUTO:ASS{0}:ACQ".format(i))
	vna.pause(timeout_ms)

# Apply calibration
vna.write("SENS1:CORR:COLL:AUTO:SAVE")

# Close connection
vna.local()
vna.close()
