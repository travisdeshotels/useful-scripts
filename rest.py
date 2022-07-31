#!/usr/bin/python
import argparse
import codecs
import json
import os
import requests
import sys

from dotenv import load_dotenv


def get_env_value(var):
    if os.environ.get(var):
        return os.environ[var]
    else:
        print(f'Please set {var}')
        sys.exit(1)


def send_request():
    header = json.load(open(header_file))
    #print(type(header))
    #print(header)
    with open(request_body_file, 'r') as file:
        data = json.loads(file.read())
    #print(type(data))
    #print(data)
    response = requests.request(args.request_type, url=base_url, headers=header, data=json.dumps(data))
    print(response.status_code)
    print(response.text)
    f = codecs.open(response_file_name, 'w', 'utf-8')
    f.write(response.text)
    f.close()


load_dotenv()
base_url = get_env_value('base_url')
request_body_file = get_env_value('request_body_file')
response_file_name = get_env_value('response_file_name')
header_file = get_env_value('header_file')

parser = argparse.ArgumentParser()
parser.add_argument('request_type', help='get/post/put/etc')
parser.add_argument('url', nargs='?', help='endpoint url')
parser.add_argument('-i', '--input_file', help='input file for request body')
parser.add_argument('-o', '--output_file', help='output file for saving response')
parser.add_argument('-hf', '--header_file', help='file for the request header')
args = parser.parse_args()
if args.url:
    base_url = base_url + args.url
if args.input_file:
    request_body_file = args.input_file
if args.output_file:
    response_file_name = args.output_file
if args.header_file:
    header_file = args.header_file
send_request()
