FROM python:3.11

COPY requirements.txt requirements-dev.txt setup.py /workdir/
COPY app/ /workdir/app/
COPY ml/ /workdir/ml/
COPY data/embeddings_dataset/ /workdir/data/embeddings_dataset/

WORKDIR /workdir

RUN python -m pip install --upgrade pip
RUN pip install -U -e .

# Run the application
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]