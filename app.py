import streamlit as st
import time
import random

# =================================================================
# 1. CONFIGURAZIONE E DESIGN (Corazzato Anti-Errore)
# =================================================================
st.set_page_config(page_title="comunicAttivamente Toolkit", page_icon="🎯", layout="centered")

st.markdown("""
    <style>
    /* NASCONDE TUTTO IL SUPERFLUO */
    [data-testid="stHeader"] {display:none !important;}
    footer {visibility: hidden !important;}
    .stAppDeployButton {display:none !important;}
    
    /* FORZA TEMA CHIARO */
    .stApp { background-color: #ffffff !important; }
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4, span, label, div {
        color: #1a1a1a !important;
    }

    /* BOX PILLOLA (Nero puro, testo bianco) */
    .pillola-box {
        background-color: #000000 !important;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        margin: 20px 0;
    }
    .pillola-text {
        color: #ffffff !important;
        font-size: 22px !important;
        font-style: italic;
    }

    /* RISULTATI */
    .big-money {
        color: #ff4b4b !important;
        font-size: 40px !important;
        font-weight: bold;
        text-align: center;
    }

    /* WHATSAPP */
    .wa-button {
        background-color: #25D366;
        color: white !important;
        padding: 12px 24px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
    }
    </style>
    """, unsafe_allow_html=True)

# =================================================================
# 2. BRAND E NAVIGAZIONE (Stile Sommelier)
# =================================================================

# Scriviamo il brand invece di usare l'immagine (più sicuro)
st.markdown("<h1 style='text-align: center; color: #ff4b4b; margin-bottom: 0;'>comunicAttivamente</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-weight: bold; margin-top: 0;'>Esorcismo del Caos Aziendale</p>", unsafe_allow_html=True)

st.write("")

# Selettore identico a quello dei vini (infallibile su mobile)
menu = st.selectbox("SCEGLI LO STRUMENTO:", [
    "💰 La Tassa sul Caos", 
    "⏳ L'Esorcista delle Riunioni", 
    "💊 L'Esorcismo del Giorno"
])

st.divider()

# =================================================================
# 3. TOOL 1: LA TASSA SUL CAOS
# =================================================================
if menu == "💰 La Tassa sul Caos":
    st.subheader("Calcola la ricchezza sprecata")
    
    with st.container(border=True):
        n_dip = st.number_input("Quanti collaboratori hai?", min_value=1, value=5)
        min_persi = st.slider("Minuti sprecati/giorno per persona:", 5, 120, 30)
        costo_h = st.number_input("Costo orario medio collaboratore (€):", min_value=10, value=30)
    
    if st.button("CALCOLA SPRECO 💸", type="primary"):
        spreco = (min_persi / 60) * costo_h * n_dip * 220
        st.markdown(f'<p style="text-align:center;">SPRECO ANNUALE STIMATO:</p>', unsafe_allow_html=True)
        st.markdown(f'<div class="big-money">€ {spreco:,.0f}</div>', unsafe_allow_html=True)
        st.warning("Non è un costo fisso. È una perdita che puoi fermare.")
        st.link_button("FERMA L'EMORRAGIA 🔥", "mailto:daniele@comunicattivamente.it")

# =================================================================
# 4. TOOL 2: L'ESORCISTA DELLE RIUNIONI
# =================================================================
elif menu == "⏳ L'Esorcista delle Riunioni":
    st.subheader("Il cronometro del tempo perso")
    
    with st.container(border=True):
        pers = st.number_input("Persone presenti:", min_value=1, value=4)
        costo_p = st.number_input("Costo orario/persona (€):", min_value=10, value=35)
    
    cost_sec = (pers * costo_p) / 3600
    
    if "start_t" not in st.session_state: st.session_state.start_t = None

    c1, c2 = st.columns(2)
    if c1.button("START 🚀"): st.session_state.start_t = time.time()
    if c2.button("STOP / RESET 🛑"): st.session_state.start_t = None

    if st.session_state.start_t:
        ph = st.empty()
        while st.session_state.start_t:
            diff = time.time() - st.session_state.start_t
            soldi = diff * cost_sec
            ph.markdown(f"""
                <div style="text-align: center; background-color: #fff3cd; padding: 20px; border-radius: 15px; border: 2px solid #856404;">
                    <h3>Tempo: {int(diff // 60)}m {int(diff % 60)}s</h3>
                    <h1 style="color: #ff4b4b;">€ {soldi:.2f}</h1>
                    <p>SOLDI BRUCIATI</p>
                </div>
            """, unsafe_allow_html=True)
            time.sleep(1)

# =================================================================
# 5. TOOL 3: PILLOLA DI SAGGEZZA (AREA MODIFICABILE)
# =================================================================
elif menu == "💊 L'Esorcismo del Giorno":
    st.subheader("Fermati. Leggi. Applica.")
    
    # --- PUOI AGGIUNGERE LE TUE PILLOLE QUI SOTTO ---
    pillole = [
        "Se una procedura è nella tua testa, non è una procedura. È un segreto aziendale che ti tiene prigioniero.",
        "Ogni volta che dici 'Faccio prima a farlo io', stai uccidendo la tua crescita.",
        "Il fatturato è vanità, il margine è sanità. Guarda i numeri veri, non i sogni.",
        "La tua azienda deve poter funzionare se tu sparisci per 30 giorni. Altrimenti hai un lavoro faticoso, non un'azienda.",
        "Le riunioni senza ordine del giorno sono chiacchiere costose. Annullale.",
        "Dire di 'NO' ai clienti tossici è l'investimento più redditizio dell'anno."
    ]

    if st.button("ESTRAI IL CONSIGLIO 🎲", type="primary"):
        scelta = random.choice(pillole)
        st.markdown(f"""
            <div class="pillola-box">
                <p class="pillola-text">"{scelta}"</p>
            </div>
        """, unsafe_allow_html=True)

# =================================================================
# FOOTER FINALE
# =================================================================
st.write("")
st.write("---")
st.markdown(f"""
    <div style="text-align: center;">
        <p style="font-weight:bold; margin-bottom:5px;">Daniele Salvatori</p>
        <span style="font-size: 1.1em;">📞 <a href="tel:+393929334563" style="color: #ff4b4b; text-decoration: none; font-weight: bold;">+39 392 933 4563</a></span><br><br>
        <a href="https://wa.me/393929334563" class="wa-button">💬 WHATSAPP</a><br><br>
        <a href="https://www.comunicattivamente.it" target="_blank" style="color: #1a1a1a;">www.comunicattivamente.it</a>
    </div>
""", unsafe_allow_html=True)
