import re

file_path = "src/main/java/com/example/CommonsIOCVE2021_33813Example.java"

with open(file_path, "r", encoding="utf-8") as f:
    code = f.read()

# Regex to match any use of entry.getName() inside File + FileOutputStream
pattern = r'File\s+\w+\s*=\s*new\s+File\s*\(\s*"?output"?\s*\+\s*entry\.getName\(\)\s*\);[\s\S]+?new\s+FileOutputStream\([^)]*\);'

secure_fix = '''
File destDir = new File("output");
File destFile = new File(destDir, entry.getName());
String destDirPath = destDir.getCanonicalPath();
String destFilePath = destFile.getCanonicalPath();

if (!destFilePath.startsWith(destDirPath + File.separator)) {
    throw new IOException("Entry is outside the target dir: " + entry.getName());
}

new FileOutputStream(destFile); // [OK] safe now
'''

new_code, count = re.subn(pattern, secure_fix.strip(), code)

if count:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_code)
    print("[OK] Zip Slip CVE-2021-33813 remediation applied.")
else:
    print("[Sorry] Vulnerable code pattern not found. No changes made.")
