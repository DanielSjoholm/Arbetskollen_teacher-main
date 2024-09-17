from dagster import asset
import dlt
import requests
import json

# DLT-funktioner för att hämta data
def _get_ads(url_for_search, params):
    headers = {"accept": "application/json"}
    response = requests.get(url_for_search, headers=headers, params=params)
    response.raise_for_status()
    return json.loads(response.content.decode("utf8"))

@dlt.resource(write_disposition="append")
def jobsearch_resource(params, batch_size=100, max_batches=None):
    url = "https://jobsearch.api.jobtechdev.se"
    url_for_search = f"{url}/search"

    offset = 0
    batch_count = 0

    while True:
        params["offset"] = offset
        ads = _get_ads(url_for_search, params)["hits"]

        if not ads:
            break

        for ad in ads:
            yield ad

        offset += batch_size
        batch_count += 1

        if max_batches is not None and batch_count >= max_batches:
            break

# Definiera en asset som representerar att hämta och ladda jobbannonser
@asset
def fetch_job_ads():
    pipeline = dlt.pipeline(
        pipeline_name="jobsearch_teacher_pipeline",
        destination="snowflake",
        dataset_name="staging",
    )

    query = "lärare"
    params = {"q": query, "limit": 100}

    # Kör pipelinen och ladda data till Snowflake
    load_info = pipeline.run(jobsearch_resource(params=params, max_batches=10), table_name="jobsearch_teacher_data")
    return load_info