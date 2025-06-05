# lambda-cwl-dashboard


### Cloudwatch Dashboard

- Math expression
```bash
SORT(REMOVE_EMPTY(SEARCH('{AWS/Logs,LogGroupName} MetricName="IncomingBytes"', 'Sum', 2592000)), SUM, DESC)
```

- Metric Label
```bash
${LABEL} [sum: ${SUM}]
```