import numpy as np

def run_numpy_example():
    """
    Создает массив NumPy, выполняет простые операции и выводит результаты.
    """
    print("--- Запуск примера с NumPy ---")
    my_array = np.arange(10)
    print(f"Исходный массив: {my_array}")
    squared_array = np.square(my_array)
    print(f"Массив в квадрате: {squared_array}")
    mean_value = np.mean(my_array)
    print(f"Среднее значение: {mean_value:.2f}")
    print("--- Пример с NumPy завершен ---")

if __name__ == "__main__":
    run_numpy_example()