import argparse
import sys
import os.path
import data_prep.data_clean
import data_prep.data_format

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="REPLACE WITH DESCRIPTION",
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--train", "-t", type=str, default="data/twitter_train.ner", help="train file")
    parser.add_argument("--eval", "-e", type=str, nargs='+', default=["data/twitter_dev.ner"], help="evaluation files")
    parser.add_argument("--outdir", "-o", type=str, default=".", help="location of evaluation files")
    # change default tagger here
    parser.add_argument("--tagger", "-T", default="logreg", choices=["logreg", "crf"], help="which tagger to use; change the default to the one you want to use on q 3.2")
