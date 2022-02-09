import pandas as pd
import numpy as np
from PIL import Image 
import streamlit as st 
import altair as alt
 

st.image('https://th.bing.com/th/id/R.3800f3932eff75644fb9c25f556a7efc?rik=udA6NET57WN2SQ&riu=http%3a%2f%2fnewsmobile.in%2fwp-content%2fuploads%2f2018%2f07%2fDNA.jpg&ehk=KbWvj6TNiC%2bGYkwG5eW%2fRa3JMk6reIjQ5RAgVb1ix18%3d&risl=&pid=ImgRaw&r=0')
st.write(""" 
 # DNA Nucleotide Count Web App
This app counts the nucleotide composition of query DNA""")

st.header('Enter DNA Sequence')

sequence_input = """> DNA Query
gtcacatatctcggcagagttaactgatcatcatgggggagagtagatcgagagcattta
catctattgccttggcgttggtgatttctggcggtttacctactctctttcgtctgcccg
tgaacacttgcaccgaagagtagctgtcactcagaactaactggcaagtccgcaggaact
atccttcaatatcgagccttggtattcacccagtgctatatcgctcgtacaagctctcgt
atatacagccaacgtaagtcctcgttcgcagcgtttctttcaactaggccctccggtgaa
agggatgatgtcttacgtcggatatggaaccaatgaatacgtgggaattgcagccgcata
gcggacgaagagtctgagactcaactttccctcgcgaatgcttcagcggacgtgaatcta
gatagcggccagtatgctcatcgggctgttgggatcctggggattaacaaagcgaaagca
gataggaaagcatttgtatggagcgttcgagcatggagtgcagaattaggcgctgcaacg
aaaaccactctgcccctcatcatacctgcgtaaccggaattaatccgattagccccagtt
catagtatggacggtcaggctagt"""
sequence = st.text_area('Sequence input', sequence_input,height = 65)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)
st.write("""
***
""")
st.header('INPUT (DNA Query')
sequence
st.header('OUTPUT (DNA Nucleotide Count)')
def DNA_nucleotide_count(seq):
    d = dict([
        ("A",seq.count('a')+seq.count('A')),
        ("T",seq.count('t')+seq.count('T')),
        ("C",seq.count('c')+seq.count('C')),
        ("G",seq.count('g')+seq.count('G')),
    ])
    return d

X = DNA_nucleotide_count(sequence)

X_labels = list(X)
X_values = list(X.values())

st.write('There are '+str(X['A'])+ ' adenine (A)')
st.write('There are '+str(X['T'])+ ' thymine (T)')
st.write('There are '+str(X['G'])+ ' guanine (G)')
st.write('There are '+str(X['C'])+ ' cytosine (C)')