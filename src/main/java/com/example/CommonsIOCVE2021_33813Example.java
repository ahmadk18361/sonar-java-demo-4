import org.apache.log4j.Logger;

public class CVE2021_27568 {
    static Logger logger = Logger.getLogger(CVE2021_27568.class);

    public static void main(String[] args) {
        String username = "admin";
        String password = "hunter2"; // sensitive info

        logger.info("User login attempt: " + username + " / " + password); // Leaks secrets to logs
    }
}
