#include <random>
#include <algorithm>
#include <iterator>
#include <iostream>
#include <chrono>
#include <map>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    using chrono::high_resolution_clock;
    using chrono::duration_cast;
    using chrono::duration;
    using chrono::milliseconds;

    //https://stackoverflow.com/questions/13445688/how-to-generate-a-random-number-in-c
    random_device dev;
    mt19937 rng(dev());
    uniform_int_distribution<mt19937::result_type> dist(1,100);

    cout << "n,binary_tree,hash_table" << endl;

    //https://stackoverflow.com/questions/22387586/measuring-execution-time-of-a-function-in-c
    for(int n = 50000; n <= 4000000; n+=50000){
        pair<int, int>* multimap_input = new pair<int, int>[n];
        int* multiset_input = new int[n];
        
        multimap<int, int> bin_tree;
        unordered_multiset<int> hash_table;

        for(int i = 0; i < n; i++){
            multimap_input[i] = pair<int, int>(dist(rng), dist(rng));
            multiset_input[i] = dist(rng);
        }

        auto multimap_start = high_resolution_clock::now();
        for(int i = 0; i < n; i++){
            bin_tree.insert(multimap_input[i]);
        }
        auto multimap_end = high_resolution_clock::now();

        auto multiset_start = high_resolution_clock::now();
        for(int i = 0; i < 10000; i++){
            hash_table.insert(multiset_input[i]);
        }
        auto multiset_end = high_resolution_clock::now();

        auto multimap_time = duration_cast<milliseconds>(multimap_end - multimap_start);
        auto multiset_time = duration_cast<milliseconds>(multiset_end - multiset_start);

        cout << n << "," << multimap_time.count() << "," << multiset_time.count() << endl;

        delete[] multiset_input;
        delete[] multimap_input;
    }
}
