from pathlib import Path
from dagster_dbt import DbtProject

# Använd Path.home() för att hämta hemkatalogen
dbt_project_dir = Path.home().joinpath("path", "to", "dbt_code")
packaged_project_dir = Path.home().joinpath("path", "to", "dbt-project")

dbt_projektledare_project = DbtProject(
    project_dir=dbt_project_dir.resolve(),
    packaged_project_dir=packaged_project_dir.resolve(),
)

# Förbered dbt-projektet om du är i utvecklingsmiljö
dbt_projektledare_project.prepare_if_dev()