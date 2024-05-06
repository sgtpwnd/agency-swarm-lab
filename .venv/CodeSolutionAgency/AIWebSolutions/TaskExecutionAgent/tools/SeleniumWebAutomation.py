from agency_swarm.tools import BaseTool
from pydantic import Field
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class SeleniumWebAutomation(BaseTool):
    """
    This tool uses Selenium to automate web browser interactions such as form submissions, clicks, and navigations.
    It enables the TaskExecutionAgent to manage web content and interactions effectively.
    """

    url: str = Field(
        ..., description="The URL of the web page to interact with."
    )
    action: str = Field(
        ..., description="The type of action to perform (e.g., 'click', 'submit', 'navigate')."
    )
    element_identifier: str = Field(
        ..., description="The identifier for the web element to interact with (e.g., XPath, CSS selector)."
    )

    def run(self):
        """
        Executes the specified web browser interaction using Selenium.
        """
        # Setup Chrome WebDriver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        # Navigate to the URL
        driver.get(self.url)

        # Perform the action
        if self.action == 'navigate':
            driver.get(self.element_identifier)  # Assuming element_identifier is a URL for navigation
        elif self.action == 'click':
            element = driver.find_element(By.XPATH, self.element_identifier)
            element.click()
        elif self.action == 'submit':
            element = driver.find_element(By.XPATH, self.element_identifier)
            element.submit()

        # Optionally, return some information or handle the page after action
        page_source = driver.page_source
        driver.quit()

        return page_source

# Example usage:
# tool = SeleniumWebAutomation(url="https://example.com", action="click", element_identifier="//button[@id='submit']")
# result = tool.run()
# print(result)