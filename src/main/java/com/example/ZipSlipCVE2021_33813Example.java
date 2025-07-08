import java.io.*;
import java.util.zip.*;

public class ZipSlipCVE2021_33813Example {
    public static void main(String[] args) throws IOException {
        String zipFilePath = "malicious.zip";
        File destDir = new File("output");
        byte[] buffer = new byte[1024];
        ZipInputStream zis = new ZipInputStream(new FileInputStream(zipFilePath));
        ZipEntry zipEntry;

        while ((zipEntry = zis.getNextEntry()) != null) {
            File newFile = new File(destDir, zipEntry.getName()); // Vulnerable to "../"
            FileOutputStream fos = new FileOutputStream(newFile);
            int len;
            while ((len = zis.read(buffer)) > 0) {
                fos.write(buffer, 0, len);
            }
            fos.close();
            zis.closeEntry();
        }
        zis.close();
    }
}
