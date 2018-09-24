**Version 1.0:**
- Initial program release
- Added Nmap scan using switch -sV #credit to Alexandre Norman (xael) for some of the Nmap code 

**Version 1.1:**
- Added Nikto Scanner
- Added Fierce Scanner
- Added NBTScan Scanner
- Added Snmpwalk Scanner
- Added Enum4Linux Scanner
- Added Function for creating output for a folder for scan results

**Version 1.2:**
- Added FTP Anonymous Login Attempt
- Added FTP Bruteforce Login Attempt
- Removed spaces by the print statements and added tabs instead
- Added target IP address to be part of the generated folder name to distinguish from different IP scans

**Version 1.3:**
- Added GoBuster
- Added FTP Anonymous Directory Enumeration
- Changed SNMPWalk to SNMPCheck
- Change Nmap scanning command to `-n -sV --min-rate 5000 --max-retries 2 -p-` for faster scanning
- Removed the color coding at the end of the scan because it throws off the terminal coloring
- Fixed general bugs in code