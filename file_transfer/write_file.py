from rohdeschwarz.instruments.vna import Vna

# Connect
vna = Vna()
vna.open_tcp()

# Write local_file to dest
local_file = "write.znx"
dest       = "C:\\Users\\Public\\Documents\\Rohde-Schwarz\\Vna\\RecallSets\\write.znx"

data     = open(local_file, 'rb').read()
size_str = str(len(data))
header   = "#{0}{1}".format(len(size_str), size_str)

scpi     = "MMEM:DATA '{0}', {1}{2}"
scpi     = scpi.format(dest, header, data)
vna.write_raw_no_end(scpi)
vna.write_raw_no_end('\n') # EOI sometimes necessary

vna.close()