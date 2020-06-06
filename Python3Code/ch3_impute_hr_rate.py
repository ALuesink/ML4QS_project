import matplotlib.pyplot as plt
import matplotlib.dates as md
import pandas as pd
from Chapter3.KalmanFilters import KalmanFilters
from util.VisualizeDataset import VisualizeDataset
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
    # print(dataset.index)

    DataViz.plot_dataset(dataset, ['hr_watch_rate', 'hr_watch_rate_kalman'], ['exact', 'exact'], ['line', 'line'])
    # DataViz.plot_xy([dataset.index], [dataset['hr_watch_rate']])

    # xfmt = md.DateFormatter('%H:%M')
    #
    # fig, axs = plt.subplots(2, sharex=True, sharey=False)
    # axs[0].xaxis.set_major_formatter(xfmt)
    # axs[0].plot(dataset.index, 'hr_watch_rate', 'bo', data=dataset)
    # axs[0].set_title('hr_watch_rate')
    # axs[1].xaxis.set_major_formatter(xfmt)
    # axs[1].plot(dataset.index, 'hr_watch_rate_kalman', 'bo', data=dataset)
    # axs[1].set_title('hr_watch_rate_kalman')
    # plt.show()

    # dataset.to_csv(DATA_PATH / RESULT_FNAME)

if __name__ == '__main__':
    main()