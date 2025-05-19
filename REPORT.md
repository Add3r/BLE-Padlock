# BLE Smart Lock Unlock – Progress Report (2025-05-19)

## ✅ Summary

This report documents the progress of our BLE padlock security analysis using the provided hardware (Ubertooth only).

- Target BLE MAC address identified using nRF Connect
- GATT UUIDs for PIN and unlock operation extracted
- Based on observed properties, unlock flow reconstructed and scripted using `bleak`
- Unlock PoC prepared (`unlock_ble.py`) and fully config-driven
- Due to lack of BLE TX adapter, actual unlock execution is pending
- Ubertooth used for passive validation of BLE activity

## ✅ Extracted UUIDs

| Type | UUID |
|------|------|
| passcode_uuid | `0000xxxx-0000-1000-8000-00805f9b34fb` |
| unlock_uuid   | `0000xxxx-0000-1000-8000-00805f9b34fb` |

xxxx being the sensitive uuids.

## ✅ Prepared Files

- `unlock_config.json` – contains extracted UUIDs, MAC address, and values (the included is dummy data)
- `unlock_ble.py` – bleak-based unlock flow
- `ble_workflow.md` – step-by-step process documentation

## ⛔ Execution Status

| Step | Status |
|------|--------|
| Connect to BLE | ❌ Adapter not available |
| Send PIN        | ❌ Not tested |
| Send unlock     | ❌ Not tested |
| BLE packet capture | ✅ Partial via Ubertooth |

## 📎 Screenshots available

- UUIDs observed via nRF Connect
- Ubertooth scan output
- unlock_ble.py execution attempt + error trace (missing BLE adapter)

## 🔁 Next Steps

- Request BLE adapter (CSR or Broadcom preferred)
- Perform actual unlock attempt and capture traffic with Ubertooth
- Confirm unlock value (`01`, `FF`, etc.)
- Package final PoC for internal demo
