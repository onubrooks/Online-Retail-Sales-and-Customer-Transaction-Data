curl -X POST retailanalytics-s6vogpdjna-ew.a.run.app/api/pipeline_schedules/1/pipeline_runs/f90a83889bb74b82b4472b1baabf6515 \
  --header 'Content-Type: application/json' \
  --data '
{
  "pipeline_run": {
    "variables": {
      "dataset": "all",
      "batch": "true"
    }
  }
}'