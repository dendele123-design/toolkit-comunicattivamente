import streamlit as st
import time
import random

# =================================================================
# 1. CONFIGURAZIONE E DESIGN (comunicAttivamente Identity)
# =================================================================
st.set_page_config(page_title="comunicAttivamente Toolkit", page_icon="🎯", layout="centered")

ROSSO_BRAND = "#DC0612"

st.markdown(f"""
    <style>
    /* NASCONDE TUTTO IL SUPERFLUO */
    [data-testid="stHeader"] {{display:none !important;}}
    footer {{visibility: hidden !important;}}
    .stAppDeployButton {{display:none !important;}}
    
    /* FORZA TEMA CHIARO (ANTI DARK-MODE) */
    .stApp {{ background-color: #ffffff !important; }}
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4, span, label, div {{
        color: #1a1a1a !important;
    }}

    /* BOX PILLOLA (Nero puro, testo bianco brillante) */
    .pillola-box {{
        background-color: #000000 !important;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        margin: 20px 0;
        border-left: 10px solid {ROSSO_BRAND};
    }}
    .pillola-text {{
        color: #ffffff !important; /* FORZA BIANCO */
        font-size: 22px !important;
        font-style: italic;
        line-height: 1.4;
    }}

    /* RISULTATI ECONOMICI */
    .big-money {{
        color: {ROSSO_BRAND} !important;
        font-size: 42px !important;
        font-weight: bold;
        text-align: center;
        margin: 15px 0;
    }}

    /* BOTTONE WHATSAPP */
    .wa-button {{
        background-color: #25D366;
        color: white !important;
        padding: 12px 24px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        margin-top: 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

# =================================================================
# 2. BRAND E NAVIGAZIONE
# =================================================================

# Logo testuale infrangibile
st.markdown(f"<h1 style='text-align: center; color: {ROSSO_BRAND}; margin-bottom: 0;'>comunicAttivamente</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-weight: bold; margin-top: 0;'>Toolkit per l'Efficienza Aziendale</p>", unsafe_allow_html=True)

st.write("")

# Menu a tendina (il più stabile su mobile)
menu = st.selectbox("QUALE STRUMENTO VUOI USARE?", [
    "💰 La Tassa sul Caos", 
    "⏳ L'Esorcista delle Riunioni", 
    "💊 L'Esorcismo del Giorno"
])

st.divider()

# =================================================================
# 3. TOOL 1: LA TASSA SUL CAOS
# =================================================================
if menu == "💰 La Tassa sul Caos":
    st.subheader("Calcola il capitale sprecato")
    
    with st.container(border=True):
        n_dip = st.number_input("Quanti collaboratori hai nel team?", min_value=1, value=5)
        min_persi = st.slider("Minuti sprecati al giorno per persona (caos, file persi, dubbi):", 5, 120, 30)
        costo_h = st.number_input("Costo orario medio collaboratore (€):", min_value=10, value=30)
    
    if st.button("CALCOLA SPRECO ANNUALE 💸", type="primary"):
        with st.spinner("L'Esorcista sta facendo i conti..."):
            time.sleep(0.8)
        spreco = (min_persi / 60) * costo_h * n_dip * 220
        st.markdown(f'<p style="text-align:center; font-weight:bold; margin-top:20px;">LA TUA TASSA SUL CAOS OGNI ANNO È:</p>', unsafe_allow_html=True)
        st.markdown(f'<div class="big-money">€ {spreco:,.0f}</div>', unsafe_allow_html=True)
        st.warning("⚠️ Questo non è un costo fisso. È ricchezza che stai sottraendo al tuo utile.")
        st.link_button("SMETTI DI BRUCIARE SOLDI 🔥", "mailto:daniele@comunicattivamente.it")

# =================================================================
# 4. TOOL 2: L'ESORCISTA DELLE RIUNIONI
# =================================================================
elif menu == "⏳ L'Esorcista delle Riunioni":
    st.subheader("Quanto ti costa questa riunione?")
    
    with st.container(border=True):
        pers = st.number_input("Partecipanti presenti:", min_value=1, value=4)
        costo_p = st.number_input("Costo orario medio per partecipante (€):", min_value=10, value=35)
    
    costo_sec = (pers * costo_p) / 3600
    
    if "start_t" not in st.session_state: st.session_state.start_t = None

    c1, c2 = st.columns(2)
    if c1.button("INIZIA RIUNIONE 🚀"): st.session_state.start_t = time.time()
    if c2.button("STOP / RESET 🛑"): st.session_state.start_t = None

    if st.session_state.start_t:
        ph = st.empty()
        while st.session_state.start_t:
            diff = time.time() - st.session_state.start_t
            soldi = diff * costo_sec
            ph.markdown(f"""
                <div style="text-align: center; background-color: #fff3cd; padding: 25px; border-radius: 15px; border: 2px solid #856404; margin-top:20px;">
                    <h3>Tempo: {int(diff // 60)}m {int(diff % 60)}s</h3>
                    <h1 style="color: #ff4b4b; font-size: 50px; margin: 10px 0;">€ {soldi:.2f}</h1>
                    <p style="font-weight: bold; color:#856404;">SOLDI BRUCIATI IN TEMPO REALE</p>
                </div>
            """, unsafe_allow_html=True)
            time.sleep(1)

# =================================================================
# 5. TOOL 3: PILLOLA DI SAGGEZZA
# =================================================================
elif menu == "💊 L'Esorcismo del Giorno":
    st.subheader("Fermati. Leggi. Applica.")
    
    # --- PUOI AGGIUNGERE LE TUE PILLOLE QUI SOTTO ---
    pillole = [
        "Se una procedura è nella tua testa, non è una procedura. È un segreto aziendale che ti tiene prigioniero.",
        "Ogni volta che dici 'Faccio prima a farlo io', stai uccidendo la tua crescita.",
        "Il fatturato è vanità, il margine è sanità. Guarda i numeri veri, non i sogni.",
        "La tua azienda deve poter funzionare se tu sparisci per 30 giorni. Altrimenti hai un lavoro faticoso, non un'azienda.",
        "Le riunioni senza ordine del giorno sono chiacchiere costose. Annullale tutte.",
        "Dire di 'NO' ai clienti tossici è l'investimento più redditizio dell'anno.",
        "Smetti di essere il centralinista della tua azienda. Delega il telefono."
    ]

    if st.button("ESTRAI IL CONSIGLIO 🎲", type="primary"):
        scelta = random.choice(pillole)
        st.markdown(f"""
            <div class="pillola-box">
                <p class="pillola-text">"{scelta}"</p>
            </div>
        """, unsafe_allow_html=True)

# =================================================================
# 6. TASTO HUB UNIVERSALE (Fisso in fondo)
# =================================================================
st.write("")
st.write("---")
st.markdown("<p style='text-align:center; font-size:13px; color:#888;'>Hai bisogno di altri strumenti?</p>", unsafe_allow_html=True)
st.link_button("🌐 VEDI TUTTE LE NOSTRE WEB APP", "https://app-comunicattivamente-center.streamlit.app/")

# =================================================================
# FOOTER FINALE
# =================================================================
st.write("")
st.markdown(f"""
    <div style="text-align: center; padding: 20px; background-color: #f1f1f1; border-radius: 15px;">
        <p style="font-weight:bold; margin-bottom:5px;">Daniele Salvatori</p>
        <span style="font-size: 1.1em;">📞 <a href="tel:+393929334563" style="color: {ROSSO_BRAND}; text-decoration: none; font-weight: bold;">+39 392 933 4563</a></span><br><br>
        <a href="https://wa.me/393929334563" class="wa-button">💬 WHATSAPP</a><br><br>
        <div style="font-size: 12px; color: #888;">Powered by <a href="https://www.superstart.it" target="_blank" style="color:{ROSSO_BRAND}; text-decoration:none; font-weight:bold;">SuPeR</a> & Streamlit</div>
    </div>
""", unsafe_allow_html=True)
