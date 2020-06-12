import multiprocessing


def spawn(num):
    print('Spawned! {}'.format(num))

'''
if __name__ == '__main__':  # necessary in multiprocessing
    for i in range(20):
        p = multiprocessing.Process(target=spawn, args=(i,))
        p.start()  # starts the process
        # p.join()  # waits for the process to be over

'''

from multiprocessing import Pool


def job(num):
    return num * 2


if __name__ == '__main__':
    p = Pool(processes=20)
    data1 = p.map(job, range(20))    # maps function to an iterable or a single vlaue
    data2 = p.map(job, [1, 6, 66, 7])
    p.close()
    print(data1)
    print(data2)
