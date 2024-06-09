from pathlib import Path
import sys
sys.path.insert(0, "C:\\Users\\Alexander Kazakov\\Documents\\bot_anekdot\\src")
from sbert import SbertPretrained

def main():
    model = SbertPretrained()

    print('-- Getting embeddings...')
    embeddings_dataset_path = Path.cwd() / 'data' / 'embeddings_dataset'
    model.load_df() if not embeddings_dataset_path.exists() else model.load_embeddings()
    print('-- Adding FAISS index...')
    model.add_faiss_index()

    while True:
        print('White base anekdot:')
        model.find_similar(input())


if __name__ == '__main__':
    main()
