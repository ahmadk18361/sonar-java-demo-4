import os

file_path = "src/main/java/com/example/CommonsCVE2021_33813Example.java"

with open(file_path, "r", encoding="utf-8") as f:
    code = f.read()

# New secure code block (replace vulnerable while-loop)
fix_code = '''
while ((zipEntry = zis.getNextEntry()) != null) {
    Path destPath = Paths.get("test").resolve(zipEntry.getName()).normalize();
    if (!destPath.startsWith(Paths.get("test").toAbsolutePath())) {
        throw new IOException("Bad zip entry: " + zipEntry.getName());
    }
    File destFile = destPath.toFile();
}
'''

# Replace the old insecure while-loop
code = code.replace(
    'while ((zipEntry = zis.getNextEntry()) != null) {',
    fix_code
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(code)

print("[OK] Zip Slip CVE-2021-33813 remediation applied.")
