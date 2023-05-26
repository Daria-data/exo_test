import pandas as pd
from pipeline_data import compute_median_mean_diff


def test_compute_median_mean_diff():
    # Générer des données pour le test
    data = pd.DataFrame({'Value': [1, 2, 3, 4, 5]})

    # Calculer la différence entre la moyenne et la médiane
    result = compute_median_mean_diff(data)

    # Vérifier les valeurs attendues
    assert result['Mean'][0] == 3.0
    assert result['Median'][0] == 3.0
    assert result['Difference'][0] == 0.0
