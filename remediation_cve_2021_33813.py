import re

with open("src/main/java/com/example/CommonsIOCVE2021_33813Example.java", "r") as file:
    code = file.read()

# Add path normalization check to prevent Zip Slip
if 'normalize' not in code:
    fix = '''
    File destFile = new File(destDir, zipEntry.getName());
    String destDirPath = destDir.getCanonicalPath();
    String destFilePath = destFile.getCanonicalPath();
    if (!destFilePath.startsWith(destDirPath + File.separator)) {
        throw new IOException("Entry is outside of the target dir: " + zipEntry.getName());
    }
    '''
    code = code.replace("while ((zipEntry = zis.getNextEntry()) != null) {", 
                        "while ((zipEntry = zis.getNextEntry()) != null) {
" + fix)

with open("ZipSlipCVE2021_33813Example.java", "w") as file:
    file.write(code)
