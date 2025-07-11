import java.io.*;

public class CVE_Example_CommandInjection {
    public static void main(String[] args) throws Exception {
        String userInput = "calc"; // Simulating unsafe input
        Runtime.getRuntime().exec("cmd /c " + userInput); // Vulnerable
    }
}
