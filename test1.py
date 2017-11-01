import unittest
import credentials
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

class LoopLogInTest(unittest.TestCase):
    
  def setUp(self):
    self.driver = webdriver.Firefox()

  
  def log_in(self):
    driver = self.driver
    driver.get("https://autoloopbeta.us/DMS/Default.aspx")
    self.assertIn("AutoLoop", driver.title)
    username = driver.find_element_by_id("Username")
    password = driver.find_element_by_id("Password")
    username.send_keys(credentials.username)
    password.send_keys(credentials.password, Keys.ENTER)
    WebDriverWait(driver, 10).until(
      expected_conditions.text_to_be_present_in_element(
        (By.ID, 'ctl00_ctl00_Main_Main_lblCompanyId'), 'Or enter a ')
      )
    self.assertIn("Selection", driver.title)
    dealerID = driver.find_element_by_css_selector("input#ctl00_ctl00_Main_Main_txtCompanyId")
    dealerID.send_keys('344', Keys.ENTER)
    WebDriverWait(driver, 10).until(expected_conditions.title_contains("Administration"))
    self.assertIn("Administration", driver.title)
    print("\nLOG IN TEST: PASSED")
    
  def gallery(self):
    driver = self.driver
    self.log_in()
    driver.get("https://autoloopbeta.us/DMS/App/CampaignMngr/Gallery/Default.aspx")
    self.assertIn("Gallery", driver.title)
    print("GALLERY TEST: PASSED")
    
  def test020_start_campaign(self):
    driver = self.driver
    self.gallery()
    campaignID = driver.find_element_by_css_selector("input#ctl00_ctl00_ctl00_Main_Main_Main_SearchTextBox")
    campaignID.send_keys('Dynamic Print Header', Keys.ENTER)
    driver.find_element_by_css_selector('a.galleryRequestLink')
    print(driver.current_url)
    
  def tearDown(self):
    self.driver.close()
      
suite = unittest.TestLoader().loadTestsFromTestCase(LoopLogInTest)
unittest.TextTestRunner(verbosity=2).run(suite)