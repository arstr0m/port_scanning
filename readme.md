# Nmap Port Scanner

Python script that uses the `nmap` library to scan the open ports of a given IP address. The script scans ports from 1 to 1024 using the SYN scan technique and prints the status of the IP and the open ports.

## Prerequisites

- Python 3.x
- `nmap` library for Python (`python-nmap`)

## Installation

1. Make sure you have Python installed. You can download it from [python.org](https://www.python.org/).

2. Install the `nmap` library for Python. You can install it using `pip`:

    ```sh
    pip install python-nmap
    ```

3. Ensure you have Nmap installed on your system. You can download it from [nmap.org](https://nmap.org/download.html).

## Usage

1. Save the following script in a file, for example, `nmap_scanner.py`:

    ```python
    import nmap

    scanner = nmap.PortScanner()
    ip = input("IP: ")

    try:
        scanner.scan(ip, "1-1024", "-v -sS -T2")
        print("IP Status:", scanner[ip].state())
        scanner[ip].all_protocols()
        print("Open Ports:")
        for port in scanner[ip]['tcp'].keys():
            print(port, scanner[ip]['tcp'][port]['state'])
    except nmap.PortScannerError as e:
        print("Error:", e)
    ```

2. Run the script:

    ```sh
    python nmap_scanner.py
    ```

3. Enter the IP address you want to scan when prompted.

4. The script will output the status of the IP and a list of open ports.

## Example Output

```sh
IP: 192.168.1.1
IP Status: up
Found Ports:
22 open
80 open
443 open
