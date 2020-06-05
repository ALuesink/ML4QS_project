from Chapter3.KalmanFilters import KalmanFilters
from util.VisualizeDataset import VisualizeDataset
import pandas as pd
from pathlib import Path

def main():
    DATA_PATH = Path('./intermediate_datafiles/')
    DATASET_FNAME = 'chapter2_result.csv'
    RESULT_FNAME = 'chapter3_heart_rate.csv'

    try:
        dataset = pd.read_csv(Path(DATA_PATH / DATASET_FNAME), index_col=0)
        dataset.index = pd.to_datetime(dataset.index)
    except IOError as e:
        print('File not found, try to run the preceding crowdsignals scripts first!')
        raise e

    DataViz = VisualizeDataset(__file__)

    # Original heart rate values
    # DataViz.plot_imputed_values(dataset, ['original'], 'hr_watch_rate')

    Kalman = KalmanFilters()

    dataset = Kalman.apply_kalman_filter(dataset, 'hr_watch_rate')
    # print(dataset.head())
    # print(dataset.columns)

    DataViz.plot_dataset(dataset, ['hr_watch_rate', 'hr_watch_rate_kalman'], ['exact','exact'], ['line', 'line'])

    dataset.to_csv(DATA_PATH / RESULT_FNAME)

if __name__ == '__main__':
    main()