Write-host "Starting project... in 5 secs in PRODUCTION MODE" -ForegroundColor Green
uvicorn main:app   --port 8000
# uvicorn main:app --host 0.0.0.0 --port 8080 --log-level critical