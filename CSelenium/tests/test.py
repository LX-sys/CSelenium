from src.Cselenium.CSelenium import ChromeSelenium


def test1():
    cs = ChromeSelenium()
    cs.get("http://www.baidu.com")
    cs.wait(2)
    cs.quit()


def test2():
    cs = ChromeSelenium()
    cs.get("http://www.baidu.com")
    cs.id("kw").send_keys("hello world")
    cs.wait(2)
    cs.quit()


def test3():
    cs = ChromeSelenium()
    cs.get("http://www.baidu.com")
    cs.id("kw").send_keys("hello world")
    cs.id("su").click()
    cs.wait(2)
    cs.quit()

def test4():
    cs = ChromeSelenium()
    cs.get("http://www.baidu.com")
    cs.id("kw").send_keys("abc")
    cs.simulationKeyDown(cs.Key.F12)
    # cs.id("su").click()
    cs.wait(2)
    cs.quit()

test4()