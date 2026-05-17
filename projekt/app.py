import streamlit as st
import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

st.set_page_config(page_title="FuzzyVitals - Jakub Sikora", layout="wide")

st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: #111111;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.title("Autor Projektu")
st.sidebar.subheader("Jakub Sikora")
st.sidebar.write("Nr albumu: 347903")
st.sidebar.write("Przedmiot: Zbiory i Systemy Rozmyte")
st.sidebar.write("---")
st.sidebar.markdown("""
### Opis Systemu
Klasyfikator obciazen treningowych oparty na logice Mamdani. 
System analizuje subiektywne i obiektywne parametry wejsciowe, 
poddaje je procesowi fuzji, a nastepnie wylicza wynik 
metoda srodka ciezkosci.

System został zbudowany w języku Python jako reaktywny dashboard webowy. 
Wykorzystuje bibliotekę scikit-fuzzy do obliczeń logicznych oraz framework Streamlit do obsługi interfejsu użytkownika. 
Za dynamiczną wizualizację danych odpowiada silnik Matplotlib.

""")

x_range = np.arange(0, 101, 1)
v_range = np.arange(0, 11, 1)
a_range = np.arange(15, 81, 1)

sen = ctrl.Antecedent(v_range, 'sen')
stres = ctrl.Antecedent(v_range, 'stres')
doms = ctrl.Antecedent(v_range, 'doms')
motywacja = ctrl.Antecedent(v_range, 'motywacja')
wiek = ctrl.Antecedent(a_range, 'wiek')
intensywnosc = ctrl.Consequent(x_range, 'intensywnosc')

sen.automf(3, names=['malo', 'srednio', 'duzo'])
stres.automf(3, names=['niski', 'sredni', 'wysoki'])
doms.automf(3, names=['brak', 'zakwasy', 'bol'])
motywacja.automf(3, names=['brak', 'srednia', 'ogien'])

wiek['mlody'] = fuzzy.trimf(wiek.universe, [15, 15, 40])
wiek['sredni'] = fuzzy.trimf(wiek.universe, [30, 45, 60])
wiek['starszy'] = fuzzy.trimf(wiek.universe, [50, 80, 80])

intensywnosc['regeneracja'] = fuzzy.trimf(intensywnosc.universe, [0, 0, 45])
intensywnosc['lekki'] = fuzzy.trimf(intensywnosc.universe, [35, 60, 85])
intensywnosc['mocny'] = fuzzy.trimf(intensywnosc.universe, [75, 100, 100])

rules = [
    ctrl.Rule(sen['malo'] | stres['wysoki'], intensywnosc['regeneracja']),
    ctrl.Rule(doms['bol'], intensywnosc['regeneracja']),
    ctrl.Rule(wiek['starszy'] & doms['zakwasy'], intensywnosc['regeneracja']),
    ctrl.Rule(wiek['mlody'] & motywacja['ogien'] & sen['duzo'], intensywnosc['mocny']),
    ctrl.Rule(motywacja['ogien'] & doms['zakwasy'] & wiek['mlody'], intensywnosc['mocny']),
    ctrl.Rule(stres['niski'] & sen['srednio'], intensywnosc['lekki']),
    ctrl.Rule(wiek['starszy'] & sen['duzo'] & stres['niski'], intensywnosc['lekki'])
]

train_ctrl = ctrl.ControlSystem(rules)
train_sim = ctrl.ControlSystemSimulation(train_ctrl)

st.title("FuzzyVitals: System Rozmyty")
st.write("---")
c1, c2, c3, c4, c5 = st.columns(5)
with c1: v_s = st.slider("Sen (h)", 0, 10, 7)
with c2: v_st = st.slider("Stres", 0, 10, 3)
with c3: v_d = st.slider("Bol miesni (DOMS)", 0, 10, 2)
with c4: v_m = st.slider("Motywacja", 0, 10, 8)
with c5: v_w = st.slider("Wiek", 15, 80, 25)

train_sim.input['sen'] = v_s
train_sim.input['stres'] = v_st
train_sim.input['doms'] = v_d
train_sim.input['motywacja'] = v_m
train_sim.input['wiek'] = v_w

try:
    train_sim.compute()
    out_val = train_sim.output['intensywnosc']
except:
    out_val = 0

col_graph, col_res = st.columns([2, 1])

with col_graph:
    st.subheader("Wizualizacja zbiorow wyjsciowych")
    
    y_reg = fuzzy.trimf(x_range, [0, 0, 45])
    y_lek = fuzzy.trimf(x_range, [35, 60, 85])
    y_moc = fuzzy.trimf(x_range, [75, 100, 100])

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.fill_between(x_range, 0, y_reg, facecolor='red', alpha=0.2, label='Regeneracja')
    ax.fill_between(x_range, 0, y_lek, facecolor='yellow', alpha=0.2, label='Lekki')
    ax.fill_between(x_range, 0, y_moc, facecolor='green', alpha=0.2, label='Mocny')
    
    ax.axvline(x=out_val, color='blue', linestyle='--', linewidth=3, label=f'Wynik: {out_val:.1f}%')
    ax.plot([out_val], [0], 'bo') 
    
    ax.set_ylim(0, 1.1)
    ax.legend()
    st.pyplot(fig)

with col_res:
    st.subheader("Diagnoza")
    st.metric("Intensywnosc", f"{out_val:.2f} %")
    
    if out_val < 40:
        st.error("KLASYFIKACJA: REGENERACJA")
        st.write("Zalecenie: Odpoczynek.")
    elif out_val < 75:
        st.warning("KLASYFIKACJA: TRENING LEKKI")
        st.write("Zalecenie: Niska intensywnosc.")
    else:
        st.success("KLASYFIKACJA: TRENING MOCNY")
        st.write("Zalecenie: Wysoka intensywnosc.")