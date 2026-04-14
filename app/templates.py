"""
A collection of professional, 'blank' high-converting landing page templates.
These serve as the 'existing page' that the AI personalizes.
"""

# A hyper-modern, clean SaaS/Product template
SAAS_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; }
        .hero-gradient { background: radial-gradient(circle at top, rgba(99, 102, 241, 0.1) 0%, transparent 70%); }
    </style>
</head>
<body class="bg-slate-50 text-slate-900 border-t-4 border-indigo-600">
    <nav class="max-w-7xl mx-auto px-6 py-6 flex justify-between items-center">
        <div class="text-2xl font-bold tracking-tight text-slate-800">{{BRAND_NAME}}</div>
        <div class="hidden md:flex gap-8 text-sm font-medium text-slate-600">
            <a href="#">Features</a>
            <a href="#">Pricing</a>
            <a href="#">About</a>
        </div>
        <a href="#cta" class="bg-indigo-600 text-white px-5 py-2.5 rounded-full text-sm font-bold hover:shadow-lg transition-all">{{NAV_CTA}}</a>
    </nav>

    <header class="hero-gradient pt-20 pb-32 px-6">
        <div class="max-w-4xl mx-auto text-center">
            <div id="offer-tag" class="inline-block bg-indigo-100 text-indigo-700 px-4 py-1.5 rounded-full text-xs font-bold uppercase tracking-wider mb-6">
                {{OFFER_TAG}}
            </div>
            <h1 class="text-5xl md:text-7xl font-extrabold tracking-tight text-slate-900 mb-8 leading-tight">
                {{HERO_HEADLINE}}
            </h1>
            <p class="text-xl text-slate-600 mb-10 max-w-2xl mx-auto leading-relaxed">
                {{HERO_SUBHEADLINE}}
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
                <a href="#cta" class="w-full sm:w-auto bg-indigo-600 text-white px-10 py-4 rounded-xl text-lg font-bold hover:bg-indigo-700 transition-all shadow-xl shadow-indigo-100">
                    {{MAIN_CTA}}
                </a>
                <span class="text-sm text-slate-400">No credit card required.</span>
            </div>
        </div>
    </header>

    <section class="max-w-7xl mx-auto px-6 -mt-16 mb-32">
        <div class="bg-white rounded-3xl border border-slate-200 shadow-2xl p-4 overflow-hidden">
            <div class="aspect-video bg-slate-100 rounded-2xl flex items-center justify-center text-slate-400 font-medium">
                {{PRODUCT_IMAGE_PLACEHOLDER}}
            </div>
        </div>
    </section>

    <section class="max-w-7xl mx-auto px-6 mb-32">
        <div class="text-center mb-16">
            <h2 class="text-3xl font-bold text-slate-900">Why choose {{BRAND_NAME}}?</h2>
        </div>
        <div class="grid md:grid-cols-3 gap-12" id="usps">
            {{USP_SECTION}}
        </div>
    </section>

    <footer id="cta" class="bg-slate-900 text-white py-24 px-6 text-center">
        <h2 class="text-4xl font-bold mb-6 italic text-indigo-400">Ready to transform your workflow?</h2>
        <p class="text-slate-400 mb-10">Join 10,000+ companies using {{BRAND_NAME}}</p>
        <a href="#" class="bg-white text-slate-900 px-12 py-5 rounded-2xl text-xl font-bold hover:bg-slate-100 transition-all">
            {{FOOTER_CTA}}
        </a>
    </footer>
</body>
</html>
"""

# A high-end commerce/retail template
RETAIL_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,700&family=Plus+Jakarta+Sans:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Plus Jakarta Sans', sans-serif; }
        h1, h2 { font-family: 'Playfair Display', serif; }
    </style>
</head>
<body class="bg-white text-zinc-900">
    <div class="bg-zinc-900 text-white text-[10px] uppercase tracking-[0.2em] py-2 text-center font-bold">
        {{TOP_BAR_MESSAGING}}
    </div>
    
    <nav class="border-b border-zinc-100 px-10 py-6 flex justify-between items-center bg-white sticky top-0 z-50">
        <div class="text-2xl font-bold italic">{{BRAND_NAME}}</div>
        <div class="space-x-8 text-xs font-bold uppercase tracking-widest text-zinc-400">
            <a href="#" class="text-zinc-900">Shop</a>
            <a href="#">Our Story</a>
            <a href="#">Reviews</a>
        </div>
        <div class="w-10 h-10 border border-zinc-200 rounded-full flex items-center justify-center cursor-pointer">
            🛒
        </div>
    </nav>

    <main class="grid lg:grid-cols-2 min-h-[80vh]">
        <div class="p-12 lg:p-24 flex flex-col justify-center">
            <div class="text-sm font-bold text-amber-600 mb-6 uppercase tracking-[0.3em]">{{CATEGORY_TAG}}</div>
            <h1 class="text-6xl md:text-8xl mb-8 leading-tight">{{HERO_HEADLINE}}</h1>
            <p class="text-xl text-zinc-500 mb-12 leading-relaxed max-w-lg">{{HERO_SUBHEADLINE}}</p>
            <div class="space-y-6">
                <a href="#buy" class="inline-block bg-zinc-900 text-white px-12 py-5 text-sm font-bold uppercase tracking-widest hover:bg-zinc-800 transition-all">
                    {{MAIN_CTA}}
                </a>
                <div class="flex items-center gap-4 text-xs font-bold text-zinc-400">
                    <div class="flex text-amber-400">★★★★★</div>
                    <span>4.9/5 OVER 2,000 REVIEWS</span>
                </div>
            </div>
        </div>
        <div class="bg-zinc-100 flex items-center justify-center p-20">
            <div class="w-full h-full bg-zinc-200 rounded-sm shadow-xl flex items-center justify-center text-zinc-400 font-bold italic text-3xl">
                {{PRODUCT_IMAGE_PLACEHOLDER}}
            </div>
        </div>
    </main>

    <section class="py-32 px-10 bg-zinc-50">
        <div class="max-w-4xl mx-auto text-center">
            <h2 class="text-4xl mb-16">{{USP_HEADLINE}}</h2>
            <div class="grid md:grid-cols-3 gap-16 text-left">
                {{USP_SECTION}}
            </div>
        </div>
    </section>

    <section class="py-32 px-10 border-t border-zinc-100">
        <div class="max-w-xl mx-auto text-center">
            <h2 class="text-5xl mb-8 italic">Stay in the circle</h2>
            <p class="text-zinc-500 mb-12">Join our newsletter to receive {{OFFER_DETAILS}} and early access to new collections.</p>
            <div class="flex">
                <input type="email" placeholder="Email address" class="flex-1 border-b-2 border-zinc-900 py-4 outline-none">
                <button class="font-bold uppercase tracking-widest text-xs px-6">Submit</button>
            </div>
        </div>
    </section>
</body>
</html>
"""
