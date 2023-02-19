# hands are numbers 0 | 1 | 2
# rock=0,paper=1,scissors=2
HAND_TO_S=['Rock','Paper','Scissors'];
# maybe we will need this later
S_TO_HAND={'Rock':0,'Paper':1,'Scissors':2}
# num_hand_str
NUM_HAND_STR=set('0 1 2'.split(' ') );
# also numbered 0...4
MODEL_SZ=4;
# array to store hands of of hn
HN_HANDS=[];
# random,matching,markov,river online learning
# hands played by models
MODELS_HANDS=[[] for j in range(MODEL_SZ)]
# score of hn->model
HN_TO_MODEL=[0]*MODEL_SZ;
# score of model->hn
MODEL_TO_HN=[0]*MODEL_SZ;
# ACC for model 1, atleast 4 hands must match
ACC=0.8

# transition matrix for Markov
# may not need it
# TR_MATRIX=[[1/3]*len(HAND_TO_S) ]*len(HAND_TO_S);
# observation matrix to later change the probability
# has extra field for number of all observations len(HAND_TO_S)+1
OB_MATRIX=[[0 for i in range(len(HAND_TO_S)+1)] for j in range(len(HAND_TO_S)+1)]

# seq len for model 1,3. make it as function of n? 
K=5;
# for testing
T=10