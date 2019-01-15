#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
SWARM_STATE=$(docker info --format '{{.Swarm.LocalNodeState}}')

if [ "${SWARM_STATE}" != 'active']; then
  docker swarm init
fi

docker stack deploy -c "${DIR}/docker-compose.yml" fgtc