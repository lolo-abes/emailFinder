from unittest import result
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException        
import csv  
import re

def check_exists_by_xpath(xpath):
    try:
        browser.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

browser = webdriver.Chrome()
browser.get('https://www.annuaire-mairie.fr/commercants-montpellier.html')
browser.maximize_window()

# save_btn = browser.find_element_by_class('.otkbtn.otkbtn-primary').click()
browser.implicitly_wait(10)
browser.find_element(By.XPATH, '//*[@id="unic-b"]/div/div/div/div[2]/div[2]/button[2]').click()
boucle=True

# /html/body/div[2]/div[1]/div[3]/ul/li[11]/div/div[1]
# /html/body/div[2]/div[1]/div[3]/ul/li[1]/div/div[1]
# /html/body/div[2]/div[1]/div[4]/ul/li[1]/div/div[1]
# /html/body/div[2]/div[1]/div[4]/ul/li[12]/div/div[1]
# //*[@id="liste_boulangerie"]/ul/li[1]/div/div[1]
# //*[@id="liste_boulangerie"]/ul/li[2]/div/div[1]
# //*[@id="liste_boulangerie"]/ul/li[18]/div/div[1]
# //*[@id="liste_boucherie"]/ul/li[1]/div/div[1]
# //*[@id="liste_boucherie"]/ul/li[12]/div/div[1]

# /html/body/div[2]/div[1]/div[5]/ul[1]/li[1]/div/div[1]
# /html/body/div[2]/div[1]/div[5]/ul[2]/li[1]/div/div[1]
# /html/body/div[2]/div[1]/div[5]/ul[3]/li[2]/div/div[1]

count=0
# //*[@class="annonce_titre"]
# if check_exists_by_xpath('//div[@class="annonce_titre"]'):
#     element = browser.find_elements(By.XPATH, '//div[@class="annonce_titre"]')
#     for e in element:
#         print(e.text)
#         count=count+1
# print(count)
# browser.get('https://www.annuaire-mairie.fr/entreprise-industrie-manufacturiere-montpellier.html')
# browser.implicitly_wait(3)

liste = []
liste_entreprise = []
liste_adresses = []

if check_exists_by_xpath('//div[@class="annonce_content"]/div[1]'):
    element = browser.find_elements(By.XPATH, '//div[@class="annonce_content"]/div[1]')
    for e in element:
        test = [e.text]
        liste_entreprise.append(test)
        print(e.text)
        count=count+1
print(count)
print(liste)
if check_exists_by_xpath('//div[@class="annonce_desc"]/div[1]/div[1]'):
    element = browser.find_elements(By.XPATH, '//div[@class="annonce_desc"]/div[1]/div[1]')
    for e in element:
        print(e.text)
        test = [e.text]
        liste_adresses.append(test)
resultat = []
for entreprise, adresse in zip(liste_entreprise,liste_adresses):
    resultat.append( [*entreprise, str(re.sub(r'.*\n', '', *adresse))] )
    print(entreprise,str(re.sub(r'.*\n', '', *adresse)))
print(resultat)
# header = ['Entreprise', 'Type', 'Adresses', 'Mails']
header = ['Entreprise', 'Adresses']
with open('result.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f,quoting=csv.QUOTE_ALL)
    writer.writerow(header)
    writer.writerows(resultat)


# browser.get('https://www.annuaire-mairie.fr/entreprise-agriculture-sylviculture-peche-montpellier.html')
# browser.implicitly_wait(3)

# if check_exists_by_xpath('//div[@class="annonce_content"]/div[1]'):
#     element = browser.find_elements(By.XPATH, '//div[@class="annonce_content"]/div[1]')
#     for e in element:
#         print(e.text)
#         count=count+1
# if check_exists_by_xpath('//div[@class="annonce_desc"]/div[1]/div[1]'):
#     element = browser.find_elements(By.XPATH, '//div[@class="annonce_desc"]/div[1]/div[1]')
#     for e in element:
#         print(e.text)
# print(count)
# i=1
# y=0
# x=3
# while boucle == True:
#     if check_exists_by_xpath('/html/body/div[2]/div[1]/div['+ str(x) +']/ul/li[' + str(i) + ']/div/div[1]'):
#         element = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div['+ str(x) +']/ul/li[' + str(i) + ']/div/div[1]')
#         print(element.text)
#         if i == 1:
#             y=y+1
#         i=i+1
#     if not check_exists_by_xpath('/html/body/div[2]/div[1]/div['+ str(x) +']/ul/li[' + str(i) + ']/div/div[1]'):
#         print('jai r trouvé frere')
#         x=x+1
#         i=1
#         if (x-3) > y:
#             print('on termine non mais oh !')
#             boucle=False
#     browser.implicitly_wait(1)

# # /html/body/div[2]/div[1]/div[6]/ul[1]/li[1]/div/div[1]
# browser.get('https://www.annuaire-mairie.fr/entreprise-industrie-manufacturiere-montpellier.html')
# browser.implicitly_wait(3)
# i=1
# y=0
# x=1
# z=5
# boucle=True
# while boucle == True:
#     if check_exists_by_xpath('/html/body/div[2]/div[1]/div[' + str(z) + ']/ul[' + str(x) + ']/li[' + str(i) + ']/div/div[1]'):
#         element = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[' + str(z) + ']/ul[' + str(x) + ']/li[' + str(i) + ']/div/div[1]')
#         print(element.text)
#         if i == 1:
#             y=y+1
#         i=i+1
#     if not check_exists_by_xpath('/html/body/div[2]/div[1]/div[' + str(z) + ']/ul[' + str(x) + ']/li[' + str(i) + ']/div/div[1]'):
#         print('jai r trouvé frere')
#         x=x+1
#         i=1
#         if (x-2) > y:
#             print('on termine non mais oh !')
#             z=z+1
#             x=1
#     print("i :" + str(i))
#     print("x :" + str(x))
#     print("y :" + str(z))
#     print("z :" + str(z))
#     browser.implicitly_wait(1)
# browser.implicitly_wait(3)
# if check_exists_by_xpath('//*[@id="otkmodal"]/div[2]/div/origin-dialog-content-geoconfirmation/div[3]/button'):
#     elem = browser.find_element(By.XPATH, '//*[@id="otkmodal"]/div[2]/div/origin-dialog-content-geoconfirmation/div[3]/button')
#     elem.click()
# browser.implicitly_wait(3)
# browser.find_element(By.XPATH, '//*[@id="truste-consent-button"]').click()
# browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/section/div/nav/div/div[5]/ul/li[1]/origin-cta-login/origin-cta-primary/div/a').click()
# save_btn.click()