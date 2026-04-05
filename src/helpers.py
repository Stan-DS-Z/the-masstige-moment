# src/helpers.py
# ── Single source of truth for all Masstige Moment notebooks ──────────────────
# Imports: matplotlib only (seaborn dependency removed)
# Canonical: TIER_ORDER, TIER_COLOURS, COMPANY_COLOURS, FIG_*, weighted_sentiment

import matplotlib.pyplot as plt
import os

# ── Paths (anchored to this file — safe regardless of notebook CWD) ───────────
_SRC_DIR  = os.path.dirname(os.path.abspath(__file__))
_ROOT_DIR = os.path.dirname(_SRC_DIR)
CHART_DIR = os.path.join(_ROOT_DIR, "outputs", "charts")

# ── Tier → Company Mapping ─────────────────────────────────────────────────────
# Reflects actual basket in master_revenue.csv
TIERS = {
    "Luxury":   ["Estée Lauder", "LVMH Perfumes & Cosmetics"],
    "Prestige": ["L'Oréal Luxe", "Shiseido", "Kosé"],
    "Masstige": ["L'Oréal Dermatological Beauty"],
    "Mass":     ["L'Oréal Consumer Products", "Unilever Beauty & Wellbeing", "Kao Cosmetics"],
}

# ── Canonical Tier Order ───────────────────────────────────────────────────────
TIER_ORDER = ["Luxury", "Prestige", "Masstige", "Mass"]

# ── Tier Colours (British spelling — enforced project-wide) ───────────────────
# Luxury  : deep navy    — premium signal, recedes slightly vs Masstige hero
# Prestige: deep violet  — distinctive, mid-market premium
# Masstige: deep teal    — the thesis hero; reads as clinical/efficacy not luxury
#                          (CeraVe, La Roche-Posay, Vichy aesthetic DNA)
# Mass    : neutral grey — recedes deliberately; supporting cast
TIER_COLOURS = {
    "Luxury":   "#1a1a2e",
    "Prestige": "#6b3fa0",
    "Masstige": "#2a7d6e",
    "Mass":     "#a8a8a8",
}

# ── Company Colours (NB02) ─────────────────────────────────────────────────────
COMPANY_COLOURS = {
    "Estée Lauder": "#040a2b",   # brand navy
    "LVMH":         "#8d7c71",   # taupe/almond — avoids clash with ELC
    "L'Oréal":      "#f4d42c",   # brand gold/yellow
    "Shiseido":     "#c80421",   # brand red
    "Kosé":         "#6d2b50",   # deep plum (packaging-derived)
    "Unilever":     "#0f0e9a",   # brand royal blue
    "Kao":          "#006b3c",   # brand green
}

# ── Canonical Figure Sizes ─────────────────────────────────────────────────────
FIG_STANDARD = (10, 6)   # bar charts, dot plots, most charts
FIG_WIDE     = (12, 5)   # time series, trend lines
FIG_SQUARE   = (7,  7)   # radar, scatter
FIG_DOUBLE   = (14, 6)   # side-by-side panels, dumbbells

# ── Shared Constants ───────────────────────────────────────────────────────────
BACKGROUND   = "#FAFAF8"
SOURCE_LABEL = (
    "Source: Company annual reports, Google Trends, YouTube Data API v3 | "
    "Stan Zaen · The Masstige Moment"
)

# ── Chart Styling ──────────────────────────────────────────────────────────────
def set_style():
    """
    Apply consistent visual style across all notebooks.
    Call once per notebook at the top, after imports.

    Design decisions:
    - Titles left-aligned (editorial convention — not centred academic)
    - Top/right spines removed (FT/Bloomberg standard)
    - Horizontal gridlines only, very light — don't compete with data
    - Background #FAFAF8 — warm off-white, easier on the eye than pure white
    - No seaborn dependency — pure rcParams
    """
    plt.rcParams.update({
        # Figure
        "figure.figsize":       FIG_STANDARD,
        "figure.facecolor":     BACKGROUND,
        "figure.dpi":           120,

        # Axes
        "axes.facecolor":       BACKGROUND,
        "axes.titlesize":       13,
        "axes.titleweight":     "bold",
        "axes.titlelocation":   "left",    # left-aligned titles — editorial standard
        "axes.titlepad":        12,
        "axes.labelsize":       10,
        "axes.labelcolor":      "#444444",
        "axes.edgecolor":       "#CCCCCC",

        # Spines — remove top and right (FT/Bloomberg convention)
        "axes.spines.top":      False,
        "axes.spines.right":    False,
        "axes.spines.left":     True,
        "axes.spines.bottom":   True,

        # Grid — configured per-chart via apply_grid(ax)
        # grid.axis is not a valid rcParam across matplotlib versions;
        # use apply_grid(ax) after creating each axis to get y-only gridlines.
        "axes.grid":            False,     # off by default; apply_grid(ax) enables selectively
        "axes.axisbelow":       True,
        "grid.color":           "#EEEEEE",
        "grid.linewidth":       0.8,

        # Ticks
        "xtick.labelsize":      9,
        "ytick.labelsize":      9,
        "xtick.color":          "#666666",
        "ytick.color":          "#666666",
        "xtick.direction":      "out",
        "ytick.direction":      "out",

        # Legend
        "legend.frameon":       False,
        "legend.fontsize":      9,
        "legend.title_fontsize": 9,

        # Font
        "font.family":          "sans-serif",
    })


# ── Chart Annotation Helpers ───────────────────────────────────────────────────
def apply_grid(ax):
    """
    Apply y-axis-only gridlines to an axis.

    grid.axis is not a valid rcParam across matplotlib versions, so y-only
    gridlines must be applied per-axis. Call this after creating each ax:

        fig, ax = plt.subplots(figsize=FIG_STANDARD)
        apply_grid(ax)
    """
    ax.yaxis.grid(True, color="#EEEEEE", linewidth=0.8)
    ax.xaxis.grid(False)
    ax.set_axisbelow(True)


def add_source(fig, text=SOURCE_LABEL):
    """
    Stamp source attribution to bottom-right of figure.
    Call before save_chart() or plt.show().
    """
    fig.text(
        0.99, 0.01, text,
        ha="right", va="bottom",
        fontsize=7.5, color="#AAAAAA", style="italic",
        transform=fig.transFigure,
    )


def add_subtitle(ax, text, y=1.06):
    """
    Add a grey subtitle line immediately below the main axis title.
    Provides context without competing with the insight headline.

    Args:
        ax   : matplotlib Axes object
        text : subtitle string
        y    : vertical position in axes coordinates (default 1.06).
               Increase if subtitle overlaps title; decrease for tighter layouts.
               Pair with fig.subplots_adjust(top=0.82) for most chart types.

    Usage:
        ax.set_title("Masstige CAGR Leads All Tiers at 14.67%")
        add_subtitle(ax, "Revenue index, USD millions · 9 companies · 2022–2025")
    """
    ax.text(
        0, y, text,
        transform=ax.transAxes,
        fontsize=9, color="#888888",
        va="bottom", ha="left",
    )


# ── Weighted Sentiment ─────────────────────────────────────────────────────────
def weighted_sentiment(group, score_col="compound", weight_col="likes"):
    """
    Upvote-weighted mean sentiment score.
    +1 floor on weights prevents zero-weight for unliked comments.

    Used in: NB04A, NB04B, NB05
    Replaces three identical inline definitions across those notebooks.

    Args:
        group      : DataFrame group (from groupby().apply())
        score_col  : column holding the sentiment score (default: "compound")
        weight_col : column holding the like count (default: "likes")

    Returns:
        float: weighted mean score
    """
    weights = group[weight_col] + 1
    return (group[score_col] * weights).sum() / weights.sum()


# ── Save Chart ─────────────────────────────────────────────────────────────────
def save_chart(fig, filename, source=True):
    """
    Save figure to outputs/charts/<filename>.

    Path is anchored to the project root (derived from this file's location),
    so it works correctly regardless of which directory the notebook runs from.

    Args:
        fig      : matplotlib Figure object
        filename : e.g. "01_revenue_by_tier.png"
        source   : if True (default), stamps source attribution before saving
    """
    if source:
        add_source(fig)
    os.makedirs(CHART_DIR, exist_ok=True)
    path = os.path.join(CHART_DIR, filename)
    fig.savefig(
        path,
        dpi=150,
        bbox_inches="tight",
        facecolor=fig.get_facecolor(),
    )
    print(f"Saved: {path}")
