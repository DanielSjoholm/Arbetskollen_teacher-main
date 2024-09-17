from dagster import Definitions, load_assets_from_modules, define_asset_job
from dagster_dlt_staging import assets

# Ladda alla assets
all_assets = load_assets_from_modules([assets])

# Skapa ett jobb som kör asseten 'fetch_job_ads'
job_for_fetch_job_ads = define_asset_job(name="fetch_job_ads")

# Definiera alla assets och jobb
defs = Definitions(
    assets=all_assets,
    jobs=[job_for_fetch_job_ads],
)