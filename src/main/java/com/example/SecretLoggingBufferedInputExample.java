import java.io.*;
import org.apache.log4j.Logger;

public class SecretLoggingBufferedInputExample {
    static Logger logger = Logger.getLogger(SecretLoggingBufferedInputExample.class);

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter username: ");
        String username = reader.readLine();

        System.out.print("Enter password: ");
        String password = reader.readLine();  //  Secret input

        logger.warn("Login with: " + username + " / " + password);  //  Leaks secrets
    }
}
