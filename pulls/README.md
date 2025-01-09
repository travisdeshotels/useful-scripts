# Pulls
Report open pull requests for desired Git repositories. Draft pulls are shown first, then regular pulls.

## Build
`pip install -r requirements.txt` in the pulls root directory.  
`pip install .` in the project root to install the colors library.

## Set up
In your `.env` file, define
```
git_token=<token>
pulls_config_file=<path>/<filename>
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
