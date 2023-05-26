import pandas as pd
from pipeline_data import compute_median_mean_diff

def main():
    # Загрузка данных с помощью pandas (здесь используется пример данных)
    data = pd.DataFrame({'Value': [1, 2, 3, 4, 5]})

    # Вычисление разницы между средним и медианой
    result = compute_median_mean_diff(data)

    # Вывод результатов
    print(result)

if __name__ == '__main__':
    main()
