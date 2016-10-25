#!/usr/bin/env python

import numpy as np
from rohdeschwarz.instruments.vna import Vna

# Function for querying vna ports
# that are connected to the cal unit
# Assumes only one cal unit is connected
def connections(vna):
	# returns vna -> cal unit port connection pairs
	# cal unit port 0 means vna port not connected
	ports = vna.query("SENS:CORR:COLL:AUTO:PORT:CONN?")

	# Parse result string
	# Return vna ports that are connected
	ports = ports.split(',')
	ports = [int(i) for i in ports]
	ports = np.reshape(ports, (len(ports)/2, 2))
	ports = [port[0] for port in ports if port[1] != 0]
	return sorted(ports)

# Function that returns the steps needed
# to calibrate [ports] using a cal unit
# with num_ports ports
# example:
#     get_cal_steps([1,2,3,4,5], 4)
#       # => [[1,2,3,4], [1,5]] (2 steps)
def get_cal_steps(ports, num_ports):
	ports.sort()
	port1 = ports.pop(0)
	steps = []
	while ports:
		if len(ports) < num_ports-1:
			step = [port1]
			step += ports
			steps.append(step)
			del ports[:]
		else:
			step = [port1]
			step += ports[:num_ports-1]
			steps.append(step)
			del ports[:num_ports-1]
	return steps

