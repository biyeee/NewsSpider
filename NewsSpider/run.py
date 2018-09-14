import os
import threading


def sohu():
    os.system("scrapy crawl sohu ")


def sina():
    os.system("scrapy crawl sina ")

threads = []
t1 = threading.Thread(target=sohu, args=())
threads.append(t1)
t2 = threading.Thread(target=sina, args=())
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    for j in threads:
        j.join()
