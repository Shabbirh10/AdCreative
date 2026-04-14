"""
Produces personalized landing page via template filling.
Fixed for 100% placeholder coverage in Simulation Mode.
"""

import json
import re
from loguru import logger
import google.generativeai as genai
from google.api_core import exceptions
from app.config import GEMINI_API_KEY
from app.templates import SAAS_TEMPLATE, RETAIL_TEMPLATE

genai.configure(api_key=GEMINI_API_KEY)

def get_available_models():
    try:
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        preferred = ["models/gemini-2.0-flash", "models/gemini-1.5-flash"]
        return [p for p in preferred if p in models]
    except:
        return []

def get_mock_page(analysis: dict) -> str:
    """High-fidelity fallback generator."""
    is_retail = any(kw in str(analysis).lower() for kw in ["coffee", "brew", "shop", "retail", "buy"])
    t = RETAIL_TEMPLATE if is_retail else SAAS_TEMPLATE
    
    # Comprehensive replacement mapping
    mapping = {
        "{{TITLE}}": f"{analysis.get('brand_name')} | {analysis.get('headline')}",
        "{{BRAND_NAME}}": analysis.get('brand_name'),
        "{{NAV_CTA}}": "Start Now",
        "{{OFFER_TAG}}": analysis.get('offer_details'),
        "{{OFFER_DETAILS}}": analysis.get('offer_details'),
        "{{HERO_HEADLINE}}": analysis.get('headline'),
        "{{HERO_SUBHEADLINE}}": analysis.get('sub_headline'),
        "{{MAIN_CTA}}": analysis.get('cta_text'),
        "{{USP_HEADLINE}}": "Meticulously Crafted for Perfection",
        "{{TOP_BAR_MESSAGING}}": f"CELEBRATING OUR LAUNCH: {analysis.get('offer_details')}",
        "{{CATEGORY_TAG}}": "Direct Trade Selection" if is_retail else "Core Features",
        "{{PRODUCT_IMAGE_PLACEHOLDER}}": f"{analysis.get('brand_name')} Product Showcase",
        "{{FOOTER_CTA}}": "Get the Offer Now",
    }
    
    # Build USP list HTML
    usp_html = ""
    for usp in analysis.get('unique_selling_points', []):
        if is_retail:
            usp_html += f'<div><h3 class="font-bold mb-2">✦ {usp}</h3><p class="text-zinc-500 text-sm">Experience the difference that quality makes.</p></div>'
        else:
            usp_html += f'<div class="p-8 bg-white rounded-3xl border border-slate-100 shadow-sm"><div class="text-indigo-600 text-2xl mb-4">✔</div><h3 class="font-bold mb-2">{usp}</h3><p class="text-slate-500 text-sm">Optimized for scale and reliability.</p></div>'
    
    mapping["{{USP_SECTION}}"] = usp_html
    
    for k, v in mapping.items():
        t = t.replace(k, str(v))
    
    # Custom color injection if provided
    if analysis.get('color_palette'):
        colors = analysis.get('color_palette')
        style_override = f"""
        <style>
            .bg-indigo-600, .bg-zinc-900 {{ background-color: {colors[0]} !important; }}
            .text-indigo-600, .text-amber-600 {{ color: {colors[0]} !important; }}
            .border-indigo-600 {{ border-color: {colors[0]} !important; }}
        </style>
        """
        t = t.replace("</head>", f"{style_override}</head>")

    badge = '<div style="background:rgba(0,0,0,0.85); color:white; padding:12px 18px; position:fixed; bottom:24px; right:24px; border-radius:12px; font-size:12px; z-index:9999; font-family:sans-serif; border:1px solid rgba(255,255,255,0.1); box-shadow:0 8px 32px rgba(0,0,0,0.4);"><strong>[QUOTA EXCEEDED]</strong> System running on high-fidelity simulation.</div>'
    return t + badge

def generate_page_from_ad(ad_analysis: dict) -> str:
    models = get_available_models()
    if not models:
        return get_mock_page(ad_analysis)

    prompt = f"Fill this template based on: {json.dumps(ad_analysis)}"
    for model_name in models:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            result = response.text.strip()
            result = re.sub(r'^```(?:html)?\s*', '', result); result = re.sub(r'\s*```$', '', result)
            return result
        except exceptions.ResourceExhausted:
            continue
        except Exception:
            continue

    return get_mock_page(ad_analysis)
