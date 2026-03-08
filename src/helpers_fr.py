# -*- coding: utf-8 -*-
# ── helpers_fr.py ─────────────────────────────────────────
# Configuration spécifique au marché français — NB06

import matplotlib.pyplot as plt

# ── Couleurs par tier ─────────────────────────────────────
TIER_COULEURS_FR = {
    "Luxe":      "#1C1C2E",
    "Prestige":  "#7B6FA0",
    "Masstige":  "#A8C5A0",
    "Mass":      "#C4956A",
}

TIER_ORDER_FR = ["Luxe", "Prestige", "Masstige", "Mass"]

# ── Marques par tier ──────────────────────────────────────
MARQUES_FR = {
    "Luxe":      ["Dior Beauté", "Guerlain", "Givenchy Beauté", "YSL Beauté"],
    "Prestige":  ["Lancôme", "Clarins", "Giorgio Armani Beauté", "L'Occitane"],
    "Masstige":  ["La Roche-Posay", "Vichy", "CeraVe", "Nuxe", "Avène"],
    "Mass":      ["L'Oréal Paris", "Garnier", "Gemey-Maybelline"],
}

# ── Mots-clés Google Trends (geo=FR) ─────────────────────
KEYWORDS_TRENDS_FR = {

    "Luxe": {
        "marques": [
            "Dior beauté",
            "Guerlain soin",
            "Givenchy parfum",
            "YSL beauté",
            "Touche Éclat",
            "Parfums Christian Dior",
        ],
        "comportement": [
            "soin luxe visage",
            "crème anti-âge luxe",
            "sérum luxe peau",
            "routine beauté luxe",
            "cadeau parfum luxe",
        ],
    },

    "Prestige": {
        "marques": [
            "Lancôme soin",
            "Clarins",
            "Clarins huile",
            "Armani beauté",
            "Lancôme Génifique",
            "L'Occitane crème",
            "L'Occitane visage",
        ],
        "comportement": [
            "soin prestige visage",
            "crème visage haut de gamme",
            "sérum anti-âge efficace",
            "routine soin visage femme",
            "meilleure crème hydratante",
        ],
    },

    "Masstige": {
        "marques": [
            "La Roche-Posay",
            "Vichy soin",
            "CeraVe",
            "Nuxe Huile Prodigieuse",
            "Avène soin",
            "Vichy Liftactiv",
            "La Roche-Posay Effaclar",
        ],
        "comportement": [
            "soin pharmacie visage",
            "crème dermatologue recommande",
            "soin peau sensible",
            "routine peau sensible pharmacie",
            "produit sans parfum peau",
            "soin hypoallergénique",
        ],
    },

    "Mass": {
        "marques": [
            "L'Oréal Paris soin",
            "Garnier",
            "Gemey-Maybelline maquillage",
            "Garnier Ambre Solaire",
            "L'Oréal Revitalift",
        ],
        "comportement": [
            "routine beauté pas cher",
            "soin visage grande surface",
            "maquillage drugstore France",
            "routine beauté débutante",
            "meilleur fond de teint pas cher",
        ],
    },
}

# ── Mots-clés YouTube (langue française) ─────────────────
KEYWORDS_YOUTUBE_FR = {
    "Luxe":      ["Dior beauté routine", "Guerlain soin visage", "YSL maquillage avis"],
    "Prestige":  ["Lancôme routine soin", "Clarins crème test", "L'Occitane avis soin"],
    "Masstige":  ["La Roche-Posay routine", "Nuxe Huile Prodigieuse avis", "Avène soin peau sensible"],
    "Mass":      ["L'Oréal Paris routine", "Garnier soin visage", "Gemey-Maybelline test avis"],
}

# ── Mots-clés Beauté-Test par marque ─────────────────────
KEYWORDS_BEAUTETEST_FR = {
    "Luxe":      ["dior", "guerlain", "givenchy", "yves-saint-laurent"],
    "Prestige":  ["lancome", "clarins", "giorgio-armani", "loccitane"],
    "Masstige":  ["la-roche-posay", "vichy", "cerave", "nuxe", "avene"],
    "Mass":      ["loreal-paris", "garnier", "gemey-maybelline"],
}

# ── Batches pytrends (max 5 par requête) ─────────────────
def get_batches(tier_keywords, batch_size=5):
    """Découpe une liste de mots-clés en batches de taille batch_size."""
    all_kw = tier_keywords["marques"] + tier_keywords["comportement"]
    return [all_kw[i:i+batch_size] for i in range(0, len(all_kw), batch_size)]

# ── Fonction save_chart ───────────────────────────────────
def save_chart(fig, filename):
    fig.savefig(f"../data/processed/{filename}", dpi=150, bbox_inches="tight")
    print(f"Sauvegardé : {filename}")