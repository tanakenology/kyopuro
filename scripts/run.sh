APP=$1
DEFAULT_IMAGE="python:alpine"
IMAGE="${2:-$DEFAULT_IMAGE}"
docker run -it --rm \
    -v "$(pwd)"/$APP:/usr/src/app \
    -w /usr/src/app \
    $IMAGE \
    sh