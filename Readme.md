# Database Setup and Data Extraction

This repository contains two Python scripts, `database_setup.py` and `data_extraction.py`, designed to work with a SQLite database and extract data from it. These scripts are useful for setting up a database with sample data and extracting that data in JSON format.

## `database_setup.py`

### Overview

`database_setup.py` is responsible for setting up a SQLite database and generating sample data for two tables, "user_table" and "order_table." It uses the SQLAlchemy library for database operations and the Faker library to generate fake data.

### Usage

1. Ensure you have the required Python libraries installed:

   ```bash
   pip install sqlalchemy faker
   ```

2. Run the script to create the database and populate it with sample data:

   ```bash
   python database_setup.py
   ```

3. The script will generate a SQLite database file named `fake_data.db` and populate it with sample user and order data.

## `data_extraction.py`

### Overview

`data_extraction.py` is responsible for extracting data from the SQLite database created by `database_setup.py` and saving it in JSON format. It uses the `sqlite3` library for database operations.

### Usage

1. Ensure you have Python installed.

2. Run the script to extract data from the database and save it as JSON files:

   ```bash
   python data_extraction.py
   ```

3. The extracted data will be saved in two JSON files: `user_records.json` and `order_records.json`.

## Requirements

- Python 3.x
- SQLAlchemy
- Faker

## Author

Ankit Pushpam

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Faker](https://faker.readthedocs.io/en/master/)