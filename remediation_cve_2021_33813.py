import os

# Path to the vulnerable Java file
file_path = 'src/main/java/com/example/CommonsIOCVE2021_33813Example.java'

# Read original Java content
with open(file_path, 'r', encoding='utf-8') as f:
    code = f.read()

# New secure version of the while loop (Zip Slip fix)
secure_code = '''
        while (entry != null) {
            File destDir = new File("output");
            File destFile = new File(destDir, entry.getName());
            String destDirPath = destDir.getCanonicalPath();
            String destFilePath = destFile.getCanonicalPath();

            if (!destFilePath.startsWith(destDirPath + File.separator)) {
                throw new IOException("Entry is outside of the target dir: " + entry.getName());
            }

            new FileOutputStream(destFile); // Safe now
            zipIn.closeEntry();
            entry = zipIn.getNextEntry();
        }
'''

# Vulnerable pattern to replace
vulnerable_code = '''
        while (entry != null) {
            File outFile = new File("output/" + entry.getName()); // Vulnerable: No path validation
            new FileOutputStream(outFile); // Could overwrite sensitive files
            zipIn.closeEntry();
            entry = zipIn.getNextEntry();
        }
'''

# Replace the vulnerable code
if vulnerable_code.strip() in code:
    code = code.replace(vulnerable_code.strip(), secure_code.strip())

    # Save the updated Java file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(code)

    print("[OK] Zip Slip CVE-2021-33813 remediation applied.")
else:
    print("[Sorry] Vulnerable code pattern not found. No changes made.")
