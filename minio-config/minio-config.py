#!/usr/bin/env python

import argparse
import json

def load(source):
    f = open(source)
    t = f.read()

    l = json.loads(t)
    return l

def update(args):
    l = load(args.source)    
    webhook = l["notify"]["webhook"]
    arn = "1"
    webhook[arn]["endpoint"] = args.endpoint
    webhook[arn]["enable"] = True
    print(json.dumps(l, indent=4,sort_keys = True))

if(__name__=="__main__"):
    parser = argparse.ArgumentParser(description='Update a minio config for webhooks')

    parser.add_argument('-source', help=".minio.config file")
    parser.add_argument('-endpoint', help="HTTP/s endpoint for webhooks")
    parser.add_argument('-enabled', help="HTTP/s endpoint for webhooks")

    args = parser.parse_args()
    if args.source:
        update(args)
