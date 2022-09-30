# Pulls
Report open pull requests for desired Git repositories. Draft pulls are shown first, then regular pulls.

## Build
`pip install -r requirements-pulls.txt`

## Set up
In your `.env` file, define
```
git_token=<token>
pulls_config_file=<path>/repos.yml
```
Your git token needs the repo scope. The yaml config file uses the format shown below. 

## Example config
```yaml
---
orgs:
  - name: 1610oct24java
    repos:
      - AssociateEvaluationSystem
      - CELT
  - name: EnterpriseQualityCoding
    repos:
      - FizzBuzzEnterpriseEdition
...
```
test
