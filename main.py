from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#this code will go in "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"
#and scrape the highest paying jobs data and put them in csv

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

URL = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"


class HighestPayingJobs:
    def __init__(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(URL)
        self.rank_list = ""
        self.major_list = ""
        self.all_numbers = ""
        self.degree_type = ""
        self.early_cp = ""
        self.mid_cp = ""
        self.high_meaning = ""


    #get all data
    def get_data(self):
        self.rank_list = self.driver.find_elements(By.CSS_SELECTOR, "td.data-table__cell.csr-col--rank")
        self.major_list = self.driver.find_elements(By.CSS_SELECTOR, "td.data-table__cell.csr-col--school-name")
        self.all_numbers = self.driver.find_elements(By.CSS_SELECTOR, "td.data-table__cell.csr-col--right ")
        self.early_cp = self.all_numbers[::3]
        self.mid_cp = self.all_numbers[1::3]
        self.high_meaning = self.all_numbers[2::3]
        self.degree_type = self.driver.find_elements(By.CSS_SELECTOR,
                                           "td.data-table__cell.csr-col--school-type.data-table__cell--hidden-mobile")
    #this function put data in csv
    def put_data_in_csv(self):
        with open("Salaries_By_College_Major.csv", mode="a") as data:
            for i in range(len(self.degree_type)):
                data.write(f"\n{self.rank_list[i].text},{self.major_list[i].text},{self.degree_type[i].text},"
                           f"{self.early_cp[i].text.replace(',', '')},{self.mid_cp[i].text.replace(',', '')},"
                           f"{self.high_meaning[i].text}")

    #this function skip to next page
    def skip_page(self):
        next = self.driver.find_element(By.CSS_SELECTOR, "a.pagination__btn.pagination__next-btn")
        next.click()




highest_pj = HighestPayingJobs()

i = 32
while i > 0:
    time.sleep(2)
    highest_pj.get_data()
    highest_pj.put_data_in_csv()
    highest_pj.skip_page()
    i -= 1




