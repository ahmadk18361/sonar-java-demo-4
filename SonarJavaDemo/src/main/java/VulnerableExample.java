package example;
import java.sql.*;

public class VulnerableExample {
    public static void main(String[] args) {
        String userInput = "' OR '1'='1";
        String query = "SELECT * FROM users WHERE username = '" + userInput + "'";

        try {
            // Hardcoded credentials (security hotspot)
            String url = "jdbc:mysql://localhost:3306/testdb";
            String username = "root";
            String password = "password123";

            Connection conn = DriverManager.getConnection(url, username, password);
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(query);

            while (rs.next()) {
                System.out.println("Logged in as: " + rs.getString("username"));
            }

            // No try-with-resources or finally block (resource leak)
            rs.close();
            stmt.close();
            conn.close();

        } catch (SQLException e) {
            // Swallowed exception (bad practice)
            e.printStackTrace(); // Not logging properly
        }
    }
}
