### Becareful use file name. I used file name threading but that is same file as import file threading.
### so it keep error messasge show up, so I changed file name to han_thread now it works.
# threading meand even if x.start doesn't finish y.start kick out.
import threading

class HansMessenger(threading.Thread): ### Inherit from Threading and Thread
    def run(self): ### this is special function for thread, whenever we create thread it will call this run
        for _ in range(10): ### _ means do not care variable, means i just want to run 10 times
            print(threading.currentThread().getName())

x = HansMessenger(name = 'Send out message')
y = HansMessenger(name = 'Receive message')

### usually we need do x.run() becaue run is function but when thread it call start
x.start()   ### start means go to class and call run function
y.start()

## this program runs send message 10 timesa and receive message 10 times but it(y.start) can start before x.start finish