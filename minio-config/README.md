Here's how to edit your Minio server config to emit webhooks:

Usage:

```
# docker run -ti -v `pwd`:/root/ alexellis2/minio-config \
  -enabled=true -source=config.json -endpoint=http://gateway:8080/function/func_echoit > config.json.new
```

