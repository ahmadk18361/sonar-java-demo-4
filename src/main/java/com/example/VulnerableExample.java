package com.example;

import java.sql.*;

public class Vulnerable_ResourceLeak {
    public static void main(String[] args) {
        try {
            Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password123");
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM users");

            // Resources not closed with try-with-resources
            while (rs.next()) {
                System.out.println("User: " + rs.getString("username"));
            }

            // Manual close (error-prone if exception is thrown earlier)
            rs.close();
            stmt.close();
            conn.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}


