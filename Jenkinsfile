import os
import re

SOURCE_DIR = 'src/main/java/com/example'

# Patterns to detect and fix
SECRET_LOG_PATTERN = re.compile(r'logger\.(info|warn|error|debug)\s*\(\s*.*?(password|secret).*?\)', re.IGNORECASE)
ENCODING_PATTERN = re.compile(r'new InputStreamReader\s*\(\s*System\.in\s*\)')
IMPORT_PATTERN = re.compile(r'import java\.io\..*;')

def remediate_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified = False
    new_lines = []
    has_encoding_fix = False
    import_inserted = False
    added_import = False

    for i, line in enumerate(lines):
        # Fix secret-logging
        if SECRET_LOG_PATTERN.search(line):
            safe_line = '        logger.warn("Sensitive data logging avoided.");\n'
            new_lines.append(safe_line)
            modified = True
            continue

        # Fix InputStreamReader encoding
        if ENCODING_PATTERN.search(line):
            line = line.replace(
                'new InputStreamReader(System.in)',
                'new InputStreamReader(System.in, StandardCharsets.UTF_8)'
            )
            modified = True
            has_encoding_fix = True

        new_lines.append(line)

    # Add missing import for StandardCharsets if encoding was fixed
    if has_encoding_fix and not any('StandardCharsets' in l for l in lines):
        for i, line in enumerate(new_lines):
            if IMPORT_PATTERN.search(line) and not import_inserted:
                new_lines.insert(i + 1, 'import java.nio.charset.StandardCharsets;\n')
                modified = True
                import_inserted = True
                break

    if modified:
        with open(file_path, 'w') as file:
            file.writelines(new_lines)
        print(f"[✓] Remediated: {file_path}")
    else:
        print(f"[—] No changes needed: {file_path}")

def run_remediation():
    for root, _, files in os.walk(SOURCE_DIR):
        for filename in files:
            if filename.endswith('.java'):
                file_path = os.path.join(root, filename)
                remediate_file(file_path)

if __name__ == "__main__":
    run_remediation()
