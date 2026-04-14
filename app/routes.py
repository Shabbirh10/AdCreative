from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from loguru import logger
import requests
from app.config import GEMINI_API_KEY, USER_AGENT
from app.analyzer import analyze_ad
from app.personalizer import generate_page_from_ad

router = APIRouter(prefix="/api")

@router.post("/personalize")
async def personalize_page(
    ad_image: UploadFile = File(None),
    ad_image_url: str = Form(None),
):
    """
    Personalization engine that builds a landing page based ONLY on the ad creative.
    """
    logger.info("Incoming request for one-click personalization")
    
    if not GEMINI_API_KEY:
        logger.error("Missing Gemini API Key in .env")
        raise HTTPException(500, "GEMINI_API_KEY not configured")

    # 1. Get image bytes
    image_bytes = None
    if ad_image and ad_image.filename:
        logger.info(f"Using uploaded ad image: {ad_image.filename}")
        image_bytes = await ad_image.read()
    elif ad_image_url:
        logger.info(f"Fetching ad image from URL: {ad_image_url}")
        try:
            resp = requests.get(ad_image_url, headers={"User-Agent": USER_AGENT}, timeout=15)
            resp.raise_for_status()
            image_bytes = resp.content
        except Exception as e:
            logger.error(f"Failed to fetch image: {e}")
            raise HTTPException(400, f"Image fetch failed: {e}")
    else:
        raise HTTPException(400, "Ad creative (file or URL) required")

    # 2. Engine Pipeline
    try:
        # Step A: Analyze the ad
        logger.debug("Running Vision analysis on ad creative...")
        ad_analysis = analyze_ad(image_bytes)
        
        # Step B: Generate the page from scratch using templates
        logger.debug("Generating high-converting landing page from ad metadata...")
        personalized_html = generate_page_from_ad(ad_analysis)
        
        logger.success("Personalized page generated successfully.")
        return {
            "status": "success",
            "ad_analysis": ad_analysis,
            "personalized_html": personalized_html,
        }
        
    except Exception as e:
        logger.exception("Engine failure")
        raise HTTPException(500, f"Engine failure: {str(e)}")

@router.get("/health")
async def health():
    return {"status": "operational", "engine_version": "0.5.0", "mode": "one-click-generation"}
