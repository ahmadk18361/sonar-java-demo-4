package com.example;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertTrue;

public class VulnerableExampleTest {

    @Test
    public void testMainRuns() {
        // This test just checks that the main method runs without throwing an exception
        try {
            VulnerableExample.main(new String[]{});
            assertTrue(true); // If no exception, test passes
        } catch (Exception e) {
            assertTrue(false, "Main method threw an exception: " + e.getMessage());
        }
    }
}
