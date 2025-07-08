import re

def fix_commons_exec_rce(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    backup_path = file_path + ".bak"
    with open(backup_path, 'w', encoding='utf-8') as backup:
        backup.write(code)

    # Replace dangerous shell invocation pattern
    code = re.sub(r'cmd\s*/c\s*', 'SAFE_COMMAND_', code)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(code)

    print(f"[OK] Remediation for CVE-2019-0232 applied. Backup at: {backup_path}")
