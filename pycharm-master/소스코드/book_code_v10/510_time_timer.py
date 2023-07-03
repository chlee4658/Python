import matplotlib.pyplot as plt
import datetime
from matplotlib import gridspec
from matplotlib.widgets import Button
from matplotlib.widgets import TextBox
import threading
import webbrowser

global time_set
global time_thread
global time_text

def time_elasped():

    global time_thread
    global time_set

    time_set[0] = time_set[0] - 1
    time_set[1] = time_set[1] + 1

    if time_set[0] <= 0:

        time_thread.cancel()
        webbrowser.open("https://www.youtube.com/watch?v=Z9RTvH4raSI")

        return 0

    ax1.clear()
    ax1.pie(time_set, startangle = 90, colors=["red","white"])
    plt.draw()

    print(datetime.datetime.now())

    time_thread = threading.Timer(1, time_elasped)
    time_thread.start()

def time_start(val):
    global time_set
    global time_text
    global time_thread

    try:
        input_time = int(time_text.text)
    except:
        input_time = 60

    if input_time > 0 and input_time <= 60:
        start_time = input_time * 60
        left_time = 3600 - start_time
    else:
        input_time=60
        start_time = input_time * 60
        left_time = 3600 - start_time

    time_set = list([start_time, left_time])

    try:
        time_thread.cancel()
    except:
        pass

    time_elasped()

if __name__ == "__main__":

    fig = plt.figure(figsize=(5,5))

    gs = gridspec.GridSpec(nrows=3, ncols=1,height_ratios = [1, 10, 1])

    ax0 = plt.subplot(gs[0])
    ax1 = plt.subplot(gs[1])
    ax2 = plt.subplot(gs[2])

    ax0.axis('off')
    ax1.axis('off')
    ax2.axis('off')

    ax0.text(0.2, 0.8, "Time Timer").set_fontsize(25)

    start_pos = plt.axes([0.7, 0.05, 0.1, 0.075])
    start = Button(start_pos, "START")

    text_pos = plt.axes([0.6, 0.05, 0.08, 0.075])

    time_set = list([3600, 0])
    ax1.pie(time_set, startangle = 90, colors=["red","white"])

    time_text = TextBox(text_pos, label = "insert time to check ")
    start.on_clicked(time_start)
