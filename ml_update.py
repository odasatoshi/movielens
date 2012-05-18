#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from jubatus.recommender import client
from jubatus.recommender import types

NAME = "recommender_ml";

if __name__ == '__main__':

    recommender = client.recommender("127.0.0.1",9199)

    str_fil_types = {}
    str_fil_rules = []
    num_fil_types = {}
    num_fil_rules = []
    str_type= {}
    str_rules = []
    num_type = {}
    num_rules = [types.num_rule("*", "num")]

    converter = types.converter_config(str_fil_types, str_fil_rules, num_fil_types, num_fil_rules,
                                       str_type, str_rules, num_type, num_rules)
    config = types.config_data("lsh", converter)
    recommender.set_config(NAME, config)

    n = 0
    for line in open('./dat/ml-100k/u.data'):
        userid, movieid, rating, mtime = line[:-1].split('\t')
        datum = types.datum(  [], [[str(movieid), float(rating)]] )
        if (n % 1000 == 0):
            print n
        recommender.update_row(NAME, userid, datum)
        n = n + 1;




