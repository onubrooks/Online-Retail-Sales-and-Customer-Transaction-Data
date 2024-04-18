curl -X POST https://retailanalytics-s6vogpdjna-ew.a.run.app/api/pipeline_schedules/1/pipeline_runs/23a6aa5217a84609a81ca212ddf216a1 \
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