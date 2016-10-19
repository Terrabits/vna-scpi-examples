#!/usr/bin/env python

# Handle python 2, 3 input
# differences
try:
	input = raw_input
except:
	pass

from connections import connections
from rohdeschwarz.instruments.vna import Vna

ip_address = '127.0.0.1'
timeout_ms = 5*60*1000 # 5 mins

vna = Vna()
vna.open_tcp(ip_address)

# Start Full N port cal
vna.write("SENS1:CORR:COLL:AUTO:ASS:DEL:ALL")
vna.write("SENS1:CORR:COLL:AUTO:CONF FNPort,''")

# Define calibration steps
vna.write("SENS1:CORR:COLL:AUTO:ASS1:DEF:TPOR 1,2,3,4,5,6,7,8")
vna.write("SENS1:CORR:COLL:AUTO:ASS2:DEF:TPOR 1,9,10,11,12,13,14,15")
vna.write("SENS1:CORR:COLL:AUTO:ASS3:DEF:TPOR 1,16,17,18,19,20")

# Run calibration step 
while connections(vna) != [1,2,3,4,5,6,7,8]:
	input('Connect ports 1-8')
vna.write("SENS1:CORR:COLL:AUTO:ASS1:ACQ")
vna.pause(timeout_ms)

while connections(vna) != [1,9,10,11,12,13,14,15]:
	input('Connect ports 1, 9-15')
vna.write("SENS1:CORR:COLL:AUTO:ASS2:ACQ")
vna.pause(timeout_ms)

while connections(vna) != [1,16,17,18,19,20]:
	input('Connect ports 1, 16-20')
vna.write("SENS1:CORR:COLL:AUTO:ASS3:ACQ")
vna.pause(timeout_ms)

vna.write("SENS1:CORR:COLL:AUTO:SAVE")
vna.local()
vna.close()
