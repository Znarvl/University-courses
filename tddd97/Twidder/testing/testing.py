from xml.etree.ElementPath import find
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()


driver.get("http://127.0.0.1:5000/")

# Create user if not existing, requirement #1
def signUp(fName,famName,gender, city, country, email,password, repeatPassword):
    print('##### SIGNUP TEST #####')

    driver.find_element(By.ID, 'fname').send_keys(fName)
    driver.find_element(By.ID, 'fam-name').send_keys(famName)
    Select(driver.find_element(By.ID, 'gender-value')).select_by_value(gender)
    driver.find_element(By.ID, 'city').send_keys(city)
    driver.find_element(By.ID, 'country').send_keys(country)
    driver.find_element(By.ID, 'email-create').send_keys(email)
    driver.find_element(By.ID, 'psw-create').send_keys(password)
    driver.find_element(By.ID, 'psw-again').send_keys(repeatPassword)
    driver.find_element(By.CLASS_NAME, 'signUpButton').click()
    time.sleep(1)

    error = driver.find_elements(By.ID, 'user-email')
    if error:
        return True
    else:
        return False



### Try to login with user and password, requirement #2
def login(email, password):
    print('##### SIGNIN TEST #####')
    driver.find_element(By.ID, 'email-login').send_keys(email)
    driver.find_element(By.ID, 'psw-login').send_keys(password)
    driver.find_element(By.CLASS_NAME,'loginButton').click()
    time.sleep(1)
    error = driver.find_elements(By.ID, 'user-email')
    return True if error else False


#login work, now post on your own wall, requirement #3
def selfPost(message):
    print('##### POST ON YOUR OWN WALL TEST#####')
    driver.find_element(By.ID, 'user-post').send_keys(message)
    driver.find_element(By.ID, 'user-post-click').click()
    driver.find_element(By.ID, 'user-post').clear()
    #error = driver.find_element(By.CLASS_NAME, 'content').text()

    time.sleep(1)
    return message in driver.page_source

#Find other user in browse and post something on their wall, requirement #4
def findOtherUser(userName):
    print('#### FIND OTHER USER ####')
    time.sleep(1)
    driver.find_element(By.XPATH,'//button[text()="Browse"]').click() #path to the browse button
    driver.find_element(By.ID, 'browse-email').send_keys(userName)
    driver.find_element(By.ID, 'submit-browse').click()
    error = driver.find_element(By.ID, 'browse-success').text
    driver.find_element(By.ID, 'browse-email').clear()
    return True if error == "User found." else False

def postOtherUser(message):
    print("#### POST ON OTHER USER ####")
    driver.find_element(By.ID, 'browse-user-post').send_keys(message)
    driver.find_element(By.ID, 'browse-post-submit').click()
    driver.find_element(By.ID, 'browse-email').clear()

    return message in driver.page_source

#Change passowrd, requirement #5
def changePassword(old,new):
    print('#### CHANGE PASSOWRD TEST####')
    driver.find_element(By.XPATH,'//button[text()="Account"]').click()
    driver.find_element(By.ID, 'old-password').send_keys(old)
    driver.find_element(By.ID, 'new-password').send_keys(new)
    driver.find_element(By.ID, 'repeat-new-password').send_keys(new)
    driver.find_element(By.ID,'submit-password').click()
    error = driver.find_element(By.ID, 'change-password-error').text
    return 'Password changed.' in error


#Sign out from user, requirement #6
def signOut():
    print('#### SIGN OUT TEST####')
    driver.find_element(By.XPATH,'//button[text()="Account"]').click()
    driver.find_element(By.ID,'sign-out-button').click()
    error = driver.find_elements(By.ID, 'email-login')
    return True if error else False


def test(value, expected=True):
    if value == expected:
        print('SUCCESS ')
    else:
        print('FAIL')


# Test 1
test(signUp('Erik','Eriksson','Woman', 'Stockholm','Sweden', 'Erik133750fddfdfa@gmail.com', 'Eriksson', 'Eriksson'))
test(signOut())
test(signUp('Erik','Eriksson','Woman', 'Stockholm','Sweden', 'Erik1337420@gmail.com', 'Eriksson', 'Eriksson'), False)
test(login('Erik1337420@gmail.com', 'Eriksson1337'))
time.sleep(1)
test(selfPost('poop'))
test(findOtherUser('Erik@gmail.com'))
test(postOtherUser('poopypoop'))
test(findOtherUser('false@gmail.com'), False) #shall fail
test(changePassword('Eriksson1337', 'Eriksson1337'))
test(signOut())
test(login('Erik@gmail.com', 'Eriksson1337'))


# Test 2
#signUp('Erik','Eriksson','Male', 'Stockholm','Sweden', 'Erik1337@gmail.com', 'Eriksson', 'Eriksson')
#selfPost('test')
#findOtherUser('Erik@gmail.com')
#postOtherUser('This is a test')
#changePassword('Eriksson', 'Badpassword')
#signOut()





