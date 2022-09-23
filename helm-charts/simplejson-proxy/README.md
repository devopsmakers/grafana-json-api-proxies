# simplejson-proxy

![Version: 0.0.1](https://img.shields.io/badge/Version-0.0.1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.0.1](https://img.shields.io/badge/AppVersion-0.0.1-informational?style=flat-square)

A Helm chart for the SimpleJson Proxies

**Homepage:** <https://github.com/devopsmakers/grafana-simplejson-proxy-plugins/tree/main/helm-charts/simplejson-proxy>

## Installation
```
helm repo add devopsmakers https://devopsmakers.github.io/charts/
helm install simplejson-proxy devopsmakers/simplejson-proxy
```

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| Tim Birkett |  |  |

## Source Code

* <https://devopsmakers/grafana-simplejson-proxy-plugins/>

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` |  |
| env | list | `[]` |  |
| fullnameOverride | string | `"ical-simplejson-proxy"` |  |
| image.repository | string | `"ghcr.io/devopsmakers/ical-simplejson-proxy"` |  |
| image.tag | string | `""` |  |
| imagePullSecrets | list | `[]` |  |
| nameOverride | string | `"ical-simplejson-proxy"` |  |
| nodeSelector | object | `{}` |  |
| replicaCount | int | `1` |  |
| resources | object | `{}` |  |
| tolerations | list | `[]` |  |
