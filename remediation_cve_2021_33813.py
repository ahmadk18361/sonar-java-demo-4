import os
import re

# Directory to scan
SOURCE_DIR = 'src/main/java'

# Pattern to detect sensitive logging
SECRET_LOG_PATTERN = re.compile(
    r'logger\.(info|warn|error|debug)\s*\(.*(password|secret).*?\)', re.IGNORECASE
)

# Pattern to detect unsafe encoding in InputStreamReader
ENCODING_PATTERN = re.compile(r'new InputStreamReader\s*\(\s*System\.in\s*\)')
ENCODING_SAFE_REPLACEMENT = 'new InputStreamReader(System.in, StandardCharsets.UTF_8)'

def remediate_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified = False
    new_lines = []
    has_import = any('StandardCharsets' in line for line in lines)

    for line in lines:
        # Remediate sensitive log statements
        if SECRET_LOG_PATTERN.search(line):
            safe_line = 'logger.warn("Sensitive data logging avoided.");\n'
            new_lines.append(safe_line)
            modified = True
            continue

        # Remediate unsafe encoding
        if ENCODING_PATTERN.search(line):
            if not has_import:
                new_lines.insert(0, 'import java.nio.charset.StandardCharsets;\n')
                has_import = True
            safe_line = ENCODING_PATTERN.sub(ENCODING_SAFE_REPLACEMENT, line)
            new_lines.append(safe_line)
            modified = True
            continue

        new_lines.append(line)

    if modified:
        with open(file_path, 'w') as file:
            file.writelines(new_lines)
        print(f"[OK] Remediated: {file_path}")
    else:
        print(f"[SKIP] No changes made: {file_path}")

def run_remediation():
    for root, _, files in os.walk(SOURCE_DIR):
        for filename in files:
            if filename.endswith('.java'):
                file_path = os.path.join(root, filename)
                remediate_file(file_path)

if __name__ == '__main__':
    run_remediation()
