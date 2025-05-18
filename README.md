# hosts-tracker
This script compares two files containing HTTP probe results and identifies URLs whose HTTP status codes have changed over time.

📦 Example Workflow:

1. Run initial probe:
```
httpx -l alive_http_services.txt -probe -o probe1.txt
```
2. Wait 1 week (or any desired period)...
3. Run the probe again:
```
httpx -l alive_http_services.txt -probe -o probe2.txt
```
✅ Usage:

Compare `probe1.txt` and `probe2.txt` to detect status changes:
```
python3 tracker.py
```

🧾 Output Format:

```
https://example.com changed from [FAILED] to [SUCCESS]
```
