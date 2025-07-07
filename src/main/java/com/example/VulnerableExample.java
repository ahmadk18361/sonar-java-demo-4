package com.example;

import java.sql.*;
import java.util.logging.Logger;

public class VulnerableExample {

    private static final Logger logger = Logger.getLogger(VulnerableExample.class.getName());

    public static void main(String[] args) {
        String userInput = "' OR '1'='1";
        String query = "SELECT * FROM users WHERE username = '" + userInput + "'";

        // Hardcoded credentials (intentionally kept for security scan testing)
        String url = "jdbc:mysql://localhost:3306/testdb";
        String username = "root";
        String password = "password123";

        try (
            Connection conn = DriverManager.getConnection(url, username, password);
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(query)
        ) {
            while (rs.next()) {
                logger.info("Logged in as: " + rs.getString("username"));
            }
        } catch (SQLException e) {
            logger.severe("SQL Exception: " + e.getMessage());
        }
    }
}
