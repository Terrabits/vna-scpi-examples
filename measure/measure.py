from rohdeschwarz.instruments.vna import Vna

# Connect
vna = Vna()
vna.open_tcp()

# For touchstone file:
channel             = 1
ports_string        = "1,2,3,4"
touchstone_filename = "ch1_data.s4p"

# For trace data:
trace_name          = "Trc1"
trace_filename      = "Trc1.csv"

# Indicate which ports you want to
# capture data for before starting sweep
# Note: This must be done for each channel
# Using channel 1 for illustrative purposes:
channel = 1
scpi         = ":CALC{0}:PAR:DEF:SGR {1}"
scpi         = scpi.format(channel, ports_string)
vna.write(scpi)

# Enable manual sweep mode
# (i.e. control timing)
vna.write("INIT:CONT:ALL 0")

# Start all sweeps
vna.write("INIT:SCOP ALL")
vna.write("INIT")

# Wait for sweeps to finish
# Note: Make sure timeout is long
#       enough for sweeps to complete
vna.query("*OPC?")

# Save touchstone file to vna
# Complex formats are:
# - COMP (Re, Im)
# - LINP (Linear magnitude,   phase [deg])
# - LOGP (Log magnitude [dB], phase [deg])
complex_format = "COMP"
scpi = ":MMEM:STOR:TRAC:PORT {0},'{1}',{2},{3}"
scpi = scpi.format(channel, 'temp.s4p', complex_format, ports_string)
vna.write(scpi)

# Save trace data to vna as
# displayed on screen
# Note: See command documentation for
#       additional data format options
scpi = ":MMEM:STOR:TRAC '{0}', '{1}', FORM"
scpi = scpi.format(trace_name, 'temp.csv')
vna.write(scpi)

# Wait for saves to complete
vna.query("*OPC?")

# Transfer files from vna
# - See read_file.py
vna.file.download_file("temp.s4p", touchstone_filename)
vna.file.download_file("temp.csv", trace_filename)

# Delete files from vna
vna.file.delete("temp.s4p")
vna.file.delete("temp.csv")

vna.close()