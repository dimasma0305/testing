# Testing Challenges - Demo Event

Sample container challenges for the CTF Challenge Deployer system.


## Purpose

This repository contains a minimal web-based CTF challenge that can be used to test:
- Challenge creation from Git repositories
- Docker Compose auto-detection
- Nomad deployment
- Dynamic port allocation
- Health check monitoring
- Challenge access URLs

## Structure

```
testing/
└── demo-event/
    └── web/
        ├── web1/
        │   ├── challenge.yml       # name/category/type + compose_file
        │   ├── docker-compose.yml  # single-service compose
        │   ├── Dockerfile          # nginx serving ./web
        │   └── web/
        │       └── index.html
        └── web2/
            ├── challenge.yml
            ├── docker-compose.yml
            ├── Dockerfile
            └── web/
                └── index.html
```

## Challenge Details

- **Type**: Web Application
- **Server**: Nginx Alpine
- **Port**: 80 (dynamically allocated)
- **Flag**: `FLAG{test_deployment_successful_2024}`

## How to Use (new flow)

1. Push changes (including `challenge.yml` + compose) to the repo.
2. GitHub Actions workflow `automation/challenge-builder.yml` registers each challenge by posting to the Challenge service.
3. Orchestrator reads available challenges from the Challenge service and deploys them.

## challenge.yml fields

- `name`: Challenge display name (e.g., `web1`)
- `category`: Category (`web`, `pwn`, `crypto`, `forensics`, `misc`)
- `type`: Challenge type (currently `container`)
- `compose_file`: Relative compose file (default `docker-compose.yml`)

## What Gets Auto-Detected

From this challenge, the controller will automatically extract:

- **Name**: `testing-repo` (from directory/repo name)
- **Description**: Auto-generated from repository path
- **Category**: `misc` (default)
- **Base Image**: `nginx:alpine` (from docker-compose)
- **Required Ports**: `80` (from docker-compose)
- **Health Check**: Configured via docker-compose
- **Max Instances**: `10` (default)
- **Timeout**: `60` minutes (default)

## Expected Results

When deployed successfully, you should see:
- ✅ Challenge created with auto-detected metadata
- ✅ Deployment status progressing: pending → running → healthy
- ✅ Access URL provided (e.g., http://172.17.0.1:30123)
- ✅ Web page accessible showing the flag
- ✅ Health check passing

## Troubleshooting

### Local Path Not Working

If using a local path doesn't work (git client expects remote URLs):

1. Initialize as a git repo:
   ```bash
   cd /root/nomadlab/testing-repo
   git init
   git add .
   git commit -m "Test challenge"
   ```

2. Use `file://` protocol:
   ```
   Repository: file:///root/nomadlab/testing-repo
   ```

### Port Not Accessible

- Check Nomad allocated the port: http://localhost:4646
- Verify deployment is in "running" status
- Check firewall rules if accessing from another machine

### Health Check Failing

- Ensure nginx is serving on port 80
- Check container logs via Nomad UI
- Verify the health check command is correct

## Production Use

For production CTF challenges:
- Use private Git repositories
- Add authentication requirements
- Implement proper challenge logic
- Set appropriate timeouts and instance limits
- Use custom Docker images
- Add environment variable secrets

## Flag

🏁 **FLAG{test_deployment_successful_2024}**

If you can see this flag in your browser after deployment, everything is working correctly!
