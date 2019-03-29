#! /bin/sh

curl "https://hooks.slack.com/services/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" --data "payload={'text':'$1'}" -X POST
echo "\n"

