#!/usr/bin/env python

import capnp  # noqa: F401

import awsdata_capnp

def writeStuff():
    awsdata1 = awsdata_capnp.AwsdataA.new_message()
    awsdata3 = awsdata1.init("awsdata3", 2)

    a1 = awsdata3[0]
    a1.ec2id = 'id-bladslfksdfl'
    a1.status = 'running'


    a1 = awsdata3[1]
    a1.ec2id = 'id-adslkfdk2'
    a1.status = 'stopped'

    with open('awsdata.bin', 'w') as f1:
        awsdata1.write(f1)


if __name__ == '__main__':
    writeStuff()