
## Requirements

- Python 3.7+
- BLE-capable device (Linux, Windows, macOS)
- `bleak` library

Install dependencies:

```bash
pip install -r requirements.txt
```

On Linux, you may need to grant BLE permissions:

```bash
sudo setcap cap_net_raw+eip $(readlink -f $(which python3))
```

## Usage

```bash
python unlock_ble.py
```

