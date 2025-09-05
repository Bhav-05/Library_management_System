import csv
import os

def read_csv(file, fieldnames=None):
    """Read a CSV file into a list of dicts."""
    if not os.path.exists(file):
        return []

    with open(file, mode="r", newline="", encoding="utf-8") as f:
        if fieldnames:
            reader = csv.DictReader(f, fieldnames=fieldnames)
            data = list(reader)[1:]  # skip header
        else:
            reader = csv.DictReader(f)
            data = list(reader)  # auto-detect header
    # Strip whitespace from all values
    for row in data:
        for k, v in row.items():
            if isinstance(v, str):
                row[k] = v.strip()
    return data


def write_csv(file, fieldnames, rows):
    """Write a list of dicts to CSV file."""
    with open(file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def append_csv(file, fieldnames, row):
    """Append a single dict row to CSV file."""
    file_exists = os.path.exists(file)
    with open(file, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)

