# HCO-MetaX 🔐

> **⚠️ LEGAL DISCLAIMER:** This tool is developed strictly for educational purposes, authorized digital forensic analysis, and open-source threat research. Any unauthorized usage, cross-referencing, or target tracking without explicit legal consent is strictly prohibited. The developer (**Azhar / Hackers Colony Tech**) holds zero liability for any infrastructure misuse, legal infringements, or system violations caused by this script.

---

## 🧐 What is HCO-MetaX?
**HCO-MetaX** is an advanced open-source image forensics and Open Source Intelligence (OSINT) utility engineered for cybersecurity researchers and investigators. 

Even when standard EXIF data blocks are scrubbed or encrypted by social media transmission networks (such as WhatsApp, Facebook, or Instagram), this engine bypasses traditional limitations. By utilizing standard file headers, file structures, and advanced pixel matrix evaluations via local statistical analysis, it extracts hidden digital footprints directly from standard images or system UI buffer dumps (screenshots).

---

## 📊 Extracted Information Breakdown
The framework comprehensively runs **22+ Advanced Technical & Forensic Parameters** to gather structural data:

1. **File Structural Format:** Authentic structure verification (JPEG/PNG/GIF framework).
2. **Source Origin Heuristics:** Detects whether the file is a screenshot, raw camera capture, or a social media transit object (WhatsApp, Facebook, Instagram optimization signatures).
3. **Cryptographic Hash MD5:** Generates a unique 128-bit digital file fingerprint.
4. **Cryptographic Hash SHA256:** Generates a professional 256-bit secure tamper-verification signature.
5. **Binary Payload Weight:** Exact file system storage footprint in Kilobytes (KB) and Bytes.
6. **Pixel Resolution Profile:** Sensor grid array dimensions and total Megapixels.
7. **Display Grid Layout Mode:** Detects Landscape, Portrait, or Square Grid arrangements.
8. **Core Image Aspect Ratio:** True mechanical reduction layout format.
9. **Channel Bit-Depth Model:** Bit depth parameters (e.g., True Color RGB, Alpha Transparency channels, or Grayscale patterns).
10. **Color Palette Dominance:** Evaluates channel values to detect Red, Green, or Blue spectrum profiles.
11. **Scene Complexity Analysis:** Estimates visual entropy, complex spatial distributions, or flat graphical layers.
12. **Compression Byte Density:** Structural byte distribution density per pixel.
13. **Hardware Capturing Angle:** Original sensor alignment logic during capture (0°, 90°, 180°, or 270°).
14. **Time Stamp Log Matrix:** Extracted core chronological date and timestamp records.
15. **Target Time Zone Area:** Hardware local UTC/GMT clock offset configurations.
16. **Operational Day/Night Log:** Evaluates hour headers to estimate whether the asset was captured under daylight or nocturnal sequences.
17. **Hardware Vendor Signature:** Camera manufacturer profile strings (Make).
18. **Specific Device Build ID:** Exact hardware module index or operating kernel description (Model).
19. **Optical Lens Architecture:** Advanced integrated physical lens profiles.
20. **Aperture Shutter Value:** F-number exposures for advanced lens configurations.
21. **Active Focal Distance:** Lens focal length metric calculation.
22. **Light Sensor Flash State:** Identifies whether an artificial light burst (flash) fired or ambient configurations were utilized.
23. **🚨 GPS Geolocation Decryption:** Decrypts latitude/longitude coordinate grids and generates a direct **Google Maps Live Tracker Link** whenever location metadata tags are present in the core framework.

---

## 🛠️ Installation Guide For Kali Linux

Open your terminal environment and run the following deployment protocol sequentially:

```bash
# Update local repository structures
sudo apt update && sudo apt upgrade -y

# Install core dependencies and git
sudo apt install python3 python3-pip python3-pil git -y

# Clone the reposite 
 git clone https://github.com/OFFICIALcybersatyam27/hco_metax.git

# Navigate into the core deployment matrix
cd hco_metax

# Set execution rights for the installation script
chmod +x setup.sh

# Initialize the ecosystem environment
python3 -m pip install pillow

# Execute the master intelligence framework
python3 hco_metax.py

```bash
##📲 Installation Guide For Termux (Android)
​Copy and execute these deployment parameters step-by-step into your Termux console:

# Update and sync package repositories
pkg update -y && pkg upgrade -y

# Install Python and Git architectures
pkg install python git -y

# Install secondary library compilers required for pillow
pkg install libjpeg-turbo libtiff -y

# Clone the core system directory
git clone https://github.com/OFFICIALcybersatyam27/hco_metax.git

# Navigate inside the active directory block
cd hco_metax

# Allocate execution permissions to the automated script
chmod +x setup.sh


# Run the automated dependency installer script
./setup.sh

# Execute the core metadata tracking engine
python hco_metax.py

```
#🌐 Community Channels & Support Links
​Thank you for utilizing the HCO-MetaX module! Do support us to keep making advanced tools. If you encounter setup errors, configuration issues, or require assistance, do join us for any help via our community channels:
​📺 YouTube Channel: Hackers Colony Tech
​💬 WhatsApp Group: Join Official WhatsApp Matrix
​✈️ Telegram Portal: Join Official Telegram Channel
​<p align="center">
<b>This tool is Coded with ❤️ by SRY-OFFICIAL_cyber_satyam27</b>

<sub>© OFFICIAL_cyber_satyam27. All rights reserved.</sub>
</p>
