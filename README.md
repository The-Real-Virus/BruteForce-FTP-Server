# 💀BruteForce FTP Server💀

## 📜Description
The FTP Brute-Force Tool is a Python-based script designed for penetration testers and cybersecurity enthusiasts  
to audit the security of FTP servers by performing brute-force attacks.  
This tool supports multithreading for optimized performance and includes additional features  
like port scanning, wordlist generation, and logging of successful/failed attempts.  

## 🔑Features
- Brute-Force Attack: Perform dictionary-based brute-force attacks on FTP servers with customizable delay and multithreading.  
- Port Scanning: Scan for open ports to identify potential entry points on target servers.  
- Custom Wordlist Generator: Easily create targeted wordlists combining base words and years.  
- Attack Logs: Automatically saves results of successful and failed attempts in a log file for future reference.  
- Interactive Menu: User-friendly menu-driven interface for seamless navigation.  
- Banner & UX: Displays a detailed banner and cleans the screen for an optimal user experience.  

## 🚀Step-by-Step Guide in Linux Terminal !

Step 1: Update & upgrade your system  
>sudo apt update  
>sudo apt upgrade  

Step 2: Clone the repository  
>git clone https://github.com/The-Real-Virus/BruteForce-FTP-Server.git  

Step 3: Go to the Tool Directory where u clone it and read requirements.txt file !  
>cd BruteForce-FTP-Server  
(read requirements.txt file using cat or gedit)  

Step 4: extract the rockyou file using unrar  
>sudo apt install unrar (if it is not installed in ur kali linux)  
>unrar x rockyou.rar  

Step 5: After Completing the process now u can run script  
>python3 Script.py  

## ⚙️Troubleshooting

1) `UnicodeDecodeError when reading password files:`  
- Use a password file encoded in latin-1 or ensure compatibility by re-saving the file with proper encoding.  

2) `Permission Denied Errors:`  
- Ensure you have appropriate privileges to run the script (e.g., sudo on Linux).  

3) `Connection Issues:`  
- Verify the target FTP server is reachable, and the IP address/domain is correctly entered.  
- Ensure firewalls or network restrictions do not block access to the target server.  

4) `Missing Libraries:`  
- Install all required dependencies (read requirements.txt file).  

## 💡Tips !
- Use the port scanning feature(nmap is best) to identify open FTP ports before initiating brute-force attacks.  
- Select a smaller wordlist for testing purposes on slower systems or networks to save time.  
- Use multithreading for faster attacks, but be mindful of the target server's rate-limiting or anti-brute-force measures.  
- Always check the attack log to track progress and review results after completing an attack.  

## 🤝Follow the Prompts !
1) Enter the FTP server IP address or domain.  
2) Specify the username for the brute-force attack.  
3) Provide the password file location.  
4) Choose additional options like delay between attempts and the number of threads.  

## 🛠️MODIFICATION ( use own wordlist )

if u want to use ur own wordlist instead of rockyou.txt , u can modify in the script ,  

Step 1: create ur own wordlist  

Step 2: move it into the BruteForce-FTP-Server Directory ( deleting rockyou is not necessory )  

Step 3: While running the script , it ask for password file then type the name of ur own created list .  

## 📂Example OutPut
	Enter the FTP server IP address or domain (e.g., 192.168.1.1): 192.168.30.12
	Enter the username to brute-force (e.g., admin): admin
	Enter the path to the password file (e.g., rockyou.txt): rockyou.txt
	Enter delay between attempts in seconds (0 for no delay): 0
	Enter the number of threads to use (default 1): 5

	[*] Target FTP Server: 192.168.30.12
	[*] Username: admin
	[*] Passwords loaded: 14344393
	
	[1/14344393] Trying password: admin123
	[2/14344393] Trying password: password123
	...
	[+] Success! Password found: admin1234
	[+] Login successful for user 'admin' with password 'admin1234'
	
	[!] Brute-force attack completed. Logs saved in 'ftp_bruteforce_log.txt'
	
	Enter target IP address to scan: 192.168.30.12
	Enter the port range to scan (e.g., 20-1025): 20-100

	[*] Scanning target: 192.168.30.12
	[*] Scanning ports 20 to 100...
	
	[+] Open FTP Port Found: 21
	[!] Port scanning completed.
	
	[+] Attack Log:
	-------------------------------------
	[+] Date: 2025-01-17
	[*] Target: 192.168.30.12
	[*] Username: admin
	[*] Successful Password: admin1234
	[*] Failed Attempts: 34
	-------------------------------------

# ⚠️Disclaimer !
This tool is intended for ethical and educational use only.  
Do not use it for illegal activities. The author is not responsible for any misuse.  
This script is intended for educational purposes and authorized testing only.  
Unauthorized use of this script is illegal and unethical.  
Ensure you have explicit permission before testing any system.  
- Obtain explicit permission before testing any system.  
- Adhere to all applicable laws and regulations.  
- Respect user privacy and data.  
- By using this script, you agree to take full responsibility for your actions.  
