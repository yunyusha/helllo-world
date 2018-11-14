from selenium import webdriver
# 构建无头浏览器对象
broswer = webdriver.PhantomJS()

# 直接使用浏览器对象渲染页面

broswer.get('https://www.jd.com/')

# result = broswer.find_element_by_xpath('//img')

# broswer.find_element_by_xpath('//button').click()

# broswer.find_el/ement_by_xpath('//input').send_keys("qwer")
# 设置网页向上滚动500px
broswer.execute_script("document.body.scrollTop=500")
print(broswer.page_source)