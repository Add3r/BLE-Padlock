#!/bin/bash

echo "[*] Starting BLE capture with Ubertooth..."
FILE="ble_capture_$(date +%Y%m%d_%H%M%S).pcap"
ubertooth-btle -f -c "$FILE"
