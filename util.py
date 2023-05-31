#! -*- encoding: utf8 -*-


class Foo(object):
    id = "foo"

    def get_id(self):
        return self.id


def bar():
    return "bar"


def read_hosts():
    """ """
    res = []
    with open("/etc/hosts") as h_file:
        for line in h_file:
            res.append(res)

    return res
