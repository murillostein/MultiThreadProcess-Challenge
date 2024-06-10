import threading
import time

def print_numbers():
    for i in range(5):
        print(f'Número {i}')
        time.sleep(1)

def print_letters():
    for letter in 'abcde':
        print(f'Letra {letter}')
        time.sleep(1)

def run_threading_task():
    start_time = time.time()

    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    end_time = time.time()
    print(f"Tempo de execução com threading: {end_time - start_time:.5f} segundos")


def run_multithreading_single_task():
    """
    Caso você queira rodar a mesma função, mas com várias threads em paralelo.
    """
    start_time = time.time()
    threads = []

    for i in range(10):
        thread = threading.Thread(target=print_letters)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    print(f"Tempo de execução com threading: {end_time - start_time:.5f} segundos")

def run_normal():
    start_time = time.time()
    print_letters()
    print_numbers()
    end_time = time.time()
    print(f"Tempo de execução sem multithreading: {end_time - start_time:.5f} segundos")