#!/bin/bash

# http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -euo pipefail

if [ -e "bootstrap-salt.sh" ]; then rm "bootstrap-salt.sh"; fi
curl -s -o bootstrap-salt.sh -L https://bootstrap.saltstack.com
sh bootstrap-salt.sh