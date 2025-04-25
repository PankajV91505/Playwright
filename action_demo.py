from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False) 
    context = browser.new_context()  
    page = context.new_page()  
    page.goto("https://demo.automationtesting.in/Selectable.html")
    
    
    #mouse actions
    
    
    # hover the dropdown menu
    page.wait_for_selector('//a[text()="SwitchTo"]').hover()
    
    # click on the element
    page.wait_for_selector('//a[text()="SwitchTo"]').click()
    
    # doble click on the element
    page.wait_for_selector('//a[text()="SwitchTo"]').dblclick()
    
    # right click on the element
    page.wait_for_selector('//a[text()="SwitchTo"]').click(button='right')
    
    # shift + click on the element
    page.wait_for_selector('//a[text()="SwitchTo"]').click(modifiers=['Shift'])
    
    # control + click on the element
    page.wait_for_selector('//a[text()="SwitchTo"]').click(modifiers=['Control'])
    
    
    #keyboard actions
    
    page.wait_for_selector('//a[text()="SwitchTo"]').press("A")
    
    # A-Z , 0-9 , !@#$%^&*()_+, - = , `~ , []{};:'",.<>?/| , \ , / , space , enter , tab , backspace , delete , end , home , pageup , pagedown , arrow keys
    # f1 - f12 , esc , alt , control , shift , meta , command , option , super
    
    page.wait_for_selector('//a[text()="SwitchTo"]').press("$")
    
    page.wait_for_timeout(2000)