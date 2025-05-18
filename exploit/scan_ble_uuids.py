import asyncio
from bleak import BleakClient

target_mac = input("Enter BLE MAC address: ")

async def scan_characteristics(mac):
    async with BleakClient(mac) as client:
        if await client.is_connected():
            print(f"Connected to {mac}")
            services = await client.get_services()
            for service in services:
                for char in service.characteristics:
                    print(f"[{char.uuid}] — Properties: {char.properties}")
        else:
            print("Failed to connect.")

asyncio.run(scan_characteristics(target_mac))
