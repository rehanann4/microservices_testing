#! /usr/bin/env python3
import argparse
import requests
import json


def single_reponse(args):
    url = 'http://localhost:8080/'
    method = args.method
    url_req = url + method
    num1 = args.num1
    num2 = args.num2
    response = requests.post(url_req, data=json.dumps({'num1': num1, 'num2': num2}),
                            headers={'Content-Type' : 'application/json'}
    )
    return response.json()

def combined(args):
    pass

parser = argparse.ArgumentParser()
parser.add_argument('--api', type=str, default='None',
                        help='print text')
parser.add_argument('--method', type=str,
                        help='print text')
parser.add_argument('--num1', type=int,
                        help='print text')
parser.add_argument('--num2', type=int,
                        help='print text')

args = parser.parse_args()

if args.api:
    print(single_reponse(args))

