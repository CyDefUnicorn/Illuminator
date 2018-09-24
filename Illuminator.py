#!/usr/bin/python

import socket
import nmap
import sys
import io
from libnmap.parser import NmapParser, NmapParserException
from libnmap.process import NmapProcess
from time import sleep, time
from os import path, system, mkdir

#Function - Run Nmap FTP Anonymous and Bruteforce Scans
def run_nmap_ftp(ip, foldername):
    #Attempt FTP Anonymous Login
    print "\n[+] FTP Port 21 Detected\n"
    print "\t[-] Test 1: Starting FTP Anonymous Login Attempt..\n"
    system("nmap --script=ftp-anon --script-args ftp-anon.maxlist=-1 -p 21 \
    %s 2>&1 > %s" % (ip,path.join(foldername, "FTP-Anonymous-Scan")))
    print "\t\t[-] FTP Anonymous Login Attempt Complete.\n"

    #Attempt FTP Anonymous Directory Enumeration
    print "\t[-] Test 2: FTP Anonymous Directory Enumeration..\n"
    system("nmap -n -p 21 --script=ftp-anon.nse \
    %s 2>&1 > %s" % (ip,path.join(foldername, "FTP-Anonymous-Dir-Enum")))
    print "\t\t[-] FTP Anonymous Directory Enumeration Complete."

    #Attempt FTP Bruteforce
    print "\t[-] Test 3: FTP Brute Force Attempt..\n"
    system("nmap --script ftp-brute -p 21 \
    %s 2>&1 > %s" % (ip,path.join(foldername, "FTP-Bruteforce-Scan")))
    print "\t\t[-] FTP Brute Force Attempt Complete."


#Function - Run Nmap NSE script for SMB User Enumeration
def run_nmap_smb_users(ip, foldername):
    print "\n[+] SMB Ports Detected - Starting SMB Enum Users Scan..\n"
    system('nmap --script=smb-enum-users.nse -p 139,445 %s | grep -v "Account disabled" \
    | grep "Full name" | cut -d " " -f 7,10,11 2>&1 > %s' % (ip,path.join(foldername, "Nmap-SMB-Users")))
    print "\t[-] SMB Enum Users Scan Complete."


#Function - Run Nikto
def run_nikto(ip, foldername):
    print "\n[+] Starting Nikto Scan\n"
    #call nikto and run command against given IP
    system("nikto -h %s 2>&1 > %s" % (ip,path.join(foldername, "Nikto")))
    print "\t[-] Nikto Scan Complete."


#Function - Run SMTP scan    
def run_mailscan(ip, foldername):
    print "\n[+] SMTP Port 25 Detected - Starting SMTP User Enumeration..\n"
    system("smtp-user-enum -M VRFY -U /usr/share/metasploit-framework/data/wordlists/unix_users.txt -t \
    %s 2>&1 > %s" % (ip,path.join(foldername, "SMTP-User-Unum")))
    print "\t[-] SMTP User Enumeration Complete."


#Function - Run Fierce for DNS
def run_fierce(ip, foldername):
    print "\n[+] Starting Fierce Scan\n"
    system("fierce -dns %s 2>&1 > %s" % (ip,path.join(foldername, "Fierce")))
    print "\t[-] DNS enumeration Complete."


#Function - Run SNMPCheck for SNMP
def run_snmpcheck(ip, foldername):
    print "\n[+] SNMP Port 161 Detected - Starting SNMPCheck Scan\n"
    system("snmpcheck-1.9.rb %s 2>&1 > %s" % (ip,path.join(foldername, "SNMPCheck")))
    print "\t[-] SNMP enumeration Complete."


#Function - Run Enum4Linux
def run_enum4linux(ip, foldername):
    print "\n[+] Starting SMB enumeration using Enum4Linux\n"
    system("enum4linux %s 2>&1 > %s" % (ip,path.join(foldername, "Enum4Linux")))
    print "  [-] SMB enumeration Complete."


#Function - Run Nmap scan
def nmap_scan(ip, options):
    parsed = None
    nmproc = NmapProcess(ip, options)
    rc = nmproc.run()
    if rc != 0:
        print("nmap scan failed: {0}".format(nmproc.stderr))

    try:
        parsed = NmapParser.parse(nmproc.stdout)
    except NmapParserException as e:
        print("Exception raised while parsing scan: {0}".format(e.msg))

    return parsed


#Function - Display Nmap scan results
def process_scan(nmap_report):
    for host in nmap_report.hosts:
        if len(host.hostnames):
            tmp_host = host.hostnames.pop()
        else:
            tmp_host = host.address
            
        #Display whether host is UP or DOWN   
        print("Host is [ %s ]\n" % str.upper(host.status))
        print("  PORT     STATE         SERVICE")

        for serv in host.services:
            #Check to see if ports are open
            if serv.state == "open":
                scanned_ports.append(serv.port)
            pserv = "{0:>5s}/{1:3s}  {2:12s}  {3}".format(
                    str(serv.port),
                    serv.protocol,
                    serv.state,
                    serv.service)
            if len(serv.banner):
                pserv += " ({0})".format(serv.banner)
            #Display Nmap scan results    
            print(pserv)
        
        #Display completion of Nmap scan
        print "\n  [-] Nmap Scan Complete."
         
         
#Defining global variables
scanned_ports = []
port_map = {80:run_nikto,25:run_mailscan,110:run_mailscan,995:run_mailscan,
            53:run_fierce,139:run_nmap_smb_users,21:run_nmap_ftp,161:run_snmpcheck}


#Program Banner
if len(sys.argv) <= 1:
    print(
"""
Illuminator - Shed light onto darkness\nVersion: 1.3\nAuthor: Sam Rassam @CyDef_Unicorn

Illuminator utilizes the following tools:

 * Nmap
 * Nikto
 * Fierce
 * NBTScan
 * SNMPCheck
 * Enum4Linux

Usage: Illuminator.py <IP Address>
""")
    sys.exit()
   
        
#Grab IP Address as argument
if len(sys.argv)==2:
    ip = sys.argv[1]
    print "\n[+] Reading IP Address"


#Banner - Pass IP to Nmap then start scanning
print "\n[+] Passing " + ip + " to Nmap..."
print("\n[+] Starting Nmap Scan\n")


#Create the folder "Illuminator"
foldername = "Illuminator-%s" % ip


#Create folder
mkdir (foldername)


report = nmap_scan(ip, "-n -sV --min-rate 5000 --max-retries 2 -p-")
if report:
    process_scan(report)
    for scanned_port in scanned_ports:
        if scanned_port in port_map:
            port_map [scanned_port](ip, foldername)
            
    #Run enum4linux seperately
    run_enum4linux(ip, foldername)
    
    print "\n[**] Reports Completed [**]\n"
else:
    print("No results returned")

