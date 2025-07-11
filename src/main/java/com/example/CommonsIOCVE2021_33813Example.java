import org.apache.log4j.Logger;

public class CommonsIOCVE2021_33813Example {
    static Logger logger = Logger.getLogger(CommonsIOCVE2021_33813Example.class);

    public static void main(String[] args) {
        String username = "admin";
        String password = "hunter2"; // sensitive info

        logger.info("User login attempt: " + username + " / " + password); //  Leaks secrets to logs
    }
}
