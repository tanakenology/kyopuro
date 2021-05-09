APP=$1
docker run -it --rm \
    -v "$(pwd)"/$1:/usr/src/app \
    -w /usr/src/app \
    arm64v8/python \
    bash