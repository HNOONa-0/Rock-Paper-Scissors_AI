from data import *;
# accuracy for the sequence 
def player_a_win(a,b):
    # player a win->(b+1)%len==a
    return True if (b+1)%len(HAND_TO_S)==a else False
def player_a_lose(a,b):
    # player a lose->player b win->(a+1)%len==b
    # note there can be a draw in which case a==b & both player_a_lose,player_a_win return false;
    return player_a_win(b,a);
def opp_hand(a):
    return (a+1)%len(HAND_TO_S);
def is_match(a,b,k):
    c=0;
    for i in range(k):
        c+=(1 if HN_HANDS[a+i]==HN_HANDS[b+i] else 0);
    return c/k;
def m3_dic(arr,a):
    dic={};
    for i in range(K):
        dic['x'+str(i) ]=arr[a+i];
    return dic;
def main():
    # print([player_a_win(0,0,),player_a_lose(0,0,) ] );
    print('hello')
if __name__ == "__main__":
    main()