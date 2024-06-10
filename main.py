import time
from threading_example import run_threading_task
from multiprocessing_example import run_multiprocessing_task

def sequential_execution():
    print("Executando tarefa de forma sequencial")
    start_time = time.time()

    run_threading_task()  
    run_multiprocessing_task()  

    end_time = time.time()
    print(f"Tempo de execução sequencial: {end_time - start_time:.5f} segundos")

if __name__ == "__main__":
    sequential_execution()
