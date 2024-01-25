# custom-compliance-demo

Interacts with the Cloud One Conformity API for creating a custom compliance standard.

For technical details about the Custom Compliance Standard API see https://cloudone.trendmicro.com/docs/conformity/api-reference/tag/Custom-Compliance-Standards

All modules used are part of the Python Standard Library so no additional installation is needed.

## usage

`python create-compliance-standard.py --region REGION --apiKey APIKEY --customStandardFilename CUSTOMCOMPLIANCEFILE`

All parameters are mandatory:

- region: Specifies the Cloud One service region. It is a required argument and must be one of the specified choices (us-1, in-1, gb-1, jp-1, de-1, au-1, ca-1, sg-1, trend-us-1).

- apiKey: Requires a Cloud One API Key with administration rights

- customStandardFilename: Specifies the filename of the custom compliance standard

Additional help can be obtained by using the help switches `-h`, `--h` or `help`:

`python create-compliance-standard.py -h`

## designing a custom compliance standard

A custom compliance standard is provided as a JSON file. The script takes care of submitting the file to the API.

To create the custom compliance standard file you will need the following details:

- name: Intended name for the standard, i.e. "Internal Controls Framework"
- version: Versioning your standard is strongly encouraged
- description: Describes the intent of the custom compliance standard to the intended audience, i.e. "This standard provides prescritive guidance for configuring and operating cloud services in our environment"
- controls: A list of security controls that will comprise the custom compliance standard. Each control is specified as follows:
  - aid: A unique identifier of the control, i.e. An identifier from your own controls framework or as suggested by the issuing body
  - title: A descriptive name or label for the security control
  - headings: Provides the hierarchy in which controls will be presented to the audience. You can specify up to 3 levels using the `level1`, `level2` & `level3` properties

To provide mappings to Cloud One Conformity rules use the fields:

- `awsRules`: Use only AWS rule identifiers at https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/
- `azureRules`: Use only Azure rule identifiers at https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/
- `gcpRules`: Use only GCP rule identifiers at https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/

### design example

See the JSON below which describes the `Internal Controls Framework v0.1a` provided as an example:

> Internal Controls Framework v0.1
> This framework provides controls for configuring and operating cloud services in our cloud environments
>
> 1 Access Control
> 1.1 Least Privilege
> 1.1.1: Authorize Access to Security Functions
> 1.1.2: Review of User Privileges
>
> 2 Continuous Monitoring
> 2.1: Automation Support for Monitoring

```json
{
  "data": {
    "name": "Internal Controls Framework",
    "version": "v0.1a",
    "description": "This framework provides controls for configuring and operating cloud services in our cloud environments.",
    "isEnabled": true,
    "type": "DRAFT",
    "controls": [
      {
        "aid": "1.1.1",
        "awsRules": ["IAM-045", "IAM-066"],
        "headings": {
          "level1": "1 Access Control",
          "level2": "1.1 Least Privilege"
        },
        "title": "Authorize Access to Security Functions"
      },
      {
        "aid": "1.1.2",
        "awsRules": ["IAM-036"],
        "headings": {
          "level1": "1 Access Control",
          "level2": "1.1 Least Privilege"
        },
        "title": "Review User Privileges"
      },
      {
        "aid": "2.1",
        "awsRules": ["Config-001"],
        "headings": {
          "level1": "2 Continuous Monitoring"
        },
        "title": "Automation Support for Monitoring"
      }
    ]
  }
}
```
