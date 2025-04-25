from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False) 
    context = browser.new_context()  
    page = context.new_page()  # Corrected here
    page.goto("https://www.redbus.in/")
    
    
    # gives all cookies in the context
    my_cookies = page.context.cookies()
    print(my_cookies)
    
    #clear all cookies in the context
    page.context.clear_cookies()
    
    new_cookies = {
        'name': 'my_cookie',
        'value': 'my_value',
        'domain': '.redbus.in',
        'path': '/',
        'expires': -1,  # Set to -1 to delete the cookie
        'httpOnly': False,
        'secure': False,
        'sameSite': 'Lax'
        
    }
    page.context.add_cookies([new_cookies])
    # Add a cookie to the context
    
    #taking screenshot of the page
    page.screenshot(path='screenshot.png',full_page=True)  #taking screenshot of the page   
    #taking screenshot of the page with full page option