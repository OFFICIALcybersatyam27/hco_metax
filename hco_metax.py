import os
import sys
import time
import subprocess
import re
import hashlib
from PIL import Image, ImageStat
from PIL.ExifTags import TAGS, GPSTAGS

# Premium Hacker Terminal Color Palette
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"

def lock_and_redirect():
    print(f"{RED}[🔒 SYSTEM LOCK] This tool is locked 🔐{RESET}")
    print(f"{YELLOW}[*] Like, subscribe & click on the bell 🔔 icon to unlock 🔓{RESET}")
    print(f"{CYAN}[*] Redirecting to Youtube app...{RESET}\n")
    time.sleep(1)
    
    countdown_colors = [RED, MAGENTA, YELLOW, BLUE, CYAN, GREEN, BOLD+GREEN, BOLD+CYAN]
    for i in range(8, 0, -1):
        color = countdown_colors[i-1]
        sys.stdout.write(f"\r{color}[⏳] Redirecting in: {i}...{RESET}")
        sys.stdout.flush()
        time.sleep(1)
    print("\n")
    
    url = "https://youtube.com/@official_cyber_satyam27?si=KIjUlKKtDObLRGT9"
    try:
        if sys.platform == "linux" and "com.termux" in os.environ.get("PREFIX", ""):
            subprocess.Popen(["am", "start", "-a", "android.intent.action.VIEW", "-d", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif sys.platform == "win32":
            os.system(f"start {url}")
        else:
            os.system(f"xdg-open {url}")
    except:
        pass

    print(f"{MAGENTA}=========================================================================={RESET}")
    input(f"{GREEN}[➔] Click ENTER to run the tool: {RESET}")
    os.system('clear' if os.name != 'nt' else 'cls')

def print_banner():
    print(f"{RED}{BOLD}██╗  ██╗ ██████╗ ██████╗      ███╗   ███╗███████╗████████╗ █████╗ ██╗  ██╗{RESET}")
print(f"{ORANGE}{BOLD}██║  ██║██╔════╝██╔═══██╗     ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗╚██╗██╔╝{RESET}")
print(f"{GOLD}{BOLD}███████║██║     ██║   ██║     ██╔████╔██║█████╗     ██║   ███████║ ╚███╔╝ {RESET}")
print(f"{LIME}{BOLD}██╔══██║██║     ██║   ██║     ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║ ██╔██╗ {RESET}")
print(f"{CYAN}{BOLD}██║  ██║╚██████╗╚██████╔╝     ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║██╔╝ ██╗{RESET}")
print(f"{MAGENTA}{BOLD}╚═╝  ╚═╝ ╚═════╝ ╚═════╝      ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝{RESET}")

print(f"{NEON}╔════════════════════════════════════════════════════════════════════════════╗{RESET}")
print(f"{SKY}{BOLD}║                 ⌬ HCO-METAX-SRY METADATA INTELLIGENCE SYSTEM ⌬           ║{RESET}")
print(f"{PINK}║                     ⚡ Powered by OFFICIALcybersatyam27 ⚡               ║{RESET}")
print(f"{PURPLE}║               👑 BY 𒉭 ᎠᴀʀᴋㅤᏙᴇɴᴏᴍ | 𝐄𝐌𝐏𝐄𝐑𝐎𝐑 👑                    ║{RESET}")
print(f"{GREEN}╚════════════════════════════════════════════════════════════════════════════╝{RESET}\n")
def convert_to_degrees(value):
    try:
        d = float(value[0])
        m = float(value[1])
        s = float(value[2])
        return d + (m / 60.0) + (s / 3600.0)
    except:
        return None

def verify_file_integrity(file_path):
    try:
        with open(file_path, 'rb') as f:
            header = f.read(4)
            if header.startswith(b'\xff\xd8\xff'): return "JPEG / JPG Forensic Matrix"
            elif header.startswith(b'\x89PNG'): return "Portable Network Graphics (PNG)"
            elif header.startswith(b'GIF8'): return "Graphics Interchange Format (GIF)"
            else: return "Unknown Binary Stream Model"
    except:
        return "Unreadable Structural Bytes"

def calculate_hashes(file_path):
    md5_hash = hashlib.md5()
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                md5_hash.update(byte_block)
                sha256_hash.update(byte_block)
        return md5_hash.hexdigest().upper(), sha256_hash.hexdigest().upper()
    except:
        return "ERR_CALC", "ERR_CALC"

def analyze_image(image_path):
    filename = os.path.basename(image_path)
    print(f"\n{CYAN}[⚙️ Processing Target Payload]: {filename}{RESET}")
    print(f"{BLUE}--------------------------------------------------------------------------{RESET}")
    
    if not os.path.exists(image_path):
        print(f"{RED}[Error] Analysis Interrupted: Target structural node inaccessible.{RESET}")
        return

    try:
        # Cryptographic Data Fingerprinting
        md5_f, sha256_f = calculate_hashes(image_path)
        file_bytes = os.path.getsize(image_path)
        file_kb = round(file_bytes / 1024, 2)
        
        # Load Image Layer for Deeper Computations
        image = Image.open(image_path)
        width, height = image.size
        megapixels = round((width * height) / 1000000, 2)
        
        # Structural Verification & Compression Check
        structural_format = verify_file_integrity(image_path)
        byte_density = round(file_bytes / (width * height), 3)

        # Aspect Ratio & Screen Grid Vector logic
        def gcd(a, b):
            while b: a, b = b, a % b
            return a
        r_gcd = gcd(width, height)
        aspect_ratio = f"{int(width/r_gcd)}:{int(height/r_gcd)}"
        
        # Determine Orientation/Layout Framework
        layout_mode = "Landscape Mode (Horizontal Orientation)" if width > height else "Portrait Mode (Vertical Orientation)"
        if width == height: layout_mode = "Square Matrix Grid"

        # Image Mode & Bit Depth Identification
        color_mode = image.mode
        bit_depth_mapping = {"1": "1-bit (Monochrome)", "L": "8-bit (Grayscale)", "P": "8-bit Palette", "RGB": "24-bit (True Color RGB)", "RGBA": "32-bit (RGB with Alpha Transparency Channel)"}
        resolved_depth = bit_depth_mapping.get(color_mode, f"Custom Channel Depth ({color_mode})")

        # Smart Analytics Engine via ImageStat (Bina Metadata ke chalne wale real features)
        stats = ImageStat.Stat(image)
        pixel_means = stats.mean
        pixel_stdevs = stats.stddev
        
        # Color Palette Spectrum Dominance Analysis
        if len(pixel_means) >= 3:
            r_avg, g_avg, b_avg = pixel_means[0], pixel_means[1], pixel_means[2]
            max_channel = max(r_avg, g_avg, b_avg)
            if max_channel == r_avg: dominance = "Red Channel Dominant (Warm Temperature Profile)"
            elif max_channel == g_avg: dominance = "Green Channel Dominant (Natural Environment Profile)"
            else: dominance = "Blue Channel Dominant (Cool Atmospheric Profile)"
            
            avg_deviation = sum(pixel_stdevs[:3]) / 3
            structural_entropy = "High Variance (Detailed/Complex Scene Layout)" if avg_deviation > 50 else "Low Variance (Flat/Soft Gradients or Plain Graphical Design)"
        else:
            dominance = "Monochrome Matrix (No Color Channels Detected)"
            structural_entropy = "Grayscale Layout Protocol"

        # Check for Common Digital Signature Flags (WhatsApp, FB, Screenshots)
        source_heuristic = "Individually Captured Camera / Raw Render Asset"
        lower_name = filename.lower()
        if "whatsapp" in lower_name or lower_name.startswith("img-") and "-" in lower_name:
            source_heuristic = "WhatsApp Compressed Media Transit Matrix (EXIF Block Stripped)"
        elif "fb" in lower_name or "facebook" in lower_name:
            source_heuristic = "Facebook Network Optimization Engine Asset"
        elif "instagram" in lower_name:
            source_heuristic = "Instagram Content Injection System Object"
        elif "screenshot" in lower_name or lower_name.startswith("screenshot_"):
            source_heuristic = "Local System UI Screen Buffer Dump (Screenshot Image)"

        # EXIF Standard Extraction Block
        info = image._getexif()
        exif_data = {}
        if info:
            for tag, value in info.items():
                decoded = TAGS.get(tag, tag)
                if decoded == "GPSInfo":
                    gps_data = {}
                    for t in value:
                        sub_decoded = GPSTAGS.get(t, t)
                        gps_data[sub_decoded] = value[t]
                    exif_data[decoded] = gps_data
                else:
                    exif_data[decoded] = value

        # Mapping values with advanced structural fallbacks
        photo_time = exif_data.get('DateTimeOriginal', exif_data.get('DateTime', 'Absent / Cleared by Social Media Infrastructure'))
        device_brand = exif_data.get('Make', 'Not Embedded (No Hardware Signature Found)')
        device_model = exif_data.get('Model', 'Not Embedded (No Operating Kernel ID Found)')
        time_zone = exif_data.get('OffsetTimeOriginal', 'UTC Offset Data Cleared / Private Field')
        lens_model = exif_data.get('LensModel', 'Standard / Dynamic Integrated Sensor Array')
        f_number = f"f/{exif_data.get('FNumber')}" if exif_data.get('FNumber') else 'Stripped Core Exposure Variable'
        focal_length = f"{exif_data.get('FocalLength')} mm" if exif_data.get('FocalLength') else 'Stripped Core Focal Variable'
        
        flash_val = exif_data.get('Flash', 0)
        flash_status = "Flash Fired (Artificial Light Burst Verified)" if (flash_val & 1) else "Flash Did Not Fire (Ambient Lighting Matrix Mode)"

        day_night_status = "Undetermined (Missing Time/Luminance Headers)"
        if 'DateTime' in exif_data or 'DateTimeOriginal' in exif_data:
            try:
                time_str = exif_data.get('DateTimeOriginal', exif_data.get('DateTime'))
                hour = int(time_str.split()[1].split(':')[0])
                if 6 <= hour < 18: day_night_status = f"Daylight Capture Sequence (~{hour}:00 Hrs)"
                else: day_night_status = f"Nocturnal / Night Capture Sequence (~{hour}:00 Hrs)"
            except: pass

        orientation_raw = exif_data.get('Orientation', 1)
        angle_mapping = {1: "0° (Normal Horizontal View)", 3: "180° (Inverted Axis)", 6: "90° (Rotated Right)", 8: "270° (Rotated Left)"}
        capture_angle = angle_mapping.get(orientation_raw, "Standard Degree Plane")

        # --- 💥 LINE-BY-LINE 22 ADVANCED FORENSIC DISPLAY 💥 ---
        print(f"{BLUE}[01] File Structural Format   :{RESET} {YELLOW}{structural_format}{RESET}")
        print(f"{BLUE}[02] Source Origin Heuristics  :{RESET} {MAGENTA}{source_heuristic}{RESET}")
        print(f"{BLUE}[03] Cryptographic Hash MD5    :{RESET} {GREEN}{md5_f}{RESET}")
        print(f"{BLUE}[04] Cryptographic Hash SHA256 :{RESET} {GREEN}{sha256_f}{RESET}")
        print(f"{BLUE}[05] Binary Payload Weight     :{RESET} {YELLOW}{file_kb} KB ({file_bytes} Bytes){RESET}")
        print(f"{BLUE}[06] Pixel Resolution Profile  :{RESET} {YELLOW}{megapixels} Megapixels ({width}x{height}){RESET}")
        print(f"{BLUE}[07] Display Grid Layout Mode  :{RESET} {YELLOW}{layout_mode}{RESET}")
        print(f"{BLUE}[08] Core Image Aspect Ratio   :{RESET} {YELLOW}{aspect_ratio}{RESET}")
        print(f"{BLUE}[09] Channel Bit-Depth Model   :{RESET} {YELLOW}{resolved_depth}{RESET}")
        print(f"{BLUE}[10] Color Palette Dominance   :{RESET} {YELLOW}{dominance}{RESET}")
        print(f"{BLUE}[11] Scene Complexity Analysis  :{RESET} {YELLOW}{structural_entropy}{RESET}")
        print(f"{BLUE}[12] Compression Byte Density  :{RESET} {YELLOW}{byte_density} Bytes/pixel{RESET}")
        print(f"{BLUE}[13] Hardware Capturing Angle  :{RESET} {YELLOW}{capture_angle}{RESET}")
        print(f"{BLUE}[14] Time Stamp Log Matrix     :{RESET} {YELLOW}{photo_time}{RESET}")
        print(f"{BLUE}[15] Target Time Zone Area     :{RESET} {YELLOW}{time_zone}{RESET}")
        print(f"{BLUE}[16] Operational Day/Night Log :{RESET} {YELLOW}{day_night_status}{RESET}")
        print(f"{BLUE}[17] Hardware Vendor Signature :{RESET} {YELLOW}{device_brand}{RESET}")
        print(f"{BLUE}[18] Specific Device Build ID  :{RESET} {YELLOW}{device_model}{RESET}")
        print(f"{BLUE}[19] Optical Lens Architecture :{RESET} {YELLOW}{lens_model}{RESET}")
        print(f"{BLUE}[20] Aperture Shutter Value    :{RESET} {YELLOW}{f_number}{RESET}")
        print(f"{BLUE}[21] Active Focal Distance     :{RESET} {YELLOW}{focal_length}{RESET}")
        print(f"{BLUE}[22] Light Sensor Flash State  :{RESET} {YELLOW}{flash_status}{RESET}")

        # Geolocation Parser Block
        maps_link = None
        if "GPSInfo" in exif_data:
            gps_info = exif_data["GPSInfo"]
            lat_val = gps_info.get("GPSLatitude")
            lat_ref = gps_info.get("GPSLatitudeRef")
            lon_val = gps_info.get("GPSLongitude")
            lon_ref = gps_info.get("GPSLongitudeRef")

            if lat_val and lat_ref and lon_val and lon_ref:
                lat = convert_to_degrees(lat_val)
                lon = convert_to_degrees(lon_val)
                if lat_ref != "N": lat = 0 - lat
                if lon_ref != "E": lon = 0 - lon

                print(f"\n{RED}{BOLD}[🚨 GEOLOCATION TARGET POSITION DECRYPTED]{RESET}")
                print(f"{GREEN}[+] Coords Structural Matrix   :{RESET} {MAGENTA}{lat}, {lon}{RESET}")
                maps_link = f"http://googleusercontent.com/maps.google.com/6{lat},{lon}"
                print(f"{YELLOW}[📌 LIVE GOOGLE MAP LINK]      :{RESET} {GREEN}{BOLD}{maps_link}{RESET}")
            else:
                print(f"\n{RED}[+] Target Location Metadata   : Locked / No Embedded GPS Signals Extracted{RESET}")
        else:
            print(f"\n{RED}[+] Target Location Metadata   : Locked / No Embedded GPS Signals Extracted{RESET}")

        # Comprehensive Structural File Export
        report_file = f"HCO_MetaX_Report_{os.path.splitext(filename)[0]}.txt"
        with open(report_file, 'w') as r:
            r.write("==========================================================================\n")
            r.write(f"          HCO-METAX FORRENSIC OSINT REPORT BY AZHAR HCO TEAM             \n")
            r.write("==========================================================================\n\n")
            r.write(f"[+] File: {filename}\n[+] MD5: {md5_f}\n[+] SHA256: {sha256_f}\n[+] Resolution: {width}x{height}\n[+] Format: {structural_format}\n[+] Source Guess: {source_heuristic}\n")
            if maps_link: r.write(f"[+] Tracker Link: {maps_link}\n")
        print(f"{GREEN}[📊 MASTER FORENSIC REPORT EXPORTED]:{RESET} {report_file}")
        print(f"{BLUE}--------------------------------------------------------------------------{RESET}")

    except Exception as e:
        print(f"{RED}[Error] Fatal system loop exception inside parsing block: {str(e)}{RESET}")

def main_menu():
    while True:
        print(f"\n{GREEN}Menu{RESET}")
        print(f"{GREEN}1.Run Tool{RESET}")
        print(f"{RED}2.Exit{RESET}")
        
        raw_choice = input(f"\n{YELLOW}Choose an option (1/2)= {RESET}")
        choice = "".join(re.findall(r'\d+', raw_choice)).strip()
        
        if choice == "1":
            raw_path = input(f"\n{GREEN}[➔] Enter image path: {RESET}").strip()
            sanitized = raw_path.replace("Location", "").strip("'\" ")
            target_path = re.sub(r'\s+', ' ', sanitized)
            
            if not os.path.exists(target_path):
                potential_joined_path = target_path.replace(" /", "/").replace(" ", "")
                if os.path.exists(potential_joined_path): target_path = potential_joined_path

            if not os.path.exists(target_path):
                alternative_paths = [
                    target_path,
                    os.path.join("/sdcard", target_path.lstrip("/")),
                    target_path.replace("/storage/emulated/0/", "/sdcard/"),
                    target_path.replace("/sdcard/", "/storage/emulated/0/"),
                    os.path.join("/storage/emulated/0/Pictures/WhatsApp", os.path.basename(target_path)),
                    os.path.join("/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images", os.path.basename(target_path))
                ]
                for alt in alternative_paths:
                    if os.path.exists(alt):
                        target_path = alt
                        break

            if os.path.isdir(target_path):
                print(f"{CYAN}[*] Folder designated. Processing array pipeline...{RESET}")
                files_found = False
                for file in os.listdir(target_path):
                    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                        files_found = True
                        analyze_image(os.path.join(target_path, file))
                if not files_found:
                    print(f"{YELLOW}[!] Notice: No matching media assets (.png/.jpg) found in directory.{RESET}")
            elif os.path.exists(target_path):
                analyze_image(target_path)
            else:
                print(f"{RED}[⚠️ PATH ERROR] Target could not be resolved. File does not exist.{RESET}")
                
        elif choice == "2":
            print(f"{RED}[*] Shutting down HCO-MetaX modules. Goodbye!{RESET}")
            sys.exit(0)
        else:
            print(f"{RED}[!] Invalid choice selection syntax. Choose 1 or 2.{RESET}")

if __name__ == "__main__":
    os.system('clear' if os.name != 'nt' else 'cls')
    lock_and_redirect()
    print_banner()
    main_menu()
