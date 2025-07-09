import os

file_path = "src/main/java/com/example/CommonsIOCVE2021_33813Example.java"

# 1. Read and print original code
with open(file_path, "r", encoding="utf-8") as f:
    code = f.read()

print("🔍 Original code:\n", code)

# 2. Prepare secure code
fix_code = '''
while ((zipEntry = zis.getNextEntry()) != null) {
    Path destPath = Paths.get("test").resolve(zipEntry.getName()).normalize();
    if (!destPath.startsWith(Paths.get("test").toAbsolutePath())) {
        throw new IOException("Bad zip entry: " + zipEntry.getName());
    }
    File destFile = destPath.toFile();
}
'''

# 3. Replace vulnerable code
if 'while ((zipEntry = zis.getNextEntry()) != null) {' in code:
    code = code.replace(
        'while ((zipEntry = zis.getNextEntry()) != null) {',
        fix_code
    )
    print("\n Vulnerable code replaced.\n")
else:
    print("\n Vulnerable code not found in file.\n")

# 4. Print new code
print(" New code:\n", code)

# 5. Write changes back to file
with open(file_path, "w", encoding="utf-8") as f:
    f.write(code)

print("\n File updated. Re-run SonarQube scan to verify.")
