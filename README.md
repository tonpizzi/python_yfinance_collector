# python\_yfinance\_collector

A stock and index data collector using the [yfinance](https://pypi.org/project/yfinance/) library, with support for database storage or CSV file export.

## Features

* Fetch historical stock/index data via Yahoo Finance
* Store data in a database (e.g., SupaBase, PostgreSQL) or export as CSV
* Easily configurable via environment variables

## Installation

1. Clone this repository:
   git clone https://github.com/tonpizzi/python_yfinance_collector.git
   cd python_yfinance_collector

2. (Optional) Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

## `.env` Configuration
This project uses [python-dotenv](https://pypi.org/project/python-dotenv/) to load environment variables from a `.env` file.

Create a `.env` file in the project root with the following content:

# Example configuration
SUPABASE_URL=https://example.supabase.co
SUPABASE_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxx

**Important:** Make sure your `.env` file is listed in `.gitignore` to avoid committing sensitive data.

## Usage
After configuring the `.env` file, run the main script:
python main.py

The script will collect data based on the settings and store it in the specified format.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

For more information on using `python-dotenv`, check out the [official documentation](https://github.com/theskumar/python-dotenv/blob/main/README.md).

