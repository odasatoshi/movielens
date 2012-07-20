#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, json
from jubatus.recommender import client
from jubatus.recommender import types

NAME = "recommender_ml";

if __name__ == '__main__':

    recommender = client.recommender("127.0.0.1",9199)

    converter = {
              "string_filter_types": {},
              "string_filter_rules": [],
                'num_filter_types': {},
                'num_filter_rules': [],
                'string_types': {},
                'string_rules': [],
                'num_types': {},
                'num_rules': [{"key" : "*", "type" : "num"}]
                }

    config = types.config_data("lsh", json.dumps(converter))
    recommender.set_config(NAME, config)

    n = 0
    for line in open('./dat/ml-100k/u.data'):
        userid, movieid, rating, mtime = line[:-1].split('\t')
        datum = types.datum(  [], [[str(movieid), float(rating)]] )
        if (n % 1000 == 0):
            print n
        recommender.update_row(NAME, userid, datum)
        n = n + 1;




