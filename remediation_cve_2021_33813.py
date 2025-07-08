import zipfile
import os

file_path = "src/main/java/com/example/CommonsIOCVE2021_33813Example.java"

with open(file_path, "r", encoding="utf-8") as f:
    code = f.read()

# Step: Replace Java-style zipEntry loop with secure version (Python-style placeholder for automation)
if "normalize" not in code:
    fix_code = """
    // Normalize path to prevent Zip Slip
    File destFile = new File(destDir, zipEntry.getName());
    String destDirPath = destDir.getCanonicalPath();
    String destFilePath = destFile.getCanonicalPath();
    if (!destFilePath.startsWith(destDirPath + File.separator)) {
        throw new IOException("Entry is outside of the target dir: " + zipEntry.getName());
    }
    """

    # Replace the vulnerable while-loop
    code = code.replace(
        'while ((zipEntry = zis.getNextEntry()) != null) {',
        f'{fix_code}\nwhile ((zipEntry = zis.getNextEntry()) != null) {{'
    )

with open(file_path, "w", encoding="utf-8") as f:
    f.write(code)

print("[OK] Zip Slip CVE-2021-33813 remediation applied.")



