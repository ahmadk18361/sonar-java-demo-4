import java.sql.*;

public class VulnerableLogin {

    public static void main(String[] args) {
        // SQL Injection vulnerability
        String userInput = "' OR '1'='1";
        String query = "SELECT * FROM users WHERE username = '" + userInput + "'";

        try {
            // Hardcoded database credentials (bad practice)
            String url = "jdbc:mysql://localhost:3306/testdb";
            String username = "root";
            String password = "password123";

            // No input validation (bad practice)
            Connection conn = DriverManager.getConnection(url, username, password);
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(query);

            while (rs.next()) {
                System.out.println("Logged in as: " + rs.getString("username"));
            }

            // Closing connections without finally block (resource leak risk)
            rs.close();
            stmt.close();
            conn.close();

        } catch (SQLException e) {
            // Swallowing exception without logging it properly
            e.printStackTrace();  // Bad practice
        }
    }
}