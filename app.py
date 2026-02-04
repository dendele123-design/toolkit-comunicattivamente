import streamlit as st
import time
import random

# =================================================================
# 1. CONFIGURAZIONE E DESIGN (Suite comunicAttivamente)
# =================================================================
st.set_page_config(page_title="Ansia S.p.A. Toolkit", page_icon="🐹", layout="centered")

st.markdown("""
    <style>
    /* NASCONDE TOTALMENTE HEADER E PULSANTI TECNICI */
    [data-testid="stHeader"] {display:none !important;}
    footer {visibility: hidden !important;}
    .stAppDeployButton {display:none !important;}
    
    /* FORZA IL TEMA CHIARO (ANTI DARK MODE) */
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4, span, label, div {
        color: #1a1a1a !important;
    }
    .stApp {
        background-color: #ffffff !important;
    }

    /* CONTAINER PER GLI STRUMENTI */
    .ansia-container {
        border-left: 8px solid #ff4b4b !important;
        padding: 20px;
        background-color: #f8f9fa !important;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    
    .big-money {
        color: #ff4b4b !important;
        font-size: 48px !important;
        font-weight: bold;
        text-align: center;
        margin: 20px 0;
    }

    /* BOTTONE WHATSAPP */
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
# 2. LOGICA DI NAVIGAZIONE (Senza Sidebar)
# =================================================================
# Inizializziamo lo stato del menù se non esiste
if 'menu' not in st.session_state:
    st.session_state.menu = "💰 LA TASSA"

# Header con Logo
st.image("https://www.comunicattivamente.it/wp-content/uploads/2023/logo-comunicattivamente.png", width=180)
st.write("### Toolkit Esorcismo Aziendale")

# I 3 TASTI DI NAVIGAZIONE (Sempre visibili in alto)
st.write("Seleziona lo strumento:")
col_m1, col_m2, col_m3 = st.columns(3)

if col_m1.button("💰 LA TASSA"):
    st.session_state.menu = "💰 LA TASSA"
if col_m2.button("⏳ RIUNIONI"):
    st.session_state.menu = "⏳ RIUNIONI"
if col_m3.button("💊 PILLOLA"):
    st.session_state.menu = "💊 PILLOLA"

st.divider()

# =================================================================
# 3. TOOL 1: LA TASSA SUL CAOS
# =================================================================
if st.session_state.menu == "💰 LA TASSA":
    st.title("💰 La Tassa sul Caos")
    st.write("Calcola quanta ricchezza perdi ogni anno a causa della disorganizzazione.")
    
    with st.container(border=True):
        n_dipendenti = st.number_input("Quanti collaboratori compongono il tuo team?", min_value=1, value=5)
        minuti_persi = st.slider("Quanti minuti al giorno pensi che ogni persona sprechi per attività improduttive (file persi, caos, interruzioni)?", 5, 120, 30)
        costo_orario = st.number_input("Costo orario medio aziendale per collaboratore (€/ora)?", min_value=10, value=30)
    
    if st.button("CALCOLA LO SPRECO 💸", type="primary"):
        spreco_annuale = (minuti_persi / 60) * costo_orario * n_dipendenti * 220
        st.markdown(f'<p style="text-align:center; font-weight:bold; margin-top:20px;">IL COSTO ANNUALE DEL TUO CAOS:</p>', unsafe_allow_html=True)
        st.markdown(f'<div class="big-money">€ {spreco_annuale:,.0f}</div>', unsafe_allow_html=True)
        st.info("💡 Questa tassa invisibile è il prezzo del disordine. Puoi smettere di pagarla.")
        st.link_button("FERMA QUESTA EMORRAGIA 🔥", "mailto:daniele@comunicattivamente.it")

# =================================================================
# 4. TOOL 2: L'ESORCISTA DELLE RIUNIONI
# =================================================================
elif st.session_state.menu == "⏳ RIUNIONI":
    st.title("⏳ L'Esorcista delle Riunioni")
    st.write("Quanto ti costa questa riunione? Scoprilo in tempo reale.")
    
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
                    <p style="font-weight: bold; color:#856404;">SOLDI BRUCIATI</p>
                </div>
            """, unsafe_allow_html=True)
            time.sleep(1)

# =================================================================
# 5. TOOL 3: PILLOLA DI SAGGEZZA (Senza palloncini)
# =================================================================
elif st.session_state.menu == "💊 PILLOLA":
    st.title("💊 L'Esorcismo del Giorno")
    st.write("Fermati. Leggi. Applica.")
    
    consigli = [
        "Se una procedura è nella tua testa, non è una procedura. È un segreto aziendale che ti tiene prigioniero.",
        "Smetti di fare il vigile del fuoco che spegne emergenze. Inizia a fare l'architetto che costruisce sistemi.",
        "Il fatturato serve a vantarsi con i colleghi. Il margine serve a far dormire te e la tua famiglia.",
        "Ogni volta che dici 'Faccio prima a farlo io', stai pagando per lavorare invece di farti pagare per pensare.",
        "La tua azienda deve poter funzionare se tu sparisci per 30 giorni. Se no, non hai un'azienda.",
        "Dire di 'NO' ai clienti tossici è l'investimento più redditizio che puoi fare oggi."
    ]
    
    if st.button("ESTRAI IL CONSIGLIO 🎲", type="primary"):
        st.markdown(f"""
            <div style="background-color: #000; color: white; padding: 40px; border-radius: 15px; text-align: center; font-size: 24px; font-style: italic;">
                "{random.choice(consigli)}"
            </div>
        """, unsafe_allow_html=True)
        # BALLOONS RIMOSSI COME RICHIESTO!

# =================================================================
# FOOTER FINALE (WhatsApp e Telefono Cliccabile)
# =================================================================
st.write("")
st.write("---")
st.markdown(f"""
    <div style="text-align: center; padding: 20px;">
        <p style="font-weight:bold; margin-bottom:5px;">Daniele Salvatori | comunicAttivamente</p>
        <a href="https://www.comunicattivamente.it" target="_blank" style="color: #1a1a1a;">www.comunicattivamente.it</a><br>
        <span style="font-size: 1.2em;">📞 <a href="tel:+393929334563" style="color: #ff4b4b; text-decoration: none; font-weight: bold;">+39 392 933 4563</a></span><br><br>
        <a href="https://wa.me/393929334563" class="wa-button">💬 SCRIVIMI SU WHATSAPP</a>
    </div>
""", unsafe_allow_html=True)
