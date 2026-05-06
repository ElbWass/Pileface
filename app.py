"""
Simulateur de Pile ou Face Quantique
Application Streamlit + Qiskit pour illustrer la superposition quantique.
"""

import time
import streamlit as st
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# --- Configuration de la page ---
st.set_page_config(
    page_title="Pile ou Face Quantique",
    page_icon="⚛️",
    layout="centered",
)

# --- Titre et introduction ---
st.title("⚛️ Pile ou Face Quantique")
st.markdown(
    "Découvrez la **superposition quantique** en lançant une pièce de monnaie... quantique !"
)

st.divider()

# --- Explications pédagogiques ---
with st.expander("📚 Comment ça fonctionne ? (cliquer pour lire)"):
    st.markdown(
        """
        ### 🔵 Qu'est-ce qu'un qubit ?
        Un **qubit** (quantum bit) est l'unité de base de l'information quantique.
        Contrairement à un bit classique qui vaut soit **0** soit **1**,
        un qubit peut être dans les **deux états à la fois** grâce à la *superposition quantique*.
        C'est comme une pièce de monnaie qui tournoie dans les airs : elle n'est
        ni pile ni face tant qu'elle n'a pas atterri.

        ### 🔀 Que fait la porte Hadamard ?
        La **porte Hadamard (H)** place le qubit en **superposition parfaite** :
        elle lui donne exactement 50 % de chances d'être mesuré à 0 et 50 % à 1.
        C'est l'équivalent quantique d'un lancer de pièce parfaitement équilibré.

        ### 🎲 Pourquoi le résultat est-il aléatoire ?
        Lorsqu'on **mesure** le qubit, la superposition s'effondre de façon
        **intrinsèquement aléatoire** — pas à cause d'un manque d'information,
        mais parce que c'est la nature fondamentale de la mécanique quantique.
        Avec 50/50, on obtient en moyenne autant de 0 que de 1, comme avec une pièce.
        """
    )

st.divider()

# --- Sélection du nombre d'essais ---
st.subheader("⚙️ Paramètres de l'expérience")

nb_essais = st.number_input(
    "Nombre d'essais (lancers de la pièce quantique) :",
    min_value=1,
    max_value=1000,
    value=100,
    step=1,
)
st.caption("⚠️ Maximum : 1 000 essais.")

st.markdown(f"**{nb_essais} mesures** seront effectuées sur le circuit quantique.")

# --- Bouton principal ---
st.divider()

if st.button("🚀 Lancer l'expérience quantique", use_container_width=True, type="primary"):

    coin_placeholder = st.empty()
    coin_placeholder.markdown("""
<style>
@keyframes flip-coin {
    0%   { transform: rotateY(0deg); }
    100% { transform: rotateY(360deg); }
}
.coin-anim {
    font-size: 90px;
    display: inline-block;
    animation: flip-coin 0.7s linear infinite;
}
.coin-wrap {
    text-align: center;
    padding: 24px 0 8px 0;
}
.coin-label {
    text-align: center;
    font-size: 17px;
    color: #888;
    margin-top: 6px;
}
</style>
<div class="coin-wrap"><span class="coin-anim">🪙</span></div>
<div class="coin-label">La pièce quantique est en train de tourner...</div>
""", unsafe_allow_html=True)

    with st.spinner("Simulation en cours..."):

        # --- Construction du circuit quantique ---
        # 1 qubit (notre pièce) + 1 bit classique (pour stocker le résultat)
        circuit = QuantumCircuit(1, 1)

        # Porte Hadamard : met le qubit en superposition 50/50
        circuit.h(0)

        # Mesure du qubit : effondrement de la superposition
        circuit.measure(0, 0)

        # --- Simulation ---
        simulateur = AerSimulator()
        job = simulateur.run(circuit, shots=nb_essais)
        resultat = job.result()
        comptages = resultat.get_counts(circuit)

        # Extraire les comptes (si 0 ou 1 n'est jamais apparu, on met 0 par défaut)
        nb_zero = comptages.get("0", 0)
        nb_un   = comptages.get("1", 0)
        time.sleep(2)

    # --- Pièce arrêtée sur le bon côté ---
    if nb_zero > nb_un:
        face_gagnante = "PILE"
        couleur_gagnante = "#4C72B0"
        pct_gagnant = nb_zero / nb_essais * 100
        label_resultat = f"Pile ressort en tête avec {pct_gagnant:.1f} % des lancers"
    elif nb_un > nb_zero:
        face_gagnante = "FACE"
        couleur_gagnante = "#DD8452"
        pct_gagnant = nb_un / nb_essais * 100
        label_resultat = f"Face ressort en tête avec {pct_gagnant:.1f} % des lancers"
    else:
        face_gagnante = "="
        couleur_gagnante = "#888888"
        label_resultat = "Pile et Face sont à parfaite égalité !"

    coin_placeholder.markdown(f"""
<style>
.coin-stopped {{
    width: 110px;
    height: 110px;
    background: linear-gradient(135deg, #FFD700, #FFA500);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto;
    font-size: 26px;
    font-weight: bold;
    color: white;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.4);
    border: 5px solid #CC8800;
    box-shadow: 0 6px 16px rgba(0,0,0,0.25);
}}
.coin-wrap {{
    text-align: center;
    padding: 24px 0 8px 0;
}}
.coin-label {{
    text-align: center;
    font-size: 18px;
    font-weight: bold;
    color: {couleur_gagnante};
    margin-top: 10px;
}}
</style>
<div class="coin-wrap"><div class="coin-stopped">{face_gagnante}</div></div>
<div class="coin-label">{label_resultat}</div>
""", unsafe_allow_html=True)

    # --- Résultats numériques ---
    st.subheader("Résultats")

    col1, col2, col3 = st.columns(3)
    col1.metric("🔵 Résultat 0 (Pile)", nb_zero, f"{nb_zero / nb_essais * 100:.1f} %")
    col2.metric("🔴 Résultat 1 (Face)", nb_un,   f"{nb_un   / nb_essais * 100:.1f} %")
    col3.metric("Total d'essais", nb_essais)

    # --- Graphique en barres ---
    fig, ax = plt.subplots(figsize=(5, 4))

    barres = ax.bar(
        ["0 (Pile)", "1 (Face)"],
        [nb_zero, nb_un],
        color=["#4C72B0", "#DD8452"],
        edgecolor="white",
        width=0.5,
    )

    # Afficher les valeurs au-dessus des barres
    for barre in barres:
        hauteur = barre.get_height()
        ax.text(
            barre.get_x() + barre.get_width() / 2.0,
            hauteur + nb_essais * 0.01,
            f"{int(hauteur)}\n({hauteur / nb_essais * 100:.1f} %)",
            ha="center", va="bottom", fontsize=12, fontweight="bold",
        )

    # Ligne de référence à 50 %
    ax.axhline(y=nb_essais / 2, color="gray", linestyle="--", linewidth=1, label="50 % théorique")

    ax.set_title(f"Distribution après {nb_essais} mesures quantiques", fontsize=14, pad=12)
    ax.set_ylabel("Nombre d'occurrences")
    ax.set_ylim(0, nb_essais * 1.15)
    ax.legend()
    ax.spines[["top", "right"]].set_visible(False)

    st.pyplot(fig)
    plt.close(fig)

    # --- Interprétation ---
    diff_pct = abs(nb_zero - nb_un) / nb_essais * 100
    if diff_pct < 5:
        commentaire = "✅ Résultat très équilibré — la superposition quantique est bien 50/50 !"
    elif diff_pct < 15:
        commentaire = "👌 Légère variation statistique normale pour ce nombre d'essais."
    else:
        commentaire = "📈 Écart notable — tout à fait possible avec peu d'essais (variance statistique)."

    st.info(commentaire)

# --- Pied de page ---
st.divider()
st.caption("Construit avec Streamlit · Qiskit · Matplotlib  |  ⚛️ Informatique quantique pour tous")
