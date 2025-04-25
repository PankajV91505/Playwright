from playwright.sync_api import sync_playwright
text_alert =[]


def handle_alert(dialog):
    message = dialog.message
    text_alert.append(message)
    dialog.accept()  # Accept the alert dialog

def handle_alert1(dialog):
    print("Alert message:", dialog.message)
    dialog.accept()  # Accepting the dialog



with sync_playwright() as p:
   browser = p.firefox.launch(headless=False)  
   page = browser.new_page()
   page.goto("https://demo.automationtesting.in/Alerts.html")
   
#    page.wait_for_selector("//div[@id='OKTab']/button").click()   #  / ---> because it is first child of div
#    page.wait_for_timeout(5000)

   page.wait_for_selector("//a[@href='#CancelTab']").click()
   page.wait_for_timeout(2000)
   
   # Control alert dialog
   page.on("dialog", handle_alert)  # Register the dialog handler
    
   page.wait_for_selector("//div[@id='CancelTab']/button").click() 
   page.wait_for_timeout(2000)
   print("Alert message:", text_alert[0])  # Print the alert message
   
   page.wait_for_selector("//a[@href='#Textbox']").click()
   page.wait_for_timeout(2000)
   
    # Control prompt dialog
   page.on("dialog", handle_alert1)  # Register the dialog handler
   page.wait_for_selector("//div[@id='Textbox']/button").click()
   print("Alert message:", text_alert[1])  # Print the alert message
   page.wait_for_timeout(2000)
   