#!/usr/bin/env python

import capnp  # noqa: F401

import awsdata_capnp

def readStuff():
    f1 = open("awsdata.bin", 'r')
    awsdata_1 = awsdata_capnp.AwsdataA.read(f1)
    f1.close()

    for a1 in awsdata_1.awsdata3:
        print (a1.to_dict())
        print (a1.ec2id)
        print (a1.status)

if __name__ == "__main__":
    readStuff()
