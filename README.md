# Illuminator

Illuminator is designed to perform a comprehensive scan on a single IP using the tools that are listed below to save time when attempting to gather information on the specific host.

*Nmap*  
*Nikto*  
*Fierce*  
*NBTScan*  
*Snmpwalk*  
*Enum4Linux*  

Illuminator will start with an Nmap scan using the switch -sV, and generate a folder which will contain a text file with the results from each of the tools utilized. Depending on which ports and protocols are open, and the services that are running on those ports,  Illuminator will utilize the next tool from the list based on those ports and attempt to shed light on more information to assist you in the host enumeration process.

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

### Run the script
`./Illuminator.py <ip address>`