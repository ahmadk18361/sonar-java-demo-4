import os
import re

# Directory to scan
SOURCE_DIR = 'src/main/java/com/example'

# Pattern to detect secret or sensitive logging
SECRET_LOG_PATTERN = re.compile(r'logger\.(info|warn|error|debug)\s*\(.*(password|secret|username).*?\)', re.IGNORECASE)

# Pattern to detect InputStreamReader without encoding
ENCODING_PATTERN = re.compile(r'new\s+InputStreamReader\s*\(\s*System\.in\s*\)')

# Java import for StandardCharsets
CHARSET_IMPORT_LINE = 'import java.nio.charset.StandardCharsets;\n'

def remediate_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified = False
    new_lines = []
    charset_imported = any('StandardCharsets' in line for line in lines)

    for line in lines:
        # Fix secret logging
        if SECRET_LOG_PATTERN.search(line):
            safe_line = '        logger.warn("Sensitive data logging avoided.");\n'
            new_lines.append(safe_line)
            modified = True
        # Fix encoding issue
        elif ENCODING_PATTERN.search(line):
            fixed_line = '        new InputStreamReader(System.in, StandardCharsets.UTF_8)'
            # Preserve indentation
            indentation = re.match(r'^\s*', line).group(0)
            new_lines.append(indentation + fixed_line + ';\n')
            modified = True
        else:
            new_lines.append(line)

    # Add charset import if needed
    if modified and not charset_imported:
        for i, line in enumerate(new_lines):
            if line.startswith('import ') and 'java.io' in line:
                new_lines.insert(i + 1, CHARSET_IMPORT_LINE)
                break

    if modified:
        with open(file_path, 'w') as file:
            file.writelines(new_lines)
        print(f'[OK] Remediated: {file_path}')
    else:
        print(f'[SKIP] No changes needed: {file_path}')


def run_remediation():
    for root, _, files in os.walk(SOURCE_DIR):
        for filename in files:
            if filename.endswith('.java'):
                file_path = os.path.join(root, filename)
                remediate_file(file_path)


if __name__ == '__main__':
    run_remediation()
