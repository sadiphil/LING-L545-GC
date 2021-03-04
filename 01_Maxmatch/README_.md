# implementation of code to run wer.py
# cat ja_gsd-ud-test.conllu | cut -f2 | grep -v '^#' | sed 's/^$/@@@/g' | tr '\n' ' ' | sed 's/@@@/\n/g' | sed 's/^ *//g' > ja_gsd-ud-test.reference
# python3 wer.py ja_gsd-ud-test.reference japanesehypothesis.txt
# output = Average WER 3603.673946429622 Line Count 543
# WER = 6.636600269667812
