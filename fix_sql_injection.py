import re

def fix_sql_injection(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    # Backup original
    with open(file_path + ".bak", 'w', encoding='utf-8') as backup:
        backup.write(code)

    # Step 1: Replace `Statement stmt = conn.createStatement();` with PreparedStatement
    code = code.replace(
        "Statement stmt = conn.createStatement();",
        'PreparedStatement pstmt = conn.prepareStatement("SELECT * FROM users WHERE username = ?");'
    )

    # Step 2: Replace query string + execution line
    code = re.sub(
        r'String query\s*=\s*.*?;\s*ResultSet rs\s*=\s*stmt\.executeQuery\(query\);',
        'pstmt.setString(1, userInput);\n        ResultSet rs = pstmt.executeQuery();',
        code,
        flags=re.DOTALL
    )

    # Step 3: Write modified content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(code)

    print(f"SQL injection remediation applied. Backup saved to {file_path}.bak")

# Run this on your target file
fix_sql_injection("src/main/java/com/example/VulnerableExample.java")
