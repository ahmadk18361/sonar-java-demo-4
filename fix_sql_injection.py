import re

def fix_sql_injection(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    # Backup original
    with open(file_path + '.bak', 'w', encoding='utf-8') as backup:
        backup.write(code)

    # Step 1: Replace statement creation and execution with PreparedStatement
    code = re.sub(
        r'Statement\s+stmt\s*=\s*conn\.createStatement\s*\(\s*\)\s*;',
        'PreparedStatement pstmt = conn.prepareStatement("SELECT * FROM users WHERE username = ?");',
        code
    )
    code = re.sub(
        r'ResultSet\s+rs\s*=\s*stmt\.executeQuery\s*\(\s*query\s*\)\s*;',
        'pstmt.setString(1, userInput);\n        ResultSet rs = pstmt.executeQuery();',
        code
    )

    # Step 2: Write modified content back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(code)

    print(" SQL injection remediation applied.")
