from selenium import webdriver
class music():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\\Drivers\\chromedriver.exe')
def play(self,query):
    self.query = query
    self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
