#!/usr/bin/env python

import numpy as np
from rohdeschwarz.instruments.vna import Vna

def connections(vna):
	# Query connected ports
	ports = vna.query("SENS:CORR:COLL:AUTO:PORT:CONN?")
	ports = ports.split(',')
	ports = [int(i) for i in ports]
	ports = np.reshape(ports, (len(ports)/2, 2))
	ports = [port[0] for port in ports if port[1] != 0]
	return sorted(ports)

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

print(get_cal_steps(range(1,21), 8))

# def main():
# 	print("This works!")
