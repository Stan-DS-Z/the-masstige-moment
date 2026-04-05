# -*- coding: utf-8 -*-
# src/helpers_fr.py
# ── France-market configuration — NB06 only ───────────────────────────────────
#
# Design principle: this file extends helpers.py, it does NOT redefine it.
# - Canonical colours, save_chart, add_source, add_subtitle, weighted_sentiment,
#   FIG_*, BACKGROUND, SOURCE_LABEL are all imported from helpers.py
# - This file only defines what is genuinely France-specific:
#   French tier names, colour aliases, brand lists, keyword lists, batch helper
#
# If a tier colour changes in helpers.py, it automatically propagates here.

from src.helpers import (
    TIER_COLOURS,
    set_style,
    apply_grid,
    save_chart,
    add_source,
    add_subtitle,
    weighted_sentiment,
    FIG_STANDARD,
    FIG_WIDE,
    FIG_SQUARE,
    FIG_DOUBLE,
    BACKGROUND,
)

# ── France-specific source label ───────────────────────────────────────────────
SOURCE_LABEL_FR = (
    "Source : Google Trends, API YouTube Data v3, Beauté-Test · "
    "Stan Zaen · The Masstige Moment — Marché Français"
)

# ── French tier order ──────────────────────────────────────────────────────────
TIER_ORDER_FR = ["Luxe", "Prestige", "Masstige", "Mass"]

# ── French tier colours — mapped to canonical palette from helpers.py ──────────
# Keys are French tier names; values are identical to TIER_COLOURS.
# One source of truth: change helpers.py → propagates here automatically.
TIER_COULEURS_FR = {
    "Luxe":     TIER_COLOURS["Luxury"],    # deep navy   #1a1a2e
    "Prestige": TIER_COLOURS["Prestige"],  # deep violet #6b3fa0
    "Masstige": TIER_COLOURS["Masstige"],  # deep teal   #2a7d6e
    "Mass":     TIER_COLOURS["Mass"],      # neutral grey #a8a8a8
}

# ── Marques par tier (France basket) ──────────────────────────────────────────
MARQUES_FR = {
    "Luxe":     ["Dior Beauté", "Guerlain", "Givenchy Beauté", "YSL Beauté"],
    "Prestige": ["Lancôme", "Clarins", "Giorgio Armani Beauté", "L'Occitane"],
    "Masstige": ["La Roche-Posay", "Vichy", "CeraVe", "Nuxe", "Avène"],
    "Mass":     ["L'Oréal Paris", "Garnier", "Gemey-Maybelline"],
}

# ── Mots-clés Google Trends (geo=FR) ──────────────────────────────────────────
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

# ── Mots-clés YouTube (langue française) ──────────────────────────────────────
KEYWORDS_YOUTUBE_FR = {
    "Luxe":     ["Dior beauté routine", "Guerlain soin visage", "YSL maquillage avis"],
    "Prestige": ["Lancôme routine soin", "Clarins crème test", "L'Occitane avis soin"],
    "Masstige": ["La Roche-Posay routine", "Nuxe Huile Prodigieuse avis", "Avène soin peau sensible"],
    "Mass":     ["L'Oréal Paris routine", "Garnier soin visage", "Gemey-Maybelline test avis"],
}

# ── Mots-clés Beauté-Test par marque ──────────────────────────────────────────
KEYWORDS_BEAUTETEST_FR = {
    "Luxe":     ["dior", "guerlain", "givenchy", "yves-saint-laurent"],
    "Prestige": ["lancome", "clarins", "giorgio-armani", "loccitane"],
    "Masstige": ["la-roche-posay", "vichy", "cerave", "nuxe", "avene"],
    "Mass":     ["loreal-paris", "garnier", "gemey-maybelline"],
}

# ── Batch helper (pytrends — max 5 keywords per request) ──────────────────────
def get_batches(tier_keywords, batch_size=5):
    """
    Split a tier's keyword dict into batches for pytrends.
    Combines 'marques' and 'comportement' lists before chunking.

    Args:
        tier_keywords : dict with keys 'marques' and 'comportement'
        batch_size    : int, default 5 (pytrends maximum per request)

    Returns:
        list of lists, each of length <= batch_size
    """
    all_kw = tier_keywords["marques"] + tier_keywords["comportement"]
    return [all_kw[i:i + batch_size] for i in range(0, len(all_kw), batch_size)]
