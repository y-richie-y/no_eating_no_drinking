# Defaults/constants.

BATCH_SIZE = 64
DISABLE_CUDA = False # If this is set to True, make sure it should be!
DROPOUT = 0.3
HIDDEN_DIM = 200  # Denoted by 'l' in the paper.
MAX_ITER = 4
MAXOUT_POOL_SIZE = 16
MAX_CONTEXT_LEN = 600
MAX_GRAD_NORM = 0.5
MAX_QUESTION_LEN = 30
NUM_EPOCHS = 1000 
REG_LAMBDA = 0.1
_PAD = b"<pad>"
_UNK = b"<unk>"
_START_VOCAB = [_PAD, _UNK]
PAD_ID = 0
UNK_ID = 1
