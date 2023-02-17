from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    
    # launch an instance of a firefox browser
    browser = p.chromium.launch(headless=False)
    
    # create a new tab or page
    page = browser.new_page()
    
    # visit the website given
    page.goto("https://www.google.com/")

    # make sure to close the browser at the end
    browser.close()