# -*- coding:utf-8 -*-


# Debugger for normal case
def my_debug():
    input('[Debug] 정지 :: ')
    exit()


# Debugger for case using selenium
def my_debug_sel(driver):
    input('[Debug] 정지 :: ')
    driver.quit()
    exit()
