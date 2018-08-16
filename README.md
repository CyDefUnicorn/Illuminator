# Illuminator

Illuminator is designed to perform a comprehensive scan on a single IP using the tools that are listed below to save time when attempting to gather information on the specific host.

*Nmap*  
*Nikto*  
*Fierce*  
*NBTScan*  
*Snmpwalk*  
*Enum4Linux*  

Illuminator will start with an Nmap scan using the switch -sV, and generate a folder which will contain a text file with the results from each of the tools utilized. Depending on which ports and protocols are open, and the services that are running on those ports,  Illuminator will utilize the next tool from the list based on those ports and attempt to shed light on more information to assist you in the host enumeration process.

All the listed tools should already be available in **Kali Linux**

### Run the script
`./Illuminator.py <ip address>`