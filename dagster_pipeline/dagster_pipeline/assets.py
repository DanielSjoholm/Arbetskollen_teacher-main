from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets
from .project import dbt_projektledare_project
from dlt import pipeline
from dagster_embedded_elt.dlt import DagsterDltResource, dlt_assets
from .source import project_leader
from .destination import aw_snowflake

@dlt_assets(
        dlt_source = project_leader(),
        dlt_pipeline = pipeline(
            pipeline_name="jobsearch_teacher_pipeline",
            destination="snowflake",
            dataset_name="staging",  # schema
        )
)
def compute(context: AssetExecutionContext, dlt: DagsterDltResource):
    yield from dlt.run(context=context)

@dbt_assets(manifest=dbt_projektledare_project.manifest_path)
def dbt_projektledare_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
    