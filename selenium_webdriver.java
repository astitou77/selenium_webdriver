import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver; 


public class selenium_webdriver {
    public static void main(String[] args) {
        // Set the path to the ChromeDriver executable
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver");

        // Create a new instance of the Chrome driver
        org.openqa.selenium.WebDriver driver = new org.openqa.selenium.chrome.ChromeDriver();

        // Navigate to a web page
        driver.get("https://www.example.com");

        // WebDriver driver = new ChromeDriver();


        // Perform actions on the web page...

        // Close the browser
        driver.quit();
    }
}


