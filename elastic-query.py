import logging
from elasticsearch import Elasticsearch
from elasticsearch import exceptions
from urllib3 import disable_warnings, exceptions as urllib3_exceptions

# Configure logging set to DEBUG for verbose log messages 
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Disable SSL certificate warnings 
disable_warnings(urllib3_exceptions.InsecureRequestWarning)

try:
    
    logger.info("Starting connection with Elasticsearch server...")
    # Connect to Elasticsearch with ssl certificate verification disabled
    es = Elasticsearch(
        ['https://[ELASTIC_USER]:[ELASTIC_PASSWORD]@localhost:9200'],
        verify_certs=False,
        ssl_show_warn=False
    )
    
    # Defining a query
    query = {
        "query": {
            "match_all": {}
        }
    }

    # Define the index where the query should be executed - processing_records index
    # Execute query
    response = es.search(index="processing_records", body=query)
    
    logger.info("Connection done and search sucessfully executed against Elasticsearch server")

    logger.debug("Full query response: %s", response)

    # Print results
    print("Search results:")
    for hit in response['hits']['hits']:
        print(hit['_source'])

except exceptions.ConnectionError as e:
    logger.error("Elastic Search Connection Error Exception", exc_info=True)
except exceptions.TransportError as e:
    logger.error("Transport Error while connecting or executing query against Elasticsearch", exc_info=True)
except Exception as e:
    logger.error("Unexpected error exception", exc_info=True)
