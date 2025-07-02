import java.sql.*;
import java.security.MessageDigest;
import java.util.Random;
import java.io.*;
import java.util.Scanner;

public class VulnerableLogin {
    public static void main(String[] args) {
        // SQL Injection
        String userInput = "' OR '1'='1";
        String query = "SELECT * FROM users WHERE username = '" + userInput + "'";

        try {
            // Hardcoded credentials
            String url = "jdbc:mysql://localhost:3306/testdb";
            String username = "root";
            String password = "password123";

            Connection conn = DriverManager.getConnection(url, username, password);
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(query);

            while (rs.next()) {
                System.out.println("Logged in as: " + rs.getString("username"));
            }

            rs.close();
            stmt.close();
            conn.close();

            // Weak crypto
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] hash = md.digest("password123".getBytes());
            System.out.println("MD5 Hash: " + new String(hash));

            // Insecure random
            Random random = new Random();
            int otp = random.nextInt(9999);
            System.out.println("OTP: " + otp);

            // Hardcoded API key
            String apiKey = "sk_test_ABC123XYZ";

            // File path traversal
            String filename = "../etc/passwd";
            Scanner scanner = new Scanner(new File(filename));
            while (scanner.hasNext()) {
                System.out.println(scanner.nextLine());
            }

            // Command injection
            Runtime.getRuntime().exec("rm test.txt");

        } catch (Exception e) {
            e.printStackTrace(); // Swallowed exception
        }
    }
}
