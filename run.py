import unittest
from selenium import webdriver
from bs4 import BeautifulSoup


class DouyuSelenium(unittest.TestCase):
    def setUp(self):
        '''
        初始化方法
        '''
        self.driver = webdriver.PhantomJS()

    def testDouyu(self):
        '''
        具体的测试用力方法，一定要以test开头
        :return:
        '''
        self.driver = webdriver.get('http://www.douyu.com/directory/all')
        while True:
            # 指定xmml解析
            soup = BeautifulSoup(self.driver.page_source, 'xml')
            # 返回当前页面所有房间标题列表 和 观众列表
            titles = soup.find_all('h3', {'class':'ellipsis'})
            nums = soup.find_all('span', {'class':'dy-num'})

            # 使用zip()函数来可以把列表合并,并创建一个元组对的列表[(1,2),(3,4)]
            for title, num in zip(titles, nums):
                print('观众人数:' + num.get_text().strip, '\t房间标题:' + title.get_text().strip())

            # page_source.find()未找到内容则返回-1
            if self.driver.page_source.find('shark-pager-disable-next') != -1:
                break

            # 模拟下一页点击
            self.driver.find_element_by_class_name('shark-pager-next').click()
    def tearDown(self):
        '''
        退出时的清理方法
        :return:
        '''
        print('加载完成！')
        self.driver.quit()


