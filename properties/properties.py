from rohdeschwarz.instruments.vna import Vna

# Connect
vna = Vna()
vna.open_tcp()

# Parse ID String
# Example:
#     "Rohde-Schwarz,ZNBT8-16Port,1318700624100104,2.70"
#     Manufacturer [0]: Rohde-Schwarz
#     Model        [1]: ZNBT8-16Port
#     Serial No    [2]: 1318700624100104
#     Firmware Ver [3]: 2.70
[manufacturer, model, serial_no, firmware_ver] = vna.query("*IDN?").split(",")

# Query number of physical ports
scpi  = ":INST:PORT:COUN?"
ports = int(vna.query(scpi)) # => 16
print("Ports:    {0}".format(ports))

# Query max frequency
scpi        = ":SYST:FREQ? MAX"
max_freq_Hz = float(vna.query(scpi)) # => 8.5E9 (8.5 GHz)
print("Max Freq: {0:.3e} Hz".format(max_freq_Hz))

# Query min frequency
scpi        = ":SYST:FREQ? MIN"
min_freq_Hz = float(vna.query(scpi)) # => 9.0E3 (300 KHz)
print("Min Freq: {0:.3e} Hz".format(min_freq_Hz))

vna.close()
