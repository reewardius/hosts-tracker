# hosts-tracker
This script compares two files containing HTTP probe results and identifies URLs whose HTTP status codes have changed over time.

📦 Example Workflow:

1. Make first recon and initial probe:
```
httpx -l alive_http_services.txt -probe -o probe1.txt
```
2. Wait 1 week (or any desired period)...
3. Make recon again and run the second probe:
```
httpx -l alive_http_services.txt -probe -o probe2.txt
```
✅ Usage:

Compare `probe1.txt` and `probe2.txt` to detect status changes:
```
python3 tracker.py probe1.txt probe2.txt
```

🧾 Output Format:

```
🔄 Changed statuses:
  http://example.com changed from [FAILED] to [SUCCESS]

🆕 New successful targets:
  http://newtarget.com with current status [SUCCESS]
```

If no changes or new successes are found:

```
✅ No status changes.

📭 No new successful targets.
```
