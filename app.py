import os
import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('--method', help='TODO')
parser.add_argument('--endpoint', help='TODO')
parser.add_argument('--data', help='TODO')

args = parser.parse_args()

if args.method is None or args.endpoint is None:
    print({'error': 'must provide method, and endpoint as named arguments'})
    exit(1)

url = os.environ['ELASTICSEARCH_URL'] + args.endpoint

json_header = {'Content-type': 'application/json'}

if args.method == 'get':
    print(requests.get(url).text)
elif args.method == 'post':
    if args.data is None:
        print({'error': 'must provide data to be posted'})
        exit(1)
    print(requests.post(url, data=args.data, headers=json_header).text)
elif args.method == 'put':
    if args.data is None:
        print({'error': 'must provide data to be placed'})
        exit(1)
    print(requests.put(url, data=args.data, headers=json_header).text)
elif args.method == 'delete':
    print(requests.delete(url).text)
else:
    print({'error': 'method must be one of: {get, post, put, delete}'})
    exit(1)
