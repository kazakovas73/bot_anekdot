FROM python:3.10-slim

COPY requirements.txt setup.py /workdir/
COPY app/ /workdir/app/
COPY ml/ /workdir/ml/

WORKDIR /workdir

RUN python -m pip install --upgrade pip

RUN pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
RUN pip install -U -e .

# Run the application
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]