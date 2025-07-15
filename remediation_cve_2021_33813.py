import os
import re

# Directory to scan
SOURCE_DIR = 'src/main/java/com/example'

# Detect log lines containing password or secret
SECRET_LOG_PATTERN = re.compile(r'logger\.(info|warn|error|debug)\s*\(.*(\+.*(password|secret)).*\)', re.IGNORECASE)

def remediate_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified = False
    new_lines = []

    for line in lines:
        if SECRET_LOG_PATTERN.search(line):
            # Replace the log with a safe placeholder message
            safe_line = 'logger.warn("Sensitive data logging avoided.");\n'
            new_lines.append(safe_line)
            modified = True
        else:
            new_lines.append(line)

    if modified:
        with open(file_path, 'w') as file:
            file.writelines(new_lines)
        print(f"[OK] Remediated: {file_path}")
    else:
        print(f"[SORRY] No changes made: {file_path}")

def run_remediation():
    for root, _, files in os.walk(SOURCE_DIR):
        for filename in files:
            if filename.endswith(".java"):
                file_path = os.path.join(root, filename)
                remediate_file(file_path)

if __name__ == "__main__":
    run_remediation()
