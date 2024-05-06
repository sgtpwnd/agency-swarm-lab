from agency_swarm.tools import BaseTool
from pydantic import Field
import asyncio
from pyppeteer import launch

class PuppeteerWebInteraction(BaseTool):
    """
    This tool uses Puppeteer to automate web interactions like clicking links, filling out forms, and navigating through multiple pages smoothly.
    """

    url: str = Field(
        ..., description="The URL of the web page to start the interaction with."
    )
    action: str = Field(
        ..., description="The type of action to perform (e.g., 'click', 'fill_form')."
    )
    selector: str = Field(
        ..., description="The selector for the element to interact with (e.g., CSS selector)."
    )
    input_data: dict = Field(
        default={}, description="Optional data for actions like filling out forms. Should be a dictionary where keys are selectors and values are input values."
    )

    async def run_async(self):
        """
        Asynchronously executes the specified web interaction using Puppeteer.
        """
        browser = await launch(headless=True)
        page = await browser.newPage()
        await page.goto(self.url)

        if self.action == 'click':
            await page.click(self.selector)
        elif self.action == 'fill_form':
            for field_selector, value in self.input_data.items():
                await page.type(field_selector, value)
            await page.click(self.selector)  # Assuming the selector is for the submit button

        # Optionally, navigate or handle the page after action
        await page.waitForNavigation()
        content = await page.content()
        await browser.close()
        return content

    def run(self):
        """
        Synchronous wrapper for the asynchronous Puppeteer interaction.
        """
        return asyncio.get_event_loop().run_until_complete(self.run_async())

# Example usage:
# tool = PuppeteerWebInteraction(url="https://example.com", action="fill_form", selector="#submit", input_data={"#name": "John Doe", "#email": "email@example.com"})
# result = tool.run()
# print(result)