#!/usr/bin/env python

import capnp  # noqa: F401

import awsdata_capnp

def readStuff():
    f1 = open("awsdata.bin", 'r')
    awsdata_1 = awsdata_capnp.AwsdataA.read(f1)
    f1.close()

    # my_dict = {'ec2id': 'id-bladslfksdfl'}
    # v1 = awsdata_capnp.AwsdataA.new_message(**my_dict)
    # running = awsdata_1.new_message(**my_dict)
    # print (v1)

    for a1 in awsdata_1.awsdata3:
        print (a1.to_dict())
        # print (a1.ec2id)
        # print (a1.status)

if __name__ == "__main__":
    readStuff()