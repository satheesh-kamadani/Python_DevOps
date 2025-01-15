# Log file analysis using loops

log_file = ["info: login successful",
            "Error: file not found",
            "Debug: Connection established",
            "Error: Database connnection failed"]

for line in log_file:
    if "Error" in line:
        print(line)