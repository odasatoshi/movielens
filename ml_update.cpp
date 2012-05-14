#include <iostream>
#include <fstream>
#include <time.h>
#include <sys/time.h>
#include <jubatus/client/recommender_client.hpp>
#include <jubatus/client/recommender_types.hpp>

using namespace std;
using namespace jubatus;
using namespace jubatus::client;
using namespace pfi::lang;

const string NAME = "recommender_ml";

int main(int argc, char* argv[]){

  
  config_data config;
  config.converter.num_rules.push_back((num_rule){"*", "num"});
  config.method = "lsh";

  recommender r("localhost", 9199, 1.0);
  r.set_config(NAME, config);

  ifstream ifs("./dat/ml-100k/u.data");
  if (!ifs){
    throw string ("cannot open data file");
  }

  string userid, movieid, rating, mtime;
  jubatus::datum d;
  int n = 0;
  while((ifs >> userid >> movieid >> rating >> mtime)!=0){
    d.nv.clear();
    if (n % 1000 == 0)
       cout << n << endl;
    d.nv.push_back(make_pair(movieid, pfi::lang::lexical_cast<int>(rating)));
    r.update_row(NAME, userid, d);
    n++;
  }
}


