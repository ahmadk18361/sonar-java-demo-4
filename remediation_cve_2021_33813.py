import re

def remediate_log4j_leak(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    fixed_lines = []
    for line in lines:
        # Look for the logger line that includes password
        if re.search(r'logger\.info\(.+password.*\)', line):
            # Replace the password with redacted tag
            redacted_line = re.sub(r'\+.*password.*\)', '+ "[REDACTED]")', line)
            fixed_lines.append(redacted_line)
        else:
            fixed_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(fixed_lines)

    print(f"[OK] Remediation complete for: {file_path}")

# Run remediation
remediate_log4j_leak('src/main/java/com/example/CommonsIOCVE2021_33813Example.java')
