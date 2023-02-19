from my_util import *;
import m0;
import m1;
import m2;
import m3;
# HN_HANDS=[2,2,1,0,2,1,1,2,1,0,0,1,2];

def main():
    turn=1;
    while(True):
        # hand of player
        hn_hand = input('Turn '+str(turn)+':\n');
        if hn_hand=='3':
            break;
        if hn_hand not in NUM_HAND_STR:
            continue;
        # cpmvert to int, go on
        hn_hand=int(hn_hand);
        # hands ai going to play
        ai_hands=[m0.get_hand(),m1.get_hand(),m2.get_hand(),m3.get_hand()];
        # update score for human
        for i in range(MODEL_SZ):
            HN_TO_MODEL[i]+=1 if player_a_win(hn_hand,ai_hands[i] ) else 0;
        # update score for models
        for i in range(MODEL_SZ):
            MODEL_TO_HN[i]+=1 if player_a_win(ai_hands[i],hn_hand ) else 0;
        # models should update before i append next hand;
        # update markov model
        m2.learn(hn_hand);
        # update hoeff model
        m3.learn(hn_hand);
        
        # append player hand
        HN_HANDS.append(hn_hand);
        # append models hand
        for i in range(MODEL_SZ):
            MODELS_HANDS[i].append(ai_hands[i] );
        # m3 should learn
        turn+=1;
    print(HN_TO_MODEL);
    print(MODEL_TO_HN);
    
if __name__ == "__main__":
    main()
