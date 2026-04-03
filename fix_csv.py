import csv

# Read the CSV and fix by assuming last 6 fields are fixed
with open('data.csv', 'r', encoding='utf-8') as infile:
    lines = infile.readlines()

fixed_rows = []
for line in lines:
    line = line.strip()
    if not line:
        continue
    parts = line.split(',')
    if len(parts) < 7:
        continue  # skip malformed
    # Last 6: Latitude,Longitude,Time,ReportText,HeelTap,RiskLabel
    fixed = parts[-6:]
    location = ','.join(parts[:-6])
    row = [location] + fixed
    fixed_rows.append(row)

# Write back with proper quoting
with open('data_fixed.csv', 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL)
    for row in fixed_rows:
        writer.writerow(row)

print("Fixed CSV saved as data_fixed.csv")