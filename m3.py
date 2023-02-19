from data import *;
from my_util import m3_dic,opp_hand;
import m0;

from river import tree,metrics
import numpy as np
# river's multi classifier tree model
# later figure out how it differs from normal hoeffdingTreeClassifier

# by defaulting seed we get more consistent result
# small drift window
model = tree.HoeffdingAdaptiveTreeClassifier(
    drift_window_threshold=K,
    seed=0,
    
);
# model = tree.HoeffdingTreeClassifier(
    
# );
def get_hand():
    if len(HN_HANDS)<=K:
        return m0.get_hand();
    n=len(HN_HANDS);
    # predict next hand based on sequences of earlier hands
    res=opp_hand(model.predict_one(m3_dic(HN_HANDS,n-K) ) );
    return res;
def learn(a):
    if len(HN_HANDS)<K:
        return;
    # models take in a dictionary of characteristics & predicts based on those characteristics
    n=len(HN_HANDS);
    # n-k offset by 1 bec wedont want last sequence of K, we want before-last 
    model.learn_one(m3_dic(HN_HANDS,n-K), a);
def main():
    # working
    # arr=[1,2,2,1,0,0,1,2,0,1,0,1,2,2,1]
    # n=len(arr);
    # for i in range(n-K):
    #     dic=m3_dic(arr,i);
    #     model.learn_one(dic,arr[i+K] );

    # print(model.predict_proba_one(m3_dic([0,1,0,1,0],0) ) )
    # print(model.predict_proba_one(m3_dic([0,0,0,1,1],0) ) )
    # a=[];
    # b=[];
    # for i in range(n-K):
    #     a.append(model.predict_one(m3_dic(arr,i) ) );
    #     b.append(arr[i+K] );
    # print(a);
    # print(b);
    print();
if __name__ == "__main__":
    main();