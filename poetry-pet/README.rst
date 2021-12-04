## Create poetry project
```
poetry new poetry-pet
```

# Poetry commands useful for setting up envs

```
poetry env info
poetry shell
poetry install --no-dev
poetry add <package>
poetry add -D <package>
```

# Build docker image

```
docker build -t nandhu_poetry . 
```

# Run docker image as container
```
docker run -i -t image:tag /bin/bash
```

