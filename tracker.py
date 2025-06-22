import re
import argparse

def clean_status(raw_status):
    # Remove ANSI color escape codes
    return re.sub(r'\x1b\[[0-9;]*m', '', raw_status).strip('[]')

def parse_file(filename):
    result = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():
                parts = line.strip().rsplit(' ', 1)
                if len(parts) == 2:
                    url, status = parts
                    status = clean_status(status)
                    result[url.strip()] = status
    return result

def compare_files(file1, file2):
    old = parse_file(file1)
    new = parse_file(file2)

    changed = []
    new_successes = []

    for url, status in new.items():
        if url in old:
            if old[url] != status:
                changed.append((url, old[url], status))
        else:
            if status == 'SUCCESS':
                new_successes.append(url)

    return changed, new_successes

def main():
    parser = argparse.ArgumentParser(description="Compare URL statuses between two files.")
    parser.add_argument('file1', help="First file to compare")
    parser.add_argument('file2', help="Second file to compare")
    args = parser.parse_args()

    changed, new_successes = compare_files(args.file1, args.file2)

    if changed:
        print("🔄 Changed statuses:")
        for url, old, new in sorted(changed):
            print(f"  {url} changed from [{old}] to [{new}]")
    else:
        print("✅ No status changes.")

    if new_successes:
        print("\n🆕 New successful targets:")
        for url in sorted(new_successes):
            print(f"  {url} with current status [SUCCESS]")
    else:
        print("\n📭 No new successful targets.")

if __name__ == "__main__":
    main()
