import java.io.*;
import java.util.zip.*;

public class CommonsIOCVE2021_33813Example {
    public static void main(String[] args) throws IOException {
        ZipInputStream zipIn = new ZipInputStream(new FileInputStream("sample.zip"));
        ZipEntry entry = zipIn.getNextEntry();

        

while (entry != null) {
    File destDir = new File("output");
    File destFile = new File(destDir, entry.getName());

    String destDirPath = destDir.getCanonicalPath();
    String destFilePath = destFile.getCanonicalPath();

    if (!destFilePath.startsWith(destDirPath + File.separator)) {
        throw new IOException("Entry is outside the target dir: " + entry.getName());
    }

    new FileOutputStream(destFile); // [OK] Safe now
    zipIn.closeEntry();
    entry = zipIn.getNextEntry();
}

