from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pynput import mouse
import time
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

# 指定 msedgedriver 的路径
msedgedriver_path = 'C:\\Users\\22129\\Desktop\\python文件\\dotter\\edgedriver_win64\\msedgedriver.exe'

# 创建 EdgeOptions 对象
options = Options()

# Edge 浏览器的可执行文件路径
edge_browser_path = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
options.binary_location = edge_browser_path

# 使用 Service 对象指定 msedgedriver 的路径
service = Service(executable_path=msedgedriver_path)

# 初始化 Edge 浏览器
driver = webdriver.Edge(service=service, options=options)

# 设置一个标志，用于判断是否停止点击
stop_clicking = False

# 创建一个鼠标监听器
def on_click(x, y, button, pressed):
    global stop_clicking
    if pressed:
        stop_clicking = True
        # 停止监听
        return False

# 在单独的线程中监听鼠标点击
listener = mouse.Listener(on_click=on_click)
listener.start()

driver.get('https://yjsxk.urp.seu.edu.cn/yjsxkapp/sys/xsxkapp/index.html')
time.sleep(40)

# 打开一个网页
driver.get('https://yjsxk.urp.seu.edu.cn/yjsxkapp/sys/xsxkapp/course.html')

# 找到要点击的位置，这里假设点击的是页面上的一个按钮
button = driver.find_element(By.ID, 'allkc_queryBtn')

# 循环点击按钮，直到停止标志被设置
while not stop_clicking:
    try:
        button.click()
        time.sleep(1)  # 每次点击后等待一段时间
    except Exception as e:
        print(f"Error clicking button: {e}")
        break

# 确保监听器已经停止
listener.stop()

# 关闭浏览器
# driver.quit()

