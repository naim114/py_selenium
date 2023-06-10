import random
import time
from selenium import webdriver

for i in range(25):
    try:
        driver.quit()
    except NameError:
        pass

    time.sleep(5)
    print("===========================================================")
    print("Response " + str(i + 1))

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(
        "https://docs.google.com/forms/d/e/1FAIpQLScUaQGcGez4ATrwwyXbWHsLv7rDpm0_mKlcDs241y0YFSO4YA/viewform")

    time.sleep(2)

    # What is your current age?
    rbutton_age_13 = driver.find_element("xpath", '//*[@id="i5"]/div[3]/div')
    rbutton_age_18 = driver.find_element("xpath", '//*[@id="i8"]/div[3]/div')
    rbutton_age_20 = driver.find_element("xpath", '//*[@id="i11"]/div[3]/div')
    rbutton_age_24 = driver.find_element("xpath", '//*[@id="i14"]/div[3]/div')

    # What is your gender?
    rbutton_male = driver.find_element("xpath", '//*[@id="i21"]/div[3]/div')
    rbutton_female = driver.find_element("xpath", '//*[@id="i24"]/div[3]/div')

    # What level of education have you completed or are currently pursuing?
    rbutton_high = driver.find_element("xpath", '//*[@id="i31"]/div[3]/div')
    rbutton_dip = driver.find_element("xpath", '//*[@id="i34"]/div[3]/div')
    rbutton_bach = driver.find_element("xpath", '//*[@id="i37"]/div[3]/div')
    rbutton_master = driver.find_element("xpath", '//*[@id="i40"]/div[3]/div')
    rbutton_doctor = driver.find_element("xpath", '//*[@id="i43"]/div[3]/div')

    # Have you already chosen a career path?
    rbutton_y = driver.find_element("xpath", '//*[@id="i50"]/div[3]/div')
    rbutton_n = driver.find_element("xpath", '//*[@id="i53"]/div[3]/div')

    # How influential are the following factors in your career decision-making process? Please rate them on a scale of 1 to 5, with 1 being "not influential at all" and 5 being "extremely influential".
    # Personal interests and passions
    rbutton_1_1 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div')
    rbutton_1_2 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div')
    rbutton_1_3 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/span/div[4]/div/div/div[3]/div')
    rbutton_1_4 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/span/div[5]/div/div/div[3]/div')
    rbutton_1_5 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/span/div[6]/div/div/div[3]/div')

    # Salary and financial stability
    rbutton_2_1 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]/div')
    rbutton_2_2 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div')
    rbutton_2_3 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[4]/span/div[4]/div/div/div[3]/div')
    rbutton_2_4 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[4]/span/div[5]/div/div/div[3]/div')
    rbutton_2_5 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[4]/span/div[6]/div/div/div[3]/div')

    # Work-life balance
    rbutton_3_1 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[6]/span/div[2]/div/div/div[3]/div')
    rbutton_3_2 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div/div[3]/div')
    rbutton_3_3 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[6]/span/div[4]/div/div/div[3]/div')
    rbutton_3_4 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[6]/span/div[5]/div/div/div[3]/div')
    rbutton_3_5 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[6]/span/div[6]/div/div/div[3]/div')

    # Opportunities for growth and advancement
    rbutton_4_1 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[8]/span/div[2]/div/div/div[3]/div')
    rbutton_4_2 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[8]/span/div[3]/div/div/div[3]/div')
    rbutton_4_3 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[8]/span/div[4]/div/div/div[3]/div')
    rbutton_4_4 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[8]/span/div[5]/div/div/div[3]/div')
    rbutton_4_5 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[8]/span/div[6]/div/div/div[3]/div')

    # Job security
    rbutton_5_1 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[10]/span/div[2]/div/div/div[3]/div')
    rbutton_5_2 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[10]/span/div[3]/div/div/div[3]/div')
    rbutton_5_3 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[10]/span/div[4]/div/div/div[3]/div')
    rbutton_5_4 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[10]/span/div[5]/div/div/div[3]/div')
    rbutton_5_5 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[10]/span/div[6]/div/div/div[3]/div')

    # Social impact and making a difference
    rbutton_6_1 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[12]/span/div[2]/div/div/div[3]/div')
    rbutton_6_2 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[12]/span/div[3]/div/div/div[3]/div')
    rbutton_6_3 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[12]/span/div[4]/div/div/div[3]/div')
    rbutton_6_4 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[12]/span/div[5]/div/div/div[3]/div')
    rbutton_6_5 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[12]/span/div[6]/div/div/div[3]/div')

    # Flexible work arrangements
    rbutton_7_1 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[14]/span/div[2]/div/div/div[3]/div')
    rbutton_7_2 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[14]/span/div[3]/div/div/div[3]/div')
    rbutton_7_3 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[14]/span/div[4]/div/div/div[3]/div')
    rbutton_7_4 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[14]/span/div[5]/div/div/div[3]/div')
    rbutton_7_5 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[14]/span/div[6]/div/div/div[3]/div')

    # Work culture and organizational values
    rbutton_8_1 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[16]/span/div[2]/div/div/div[3]/div')
    rbutton_8_2 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[16]/span/div[3]/div/div/div[3]/div')
    rbutton_8_3 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[16]/span/div[4]/div/div/div[3]/div')
    rbutton_8_4 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[16]/span/div[5]/div/div/div[3]/div')
    rbutton_8_5 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[16]/span/div[6]/div/div/div[3]/div')

    # Mentorship and guidance
    rbutton_9_1 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[18]/span/div[2]/div/div/div[3]/div')
    rbutton_9_2 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[18]/span/div[3]/div/div/div[3]/div')
    rbutton_9_3 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[18]/span/div[4]/div/div/div[3]/div')
    rbutton_9_4 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[18]/span/div[5]/div/div/div[3]/div')
    rbutton_9_5 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[18]/span/div[6]/div/div/div[3]/div')

    # Geographic location
    rbutton_10_1 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[20]/span/div[2]/div/div/div[3]/div')
    rbutton_10_2 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[20]/span/div[3]/div/div/div[3]/div')
    rbutton_10_3 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[20]/span/div[4]/div/div/div[3]/div')
    rbutton_10_4 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[20]/span/div[5]/div/div/div[3]/div')
    rbutton_10_5 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[20]/span/div[6]/div/div/div[3]/div')

    # Less distance to workplace
    rbutton_11_1 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[22]/span/div[2]/div/div/div[3]/div')
    rbutton_11_2 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[22]/span/div[3]/div/div/div[3]/div')
    rbutton_11_3 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[22]/span/div[4]/div/div/div[3]/div')
    rbutton_11_4 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[22]/span/div[5]/div/div/div[3]/div')
    rbutton_11_5 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[22]/span/div[6]/div/div/div[3]/div')

    # Recognition and rewards for performance
    rbutton_12_1 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[24]/span/div[2]/div/div/div[3]/div')
    rbutton_12_2 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[24]/span/div[3]/div/div/div[3]/div')
    rbutton_12_3 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[24]/span/div[4]/div/div/div[3]/div')
    rbutton_12_4 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[24]/span/div[5]/div/div/div[3]/div')
    rbutton_12_5 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[24]/span/div[6]/div/div/div[3]/div')

    # Diversity and inclusion in the workplace
    rbutton_13_1 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[26]/span/div[2]/div/div/div[3]/div')
    rbutton_13_2 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[26]/span/div[3]/div/div/div[3]/div')
    rbutton_13_3 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[26]/span/div[4]/div/div/div[3]/div')
    rbutton_13_4 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[26]/span/div[5]/div/div/div[3]/div')
    rbutton_13_5 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[26]/span/div[6]/div/div/div[3]/div')

    # How important is it for you to...
    # have a career that aligns with your personal values and beliefs?
    rbutton_14_1 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div')
    rbutton_14_2 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div')
    rbutton_14_3 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[2]/span/div[4]/div/div/div[3]/div')
    rbutton_14_4 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[2]/span/div[5]/div/div/div[3]/div')
    rbutton_14_5 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[2]/span/div[6]/div/div/div[3]/div')

    # have work-life balance when choosing your career path?
    rbutton_15_1 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]/div')
    rbutton_15_2 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div')
    rbutton_15_3 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[4]/span/div[4]/div/div/div[3]/div')
    rbutton_15_4 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[4]/span/div[5]/div/div/div[3]/div')
    rbutton_15_5 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[4]/span/div[6]/div/div/div[3]/div')

    # consider your pay or income potential in your decision-making process for a job?
    rbutton_16_1 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[6]/span/div[2]/div/div/div[3]/div')
    rbutton_16_2 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div/div[3]/div')
    rbutton_16_3 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[6]/span/div[4]/div/div/div[3]/div')
    rbutton_16_4 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[6]/span/div[5]/div/div/div[3]/div')
    rbutton_16_5 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[6]/span/div[6]/div/div/div[3]/div')

    # have the possibility of job advancement when making career decisions?
    rbutton_17_1 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[8]/span/div[2]/div/div/div[3]/div')
    rbutton_17_2 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[8]/span/div[3]/div/div/div[3]/div')
    rbutton_17_3 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[8]/span/div[4]/div/div/div[3]/div')
    rbutton_17_4 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[8]/span/div[5]/div/div/div[3]/div')
    rbutton_17_5 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[8]/span/div[6]/div/div/div[3]/div')

    # have the chance for learning and skill improvement when choosing your career path?
    rbutton_18_1 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[10]/span/div[2]/div/div/div[3]/div')
    rbutton_18_2 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[10]/span/div[3]/div/div/div[3]/div')
    rbutton_18_3 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[10]/span/div[4]/div/div/div[3]/div')
    rbutton_18_4 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[10]/span/div[5]/div/div/div[3]/div')
    rbutton_18_5 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[10]/span/div[6]/div/div/div[3]/div')

    # consider the occupation's future and potential growth when making a career choice?
    rbutton_19_1 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[12]/span/div[2]/div/div/div[3]/div')
    rbutton_19_2 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[12]/span/div[3]/div/div/div[3]/div')
    rbutton_19_3 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[12]/span/div[4]/div/div/div[3]/div')
    rbutton_19_4 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[12]/span/div[5]/div/div/div[3]/div')
    rbutton_19_5 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[12]/span/div[6]/div/div/div[3]/div')

    # have the availability of flexible hours or work-from-home options when choosing a career?
    rbutton_20_1 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[14]/span/div[2]/div/div/div[3]/div')
    rbutton_20_2 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[14]/span/div[3]/div/div/div[3]/div')
    rbutton_20_3 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[14]/span/div[4]/div/div/div[3]/div')
    rbutton_20_4 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[14]/span/div[5]/div/div/div[3]/div')
    rbutton_20_5 = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[14]/span/div[6]/div/div/div[3]/div')

    # Are there any other factors not mentioned above that significantly influence your career choices? If yes, please specify.
    factor_text = driver.find_element(
        "xpath", '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]/textarea')

    # text = "Hello hello hello, this is a test"
    # factor_text.click()
    # factor_text.send_keys(text)

    # submit button
    btn_submit = driver.find_element(
        "xpath", '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')

    # =================================================================================================== #
    # ACTION START
    # =================================================================================================== #

    # age
    age = [13, 18, 20, 24]
    choseAge = random.choices(age, weights=(1, 19, 50, 30), k=1)
    choseAge = choseAge[0]

    if (choseAge == 13):
        rbutton_age_13.click()
    elif (choseAge == 18):
        rbutton_age_18.click()
    elif (choseAge == 20):
        rbutton_age_20.click()
    elif (choseAge == 24):
        rbutton_age_24.click()

    print("What is your current age?: " + str(choseAge))
    time.sleep(1)

    # gender
    gender = ['M', 'F']
    choseGen = random.choices(gender)
    choseGen = choseGen[0]

    if (choseGen == 'M'):
        rbutton_male.click()
    elif (choseGen == 'F'):
        rbutton_female.click()

    print("What is your gender?: " + str(choseGen))
    time.sleep(1)

    # edu
    edu = ['High', 'Dip', 'Bach', 'Master', 'Doc']
    choseEdu = random.choices(edu, weights=(1, 34, 50, 10, 5), k=1)
    choseEdu = choseEdu[0]

    if (choseEdu == 'High'):
        rbutton_high.click()
    elif (choseEdu == 'Dip'):
        rbutton_dip.click()
    elif (choseEdu == 'Bach'):
        rbutton_bach.click()
    elif (choseEdu == 'Master'):
        rbutton_master.click()
    elif (choseEdu == 'Doc'):
        rbutton_doctor.click()

    print("What level of education have you completed or are currently pursuing?: " + str(choseEdu))
    time.sleep(1)

    # chose
    cpath = ['Yes', 'No']
    choseCpath = random.choices(cpath, weights=(60, 40), k=1)
    choseCpath = choseCpath[0]

    if (choseCpath == 'Yes'):
        rbutton_y.click()
    elif (choseCpath == 'No'):
        rbutton_n.click()

    print("Have you already chosen a career path?: " + str(choseCpath))
    time.sleep(1)

    # answer template
    temp = [
        [5, 5, 5, 5, 3, 5, 5, 5, 4, 3, 3, 5, 1, 2, 2, 3, 4, 2, 3, 4],
        [4, 5, 3, 5, 4, 4, 5, 5, 3, 3, 3, 4, 4, 4, 5, 4, 3, 5, 3, 4],
        [5, 2, 3, 2, 3, 4, 2, 3, 3, 1, 2, 1, 3, 4, 5, 5, 3, 5, 2, 3],
        [3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 4, 3, 3, 5, 3, 3, 5, 3, 1],
        [3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3, 4, 4, 3, 5, 4, 1],
        [3, 3, 3, 3, 3, 3, 4, 4, 4, 3, 4, 3, 4, 4, 3, 5, 1, 5, 4, 2],
        [5, 5, 5, 5, 5, 3, 5, 5, 5, 5, 5, 4, 2, 2, 4, 5, 2, 5, 5, 4],
        [5, 5, 3, 4, 4, 2, 3, 4, 4, 1, 1, 2, 3, 4, 3, 5, 4, 3, 5, 5],
        [5, 5, 5, 5, 5, 3, 5, 5, 5, 3, 5, 3, 1, 5, 3, 1, 4, 4, 2, 2],
        [5, 5, 5, 4, 5, 5, 5, 4, 5, 5, 4, 5, 2, 5, 2, 2, 5, 2, 2, 3],
    ]

    choseAns = random.choices(temp)
    choseAns = choseAns[0]

    print("\nHow influential are the following factors in your career decision-making process?")
    print("Personal interests and passions: " + str(choseAns[0]))

    if(choseAns[0] == 1):
        rbutton_1_1.click()
    if(choseAns[0] == 2):
        rbutton_1_2.click()
    if(choseAns[0] == 3):
        rbutton_1_3.click()
    if(choseAns[0] == 4):
        rbutton_1_4.click()
    if(choseAns[0] == 5):
        rbutton_1_5.click()
    time.sleep(1)

    print("Salary and financial stability: " + str(choseAns[1]))

    if(choseAns[1] == 1):
        rbutton_2_1.click()
    if(choseAns[1] == 2):
        rbutton_2_2.click()
    if(choseAns[1] == 3):
        rbutton_2_3.click()
    if(choseAns[1] == 4):
        rbutton_2_4.click()
    if(choseAns[1] == 5):
        rbutton_2_5.click()
    time.sleep(1)

    print("Work-life balance: " + str(choseAns[2]))

    if(choseAns[2] == 1):
        rbutton_3_1.click()
    if(choseAns[2] == 2):
        rbutton_3_2.click()
    if(choseAns[2] == 3):
        rbutton_3_3.click()
    if(choseAns[2] == 4):
        rbutton_3_4.click()
    if(choseAns[2] == 5):
        rbutton_3_5.click()
    time.sleep(1)

    print("Opportunities for growth and advancement: " + str(choseAns[3]))
    if(choseAns[3] == 1):
        rbutton_4_1.click()
    if(choseAns[3] == 2):
        rbutton_4_2.click()
    if(choseAns[3] == 3):
        rbutton_4_3.click()
    if(choseAns[3] == 4):
        rbutton_4_4.click()
    if(choseAns[3] == 5):
        rbutton_4_5.click()
    time.sleep(1)

    print("Job security: " + str(choseAns[4]))
    if(choseAns[4] == 1):
        rbutton_5_1.click()
    if(choseAns[4] == 2):
        rbutton_5_2.click()
    if(choseAns[4] == 3):
        rbutton_5_3.click()
    if(choseAns[4] == 4):
        rbutton_5_4.click()
    if(choseAns[4] == 5):
        rbutton_5_5.click()
    time.sleep(1)

    print("Social impact and making a difference: " + str(choseAns[5]))
    if(choseAns[5] == 1):
        rbutton_6_1.click()
    if(choseAns[5] == 2):
        rbutton_6_2.click()
    if(choseAns[5] == 3):
        rbutton_6_3.click()
    if(choseAns[5] == 4):
        rbutton_6_4.click()
    if(choseAns[5] == 5):
        rbutton_6_5.click()
    time.sleep(1)

    print("Flexible work arrangements: " + str(choseAns[6]))
    if(choseAns[6] == 1):
        rbutton_7_1.click()
    if(choseAns[6] == 2):
        rbutton_7_2.click()
    if(choseAns[6] == 3):
        rbutton_7_3.click()
    if(choseAns[6] == 4):
        rbutton_7_4.click()
    if(choseAns[6] == 5):
        rbutton_7_5.click()
    time.sleep(1)

    print("Work culture and organizational values: " + str(choseAns[7]))
    if(choseAns[7] == 1):
        rbutton_8_1.click()
    if(choseAns[7] == 2):
        rbutton_8_2.click()
    if(choseAns[7] == 3):
        rbutton_8_3.click()
    if(choseAns[7] == 4):
        rbutton_8_4.click()
    if(choseAns[7] == 5):
        rbutton_8_5.click()
    time.sleep(1)

    print("Mentorship and guidance: " + str(choseAns[8]))
    if(choseAns[8] == 1):
        rbutton_9_1.click()
    if(choseAns[8] == 2):
        rbutton_9_2.click()
    if(choseAns[8] == 3):
        rbutton_9_3.click()
    if(choseAns[8] == 4):
        rbutton_9_4.click()
    if(choseAns[8] == 5):
        rbutton_9_5.click()
    time.sleep(1)

    print("Geographic location: " + str(choseAns[9]))
    if(choseAns[9] == 1):
        rbutton_10_1.click()
    if(choseAns[9] == 2):
        rbutton_10_2.click()
    if(choseAns[9] == 3):
        rbutton_10_3.click()
    if(choseAns[9] == 4):
        rbutton_10_4.click()
    if(choseAns[9] == 5):
        rbutton_10_5.click()
    time.sleep(1)

    print("Less distance to workplace: " + str(choseAns[10]))
    if(choseAns[10] == 1):
        rbutton_11_1.click()
    if(choseAns[10] == 2):
        rbutton_11_2.click()
    if(choseAns[10] == 3):
        rbutton_11_3.click()
    if(choseAns[10] == 4):
        rbutton_11_4.click()
    if(choseAns[10] == 5):
        rbutton_11_5.click()
    time.sleep(1)

    print("Recognition and rewards for performance: " + str(choseAns[11]))
    if(choseAns[11] == 1):
        rbutton_12_1.click()
    if(choseAns[11] == 2):
        rbutton_12_2.click()
    if(choseAns[11] == 3):
        rbutton_12_3.click()
    if(choseAns[11] == 4):
        rbutton_12_4.click()
    if(choseAns[11] == 5):
        rbutton_12_5.click()
    time.sleep(1)

    print("Diversity and inclusion in the workplace: " + str(choseAns[12]))
    if(choseAns[12] == 1):
        rbutton_13_1.click()
    if(choseAns[12] == 2):
        rbutton_13_2.click()
    if(choseAns[12] == 3):
        rbutton_13_3.click()
    if(choseAns[12] == 4):
        rbutton_13_4.click()
    if(choseAns[12] == 5):
        rbutton_13_5.click()
    time.sleep(1)

    print("\nHow important is it for you to...")
    print("have a career that aligns with your personal values and beliefs?: " +
          str(choseAns[13]))
    if(choseAns[13] == 1):
        rbutton_14_1.click()
    if(choseAns[13] == 2):
        rbutton_14_2.click()
    if(choseAns[13] == 3):
        rbutton_14_3.click()
    if(choseAns[13] == 4):
        rbutton_14_4.click()
    if(choseAns[13] == 5):
        rbutton_14_5.click()
    time.sleep(1)

    print("have work-life balance when choosing your career path?: " +
          str(choseAns[14]))
    if(choseAns[14] == 1):
        rbutton_15_1.click()
    if(choseAns[14] == 2):
        rbutton_15_2.click()
    if(choseAns[14] == 3):
        rbutton_15_3.click()
    if(choseAns[14] == 4):
        rbutton_15_4.click()
    if(choseAns[14] == 5):
        rbutton_15_5.click()
    time.sleep(1)

    print("consider your pay or income potential in your decision-making process for a job?: " +
          str(choseAns[15]))
    if(choseAns[15] == 1):
        rbutton_16_1.click()
    if(choseAns[15] == 2):
        rbutton_16_2.click()
    if(choseAns[15] == 3):
        rbutton_16_3.click()
    if(choseAns[15] == 4):
        rbutton_16_4.click()
    if(choseAns[15] == 5):
        rbutton_16_5.click()
    time.sleep(1)

    print("have the possibility of job advancement when making career decisions?: " +
          str(choseAns[16]))
    if(choseAns[16] == 1):
        rbutton_17_1.click()
    if(choseAns[16] == 2):
        rbutton_17_2.click()
    if(choseAns[16] == 3):
        rbutton_17_3.click()
    if(choseAns[16] == 4):
        rbutton_17_4.click()
    if(choseAns[16] == 5):
        rbutton_17_5.click()
    time.sleep(1)

    print("have the chance for learning and skill improvement when choosing your career path?: " +
          str(choseAns[17]))
    if(choseAns[17] == 1):
        rbutton_18_1.click()
    if(choseAns[17] == 2):
        rbutton_18_2.click()
    if(choseAns[17] == 3):
        rbutton_18_3.click()
    if(choseAns[17] == 4):
        rbutton_18_4.click()
    if(choseAns[17] == 5):
        rbutton_18_5.click()
    time.sleep(1)

    print("consider the occupation's future and potential growth when making a career choice?: " +
          str(choseAns[18]))
    if(choseAns[18] == 1):
        rbutton_19_1.click()
    if(choseAns[18] == 2):
        rbutton_19_2.click()
    if(choseAns[18] == 3):
        rbutton_19_3.click()
    if(choseAns[18] == 4):
        rbutton_19_4.click()
    if(choseAns[18] == 5):
        rbutton_19_5.click()
    time.sleep(1)

    print("have the availability of flexible hours or work-from-home options when choosing a career?: " +
          str(choseAns[19]))
    if(choseAns[19] == 1):
        rbutton_20_1.click()
    if(choseAns[19] == 2):
        rbutton_20_2.click()
    if(choseAns[19] == 3):
        rbutton_20_3.click()
    if(choseAns[19] == 4):
        rbutton_20_4.click()
    if(choseAns[19] == 5):
        rbutton_20_5.click()
    time.sleep(1)

    # Factor
    factor = ['None', 'Social Media', 'Family',
              'Remote work', 'Recognition/Power', 'Peer Influence']
    choseFac = random.choices(factor, weights=(57, 10, 10, 10, 3, 10), k=1)
    choseFac = choseFac[0]

    print("Are there any other factors not mentioned above that significantly influence your career choices? If yes, please specify: " + str(choseFac))

    factor_text.click()
    factor_text.send_keys(choseFac)

    time.sleep(1)
    btn_submit.click()
    time.sleep(2)

driver.quit()
