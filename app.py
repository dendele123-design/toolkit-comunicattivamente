import streamlit as st
import time
import random

# =================================================================
# 1. CONFIGURAZIONE E STILE (Brand comunicAttivamente)
# =================================================================
st.set_page_config(page_title="Ansia S.p.A. - Suite Esorcismo", page_icon="🐹", layout="centered")

st.markdown("""
    <style>
    /* Anti Dark-Mode */
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4, span, label { color: #1a1a1a !important; }
    .stApp { background-color: #ffffff !important; }
    
    /* Card Stile Ansia S.p.A. */
    .ansia-card {
        background-color: #f8f9fa;
        padding: 25px;
        border-radius: 15px;
        border-left: 10px solid #ff4b4b;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    
    .big-money { color: #ff4b4b; font-size: 42px; font-weight: bold; text-align: center; }
    
    /* Bottoni */
    .stButton>button { width: 100%; border-radius: 5px; height: 3.5em; font-weight: bold; text-transform: uppercase; }
    
    /* Header Sidebar */
    [data-testid="stSidebar"] { background-color: #000000 !important; }
    [data-testid="stSidebar"] * { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# =================================================================
# 2. MENU LATERALE (NAVIGAZIONE)
# =================================================================
with st.sidebar:
    st.image("https://www.comunicattivamente.it/wp-content/uploads/2023/logo-comunicattivamente.png")
    st.title("Suite Esorcismo")
    menu = st.radio("Cosa vuoi fare?", [
        "💰 Calcola la Tassa sul Caos", 
        "⏳ Esorcista delle Riunioni", 
        "💊 Pillola di Saggezza"
    ])
    st.divider()
    st.caption("Creato da Daniele Salvatori")

# =================================================================
# 3. TOOL 1: LA TASSA SUL CAOS (Lead Magnet)
# =================================================================
if menu == "💰 Calcola la Tassa sul Caos":
    st.title("💰 La Tassa sul Caos")
    st.subheader("Scopri quanti soldi stai regalando al disordine ogni anno.")
    
    with st.container():
        st.markdown('<div class="ansia-card">', unsafe_allow_html=True)
        n_dipendenti = st.number_input("Quanti dipendenti/collaboratori hai?", min_value=1, value=5)
        minuti_persi = st.slider("Minuti persi al giorno per persona (ricerca file, interruzioni, caos)?", 5, 120, 30)
        costo_orario = st.number_input("Costo orario medio aziendale (€/ora)?", min_value=10, value=35)
        st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("CALCOLA LO SPRECO 💸", type="primary"):
        with st.spinner("L'Esorcista sta facendo i conti..."):
            time.sleep(1)
        
        # Calcolo: (minuti/60) * costo * persone * 220 giorni lavorativi
        spreco_giornaliero = (minuti_persi / 60) * costo_orario * n_dipendenti
        spreco_annuale = spreco_giornaliero * 220
        
        st.error(f"### ATTENZIONE!")
        st.markdown(f'<div class="big-money">€ {spreco_annuale:,.0f}</div>', unsafe_allow_html=True)
        st.write(f"Ogni anno stai bruciando circa **€ {spreco_annuale:,.0f}** a causa della disorganizzazione.")
        st.info("💡 Questo non è un costo fisso. È una tassa invisibile che puoi smettere di pagare domani mattina.")
        st.link_button("SMETTI DI BRUCIARE SOLDI 🔥", "mailto:daniele@comunicattivamente.it")

# =================================================================
# 4. TOOL 2: L'ESORCISTA DELLE RIUNIONI (Client Bonus)
# =================================================================
elif menu == "⏳ Esorcista delle Riunioni":
    st.title("⏳ L'Esorcista delle Riunioni")
    st.write("Avvia questo timer durante la riunione. Guarda i soldi che evaporano.")
    
    c1, c2 = st.columns(2)
    with c1: persone = st.number_input("Partecipanti", min_value=1, value=4)
    with c2: costo_riunione = st.number_input("Costo orario medio (€)", min_value=10, value=40)
    
    costo_al_secondo = (persone * costo_riunione) / 3600
    
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
                <div class="ansia-card" style="text-align: center;">
                    <h3>Tempo trascorso: {int(trascorso // 60)}m {int(trascorso % 60)}s</h3>
                    <h1 style="color: #ff4b4b;">€ {soldi_persi:.2f}</h1>
                    <p>SOLDI BRUCIATI IN QUESTA RIUNIONE</p>
                </div>
            """, unsafe_allow_html=True)
            time.sleep(1)

# =================================================================
# 5. TOOL 3: PILLOLA DI SAGGEZZA (Marketing Awareness)
# =================================================================
elif menu == "💊 Pillola di Saggezza":
    st.title("💊 L'Esorcismo del Giorno")
    st.write("Prendi la tua dose quotidiana di realtà imprenditoriale.")
    
    consigli = [
        "Smetti di essere il centralinista della tua azienda. Delega il telefono.",
        "Se una cosa non è scritta, non esiste. Crea una procedura oggi.",
        "Il fatturato è vanità, il margine è sanità. Guarda i numeri veri.",
        "Le riunioni senza ordine del giorno sono chat costose. Annullale tutte.",
        "Impara a dire di NO ai clienti tossici. Liberano spazio per quelli d'oro.",
        "Se devi farlo tu perché 'fai prima', sei ufficialmente un dipendente di te stesso."
    ]
    
    if st.button("ESTRAI CONSIGLIO BRUTALE 🎲"):
        with st.spinner("Consultando il libro dell'Esorcista..."):
            time.sleep(0.5)
        st.markdown(f'<div class="ansia-card" style="font-size: 24px; text-align: center;">"{random.choice(consigli)}"</div>', unsafe_allow_html=True)
        st.balloons()

# =================================================================
# FOOTER CLICCABILE
# =================================================================
st.write("")
st.write("---")
st.markdown("""
    <div style="text-align: center;">
        📞 <a href="tel:+393929334563" style="color: #ff4b4b; text-decoration: none; font-weight: bold;">+39 392 933 4563</a><br>
        📧 <a href="mailto:daniele@comunicattivamente.it" style="color: #ff4b4b; text-decoration: none;">daniele@comunicattivamente.it</a>
    </div>
""", unsafe_allow_html=True)
