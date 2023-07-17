import asyncio
from pyppeteer import launch

async def retrieve_value():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('popup.js')  # Replace with the actual path to retrieve_data.js
    await asyncio.sleep(1)  # Wait for the JavaScript code to execute

    # Get the result from the console
    result = await page.evaluate('() => { return window.result; }')

    await browser.close()

    return result

# Run the retrieval function
result_value = asyncio.get_event_loop().run_until_complete(retrieve_value())
print(result_value)
