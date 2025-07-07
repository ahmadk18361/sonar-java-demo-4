package com.example;

import java.sql.*;

public class Vulnerable_HardcodedCreds {
    public static void main(String[] args) {
        try {
            // Hardcoded credentials
            String url = "jdbc:mysql://localhost:3306/testdb";
            String username = "root";
            String password = "password123";

            Connection conn = DriverManager.getConnection(url, username, password);
            conn.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
