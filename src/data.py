import pandas as pd
from datasets import load_dataset
from funcs import clean
from pathlib import Path


class AnekdotClass:
    def __init__(self, dataset_name: str):
        self.dataset = load_dataset(dataset_name)

    def save_data(self):
        anekdots = []
        for element in self.dataset['train']:
            anekdots.append(element['text'])

        df_anekdots = pd.DataFrame(anekdots, columns=['text'])
        del anekdots

        df_anekdots['text_clean'] = df_anekdots['text'].apply(lambda x: clean(x))

        df_anekdots.dropna().to_csv(Path.cwd() / 'data' / 'anekdots.csv')