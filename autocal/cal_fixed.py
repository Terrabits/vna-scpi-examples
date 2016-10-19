#!/usr/bin/env python

# Handle python 2, 3 input
try:
	input = raw_input
except:
	pass

from rohdeschwarz.instruments.vna import Vna

ip_address = '127.0.0.1'
timeout_ms = 5*60*1000 # 5 mins

vna = Vna()
vna.open_tcp(ip_address)

# Start Full N port cal
vna.write("SENS1:CORR:COLL:AUTO:ASS:DEL:ALL")
vna.write("SENS1:CORR:COLL:AUTO:CONF FNPort,''")

# Define calibration steps
vna.write("SENS1:CORR:COLL:AUTO:ASS1:DEF 1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8")
vna.write("SENS1:CORR:COLL:AUTO:ASS2:DEF 1,1,9,2,10,3,11,4,12,5,13,6,14,7,15,8")
vna.write("SENS1:CORR:COLL:AUTO:ASS3:DEF 1,1,16,2,17,3,18,4,19,5,20,6")

# Run calibration steps
input('Start cal step 1?')
vna.write("SENS1:CORR:COLL:AUTO:ASS1:ACQ")
vna.pause(timeout_ms)
input('Start cal step 2?')
vna.write("SENS1:CORR:COLL:AUTO:ASS2:ACQ")
vna.pause(timeout_ms)
input('Start cal step 3?')
vna.write("SENS1:CORR:COLL:AUTO:ASS3:ACQ")
vna.pause(timeout_ms)

vna.write("SENS1:CORR:COLL:AUTO:SAVE")
vna.local()
vna.close()