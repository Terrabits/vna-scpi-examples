from rohdeschwarz.instruments.vna import Vna

# Connect
vna = Vna()
vna.open_tcp()

# For the purposes of demonstration:
# - create set file (.znx) on vna
# - wait for save to complete
vna.save_active_set('read.znx')
vna.query("*IDN?")

# define filenames
source     = "C:\\Users\\Public\\Documents\\Rohde-Schwarz\\Vna\\RecallSets\\read.znx"
local_dest = "read.znx"

# Query contents of source
scpi       = "MMEM:DATA? '{0}'"
scpi       = scpi.format(source)
vna.write(scpi)
block_data = vna.read_raw_no_end()

# Start parsing IEEE 388.2 block data transfer format
# Header: #<header_size-2><file_size>
header_size   = int(block_data[1])
file_start    = 2 + header_size
file_size     = int(block_data[2:file_start])

# Sometimes the contents of the entire file
# may not transfer at once. Keep reading
# until everything is transferred
while len(block_data) < 2 + header_size + file_size:
	block_data += vna.read_raw_no_end()

file_contents = block_data[file_start:file_start+file_size]
# Note: It's important to only read the amount
#       of data in the file, as an EOI may
#       sometimes follow the contents

# Write file_contents to file
f = open(local_dest, 'wb')
f.write(file_contents)
f.close()

# Clean up:
# Remove 'read.znx' from VNA
# Wait for delete to finish
vna.file.delete(source)
vna.query("*OPC?")

vna.close()