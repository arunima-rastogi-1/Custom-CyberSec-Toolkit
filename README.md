# CyberSec-Toolkit         
      
## Overview
**CyberSec-Toolkit** is a collection of cybersecurity-related tools designed for ethical hacking, penetration testing, and security research. The first tool in this repository is **WiFi Scanner**, a Java-based utility that scans available WiFi networks on a Windows machine using the Windows WLAN API via JNA.
   
## Features 
- Enumerates available WiFi interfaces.     
- Scans for nearby WiFi networks.
- Uses **Java Native Access (JNA)** to interact with the Windows WLAN API.
- Works on Windows without requiring external dependencies.

## Installation & Usage
 
### Prerequisites
- **Java 8+** installed
- **JNA Library** (`com.sun.jna`)
- Windows OS (since it interacts with Windows WLAN API)

### Running the WiFi Scanner
1. Clone the repository:
   ```sh
   git clone https://github.com/arunima-rastogi-1/CyberSec-Toolkit.git
   
2. Navigate to the WifiScanner directory:
   ```sh
   cd CyberSec-Toolkit/WifiScanner
   ```

3. Compile and run:
   ```sh
   javac -cp .;jna.jar src/com/example/seleniumdemo/WifiScanner.java
   java -cp .;jna.jar com.example.seleniumdemo.WifiScanner
   ```

## Future Tools (Planned)
Port Scanner
Network Packet Sniffer
Password Strength Analyzer
Bluetooth Device Scanner
File Integrity Checker

## Disclaimer
This repository is intended for educational and ethical research purposes only. Do not use these tools for unauthorized access or illegal activities.
  
## License
MIT License

## Contributions
Feel free to contribute by submitting pull requests or reporting issues! 
