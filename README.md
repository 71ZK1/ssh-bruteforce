# SSH Brute Forcer by LiZKi

A simple Python script to perform brute-force attacks on SSH servers using a list of passwords.

> ⚠️ **DISCLAIMER:** This tool is for educational and authorized testing purposes only. Do not use this tool on systems you do not own or have explicit permission to test. Unauthorized use is illegal.

---

## 🚀 Features

- Attempts SSH login using a given username and password wordlist.
- Handles SSH timeouts, authentication failures, and protocol exceptions gracefully.
- Clean console output for tracking progress.
- Works with Python 3.6+

---
##  installation 
```bash
sudo apt update && upgrade
sudo apt install git
gitclone https://github.com/71ZK1/ssh-bruteforce
cd ssh-bruteforce
python3 ssh.py


##  Requirements

- Python 3.6+
- `paramiko` module


Install dependencies:

```bash
pip install paramiko
