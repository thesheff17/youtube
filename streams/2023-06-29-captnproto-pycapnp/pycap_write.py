#!/usr/bin/env python

from subprocess import check_output

def get_unique_file_desc():
    cmd1 = ['capnp', 'id']
    f1 = check_output(cmd1)
    f2 = str(f1.decode('utf-8'))
    f3 = f2.strip()
    return f3

def _main():
    print ("Writing out the schema capnp file...")
    with open('awsdata.capnp', 'w+') as f2:
        f2.write(get_unique_file_desc() + ";\n\n")
        f2.write('''struct Ec2obj {
    ec2id @0 :Text;
    status @1 :Text;
    }
    struct AwsdataA {
    awsdata3 @0 :List(Ec2obj);
    }''')


if __name__ == "__main__":
    _main()