import streamlit as st
import time
import random

# =================================================================
# 1. CONFIGURAZIONE E DESIGN
# =================================================================
st.set_page_config(page_title="Ansia S.p.A. Toolkit", page_icon="🐹", layout="centered")

st.markdown("""
    <style>
    /* 1. NASCONDE FORK, GITHUB E PULSANTI TECNICI IN ALTO */
    header { visibility: hidden !important; height: 0px !important; } /* Nasconde tutto l'header */
    [data-testid="stHeader"] { display: none !important; }
    .stAppToolbar { display: none !important; }
    .stAppDeployButton { display: none !important; }
    #MainMenu { visibility: visible !important; } /* Ma vogliamo che il menù si veda */
    
    /* 2. FORZA IL TEMA CHIARO (ANTI DARK MODE) */
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4, span, label {
        color: #1a1a1a !important;
    }
    .stApp {
        background-color: #ffffff !important;
    }

    /* 3. SIDEBAR NERA PROFESSIONALE */
    [data-testid="stSidebar"] {
        background-color: #000000 !important;
        color: white !important;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* 4. BOTTONE SIDEBAR MOBILE - Lo rendiamo visibile e evidente */
    [data-testid="stSidebarNav"] { padding-top: 20px; }
    
    /* 5. STILE RISULTATI */
    .big-money {
        color: #ff4b4b !important;
        font-size: 48px !important;
        font-weight: bold;
        text-align: center;
        margin: 20px 0;
    }

    /* 6. WHATSAPP BUTTON */
    .wa-button {
        background-color: #25D366;
        color: white !important;
        padding: 12px 24px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        margin: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# =================================================================
# 2. MENU LATERALE
# =================================================================
with st.sidebar:
    st.image("https://www.comunicattivamente.it/wp-content/uploads/2023/logo-comunicattivamente.png")
    st.write("---")
    menu = st.radio("SELEZIONA STRUMENTO:", [
        "💰 La Tassa sul Caos", 
        "⏳ Esorcista delle Riunioni", 
        "💊 Pillola di Saggezza"
    ])
    st.write("---")
    st.caption("Daniele Salvatori | comunicAttivamente")

# =================================================================
# 3. AVVISO PER MOBILE (Sostituisce la freccia poco chiara)
# =================================================================
# Questo banner appare solo in cima per dire all'utente cosa fare
st.warning("👈 **APRI IL MENÙ**: Clicca le tre linee o la freccia in alto a sinistra per cambiare strumento.")

# =================================================================
# 4. TOOL 1: LA TASSA SUL CAOS
# =================================================================
if menu == "💰 La Tassa sul Caos":
    st.title("💰 La Tassa sul Caos")
    st.write("Scopri quanta ricchezza evapora ogni anno a causa della disorganizzazione.")
    
    with st.container(border=True):
        n_dipendenti = st.number_input("Quanti collaboratori compongono il tuo team?", min_value=1, value=5)
        minuti_persi = st.slider("Quanti minuti al giorno pensi che ogni persona sprechi per attività improduttive (file persi, caos, doppie spiegazioni)?", 5, 120, 30)
        costo_orario = st.number_input("Costo orario medio aziendale per collaboratore (€/ora)?", min_value=10, value=30)
    
    if st.button("CALCOLA LO SPRECO ANNUALE 💸", type="primary"):
        with st.spinner("L'Esorcista sta facendo i conti..."):
            time.sleep(1)
        spreco_annuale = (minuti_persi / 60) * costo_orario * n_dipendenti * 220
        st.markdown(f'<p style="text-align:center; font-weight:bold; margin-bottom:0;">QUESTO È QUELLO CHE STAI PERDENDO OGNI ANNO:</p>', unsafe_allow_html=True)
        st.markdown(f'<div class="big-money">€ {spreco_annuale:,.0f}</div>', unsafe_allow_html=True)
        st.info("💡 Questa tassa invisibile è il costo del Caos. Puoi smettere di pagarla domani mattina.")
        st.link_button("FERMA QUESTA EMORRAGIA 🔥", "mailto:daniele@comunicattivamente.it")

# =================================================================
# 5. TOOL 2: L'ESORCISTA DELLE RIUNIONI
# =================================================================
elif menu == "⏳ Esorcista delle Riunioni":
    st.title("⏳ L'Esorcista delle Riunioni")
    st.write("Avvia il timer e guarda i soldi dell'azienda che evaporano in tempo reale.")
    
    with st.container(border=True):
        persone = st.number_input("Partecipanti alla riunione", min_value=1, value=4)
        costo_orario_dip = st.number_input("Costo orario medio di OGNI singolo partecipante (€/ora)", min_value=10, value=35)
    
    costo_al_secondo = (persone * costo_orario_dip) / 3600
    
    if "start_time" not in st.session_state: st.session_state.start_time = None

    c1, c2 = st.columns(2)
    if c1.button("INIZIA RIUNIONE 🚀"):
        st.session_state.start_time = time.time()
    
    if c2.button("STOP / RESET 🛑"):
        st.session_state.start_time = None

    if st.session_state.start_time:
        placeholder = st.empty()
        while st.session_state.start_time:
            trascorso = time.time() - st.session_state.start_time
            soldi_persi = trascorso * costo_al_secondo
            placeholder.markdown(f"""
                <div style="text-align: center; background-color: #fff3cd; padding: 30px; border-radius: 15px; border: 2px solid #856404; margin-top:20px;">
                    <p style="margin:0; font-size:18px;">RIUNIONE IN CORSO DA: {int(trascorso // 60)}m {int(trascorso % 60)}s</p>
                    <h1 style="color: #ff4b4b; font-size: 60px; margin: 10px 0;">€ {soldi_persi:.2f}</h1>
                    <p style="font-weight: bold; color:#856404;">SOLDI BRUCIATI DALL'AZIENDA</p>
                </div>
            """, unsafe_allow_html=True)
            time.sleep(1)

# =================================================================
# 6. TOOL 3: PILLOLA DI SAGGEZZA
# =================================================================
elif menu == "💊 Pillola di Saggezza":
    st.title("💊 L'Esorcismo del Giorno")
    st.write("Fermati un secondo. Leggi. Rifletti.")
    
    consigli = [
        "Se una procedura è nella tua testa, non è una procedura. È un segreto aziendale che ti tiene prigioniero.",
        "Smetti di fare il vigile del fuoco che spegne emergenze. Inizia a fare l'architetto che costruisce sistemi.",
        "Il fatturato serve a vantarsi con i colleghi. Il margine serve a far dormire te e la tua famiglia.",
        "Ogni volta che dici 'Faccio prima a farlo io', stai pagando per lavorare invece di farti pagare per pensare.",
        "La tua azienda deve poter funzionare se tu sparisci per 30 giorni. Se no, hai un lavoro faticoso, non un'azienda.",
        "Dire di 'NO' ai clienti tossici è l'investimento più redditizio che puoi fare oggi."
    ]
    
    if st.button("ESTRAI IL CONSIGLIO 🎲", type="primary"):
        st.markdown(f"""
            <div style="background-color: #000; color: white; padding: 40px; border-radius: 15px; text-align: center; font-size: 24px; font-style: italic;">
                "{random.choice(consigli)}"
            </div>
        """, unsafe_allow_html=True)
        st.balloons()

# =================================================================
# FOOTER FINALE (WhatsApp e Sito)
# =================================================================
st.write("---")
st.markdown(f"""
    <div style="text-align: center; padding: 20px;">
        <p style="font-weight:bold; margin-bottom:10px;">Daniele Salvatori | comunicAttivamente</p>
        <a href="https://www.comunicattivamente.it" target="_blank" style="color: #1a1a1a;">www.comunicattivamente.it</a><br><br>
        <a href="https://wa.me/393929334563" class="wa-button">💬 SCRIVIMI SU WHATSAPP</a>
    </div>
""", unsafe_allow_html=True)
