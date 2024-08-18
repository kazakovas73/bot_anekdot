FROM python:3.10-slim

COPY requirements.txt setup.py /workdir/
COPY app/ /workdir/app/
COPY data/ /workdir/data/

WORKDIR /workdir

RUN python -m pip install --upgrade pip
RUN pip install -U -e .

# Run the application
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8001"]