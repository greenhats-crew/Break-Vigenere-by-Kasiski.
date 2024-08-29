import pandas as pd
import streamlit as st
import string
import re
from frequence import stat
from kasiski import kasiski
from vigenere import decrypt, encrypt

def rotate_alphabet(n):
    return string.ascii_uppercase[n:] + string.ascii_uppercase[:n]
def split_into_groups(text, key_length):
    groups = ['' for _ in range(key_length)]
    for i, char in enumerate(text):
        groups[i % key_length] += char
    return groups
def divisors(integer):
    return [n for n in range(2, integer + 1) if integer % n == 0]
encrypted_text = st.text_area("Encrypted Text")
encrypted_text = re.sub(r'[^A-Z]', '', encrypted_text.strip().upper())

if encrypted_text:
    dictionary = kasiski(encrypted_text)
    st.dataframe([{"Found": v[1], "Word": k, "Length": v[0], "Locations": v[2], "Factor": v[3]} 
                  for k, v in dictionary.items()], use_container_width=True)

    possible_keyspace = max(divisors(max([v[3] for v in dictionary.values()]))[:-1])
    
    data = {
        "Word": list(dictionary.keys()),
        **{i: ["✅" if i in divisors(v[3]) else "❌" for v in dictionary.values()] 
           for i in range(2, possible_keyspace)}
    }

    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
    col1, col2, col3, col4 = st.columns([1, 2, 1, 1])
    with col1:
        num_inputs = st.number_input("Key Length", min_value=0, max_value=25, value=0, step=1)
    with col2:
        inputs = []
        for i in range(num_inputs):
            adjustment_value = st.session_state.get(f"adjust_{i}", 0)
            adjusted_char = chr(ord('A') + adjustment_value)
            input_value = st.text_input(f"Ký tự {i + 1}", value=adjusted_char, key=f"input_{i}")
            inputs.append(input_value)
    with col3:
        adjustments = []
        for i in range(num_inputs):
            adjustment_value = st.number_input(f"Điều chỉnh {chr(97 + i)}", min_value=0, max_value=25, value=0, step=1, key=f"adjust_{i}")
            adjustments.append(adjustment_value)
    with col4:
        charts = st.number_input("Chart", min_value=0, max_value=num_inputs, value=0, step=1)
    key = ''.join(inputs)
    if num_inputs > 0 and charts > 0:
        key_length = num_inputs
        groups = split_into_groups(encrypted_text, key_length)
        selected_group = groups[charts - 1]
        frequence = stat(selected_group)
        custom_order = list(rotate_alphabet(adjustments[charts - 1]))
        frequence_df = pd.DataFrame(frequence.items(), columns=['Character', 'Frequency'])
        frequence_df['Character'] = pd.Categorical(frequence_df['Character'], categories=custom_order, ordered=True)
        frequence_df = frequence_df.sort_values('Character')
        st.bar_chart(frequence_df.set_index('Character'))
        
        # English letter frequencies
        english_frequencies = {
            'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702, 'F': 2.228,
            'G': 2.015, 'H': 6.094, 'I': 6.966, 'J': 0.153, 'K': 0.772, 'L': 4.025,
            'M': 2.406, 'N': 6.749, 'O': 7.507, 'P': 1.929, 'Q': 0.095, 'R': 5.987,
            'S': 6.327, 'T': 9.056, 'U': 2.758, 'V': 0.978, 'W': 2.360, 'X': 0.150,
            'Y': 1.974, 'Z': 0.074
        }
        english_frequencies_df = pd.DataFrame(list(english_frequencies.items()), columns=['Character', 'Frequency'])
        english_frequencies_df['Frequency'] = english_frequencies_df['Frequency'] / 100
        st.markdown("### Tần suất các ký tự trong tiếng Anh")
        st.bar_chart(english_frequencies_df.set_index('Character'))
        decrypt_text = decrypt(''.join(inputs), encrypted_text)
        st.text_area("Decrypted Text", value=decrypt_text, height=150)
