import queue

#Queue 생성
gui_queue = queue.Queue()
gui_queue.put(1)
gui_queue.get()

import threading
    
threading.Thread(target=worker_thread, args=(
        'Thread 1', 500, gui_queue,),  daemon=True).start()

def worker_thread(thread_name, run_freq, qui_queue) :
    print('Starting thread 1 - {} that runs every {} ms'.format(thread_name, run_freq))
    for i in itertools.count():
        time.sleep(run_freq/1000)
        gui_queue.put('{} - {}'.format(thread_name, i))

def the_main_gui(gui_queue):
    layout = [[sg.Text('This is multithread window')],
            [sg.Text('', size=(15, 1), key='OUTText')],
            [sg.Output(size=(40,6))],
            [sg.Button('Exit')]]

    window = sg.Window('Multithreaded Window', layout)

    while True:
        event, values = window.read(timeout=100)
        if event in (None, 'Exit'):
            break
    window.close()

message = gui_queue.get()
print(message)

while True:                 
            try:                    
                message = gui_queue.get_nowait()
            except queue.Empty:     
                break               
            # if message received from queue, display the message in the Window
            if message:
                window['OUTText'].update(message)
                window.refresh()
                print(message)
