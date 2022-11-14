import bert_score
import logging
import transformers
# import matplotlib.pyplot as plt
transformers.tokenization_utils.logger.setLevel(logging.ERROR)
transformers.configuration_utils.logger.setLevel(logging.ERROR)
transformers.modeling_utils.logger.setLevel(logging.ERROR)
# %matplotlib inline
from bert_score import score

def bert_score(text1, text2):
    with open("hype.txt") as f:
        cands = [line.strip() for line in f]

    with open("refs.txt") as f:
        refs = [line.strip() for line in f]

    P, R, F1 = score(cands, refs, lang='en', verbose=True)
    P, R, F1 = score(cands, refs, lang='en', rescale_with_baseline=True)
    single_cands = [text1]
    multi_refs = [[text2]]
    P_mul, R_mul, F_mul = score(single_cands, multi_refs, lang="en", rescale_with_baseline=True)
    return(F_mul*100)

