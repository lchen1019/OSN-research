import queue
from queue import Queue

qu = queue.Queue(maxsize=10)
qu.put(10)
print(qu.qsize())
print(qu.get())
print(qu.qsize())
