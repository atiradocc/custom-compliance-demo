#!/usr/local/bin/python3

import argparse
import urllib.request
import urllib.error
import json

def readMappingFile(mappingFileName):
    try:
        with open(mappingFileName, "r") as jsonFile:
            data = json.load(jsonFile)
            return data
    except FileNotFoundError as e:
        raise e
    except json.JSONDecodeError as e:
        raise e
    except Exception as e:
        raise e
    
def callApi(apiUrl, apiKey, data):
    try:
        jsonData = json.dumps(data).encode('utf-8')
        head = { 'Content-Type': 'application/json', 'Authorization': f"ApiKey {apiKey}" }
        req = urllib.request.Request(apiUrl, data=jsonData, headers=head, method='POST')
    
        with urllib.request.urlopen(req) as response:
            if response.getcode() == 200:
                response_data = response.read().decode('utf-8')
                data = json.loads(response_data)
                return data
            else:
                raise Exception(f"HTTP error: {response.getcode()}")
    except urllib.error.URLError as e:
        raise e
    except json.JSONDecodeError as e:
        raise e
    except Exception as e:
        raise e
    
parser = argparse.ArgumentParser(
    description='Creates a custom compliance standard in Cloud One Conformity')
parser.add_argument('--region', type=str, required=True, choices=[
                    'us-1', 'in-1', 'gb-1', 'jp-1', 'de-1', 'au-1', 'ca-1', 'sg-1', 'trend-us-1'], help='Conformity Service Region')
parser.add_argument('--apiKey', type=str, required=True,
                    help='Conformity API Key')
parser.add_argument('--customStandardFilename', type=str,
                    required=True, help='Filename of the custom compliance standard')
args = parser.parse_args()

customMappingsData = readMappingFile(mappingFileName=args.customStandardFilename)

conformityEndpoint = "https://conformity.{}.cloudone.trendmicro.com/api/compliance-standards/custom".format(
    args.region)
response = callApi(apiUrl=conformityEndpoint, data=customMappingsData, apiKey=args.apiKey)

print(json.dumps(obj=response, indent=4))
