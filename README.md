# Illuminator

Illuminator is a Python based, OSCP inspired script that is designed to perform a comprehensive scan on a single IP using the tools that are listed below to save time when attempting to gather information on the specific host. As time goes by, I will update the script and add more features and capabilities. It's not perfect, but gotta start somewhere :)

*Nmap*  
*Nikto*  
*Fierce*  
*NBTScan*  
*Snmpwalk*  
*Enum4Linux*  

Illuminator will start with an Nmap scan using the switch -sV, and generate a folder which will contain a text file with the results from each of the tools utilized. Depending on which ports and protocols are open, and the services that are running on those ports,  Illuminator will utilize the next tool from the list based on those ports and attempt to shed light on more information to assist you in the host enumeration process.

All the listed tools should already be available in **Kali Linux**

You will need to install **python-nmap** using pip to aid in using Nmap with Python

`pip install python-nmap`

If for some reason that doesn't work, you can manually download it from **[here](https://xael.org/pages/python-nmap-en.html)** and install it 

### Run the script
`./Illuminator.py <ip address>`

### Example
![image](https://user-images.githubusercontent.com/22828882/44691637-7223d000-aa2d-11e8-9729-094cc0569a12.png)

###	Soon to Add
*GoBuster*