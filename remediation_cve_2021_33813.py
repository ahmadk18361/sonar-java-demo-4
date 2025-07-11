import re

file_path = "src/main/java/com/example/CommonsIOCVE2021_33813Example.java"

with open(file_path, "r", encoding="utf-8") as f:
    code = f.read()

# Match the vulnerable pattern – flexible for spacing/indentation
pattern = r'while\s*\(entry\s*!=\s*null\)\s*\{\s*File outfile = new File\("output/" \+ entry\.getName\(\)\);\s*new FileOutputStream\(outfile\);\s*zipIn\.closeEntry\(\);\s*entry = zipIn\.getNextEntry\(\);\s*\}'
# Secure replacement code (Zip Slip fix)
secure_code = '''
while (entry != null) {
    File destDir = new File("output");
    File destFile = new File(destDir, entry.getName());

    String destDirPath = destDir.getCanonicalPath();
    String destFilePath = destFile.getCanonicalPath();

    if (!destFilePath.startsWith(destDirPath + File.separator)) {
        throw new IOException("Entry is outside the target dir: " + entry.getName());
    }

    new FileOutputStream(destFile); // [OK] safe now
    zipIn.closeEntry();
    entry = zipIn.getNextEntry();
}
'''

# Strip the vulnerable block
code, count = re.subn(pattern, secure_code, code, flags=re.DOTALL)

# Write back if changed
if count > 0:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)
    print("[OK] CVE-2021-33813 remediation applied.")
else:
    print("[SORRY] Vulnerable code pattern not found. No changes made.")
