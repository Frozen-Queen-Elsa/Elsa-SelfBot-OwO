try:

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import undetected_chromedriver as uc
    import chromedriver_binary
except Exception as e:
    from setup import install
    install()
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import undetected_chromedriver as uc
    import chromedriver_binary
from exception import exception
from time import sleep
from information import information
from twocaptcha import TwoCaptcha
from webhook import webhooks

client = information()
webhook = webhooks()
api = client.twocaptcha['api']
token = client.token

if client.twocaptcha['enable']:
    # Setting Chrom extension
    chrome_options = uc.ChromeOptions()
    chrome_options.add_extension('TwoCaptchaAutoSolve.crx')
    driver = uc.Chrome(options=chrome_options)

    # Setting key 2Captcha Solver
    driver.get('chrome-extension://ifibfemgeogfhoebkmokieepdoobkbpo/options/options.html')
    driver.find_element(By.CSS_SELECTOR, value='body > div > div.content > table > tbody > tr:nth-child(1) > td:nth-child(2) > input[type=text]')
    driver.execute_script("document.getElementsByName('apiKey')[0].value=arguments[0]", api)

    # click Login
    LoginButton = driver.find_element(By.CSS_SELECTOR, "#connect")
    driver.execute_script("arguments[0].click();", LoginButton)

    # Tắt Alert
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()

    # OWO
    driver.get('https://owobot.com/captcha')
    js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__actions.actions > button')))
    driver.find_element(By.CSS_SELECTOR, value='#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__actions.actions > button').click()

    driver.execute_script(js + f'login("{token}")')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[class="button-f2h6uQ lookFilled-yCfaCM colorBrand-I6CyqQ sizeMedium-2bFIHr grow-2sR_-F"]')))
    driver.find_element(By.CSS_SELECTOR, value='button[class="button-f2h6uQ lookFilled-yCfaCM colorBrand-I6CyqQ sizeMedium-2bFIHr grow-2sR_-F"]').click()

    # Đợi extension solver hiện lên rồi f5 vì để ko bị lỗi SiteKey
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "captcha-solver")))
    driver.refresh()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "captcha-solver")))
    SolveButton = driver.find_element(By.CLASS_NAME, "captcha-solver")
    sleep(3)
    driver.execute_script("arguments[0].click();", SolveButton)
    # Wait
    if WebDriverWait(driver, 200).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#app > div > main > div > div > div > div:nth-child(2) > div > div.v-card__actions.mb-3.welcome-text > div"), "I have verified that you're a human")):
        print('Solve Captcha Successfully')
        webhook.webhookPing(f"Solve Captcha link successfully")
        driver.quit()

else:
    # Setting Chrom extension
    chrome_options = uc.ChromeOptions()
    driver = uc.Chrome(options=chrome_options)

    # OWO
    driver.get('https://owobot.com/captcha')
    js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__actions.actions > button')))
    driver.find_element(By.CSS_SELECTOR, value='#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__actions.actions > button').click()
    driver.execute_script(js + f'login("{token}")')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[class="button-f2h6uQ lookFilled-yCfaCM colorBrand-I6CyqQ sizeMedium-2bFIHr grow-2sR_-F"]')))
    driver.find_element(By.CSS_SELECTOR, value='button[class="button-f2h6uQ lookFilled-yCfaCM colorBrand-I6CyqQ sizeMedium-2bFIHr grow-2sR_-F"]').click()
