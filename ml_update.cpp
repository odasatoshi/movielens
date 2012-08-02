#include <iostream>
#include <fstream>
#include <sstream>
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
  
  string convert;
  ifstream ifc("config.json");
  stringstream ss;
  ss << ifc.rdbuf();

  config_data config;

  config.converter = ss.str();
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
    d.num_values.clear();
    if (n % 1000 == 0)
       cout << n << endl;
    d.num_values.push_back(make_pair(movieid, pfi::lang::lexical_cast<int>(rating)));
    r.update_row(NAME, userid, d);
    n++;
  }
}


