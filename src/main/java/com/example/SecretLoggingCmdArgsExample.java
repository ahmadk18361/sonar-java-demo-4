import org.apache.log4j.Logger;

public class SecretLoggingCmdArgsExample {
    static Logger logger = Logger.getLogger(SecretLoggingCmdArgsExample.class);

    public static void main(String[] args) {
        if (args.length >= 2) {
            String username = args[0];
            String password = args[1];  //  Sensitive data
            logger.error("Credentials used: " + username + ":" + password);  //  Dangerous
        }
    }
}
