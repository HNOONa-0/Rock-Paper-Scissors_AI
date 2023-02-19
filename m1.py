from data import *;
import m0;
from my_util import is_match,opp_hand;

def get_hand():
    if len(HN_HANDS)<=K:
        return m0.get_hand();
    
    n=len(HN_HANDS);
    occ={};
    # why stop at n-K? just dont take last sequence
    for i in range(n-K):
        cur_acc=is_match(i,n-K,K);
        # print(cur_acc);
        if cur_acc>=ACC:
            if HN_HANDS[i+K] in occ:
                occ[HN_HANDS[i+K] ]+=1;
            else:
                occ[HN_HANDS[i+K] ]=1;
    return m0.get_hand() if len(occ)==0 else opp_hand(max(occ,key=occ.get ) );
def main():
    # working
    print();
if __name__ == "__main__":
    main();