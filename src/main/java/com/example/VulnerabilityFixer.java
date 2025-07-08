import re
import shutil
import os

def fix_credentials(java_file):
    # Make a backup of original file
    backup_file = java_file + ".bak"
    shutil.copy(java_file, backup_file)

    with open(java_file, "r") as f:
        code = f.read()

    # Replace username and password assignments
    code = re.sub(r'String\s+username\s*=\s*".*?";', 'String username = System.getenv("DB_USERNAME");', code)
    code = re.sub(r'String\s+password\s*=\s*".*?";', 'String password = System.getenv("DB_PASSWORD");', code)

    with open(java_file, "w") as f:
        f.write(code)

    print(f"[✔] Remediation applied. Backup saved to: {backup_file}")

# Example usage
if __name__ == "__main__":
    fix_credentials("src/main/java/com/example/VulnerableExample.java")
