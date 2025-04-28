import streamlit as st
import time

# --- Page config ---
st.set_page_config(page_title="Demand Gen That Slaps — At Scale 🚀", page_icon=":tada:", layout="wide")

# --- Custom CSS ---
st.markdown(
    """
    <style>
    body {
        background-color: #f7f9fc;
        color: #222831;
    }
    .main {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }
    section[data-testid="stSidebar"] {
        background-color: #e0f2f1;
        border-right: 1px solid #d1d8e2;
    }
    h1, h2, h3 {
        color: #0078FF;
        text-align: center;
    }
    .hero-banner {
        background: linear-gradient(135deg, #00c6ff 0%, #0072ff 100%);
        color: white;
        padding: 3rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .section-title {
        color: #005bb5;
        border-bottom: 2px solid #00c6ff;
        padding-bottom: 0.5rem;
        margin-bottom: 1rem;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Sidebar ---
st.sidebar.image("Agoda_logo.jpg", width=200)
st.sidebar.title("🧭 Explore My World")
sections = ["🏠 Home", "💖 We Go Together!", "🚀 Campaign Chronicles", "📅 30/60/90 Blueprint", "🤝 Dream Team", "🛠️ My Arsenal", "📬 Connect with Siva!"]
selection = st.sidebar.radio("Hop to a Section", sections)

# --- Home Section ---
if selection == "🏠 Home":
    with st.spinner("Igniting the Demand Gen Engine..."):
        time.sleep(1)

    st.markdown('<div class="hero-banner">', unsafe_allow_html=True)
    st.markdown("""
    <h1 style='text-align: center; font-size: 3em;'>🚀 Demand Gen That Breaks the Mold</h1>
    <p style='text-align: center; font-size: 1.5em;'>Where creativity fuels funnels, and pipelines aren’t just built — they're launched at warp speed. 🌠</p>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<h2 class="section-title">Welcome Aboard 🎉</h2>', unsafe_allow_html=True)

    st.markdown("""
    👋 Hey there! Buckle up for a thrilling ride through my demand generation universe.  
    I'm Siva, your future pipeline pilot!

    I don't just generate leads.  
    I engineer *revenue engines* that move fast, stay predictable, and scale with elegance.

    Here's what I bring to the table:
    """)
    st.markdown("""
    📈 Fuel Growth through multi-channel strategies (email, SEO, social, webinars, content).  
    🎯 Orchestrate Campaigns end-to-end with creative excellence.  
    🤝 Collaborate deeply with Sales, Product, BD, Design, RevOps.  
    🎤 Craft High-Impact Content that sells and nurtures.  
    📣 Build Audiences with magnetic digital campaigns.  
    🚀 Scale Social for maximum brand presence.  
    📊 Optimize Relentlessly through analytics and agile testing.
    """)

    st.markdown("<br>Ready to witness the magic? Let's make some serious KPI fireworks! 💥", unsafe_allow_html=True)

# --- We go together! Section ---
elif selection == "💖 We Go Together!":
    with st.spinner("Unveiling Our Story..."):
        time.sleep(1)

    st.markdown('<h2 class="section-title">The Story 🎬</h2>', unsafe_allow_html=True)

    st.markdown("""
    Why Agoda? 🛫

    Agoda feels like a high-octane rocketship in the travel galaxy — dynamic, bold, and powered by data.  
    Every team moves with startup speed but operates with the force of a global brand.  
    Innovation isn't a buzzword here; it's woven into every experiment, every sprint, every decision.  
    That's exactly the environment where I thrive.

    Why This Demand Gen Role? 🔥

    Demand Generation isn't just a job to me — it's a craft.  
    I've spent 5+ years obsessing over every lead, every conversion point, every sales alignment sync.  
    I don’t just fill pipelines — I build engines that Sales *loves* to work with.  
    Joining Agoda means amplifying that mission at one of the most exciting stages of growth possible.
    """)

# --- Campaign Chronicles Section ---
elif selection == "🚀 Campaign Chronicles":
    with st.spinner("Loading Epic Campaign Tales..."):
        time.sleep(1)

    st.markdown('<h2 class="section-title">Data-Backed Victories 🏆</h2>', unsafe_allow_html=True)

    with st.expander("🎯 Mission: CFO Takeover"):
        st.markdown("""
        **Objective:** Capture CFO mindshare in mid-market accounts.  
        **Tactic:** Precision-crafted outbound cadences and custom nurture tracks.  
        **Victory:** Tripled SQL pipeline and improved sales-cycle velocity by 27%. 
        *Fun Moment:* Our CFO email open rates were double industry benchmarks. 😉
        """)

    with st.expander("🥇 Mission: PLM Cloud Launch Spectacle"):
        st.markdown("""
        **Objective:** Launch new PLM Cloud solution with immediate impact.  
        **Tactic:** Full-stack GTM campaigns: webinars, blogs, testimonials, CTAs.  
        **Victory:** 250% MQL goal smash, $10M+ influenced pipeline within 30 days.  
        *Fun Moment:* Sales joked they needed extra hands to handle these opportunities! 😎
        """)

    with st.expander("🚀 Mission: Inbound Avengers Assemble"):
        st.markdown("""
        **Objective:** Rapid qualification of hot inbound leads.  
        **Tactic:** Built a specialized inbound squad, lightning-fast response SLAs.  
        **Victory:** Cut response time by 80%, boosting conversion rate by 22%.  
        *Fun Moment:* Gamified responses with a leaderboard — boosted team speed by 35%. 🦇
        """)

    with st.expander("🚗 Mission: Rebrand Automotive's Ride to the Future"):
        st.markdown("""
        **Objective:** Future-proof HCL’s Auto messaging with CASE alignment.  
        **Tactic:** Revamped digital presence, launched podcasts, gained analyst love.  
        **Victory:** 80% jump in organic form fills, boosted analyst visibility by 30%.  
        *Fun Moment:* The CASE story was highlighted at the global leadership townhall! 🏎️
        """)

# --- 30/60/90 Blueprint Section ---
elif selection == "📅 30/60/90 Blueprint":
    with st.spinner("Crafting the Strategic Roadmap..."):
        time.sleep(1)

    st.markdown('<h2 class="section-title">Roadmap for Success 💡</h2>', unsafe_allow_html=True)

    st.markdown('<p class="blueprint-title">First 30 Days: Recon & Rally 🚀</p>', unsafe_allow_html=True)
    st.markdown("""
    Understand Agoda’s products, ICPs, competitors inside and out.  
    Audit funnel metrics, win rates, campaign ROI.  
    Forge partnerships with Sales, Product, and Content.

    🎯 **Success looks like:** Clear demand gen baseline metrics and stakeholder alignment.
    """)

    st.markdown('<p class="blueprint-title">Next 30 Days: Pilot & Perfect 🛠️</p>', unsafe_allow_html=True)
    st.markdown("""
    Launch 1–2 quick-win pilots for immediate learning.  
    Formalize frameworks for repeatability.  
    Lock in KPI dashboards.

    🎯 **Success looks like:** First marketing-sourced pipeline closes in.
    """)

    st.markdown('<p class="blueprint-title">Final 30 Days: Scale & Conquer 🔥</p>', unsafe_allow_html=True)
    st.markdown("""
    Expand pilots into scaled plays.  
    Tighten lead qualification SLAs with Sales.  
    Forecast and roadmap next 3 quarters of campaigns.

    🎯 **Success looks like:** Predictable demand engine in full motion.
    """)

    st.snow()

# --- Connect Section ---
elif selection == "📬 Connect with Siva!":
    with st.spinner('Opening the hotline...'):
        time.sleep(1)

    st.markdown('<h2 class="section-title">Your Next Growth Partner 📬</h2>', unsafe_allow_html=True)

    st.markdown("""
    Ready to architect Agoda’s next great demand generation engine?

    📞 Call Me: <a href="tel:+916281495464">+91-6281495464</a>  
    📧 Email Me: <a href="mailto:sivasaran591@gmail.com">sivasaran591@gmail.com</a>

    P.S. I am a huge Arsenal fan ⚽️.  
    Let's talk growth, optimization, and winning demand generation strategies! 😎
    """)

    st.balloons()
