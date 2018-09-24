## Build and Run docs locally
```bash
docker build -t build/raw-api -f ./docs/api/Dockerfile ./ && docker run -p 8080:8080 build/raw-api
```