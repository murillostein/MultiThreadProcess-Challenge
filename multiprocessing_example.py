import multiprocessing
import time

def print_numbers():
    for i in range(5):
        print(f'Número {i}')
        time.sleep(1)

def print_letters(_):
    for letter in 'abcde':
        print(f'Letra {letter}')
        time.sleep(1)

def run_multiprocessing_task():
    start_time = time.time()

    process1 = multiprocessing.Process(target=print_numbers)
    process2 = multiprocessing.Process(target=print_letters, args=[1])

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    end_time = time.time()
    print(f"Tempo de execução com multiprocessing: {end_time - start_time:.5f} segundos")

def run_multiprocessing_single_task():
    """
    Caso você queira rodar a mesma função, mas com várias threads em paralelo.
    """
    start_time = time.time()
    threads = []

    iterable_ = [None]*10
    pool = multiprocessing.Pool(processes=10)  
    results = pool.map(print_letters, iterable_)

    end_time = time.time()
    print(f"Tempo de execução com multiprocessing: {end_time - start_time:.5f} segundos")



def run_normal():
    start_time = time.time()
    print_letters()
    print_numbers()
    end_time = time.time()
    print(f"Tempo de execução sem multiprocessing: {end_time - start_time:.5f} segundos")
