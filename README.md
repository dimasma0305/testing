# Testing Repository - CTF Test Challenge

A simple test challenge for the CTF Challenge Deployer system.

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
testing-repo/
├── docker-compose.yml    # Defines the challenge service
├── web/
│   └── index.html       # Simple web page with flag
└── README.md           # This file
```

## Challenge Details

- **Type**: Web Application
- **Server**: Nginx Alpine
- **Port**: 80 (dynamically allocated)
- **Flag**: `FLAG{test_deployment_successful_2024}`

## How to Use

### Via Web UI

1. Open the Web UI: http://localhost:8080
2. Go to "Create Challenge" tab
3. Fill in:
   ```
   Repository: /root/nomadlab/testing-repo
   Ref: main
   Path: .
   ```
   > Note: For local testing, you can use the absolute path. For remote testing, push this repo to GitHub/GitLab and use that URL.

4. Click "Create Challenge"
5. Deploy from the Challenges tab
6. Access the challenge via the provided URL

### Via API

**Create Challenge:**
```bash
curl -X POST http://localhost:3000/api/v1/challenges \
  -H "Content-Type: application/json" \
  -d '{
    "repository": "/root/nomadlab/testing-repo",
    "ref": "main",
    "path": "."
  }'
```

**Deploy Challenge:**
```bash
# Replace <challenge-id> with the ID from above
curl -X POST http://localhost:3000/api/v1/deployments \
  -H "Content-Type: application/json" \
  -d '{
    "challenge_id": "<challenge-id>",
    "user_id": "test-user-123"
  }'
```

**Check Deployment:**
```bash
# Replace <deployment-id> with the ID from above
curl http://localhost:3000/api/v1/deployments/<deployment-id>
```

## Testing GitHub Integration

To test with a real Git repository:

1. Create a GitHub repository
2. Push this content:
   ```bash
   cd testing-repo
   git init
   git add .
   git commit -m "Initial test challenge"
   git remote add origin https://github.com/YOUR_USERNAME/test-ctf-challenge.git
   git push -u origin main
   ```

3. Use in Web UI:
   ```
   Repository: https://github.com/YOUR_USERNAME/test-ctf-challenge.git
   Ref: main
   Path: .
   ```

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
