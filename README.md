# botaccount

A Python script to automate the creation of accounts on [myfansboxs.club](https://myfansboxs.club/). The script uses multithreading, fake user data, and logs created accounts to a CSV file.

## Features

- Generates random names, emails, and passwords using Faker
- Handles CSRF tokens automatically
- Multithreaded for faster account creation
- Logs results (success, failure, error) to `created_accounts.csv`
- Colored terminal output for status messages

## Requirements

- Python 3.11+
- See [requirements.txt](requirements.txt) for dependencies:
  - requests
  - beautifulsoup4
  - faker
  - colorama

## Installation

```sh
git clone https://github.com/yourusername/botaccount.git
cd botaccount
pip install -r requirements.txt
```

## Usage

To run the script:

```sh
python botaccount.py
```

Or with Docker:

```sh
docker build -t botaccount .
docker run --rm botaccount
```

## Configuration

- Edit `THREADS`, `REQUEST_LIMIT`, and `DELAY` in [botaccount.py](botaccount.py) to control concurrency and request rate.
- Output is saved to `created_accounts.csv`.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE)