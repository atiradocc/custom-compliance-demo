#!/usr/local/bin/python3

import argparse
import urllib.request
import urllib.error
import json

def readMappingFile(mappingFileName):
    try:
        with open(mappingFileName, "r") as jsonFile:
            data = json.load(fp=jsonFile)
            return data
    except FileNotFoundError as e:
        print(f'''
Could not find custom compliance standard file.
Filename: {e.filename}
''')
        raise e
    except json.JSONDecodeError as e:
        print(f'''
\n\nError while parsing JSON file.\n
Line:\t{e.lineno}
Column:\t{e.colno}
Character number:\t{e.pos}\n\n''')
        raise e
    except Exception as e:
        raise e
    
def callApi(apiUrl, apiKey, data):
    try:
        jsonData = json.dumps(data).encode(encoding="utf-8")
        head = { 'Content-Type': 'application/vnd.api+json', 'Authorization': f"ApiKey {apiKey}" }
        req = urllib.request.Request(apiUrl, data=jsonData, headers=head, method='POST')

        print(f'''\n\n
Querying the Cloud One Conformity API to create a custom compliance standard..\n
    Api:\t{req.full_url}
    Method:\t{req.method}\n\n''')

        with urllib.request.urlopen(req) as response:
            responseData = response.read()
            data = json.loads(responseData)
            return data
    except urllib.error.HTTPError as e:
        error = json.loads(e.read())
        print(f'''
\n\nHTTP error code:\t{e.code}\n
{json.dumps(error, indent=4)}\n\n
''')
        raise e
    except urllib.error.URLError as e:
        print(f'\n\nCould not reach the API: {e.reason}\n\n')
        raise e
    except json.JSONDecodeError as e:
        print(f'''
\n\nError while parsing API response.\n
Line:\t{e.lineno}
Column:\t{e.colno}
Message:\t{e.msg}
Response:\n{e.doc}\n\n''')
        raise e
    except Exception as e:
        print(f'An error occurred: {e.reason}')
        raise e
    
parser = argparse.ArgumentParser(
    description='''
create-compliance-standard
Creates a custom compliance standard in Cloud One Conformity.
See the API documentation for more details at https://cloudone.trendmicro.com/docs/conformity/api-reference/tag/Custom-Compliance-Standards
Use the -h or --help switch for running this command.
''')
parser.add_argument('--region', type=str, required=True, choices=[
                    'us-1', 'in-1', 'gb-1', 'jp-1', 'de-1', 'au-1', 'ca-1', 'sg-1', 'trend-us-1'], help='Conformity Service Region')
parser.add_argument('--apiKey', type=str, required=True,
                    help='Conformity API Key with administration rights')
parser.add_argument('--customStandardFilename', type=str,
                    required=True, help='Filename of the custom compliance standard')
args = parser.parse_args()

customMappingsData = readMappingFile(mappingFileName=args.customStandardFilename)

conformityEndpoint = f"https://conformity.{args.region}.cloudone.trendmicro.com/api/compliance-standards/custom"

response = callApi(apiUrl=conformityEndpoint, data=customMappingsData, apiKey=args.apiKey)

print(json.dumps(obj=response, indent=4))
