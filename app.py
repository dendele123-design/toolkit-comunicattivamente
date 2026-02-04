import streamlit as st
import time
import random

# =================================================================
# 1. CONFIGURAZIONE E DESIGN (Suite Professionale)
# =================================================================
st.set_page_config(page_title="Ansia S.p.A. Toolkit", page_icon="🐹", layout="centered")

st.markdown("""
    <style>
    /* NASCONDE ELEMENTI DI SISTEMA (GITHUB, FORK, HEADER) */
    header {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    #MainMenu {visibility: hidden !important;}
    .stAppDeployButton {display:none !important;}
    [data-testid="stHeader"] {display:none !important;}
    [data-testid="stToolbar"] {display: none !important;}
    #GithubIcon {visibility: hidden !important;}

    /* FORZA IL COLORE DEL TESTO (ANTI DARK MODE) */
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4, span, label { color: #1a1a1a !important; }
    .stApp { background-color: #ffffff !important; }
    
    /* CARD STILE ANSIA S.P.A. */
    .ansia-container {
        border-left: 8px solid #ff4b4b !important;
        padding: 20px;
        background-color: #f8f9fa;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    
    .big-money { color: #ff4b4b !important; font-size: 42px; font-weight: bold; text-align: center; margin: 20px 0; }
    
    /* BOTTONI */
    .stButton>button { width: 100%; border-radius: 5px; height: 3.5em; font-weight: bold; text-transform: uppercase; }
    
    /* SIDEBAR NERA */
    [data-testid="stSidebar"] { background-color: #000000 !important; }
    [data-testid="stSidebar"] * { color: white !important; }
    
    /* FOOTER CONTATTI */
    .footer-box {
        text-align: center;
        padding: 30px;
        background-color: #f1f1f1;
        border-radius: 15px;
        margin-top: 50px;
    }
    .wa-button {
        background-color: #25D366;
        color: white !important;
        padding: 10px 20px;
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

# MESSAGGIO DI AIUTO PER MOBILE
st.caption("👈 Clicca la freccetta o le tre linee in alto a sinistra per cambiare strumento")

# =================================================================
# 3. TOOL 1: LA TASSA SUL CAOS
# =================================================================
if menu == "💰 La Tassa sul Caos":
    st.title("💰 La Tassa sul Caos")
    st.write("Scopri quanta ricchezza evapora ogni anno a causa della disorganizzazione.")
    
    # Raggruppiamo i campi in un box visivo unico
    with st.container():
        st.markdown('<div class="ansia-container">', unsafe_allow_html=True)
        n_dipendenti = st.number_input("Quanti collaboratori compongono il tuo team?", min_value=1, value=5)
        minuti_persi = st.slider("Minuti al giorno che ogni persona spreca (cercare file, chiedere info già date, gestire il caos)?", 5, 120, 30)
        costo_orario = st.number_input("Costo orario medio di un collaboratore (€/ora)?", min_value=10, value=30)
        st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("CALCOLA LO SPRECO ANNUALE 💸", type="primary"):
        with st.spinner("L'Esorcista sta facendo i conti..."):
            time.sleep(1)
        
        # Calcolo: (minuti/60) * costo * persone * 220 giorni lavorativi
        spreco_annuale = (minuti_persi / 60) * costo_orario * n_dipendenti * 220
        
        st.error(f"### QUESTO È QUELLO CHE STAI PERDENDO:")
        st.markdown(f'<div class="big-money">€ {spreco_annuale:,.0f}</div>', unsafe_allow_html=True)
        st.write(f"In base alle tue stime, la disorganizzazione ti costa **€ {spreco_annuale:,.0f} ogni anno**.")
        st.info("💡 Non è un costo ineluttabile. È denaro che potresti usare per investire, assumere o... andare in vacanza.")
        st.link_button("FERMA QUESTA EMORRAGIA 🔥", "mailto:daniele@comunicattivamente.it")

# =================================================================
# 4. TOOL 2: L'ESORCISTA DELLE RIUNIONI
# =================================================================
elif menu == "⏳ Esorcista delle Riunioni":
    st.title("⏳ L'Esorcista delle Riunioni")
    st.write("Usa questo timer in tempo reale. Metti a nudo il costo del tempo perso.")
    
    with st.container():
        st.markdown('<div class="ansia-container">', unsafe_allow_html=True)
        persone = st.number_input("Numero di persone presenti nella stanza", min_value=1, value=4)
        costo_orario_dip = st.number_input("Costo orario medio di UN singolo partecipante (€)", min_value=10, value=35)
        st.markdown('</div>', unsafe_allow_html=True)
    
    costo_al_secondo = (persone * costo_orario_dip) / 3600
    
    if "timer_on" not in st.session_state: st.session_state.timer_on = False
    if "start_time" not in st.session_state: st.session_state.start_time = 0

    col_t1, col_t2 = st.columns(2)
    if col_t1.button("INIZIA RIUNIONE 🚀"):
        st.session_state.timer_on = True
        st.session_state.start_time = time.time()
    
    if col_t2.button("STOP / RESET 🛑"):
        st.session_state.timer_on = False
        st.session_state.start_time = 0

    if st.session_state.timer_on:
        placeholder = st.empty()
        while st.session_state.timer_on:
            trascorso = time.time() - st.session_state.start_time
            soldi_persi = trascorso * costo_al_secondo
            placeholder.markdown(f"""
                <div style="text-align: center; background-color: #fff3cd; padding: 20px; border-radius: 15px; border: 2px solid #856404;">
                    <p style="margin:0;">RIUNIONE IN CORSO DA: {int(trascorso // 60)}m {int(trascorso % 60)}s</p>
                    <h1 style="color: #ff4b4b; font-size: 50px; margin: 10px 0;">€ {soldi_persi:.2f}</h1>
                    <p style="font-weight: bold;">SOLDI BRUCIATI FINO AD ORA</p>
                </div>
            """, unsafe_allow_html=True)
            time.sleep(1)

# =================================================================
# 5. TOOL 3: PILLOLA DI SAGGEZZA
# =================================================================
elif menu == "💊 Pillola di Saggezza":
    st.title("💊 L'Esorcismo del Giorno")
    st.write("Fermati. Leggi. Applica.")
    
    consigli = [
        "Se una procedura è nella tua testa, non è una procedura. È un segreto.",
        "Smetti di fare il vigile del fuoco e inizia a fare l'architetto della tua azienda.",
        "Il fatturato serve a vantarsi al bar. Il margine serve a far crescere l'azienda.",
        "Ogni volta che dici 'Faccio prima a farlo io', stai uccidendo la tua crescita.",
        "Delegare non significa 'scaricare', significa dare le istruzioni giuste a chi può far meglio di te.",
        "La tua azienda deve poter funzionare se tu vai in vacanza per 30 giorni. Se no, non hai un'azienda."
    ]
    
    if st.button("ESTRAI CONSIGLIO DELL'ESORCISTA 🎲", type="primary"):
        st.markdown(f"""
            <div style="background-color: #000; color: white; padding: 40px; border-radius: 15px; text-align: center; font-size: 24px; font-style: italic;">
                "{random.choice(consigli)}"
            </div>
        """, unsafe_allow_html=True)
        st.balloons()

# =================================================================
# FOOTER FINALE (WhatsApp e Sito)
# =================================================================
st.markdown(f"""
    <div class="footer-box">
        <b>Daniele Salvatori | comunicAttivamente</b><br>
        <a href="https://www.comunicattivamente.it" target="_blank" style="color: #1a1a1a; text-decoration: underline;">www.comunicattivamente.it</a><br><br>
        <a href="https://wa.me/393929334563" class="wa-button">💬 SCRIVIMI SU WHATSAPP</a>
    </div>
""", unsafe_allow_html=True)
