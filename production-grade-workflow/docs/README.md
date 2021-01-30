# Shared Volumes

Shared volumes are used to create a link from a local directory to the Docker container folders
To create a volume use

```
docker run -p client_port:docker_port -v /local/dict/path -v$(pwd):/containers/path - <image-id>
```

