from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import random

path = "F:\Programming\GitHub\python_projects\WhatsAppBot"
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

time.sleep(12)

def msg_lower(msglist):
    """Makes all the messages lowercase for message-list"""
    msg_list_lower = list(map(lambda x:x.lower(), msglist))
    return list(map(lambda x: x.split(), msg_list_lower))

def morning_msg_list():
    morning_msg_file = open('morningMsg.txt', "r") #opens the file morningMsg.txt in read mode
    morning_list = morning_msg_file.read().splitlines() #puts the file into an array
    morning_msg_file.close()
    # print(morningList)
    return random.choice(morning_list)

def night_msg_list():
    night_msg_file = open('nightMsg.txt', "r") #opens the file nightMsg.txt in read mode
    night_list = night_msg_file.read().splitlines() #puts the file into an array
    night_msg_file.close()
    # print(nightList)
    return random.choice(night_list)
    

def read_file(file_name):
        file_obj = open(file_name, "r") #opens the file contacts.txt in read mode
        words = file_obj.read().splitlines() #puts the file into an array
        file_obj.close()
        return words
names = read_file('contacts.txt')  # Create a contact.txt file in same folder

if __name__ == '__main__':
    while True:
        timeThen = str(datetime.now().strftime('%H:%M:%S'))
        
        for name in names:
            if timeThen == "07:00:00":
                try:
                    person = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
                    person.click()

                    for in range(1,3):
                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                    msg_got = driver.find_elements_by_xpath('//div[@class="_1RAno message-out focusable-list-item"]//div//div//div//div//div//span[@class="_1VzZY selectable-text invisible-space copyable-text"]')
                    msglist = [message.text for message in msg_got]

                    day_check = driver.find_elements_by_xpath('//div[@class="_1ij5F KpuSa"]//span[@dir="auto"][@class="_1VzZY"]')
                    day = [days.text for days in day_check]
                    msgLowerList = msg_lower(msglist)

                    try:
                        msgFinalList = msgLowerList[-1]
                        # print(msgFinalList)
                        flag = 0
                        for msgWord in msgFinalList:
                            if msgWord == "morning":
                                flag = 1
                                break
                        if flag == 0 and day != "TODAY":
                            reply = driver.find_element_by_xpath('//div[@data-tab="6"]')
                            reply.clear()
                            reply.send_keys(f"{morning_msg_list()}")
                            reply.send_keys(Keys.RETURN)
                            print(f"Sent to {name}")
                        else:
                            print(f"Already sent to {name}")
                    except Exception as e:
                        print(e)
                except Exception as e:
                    print(e)
        
            elif timeThen == "23:30:00":
                try:
                    person = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
                    person.click()

                    for i in range(1,3):
                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                    msg_got = driver.find_elements_by_xpath('//div[@class="_1RAno message-out focusable-list-item"]//div//div//div//div//div//span[@class="_1VzZY selectable-text invisible-space copyable-text"]')
                    msglist = [message.text for message in msg_got]

                    day_check = driver.find_elements_by_xpath('//div[@class="_1ij5F KpuSa"]//span[@dir="auto"][@class="_1VzZY"]')
                    day = [days.text for days in day_check]
                    msgLowerList = msg_lower(msglist)

                    try:
                        msgFinalList = msgLowerList[-1]
                        flag = 0
                        for msgWord in msgFinalList:
                            if msgWord == "night":
                                flag = 1
                                break
                        if flag == 0 and day != "TODAY":
                            reply = driver.find_element_by_xpath('//div[@data-tab="6"]')
                            reply.clear()
                            reply.send_keys(f"{night_msg_list()}")
                            reply.send_keys(Keys.RETURN)
                            print(f"Sent to {name}")
                        else:
                            print(f"Already sent to {name}")
                    except Exception as e:
                        print(e)
                except Exception as e:
                    print(e)
