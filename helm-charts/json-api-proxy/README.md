# json-api-proxy

![Version: 0.0.4](https://img.shields.io/badge/Version-0.0.4-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.0.4](https://img.shields.io/badge/AppVersion-0.0.4-informational?style=flat-square)

A Helm chart for the JSON API Proxies

**Homepage:** <https://github.com/devopsmakers/grafana-json-api-proxies/tree/main/helm-charts/json-api-proxy>

## Installation
```
helm repo add grafana-json-apis-proxies https://devopsmakers.github.io/grafana-json-apis-proxies
helm install json-api-proxy grafana-json-api-proxies/json-api-proxy
```

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| Tim Birkett |  |  |

## Source Code

* <https://github.com/devopsmakers/grafana-json-api-proxies/>

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` |  |
| env | list | `[]` |  |
| fullnameOverride | string | `"ical-proxy"` |  |
| image.repository | string | `"ghcr.io/devopsmakers/ical-proxy"` |  |
| image.tag | string | `""` |  |
| imagePullSecrets | list | `[]` |  |
| nameOverride | string | `"ical-proxy"` |  |
| nodeSelector | object | `{}` |  |
| replicaCount | int | `1` |  |
| resources | object | `{}` |  |
| tolerations | list | `[]` |  |
