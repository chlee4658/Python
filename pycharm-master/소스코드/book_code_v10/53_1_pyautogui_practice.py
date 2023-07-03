import pyautogui

print(pyautogui.size())

while True:
    print(pyautogui.position())

# 왼쪽 버튼 클릭
pyautogui.click()

# 오른쪽 버튼 클릭
pyautogui.click(button='right')

# 1초마다 2번 클릭
pyautogui.clikck(clicks=2, interval=1)

# 더블클릭
pyautogui.doubleClick()

# 마우스 왼쪽 버튼을 누른다.
pyautogui.mouseDown()

# 마우스 오른쪽 버튼을 뗀다.
pyautogui.mouseUp(button='right')

# 마우스 왼쪽 버튼을 누르고 드래그하기
pyautogui.dragTo(100,200,button='left')

# 10만큼 스클로하여 내린다
pyautogui.scroll(10)

# 우측으로 10만큼 스크롤한다
pyautogui.hscroll(10)

pyautogui.typewrite("Hello world")
pyautogui.hotkey('alt', 'tab')

