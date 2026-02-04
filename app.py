import streamlit as st
import time
import random

# =================================================================
# 1. CONFIGURAZIONE E DESIGN (Suite comunicAttivamente)
# =================================================================
st.set_page_config(page_title="Ansia S.p.A. Toolkit", page_icon="🐹", layout="centered")

st.markdown("""
    <style>
    /* RIPRISTINA IL TASTO MENU MA NASCONDE IL RESTO (GitHub, Fork, etc.) */
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    .stAppDeployButton { display:none !important; }
    #MainMenu { visibility: visible !important; } /* Il menu deve vedersi! */
    footer { visibility: hidden !important; }
    
    /* FORZA IL TEMA CHIARO (ANTI DARK MODE) */
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4, span, label {
        color: #1a1a1a !important;
    }
    .stApp {
        background-color: #ffffff !important;
    }

    /* PULIZIA SIDEBAR (Nera) */
    [data-testid="stSidebar"] {
        background-color: #000000 !important;
        color: white !important;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* STILE DEI RISULTATI (Grandi Numeri) */
    .big-money {
        color: #ff4b4b !important;
        font-size: 48px !important;
        font-weight: bold;
        text-align: center;
        margin: 20px 0;
    }

    /* FOOTER */
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
# 3. TOOL 1: LA TASSA SUL CAOS
# =================================================================
if menu == "💰 La Tassa sul Caos":
    st.title("💰 La Tassa sul Caos")
    st.subheader("Quanti soldi stai regalando al disordine?")
    
    # Usiamo un container nativo (senza HTML rotto)
    with st.container(border=True):
        st.write("Inserisci i dati del tuo team:")
        n_dipendenti = st.number_input("Quanti collaboratori compongono il tuo team?", min_value=1, value=5)
        minuti_persi = st.slider("Quanti minuti al giorno pensi che ogni persona sprechi per trovare file, gestire interruzioni o a causa del caos?", 5, 120, 30)
        costo_orario = st.number_input("Costo orario medio di un collaboratore (€/ora)?", min_value=10, value=30)
    
    if st.button("CALCOLA LO SPRECO ANNUALE 💸", type="primary"):
        with st.spinner("L'Esorcista sta facendo i conti..."):
            time.sleep(1)
        
        spreco_annuale = (minuti_persi / 60) * costo_orario * n_dipendenti * 220
        
        st.markdown(f'<p style="text-align:center; font-weight:bold; margin-bottom:0;">QUESTO È QUELLO CHE STAI PERDENDO OGNI ANNO:</p>', unsafe_allow_html=True)
        st.markdown(f'<div class="big-money">€ {spreco_annuale:,.0f}</div>', unsafe_allow_html=True)
        
        st.warning("⚠️ Questa non è una fatalità, è una scelta. Puoi smettere di pagare questa tassa invisibile oggi stesso.")
        st.link_button("FERMA QUESTA EMORRAGIA 🔥", "mailto:daniele@comunicattivamente.it")

# =================================================================
# 4. TOOL 2: L'ESORCISTA DELLE RIUNIONI
# =================================================================
elif menu == "⏳ Esorcista delle Riunioni":
    st.title("⏳ L'Esorcista delle Riunioni")
    st.write("Metti a nudo il costo reale del tempo perso in sala riunioni.")
    
    with st.container(border=True):
        persone = st.number_input("Numero di partecipanti alla riunione", min_value=1, value=4)
        costo_orario_dip = st.number_input("Costo orario medio di OGNI singolo partecipante (€/ora)", min_value=10, value=35)
    
    costo_al_secondo = (persone * costo_orario_dip) / 3600
    
    if "timer_on" not in st.session_state: st.session_state.timer_on = False
    if "start_time" not in st.session_state: st.session_state.start_time = 0

    c1, c2 = st.columns(2)
    if c1.button("INIZIA RIUNIONE 🚀"):
        st.session_state.timer_on = True
        st.session_state.start_time = time.time()
    
    if c2.button("STOP / RESET 🛑"):
        st.session_state.timer_on = False
        st.session_state.start_time = 0

    if st.session_state.timer_on:
        placeholder = st.empty()
        while st.session_state.timer_on:
            trascorso = time.time() - st.session_state.start_time
            soldi_persi = trascorso * costo_al_secondo
            placeholder.markdown(f"""
                <div style="text-align: center; background-color: #fff3cd; padding: 30px; border-radius: 15px; border: 2px solid #856404; margin-top:20px;">
                    <p style="margin:0; font-size:18px;">RIUNIONE IN CORSO DA: {int(trascorso // 60)}m {int(trascorso % 60)}s</p>
                    <h1 style="color: #ff4b4b; font-size: 60px; margin: 10px 0;">€ {soldi_persi:.2f}</h1>
                    <p style="font-weight: bold; color:#856404;">SOLDI BRUCIATI DALL'AZIENDA IN TEMPO REALE</p>
                </div>
            """, unsafe_allow_html=True)
            time.sleep(1)

# =================================================================
# 5. TOOL 3: PILLOLA DI SAGGEZZA
# =================================================================
elif menu == "💊 Pillola di Saggezza":
    st.title("💊 L'Esorcismo del Giorno")
    st.write("Una dose di realtà per smettere di essere un titolare criceto.")
    
    consigli = [
        "Se una procedura è nella tua testa, non è una procedura. È un segreto aziendale che ti tiene prigioniero.",
        "Il fatturato serve a vantarsi con i colleghi. Il margine serve a far dormire te e la tua famiglia.",
        "Smetti di fare il vigile del fuoco che spegne emergenze. Inizia a fare l'architetto che costruisce sistemi.",
        "Ogni volta che dici 'Faccio prima a farlo io', stai pagando per lavorare invece di farti pagare per pensare.",
        "La tua azienda deve poter funzionare se tu sparisci per 30 giorni. Se crolla tutto, non hai un'azienda, hai un lavoro faticoso.",
        "Dire di 'NO' ai clienti tossici è l'investimento più redditizio che puoi fare quest'anno."
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
