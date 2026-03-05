# src/helpers.py

# ── Imports ────────────────────────────────────────────────
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ── Tier → Company Mapping ─────────────────────────────────
# Reflects actual basket in master_revenue.csv
TIERS = {
    "Luxury":   ["Estée Lauder", "LVMH Perfumes & Cosmetics"],
    "Prestige": ["L'Oréal Luxe", "Shiseido", "Kosé"],
    "Masstige": ["L'Oréal Dermatological Beauty"],
    "Mass":     ["L'Oréal Consumer Products", "Unilever Beauty & Wellbeing", "Kao Cosmetics"],
}

# ── Tier Colours ───────────────────────────────────────────
TIER_COLOURS = {
    "Luxury":   "#1a1a2e",    # deep navy
    "Prestige": "#6b3fa0",    # deep violet
    "Masstige": "#b08d57",    # warm gold
    "Mass":     "#a8a8a8",    # neutral grey
}

# ── Chart Styling ──────────────────────────────────────────
def set_style():
    """Apply consistent visual style across all notebooks."""
    sns.set_theme(style="whitegrid")
    plt.rcParams.update({
        "figure.figsize": (12, 6),
        "font.family": "sans-serif",
        "axes.titlesize": 14,
        "axes.titleweight": "bold",
        "axes.labelsize": 11,
    })

# ── Save Chart ─────────────────────────────────────────────
def save_chart(fig, filename):
    """Save chart to outputs/charts/ for use in final report."""
    path = os.path.join("outputs", "charts", filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"Saved: {path}")
