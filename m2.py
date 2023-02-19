from data import *;
import m0;
from my_util import opp_hand;
def get_hand():
    # before current hand
    if len(HN_HANDS)==0 or OB_MATRIX[HN_HANDS[-1] ][-1]==0:
        return m0.get_hand();
    # subarray in question, note last entry is total number of observations
    bfc=HN_HANDS[-1];
    arr=OB_MATRIX[bfc][0:len(S_TO_HAND) ];
    # most frequent hand after bfc
    id=arr.index(max(arr) );
    return opp_hand(id);
def learn(a):
    # a is current hand played
    if len(HN_HANDS)<=1:
        return
    # before current hand
    bfc=HN_HANDS[-1];
    # update current hand freq
    OB_MATRIX[bfc ][a ]+=1;
    # update number of  observations
    OB_MATRIX[bfc ][len(S_TO_HAND) ]+=1;

def main():
    # working
    # arr=[2,2,1,0,2,1,1,2,1,0,0,1,2];
    # for i in range(len(arr) ):
    #     a=arr[i];
    #     learn(a);
    #     print(OB_MATRIX);
    #     print();
    #     HN_HANDS.append(a);
    print();
if __name__ == "__main__":
    main();