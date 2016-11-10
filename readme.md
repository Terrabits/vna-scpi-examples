SCPI Command Examples
=====================
This project contains several Rohde & Schwarz VNA programming examples to help you get started. The examples are in python, but they all use raw SCPI commands and can be translated with a little effort into any language. Each script is commented liberally to help in this regard.

The examples are divided into sections. SCPI command documentation is also included in the `commands\` folders for each section. This documentation comes from the ZNB manual.

Sections
--------

The examples are organized into the following sections, with a folder corresponding to each:  

### Properties
Query the VNA model, number of ports and frequency range to make sure that it suits your needs before you start measurement.

### Autocal
Programmatically control calibration with an autocal unit as part of your test automation.

### Deembedding
Apply deembedding for each port from touchstone (`s2p`) files.

### File Transfer
Read (download) and write (upload) files to and from the VNA

### Measure
Examples on performing the following:
- Performing a synchronous sweep
- Saving a touchstone (`snp`) file
- Saving trace data to a `csv` file

### Screenshots
After performing the measurement as outlined in the section above, save screenshots of individual diagrams or the entire screen to file.
