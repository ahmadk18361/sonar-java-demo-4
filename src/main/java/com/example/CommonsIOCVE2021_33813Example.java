import java.io.*;
import java.util.zip.*;

public class CommonsIOCVE2021_33813Example {
    public static void main(String[] args) throws IOException {
        ZipInputStream zipIn = new ZipInputStream(new FileInputStream("sample.zip"));
        ZipEntry entry = zipIn.getNextEntry();

        while (entry != null) {
            File outFile = new File("output/" + entry.getName()); // Vulnerable: No path validation
            new FileOutputStream(outFile); // Could overwrite sensitive files
            zipIn.closeEntry();
            entry = zipIn.getNextEntry();
        }

        zipIn.close();
    }
}
