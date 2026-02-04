import streamlit as st
import time
import random

# =================================================================
# 1. CONFIGURAZIONE E DESIGN
# =================================================================
st.set_page_config(page_title="Ansia S.p.A. Toolkit", page_icon="🐹", layout="centered")

st.markdown("""
    <style>
    /* NASCONDE HEADER E PULSANTI TECNICI */
    [data-testid="stHeader"] {display:none !important;}
    footer {visibility: hidden !important;}
    .stAppDeployButton {display:none !important;}
    
    /* SFONDO GENERALE CHIARO */
    .stApp { background-color: #ffffff !important; }

    /* FORZA COLORE TESTO GENERALE (Tranne dove specificato) */
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4, span, label {
        color: #1a1a1a !important;
    }

    /* TASTI NAVIGAZIONE ORIZZONTALI */
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        font-size: 12px !important;
        padding: 5px !important;
        height: 3em !important;
        background-color: #f0f2f6 !important;
    }

    /* BOX PILLOLA (Nero con testo Bianco) */
    .pillola-box {
        background-color: #000000 !important;
        padding: 40px;
        border-radius: 15px;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
    .pillola-text {
        color: #ffffff !important; /* FORZA BIANCO */
        font-size: 24px !important;
        font-style: italic;
        line-height: 1.4;
    }

    /* RISULTATI ECONOMICI */
    .big-money {
        color: #ff4b4b !important;
        font-size: 42px !important;
        font-weight: bold;
        text-align: center;
        margin: 15px 0;
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
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# =================================================================
# 2. LOGICA NAVIGAZIONE ORIZZONTALE
# =================================================================
if 'menu' not in st.session_state:
    st.session_state.menu = "💰 LA TASSA"

# Logo
st.image("https://www.comunicattivamente.it/wp-content/uploads/2023/logo-comunicattivamente.png", width=160)

# TASTI ORIZZONTALI (SX, CENTRO, DX)
c_nav1, c_nav2, c_nav3 = st.columns(3)

with c_nav1:
    if st.button("💰 LA TASSA"): st.session_state.menu = "💰 LA TASSA"
with c_nav2:
    if st.button("⏳ RIUNIONI"): st.session_state.menu = "⏳ RIUNIONI"
with c_nav3:
    if st.button("💊 PILLOLA"): st.session_state.menu = "💊 PILLOLA"

st.divider()

# =================================================================
# 3. TOOL 1: LA TASSA SUL CAOS
# =================================================================
if st.session_state.menu == "💰 LA TASSA":
    st.title("💰 La Tassa sul Caos")
    st.write("Quanta ricchezza perdi ogni anno a causa della disorganizzazione?")
    
    with st.container(border=True):
        n_dipendenti = st.number_input("Numero collaboratori/team:", min_value=1, value=5)
        minuti_persi = st.slider("Minuti sprecati al giorno per persona (caos, file persi...):", 5, 120, 30)
        costo_orario = st.number_input("Costo orario medio collaboratore (€/ora):", min_value=10, value=30)
    
    if st.button("CALCOLA SPRECO 💸", type="primary"):
        spreco = (minuti_persi / 60) * costo_orario * n_dipendenti * 220
        st.markdown(f'<p style="text-align:center; font-weight:bold;">SPRECO ANNUALE STIMATO:</p>', unsafe_allow_html=True)
        st.markdown(f'<div class="big-money">€ {spreco:,.0f}</div>', unsafe_allow_html=True)
        st.info("💡 Questo è il costo del disordine. Puoi fermarlo oggi.")
        st.link_button("FERMA L'EMORRAGIA 🔥", "mailto:daniele@comunicattivamente.it")

# =================================================================
# 4. TOOL 2: L'ESORCISTA DELLE RIUNIONI
# =================================================================
elif st.session_state.menu == "⏳ RIUNIONI":
    st.title("⏳ L'Esorcista delle Riunioni")
    st.write("Il costo della riunione in tempo reale.")
    
    with st.container(border=True):
        persone = st.number_input("Partecipanti presenti:", min_value=1, value=4)
        costo_h = st.number_input("Costo orario medio per partecipante (€/ora):", min_value=10, value=35)
    
    costo_sec = (persone * costo_h) / 3600
    if "start_time" not in st.session_state: st.session_state.start_time = None

    col_t1, col_t2 = st.columns(2)
    if col_t1.button("START 🚀"): st.session_state.start_time = time.time()
    if col_t2.button("STOP 🛑"): st.session_state.start_time = None

    if st.session_state.start_time:
        placeholder = st.empty()
        while st.session_state.start_time:
            t = time.time() - st.session_state.start_time
            soldi = t * costo_sec
            placeholder.markdown(f"""
                <div style="text-align: center; background-color: #fff3cd; padding: 25px; border-radius: 15px; border: 2px solid #856404;">
                    <p style="margin:0;">DA: {int(t // 60)}m {int(t % 60)}s</p>
                    <h1 style="color: #ff4b4b; font-size: 50px; margin: 5px 0;">€ {soldi:.2f}</h1>
                    <p style="font-weight: bold; color:#856404;">SOLDI EVAPORATI</p>
                </div>
            """, unsafe_allow_html=True)
            time.sleep(1)

# =================================================================
# 5. TOOL 3: PILLOLA DI SAGGEZZA (AREA MODIFICABILE)
# =================================================================
elif st.session_state.menu == "💊 PILLOLA":
    st.title("💊 L'Esorcismo del Giorno")
    st.write("Fermati. Leggi. Applica.")
    
    # --- AREA DOVE PUOI AGGIUNGERE LE TUE PILLOLE ---
    database_pillole = [
        "Se una procedura è nella tua testa, non è una procedura. È un segreto aziendale che ti tiene prigioniero.",
        "Smetti di fare il vigile del fuoco e inizia a fare l'architetto della tua azienda.",
        "Il fatturato serve a vantarsi con i colleghi. Il margine serve a far dormire la tua famiglia.",
        "Ogni volta che dici 'Faccio prima a farlo io', stai pagando per lavorare invece di farti pagare per pensare.",
        "La tua azienda deve poter funzionare se tu sparisci per 30 giorni. Se no, hai solo un lavoro faticoso.",
        "Dire di 'NO' ai clienti tossici è l'investimento più redditizio che puoi fare oggi.",
        "SCRIZIONE NUOVA PILLOLA QUI", # Aggiungine quante ne vuoi così
    ]
    # -----------------------------------------------

    if st.button("ESTRAI IL CONSIGLIO 🎲", type="primary"):
        consiglio = random.choice(database_pillole)
        st.markdown(f"""
            <div class="pillola-box">
                <p class="pillola-text">"{consiglio}"</p>
            </div>
        """, unsafe_allow_html=True)

# =================================================================
# FOOTER FINALE
# =================================================================
st.write("")
st.write("---")
st.markdown(f"""
    <div style="text-align: center; padding: 10px;">
        <p style="font-weight:bold; margin-bottom:5px;">Daniele Salvatori | comunicAttivamente</p>
        <a href="https://www.comunicattivamente.it" target="_blank" style="color: #1a1a1a;">www.comunicattivamente.it</a><br>
        <span style="font-size: 1.1em;">📞 <a href="tel:+393929334563" style="color: #ff4b4b; text-decoration: none; font-weight: bold;">+39 392 933 4563</a></span><br><br>
        <a href="https://wa.me/393929334563" class="wa-button">💬 WHATSAPP</a>
    </div>
""", unsafe_allow_html=True)
