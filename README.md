# elasticsearch-python-example

## Elasticsearch Query Script

This script connects to an Elasticsearch server, runs a query to fetch all documents from a specified index, and prints the results. The script includes logging and exception handling for robust error reporting.

## Notes
This script is configured to disable SSL certificate verification. This is suitable for development environments but should be handled with caution in production. This code also considers a local installation of Elasticsearch running as localhost, however it can be modified to connect to any remote server with basic authentication.

Replace your server details and credentials in the elastic-query.py as following:

```bash
https://[ELASTIC_USER]:[ELASTIC_PASSWORD]@localhost:9200
```

Make sure your Elasticsearch server is running and accessible at the specified URL.

## Requirements

- Python 3.x
- `elasticsearch` library
- `urllib3` library

## Installation

1. **Clone the repository** (if applicable):
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv myenv
    source myenv/bin/activate  # On Windows: myenv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install elasticsearch urllib3
    ```

## Configuration

Before running the script, replace `[ELASTIC_USER]` and `[ELASTIC_PASSWORD]` in the `Elasticsearch` connection string with your actual Elasticsearch credentials.

## Usage

Run the script with Python (Windows):
```bash
python .\elastic-query.py

