import os
import threading


def sohu():
    os.system("scrapy crawl sohu ")


def sina():
    os.system("scrapy crawl sina ")


def ifeng():
    os.system("scrapy crawl ifeng ")


threads = []
t1 = threading.Thread(target=sohu, args=())
threads.append(t1)
t2 = threading.Thread(target=sina, args=())
threads.append(t2)
t3 = threading.Thread(target=ifeng, args=())
threads.append(t3)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    for j in threads:
        j.join()
