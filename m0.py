from data import *
from numpy import random
def get_hand():
    # print('m0 get hand called');
    return random.randint(0,len(HAND_TO_S) );
def main():
    # working
    arr=[];
    i=0;
    while(True):
        if i>=T:
            break;
        arr.append(get_hand() );
        i+=1;
    print(arr);
if __name__ == "__main__":
    main()
