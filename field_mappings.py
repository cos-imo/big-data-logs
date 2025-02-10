from elasticsearch import Elasticsearch
client = Elasticsearch(
    "",
    api_key=""
)
index_name = "projet-big-data-2025"
mappings = {
    "properties": {
        "text": {
            "type": "text"
        }
    }
}
mapping_response = client.indices.put_mapping(index=index_name, body=mappings)
print(mapping_response)
