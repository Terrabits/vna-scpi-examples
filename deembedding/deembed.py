from rohdeschwarz.instruments.vna import Vna
import os

# Connect
vna = Vna()
vna.open_tcp()

channel  = 1
ports    = range(1, 5) # Ports 1-4
filename = "test.s2p"
# s2p file must exist locally on VNA

for port in ports:
	# Set deembed model to touchstone file
	scpi     = "CALC{0}:TRAN:VNET:SEND:DEEM{1}:TND FIMP"
	scpi     = scpi.format(channel, port)
	vna.write(scpi)

	## Option a:
	## Set via touchstone file on VNA
	# scpi     = "MMEM:LOAD:VNET{0}:SEND:DEEM{1} '{2}'"
	# scpi     = scpi.format(channel, port, filename)
	# vna.write(scpi)

	# Option b:
	# Set via data transfer
	data     = open(filename, 'rb').read()
	size_str = str(len(data))
	header   = "#{0}{1}".format(len(size_str), size_str)
	scpi     = "CALC{0}:TRAN:VNET:SEND:DEEM{1}:PAR:DATA FPOR,{2}{3}"
	scpi     = scpi.format(channel, port, header, data)
	vna.write(scpi)

	# Turn deembedding on
	scpi     = "CALC{0}:TRAN:VNET:SEND:DEEM{1} 1"
	scpi     = scpi.format(channel, port)
	vna.write(scpi)

vna.close()
