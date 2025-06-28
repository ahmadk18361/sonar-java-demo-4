import java.sql.*;
import javax.servlet.http.*;

public class VulnerableLogin extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) {
        try {
            String username = request.getParameter("username");
            String password = request.getParameter("password");

            String query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'";

            Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/app", "root", "password");

            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(query);

            if (rs.next()) {
                response.getWriter().println("Welcome, " + username);
            } else {
                response.getWriter().println("Invalid login.");
            }

            conn.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
