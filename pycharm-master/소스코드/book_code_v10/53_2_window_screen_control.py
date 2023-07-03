import pyautogui as pag
import time
import os

# 1) 크롬 브라우저 실행
command = '"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --start-maximized ' + "https://news.naver.com/"
os.system(command)
time.sleep(0.2)

# 2) 전체 화면으로 전환
pag.hotkey('alt', 'space')
pag.press('x')
time.sleep(0.1)

# 3) 좌측으로 창이동
pag.hotkey('winleft', 'left')
time.sleep(0.1)

# 4)우측에 놓을 프로그램 선택 취소
pag.press('esc')
time.sleep(0.1)

# 5) 워드 실행
os.system('"C:\Program Files\Microsoft Office\Office14\WINWORD.EXE"')
time.sleep(0.2)

# 6) 우측으로 창 이동
pag.hotkey('winleft', 'right')

