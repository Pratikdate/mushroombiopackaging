import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the main news section
new_sp_news = """      <div class="sp-page" id="sp-news" style="display:none">
        <header class="sp-header">
          <div class="sp-header-inner">
            <button class="sp-back" onclick="closePage()">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M19 12H5M12 5l-7 7 7 7" />
              </svg>
              Back to Home
            </button>
            <div class="sp-logo-name">Mushroom<br>Bio Packaging<span>Grown, Not Made.</span></div>
            <div class="sp-breadcrumb">Home / <span>News & Updates</span></div>
          </div>
        </header>

        <div class="sp-hero">
          <h1>Our Journey Begins</h1>
          <p>Follow our progress as we develop, prototype, and seek partners for our mycelium packaging technology.</p>
        </div>

        <div class="sp-body">
          <div class="sp-two-col sp-reveal" style="margin-top:0; border-bottom:1px solid #e0ddd8; padding-bottom:48px">
            <img class="sp-img-block"
              src="./watch_packaging.png"
              alt="News">
            <div>
              <div class="sp-card-tag" style="display:block;margin-bottom:10px">Announcement · May 2026</div>
              <h2 style="font-size:26px;font-weight:700;line-height:1.3;margin-bottom:14px">Seeking Early Adopters for Pilot Program</h2>
              <p style="color:#555;font-size:14px;line-height:1.75">We are excited to officially launch our search for visionary brand partners. We are looking for forward-thinking clients willing to pilot our custom-grown mycelium packaging solutions and help us refine our technology for commercial scale.</p>
              <div class="sp-card-link" style="margin-top:20px;cursor:pointer" onclick="openPage('news-1')">Read Full Update →</div>
            </div>
          </div>

          <div class="sp-grid sp-reveal" style="margin-top:48px">
            <div class="sp-card">
              <div class="sp-card-body">
                <div class="sp-card-tag">Prototyping · March 2026</div>
                <h3>Prototyping Our First Cold-Chain Liner</h3>
                <p>We've successfully grown our first batch of thermal insulating liners. Early lab tests show promising results against traditional EPS coolers.</p>
                <div class="sp-card-link" style="margin-top:14px;cursor:pointer" onclick="openPage('news-2')">Read More →</div>
              </div>
            </div>
            <div class="sp-card">
              <div class="sp-card-body">
                <div class="sp-card-tag">Partnership · February 2026</div>
                <h3>Seeking Visionary Luxury Brands for Beta Testing</h3>
                <p>We believe the luxury sector is perfect for mycelium packaging. We're actively looking for boutique brands to test our velvet-soft custom molds.</p>
                <div class="sp-card-link" style="margin-top:14px;cursor:pointer" onclick="openPage('news-3')">Read More →</div>
              </div>
            </div>
            <div class="sp-card">
              <div class="sp-card-body">
                <div class="sp-card-tag">Research · January 2026</div>
                <h3>Early Testing Shows Promising Compostability</h3>
                <p>Our initial backyard compost tests indicate that our prototypes break down within 60 days, leaving no toxic residue behind.</p>
                <div class="sp-card-link" style="margin-top:14px;cursor:pointer" onclick="openPage('news-4')">Read More →</div>
              </div>
            </div>
            <div class="sp-card">
              <div class="sp-card-body">
                <div class="sp-card-tag">Vision · December 2025</div>
                <h3>Our Vision for a Plastic-Free 2030</h3>
                <p>Read our founding manifesto on why we started Mushroom Bio Packaging and how we plan to eliminate single-use foam.</p>
                <div class="sp-card-link" style="margin-top:14px;cursor:pointer" onclick="openPage('news-5')">Read More →</div>
              </div>
            </div>
            <div class="sp-card">
              <div class="sp-card-body">
                <div class="sp-card-tag">Development · November 2025</div>
                <h3>Developing the Breakaway Corner Prototype</h3>
                <p>A behind-the-scenes look at how we engineered our first product design: the home-compostable breakaway corner protector.</p>
                <div class="sp-card-link" style="margin-top:14px;cursor:pointer" onclick="openPage('news-6')">Read More →</div>
              </div>
            </div>
            <div class="sp-card">
              <div class="sp-card-body">
                <div class="sp-card-tag">Product · October 2025</div>
                <h3>Request a Prototype: See the Material Yourself</h3>
                <p>We are putting together limited sample sets for interested investors and potential pilot clients. Request yours today.</p>
                <div class="sp-card-link" style="margin-top:14px;cursor:pointer" onclick="openPage('news-7')">Read More →</div>
              </div>
            </div>
          </div>
        </div>
      </div>\n"""

content = re.sub(
    r'<div class="sp-page" id="sp-news" style="display:none">.*?(?=<div class="sp-page" id="sp-licensees" style="display:none">)',
    new_sp_news,
    content,
    flags=re.DOTALL
)

# 2. Replace the detailed news pages
new_sp_news_pages = """      <!-- ── NEWS PAGE 1 ── -->
      <div class="sp-page" id="sp-news-1" style="display:none">
        <header class="sp-header">
          <div class="sp-header-inner">
            <button class="sp-back" onclick="openPage('news')">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 5l-7 7 7 7" /></svg> Back to News
            </button>
            <div class="sp-logo-name">Mushroom<br>Bio Packaging<span>Grown, Not Made.</span></div>
            <div class="sp-breadcrumb">Home / News / <span>Pilot Program</span></div>
          </div>
        </header>
        <div class="sp-hero">
          <h1>Seeking Early Adopters for Pilot Program</h1>
          <p>Announcement · May 2026</p>
        </div>
        <div class="sp-body" style="max-width:800px; margin:0 auto; padding-top:40px;">
          <img src="./watch_packaging.png" alt="Prototype Packaging" style="width:100%; height:auto; margin-bottom: 32px; border:1px solid #e0ddd8">
          <div class="sp-reveal" style="font-size:16px; line-height:1.8; color:#444;">
             <p>As an early-stage startup, our most critical goal is transitioning from the lab to the real world. We are excited to officially launch our search for visionary brand partners willing to participate in our pilot program.</p>
             <p>We are looking for forward-thinking clients who share our commitment to a plastic-free future. By partnering with us now, you will help us test and refine our custom-grown mycelium packaging solutions. Your feedback will directly influence our manufacturing processes as we prepare for commercial scale.</p>
             <p>"This is an opportunity for brands to be at the forefront of biological manufacturing," said our founder. "We are offering our early clients heavily subsidized prototyping and dedicated engineering support to ensure their products are protected sustainably."</p>
             <p>If you are a business looking to eliminate EPS foam from your supply chain, we invite you to reach out and explore a pilot project with us.</p>
          </div>
        </div>
      </div>

      <!-- ── NEWS PAGE 2 ── -->
      <div class="sp-page" id="sp-news-2" style="display:none">
        <header class="sp-header">
          <div class="sp-header-inner">
            <button class="sp-back" onclick="openPage('news')">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 5l-7 7 7 7" /></svg> Back to News
            </button>
            <div class="sp-logo-name">Mushroom<br>Bio Packaging<span>Grown, Not Made.</span></div>
            <div class="sp-breadcrumb">Home / News / <span>Prototyping</span></div>
          </div>
        </header>
        <div class="sp-hero">
          <h1>Prototyping Our First Cold-Chain Liner</h1>
          <p>Prototyping · March 2026</p>
        </div>
        <div class="sp-body" style="max-width:800px; margin:0 auto; padding-top:40px;">
          <div class="sp-reveal" style="font-size:16px; line-height:1.8; color:#444;">
             <p>We've successfully grown our first batch of thermal insulating liners in our experimental lab space. The cold chain industry relies heavily on single-use plastics to transport perishable foods and medical supplies, making it a prime target for disruption.</p>
             <p>Our early prototypes show exceptional thermal insulation—comparable to traditional Styrofoam coolers. More importantly, these liners remain 100% home compostable. While we are still optimizing the growth cycles and mold designs, these initial results prove that our concept is viable.</p>
             <p>We are currently seeking small-scale food delivery or local farm partners to conduct real-world transit tests. If you ship perishable goods and want to ditch the foam coolers, let's talk.</p>
          </div>
        </div>
      </div>

      <!-- ── NEWS PAGE 3 ── -->
      <div class="sp-page" id="sp-news-3" style="display:none">
        <header class="sp-header">
          <div class="sp-header-inner">
            <button class="sp-back" onclick="openPage('news')">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 5l-7 7 7 7" /></svg> Back to News
            </button>
            <div class="sp-logo-name">Mushroom<br>Bio Packaging<span>Grown, Not Made.</span></div>
            <div class="sp-breadcrumb">Home / News / <span>Luxury Beta</span></div>
          </div>
        </header>
        <div class="sp-hero">
          <h1>Seeking Visionary Luxury Brands for Beta Testing</h1>
          <p>Partnership · February 2026</p>
        </div>
        <div class="sp-body" style="max-width:800px; margin:0 auto; padding-top:40px;">
          <div class="sp-reveal" style="font-size:16px; line-height:1.8; color:#444;">
             <p>Luxury packaging should feel premium, but it shouldn't cost the earth. We believe the luxury sector is perfect for the tactile, velvet-soft finish of our mycelium material.</p>
             <p>We are actively looking for boutique brands in cosmetics, fragrances, and jewelry to beta test our custom molds. Because we grow the packaging to perfectly cradle your product, we can offer an unboxing experience that is both highly protective and deeply sustainable.</p>
             <p>Beta partners will work directly with our design team to create bespoke shapes that reflect their brand's aesthetic, helping us prove the viability of biological packaging in high-end retail.</p>
          </div>
        </div>
      </div>

      <!-- ── NEWS PAGE 4 ── -->
      <div class="sp-page" id="sp-news-4" style="display:none">
        <header class="sp-header">
          <div class="sp-header-inner">
            <button class="sp-back" onclick="openPage('news')">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 5l-7 7 7 7" /></svg> Back to News
            </button>
            <div class="sp-logo-name">Mushroom<br>Bio Packaging<span>Grown, Not Made.</span></div>
            <div class="sp-breadcrumb">Home / News / <span>Compost Testing</span></div>
          </div>
        </header>
        <div class="sp-hero">
          <h1>Early Testing Shows Promising Compostability</h1>
          <p>Research · January 2026</p>
        </div>
        <div class="sp-body" style="max-width:800px; margin:0 auto; padding-top:40px;">
          <div class="sp-reveal" style="font-size:16px; line-height:1.8; color:#444;">
             <p>A core promise of our technology is that it returns to the earth without a trace. This month, we concluded our first round of internal backyard compost tests.</p>
             <p>We placed several prototype corner blocks into standard, unmanaged soil bins. We observed that the mycelium and hemp hurd structure began breaking down within 30 days. By day 60, the material had completely disintegrated, adding organic matter to the soil without leaving any microplastics or toxic residue behind.</p>
             <p>While we plan to seek official third-party certifications once our manufacturing process is finalized, these early results give us immense confidence in the environmental benefits of our product.</p>
          </div>
        </div>
      </div>

      <!-- ── NEWS PAGE 5 ── -->
      <div class="sp-page" id="sp-news-5" style="display:none">
        <header class="sp-header">
          <div class="sp-header-inner">
            <button class="sp-back" onclick="openPage('news')">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 5l-7 7 7 7" /></svg> Back to News
            </button>
            <div class="sp-logo-name">Mushroom<br>Bio Packaging<span>Grown, Not Made.</span></div>
            <div class="sp-breadcrumb">Home / News / <span>Our Vision</span></div>
          </div>
        </header>
        <div class="sp-hero">
          <h1>Our Vision for a Plastic-Free 2030</h1>
          <p>Vision · December 2025</p>
        </div>
        <div class="sp-body" style="max-width:800px; margin:0 auto; padding-top:40px;">
          <div class="sp-reveal" style="font-size:16px; line-height:1.8; color:#444;">
             <p>We started Mushroom Bio Packaging because we were tired of seeing rivers choked with polystyrene and landfills overflowing with "recyclable" plastics that never actually get recycled.</p>
             <p>Our vision is simple: by 2030, biological, grown packaging should be the default for protective shipping. We are building the foundational technology to make this possible. It requires rethinking the entire supply chain—from utilizing agricultural waste as raw material to decentralizing production so packaging is grown near where it's used.</p>
             <p>We are just getting started, but our roadmap is clear. We are seeking investors, clients, and team members who share this ambitious vision to join us on this journey.</p>
          </div>
        </div>
      </div>

      <!-- ── NEWS PAGE 6 ── -->
      <div class="sp-page" id="sp-news-6" style="display:none">
        <header class="sp-header">
          <div class="sp-header-inner">
            <button class="sp-back" onclick="openPage('news')">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 5l-7 7 7 7" /></svg> Back to News
            </button>
            <div class="sp-logo-name">Mushroom<br>Bio Packaging<span>Grown, Not Made.</span></div>
            <div class="sp-breadcrumb">Home / News / <span>Breakaway Prototype</span></div>
          </div>
        </header>
        <div class="sp-hero">
          <h1>Developing the Breakaway Corner Prototype</h1>
          <p>Development · November 2025</p>
        </div>
        <div class="sp-body" style="max-width:800px; margin:0 auto; padding-top:40px;">
          <div class="sp-reveal" style="font-size:16px; line-height:1.8; color:#444;">
             <p>Designing packaging that is both protective and easy to dispose of is a significant engineering challenge. This month, we unveiled our first design concept: the Breakaway Corner.</p>
             <p>Intended to replace styrofoam corner blocks used in shipping furniture and electronics, our prototype features precisely engineered perforations. This allows the end consumer to easily snap the corner into smaller pieces, which drastically speeds up the composting process in a home garden.</p>
             <p>We are currently stress-testing these corners in our lab to ensure they meet standard drop-test requirements, tweaking the density of the mycelium growth to find the perfect balance between rigidity and flexibility.</p>
          </div>
        </div>
      </div>

      <!-- ── NEWS PAGE 7 ── -->
      <div class="sp-page" id="sp-news-7" style="display:none">
        <header class="sp-header">
          <div class="sp-header-inner">
            <button class="sp-back" onclick="openPage('news')">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 5l-7 7 7 7" /></svg> Back to News
            </button>
            <div class="sp-logo-name">Mushroom<br>Bio Packaging<span>Grown, Not Made.</span></div>
            <div class="sp-breadcrumb">Home / News / <span>Request a Prototype</span></div>
          </div>
        </header>
        <div class="sp-hero">
          <h1>Request a Prototype: See the Material Yourself</h1>
          <p>Product · October 2025</p>
        </div>
        <div class="sp-body" style="max-width:800px; margin:0 auto; padding-top:40px;">
          <div class="sp-reveal" style="font-size:16px; line-height:1.8; color:#444;">
             <p>Seeing is believing. To help potential investors and pilot clients understand the potential of mycelium packaging, we are putting together a limited number of prototype sample sets.</p>
             <p>These early samples demonstrate the versatility, strength, and unique velvety feel of mycelium materials. Because we are producing these by hand in our experimental lab, availability is strictly limited.</p>
             <p>If your brand is serious about exploring biological packaging, or if you are an investor interested in the future of sustainable materials, please use our contact form to request a prototype kit. We'd love to show you what we're building.</p>
          </div>
        </div>
      </div>
\n"""

content = re.sub(
    r'<!-- ── NEWS PAGE 1 ── -->.*?(?=<!-- ── BLOG PAGE CUSTOM ── -->)',
    new_sp_news_pages,
    content,
    flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html to reflect early-stage startup narrative")
