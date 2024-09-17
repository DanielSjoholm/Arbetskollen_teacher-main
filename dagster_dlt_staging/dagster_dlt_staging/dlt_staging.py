from dagster import schedule
from dagster_dlt_staging.definitions import job_for_fetch_job_ads

# Schemalägg jobbet att köras varje dag vid midnatt
@schedule(cron_schedule="0 0 * * *", job=job_for_fetch_job_ads)
def daily_dlt_schedule(_context):
    return {}