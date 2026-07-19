#!/bin/bash

set -e

curl -f http://app.ajay.bar
curl -f http://app.ajay.bar/api/health

echo "Application is healthy"