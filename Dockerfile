FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

# Add auto-restart logic
CMD bash -c "until python botaccount.py; do echo 'App crashed. Restarting in 5s...'; sleep 5; done"
