$BaseUrl = if ($args.Count -gt 0) { $args[0] } else { "http://127.0.0.1:8080" }

Write-Host "Checking /health"
$health = Invoke-RestMethod -Uri "$BaseUrl/health"
if ($health.status -ne "ok") { throw "Health check failed" }

Write-Host "Checking /ready"
$ready = Invoke-RestMethod -Uri "$BaseUrl/ready"
if ($ready.status -ne "ready") { throw "Readiness check failed" }

Write-Host "Checking /version"
$version = Invoke-RestMethod -Uri "$BaseUrl/version"
if (-not $version.version) { throw "Version response missing version" }

Write-Host "Smoke test passed for $BaseUrl"
