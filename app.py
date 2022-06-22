from selenium import webdriver
navegador = webdriver.Chrome()
navegador.get("https://blaze.com/pt/games/mines")
navegador.find_element_by_xpath('//*[@id="mine-controller"]/div[1]/div/button').click()
navegador.find_element_by_xpath('//*[@id="auth-modal"]/div[2]/form/div[1]').click('')
email_element = navegador.find_element_by_name('#auth-modal > div.body > form > div:nth-child(1)')


email_element.send_keys('luke_adm@hotmail.com')

