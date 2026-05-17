import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace links in news section
content = content.replace(
    '<div class="sp-card-link" style="margin-top:20px">Read Full Release →</div>',
    '<div class="sp-card-link" style="margin-top:20px;cursor:pointer" onclick="openPage(\'news-1\')">Read Full Release →</div>'
)

# For the other 6, replace one by one. We can do this with re.sub using a function
counter = 2
def replace_read_more(match):
    global counter
    res = f'<div class="sp-card-link" style="margin-top:14px;cursor:pointer" onclick="openPage(\'news-{counter}\')">Read More →</div>'
    counter += 1
    return res

content = re.sub(r'<div class="sp-card-link" style="margin-top:14px">Read More →</div>', replace_read_more, content)

pages_html = """
      <!-- ── NEWS PAGE 1 ── -->
      <div class="sp-page" id="sp-news-1" style="display:none">
        <header class="sp-header">
          <div class="sp-header-inner">
            <button class="sp-back" onclick="openPage('news')">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 5l-7 7 7 7" /></svg> Back to News
            </button>
            <div class="sp-logo-name">Mushroom<br>Bio Packaging<span>Grown, Not Made.</span></div>
            <div class="sp-breadcrumb">Home / News / <span>Series B</span></div>
          </div>
        </header>
        <div class="sp-hero">
          <h1>Mushroom Bio Packaging Raises Series B to Scale Mycelium Production Globally</h1>
          <p>Press Release · May 2026</p>
        </div>
        <div class="sp-body" style="max-width:800px; margin:0 auto; padding-top:40px;">
          <div class="sp-reveal" style="font-size:16px; line-height:1.8; color:#444;">
             <p>We are proud to announce the close of our $28M Series B funding round, led by Earthrise Ventures. This capital will be used to significantly expand our growing facilities across Europe and Southeast Asia, effectively doubling our production capacity to meet surging global demand.</p>
             <p>As the transition away from expanded polystyrene (EPS) foam accelerates, large consumer brands are seeking reliable, scalable alternatives. Mycelium packaging offers a 100% home-compostable solution that matches the shock absorption of EPS without the environmental toll. This funding allows us to support multi-national supply chains without compromising on our sustainability ethos.</p>
             <p>"This is a pivotal moment for biological manufacturing," said our CEO. "We're not just making a product; we are growing a new industrial paradigm. By localizing our production facilities near key manufacturing hubs in Europe and Asia, we drastically reduce shipping emissions while providing just-in-time inventory for our partners."</p>
             <p>The expansion will also create over 150 green jobs across our new facilities and enable further R&D into advanced material properties, such as increased fire resistance and custom structural densities.</p>
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
            <div class="sp-breadcrumb">Home / News / <span>Fast Company</span></div>
          </div>
        </header>
        <div class="sp-hero">
          <h1>Featured in Fast Company's World Changing Ideas 2026</h1>
          <p>Industry · March 2026</p>
        </div>
        <div class="sp-body" style="max-width:800px; margin:0 auto; padding-top:40px;">
          <div class="sp-reveal" style="font-size:16px; line-height:1.8; color:#444;">
             <p>Our mycelium cold-chain liner was recognised as one of Fast Company's top innovations in sustainable logistics for 2026, marking a significant milestone in our journey to replace EPS in temperature-controlled shipping.</p>
             <p>The cold chain industry relies heavily on single-use plastics to transport perishable foods and medical supplies. Our mycelium liners offer exceptional thermal insulation—comparable to traditional Styrofoam coolers—while remaining 100% home compostable. Within 45 days, these liners can turn into nutrient-rich soil.</p>
             <p>Being recognized by Fast Company highlights the urgency and feasibility of switching to biologically grown materials. The award specifically noted our design's breathability, which helps prevent condensation buildup, a common issue in traditional foam coolers that can spoil perishable goods.</p>
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
            <div class="sp-breadcrumb">Home / News / <span>Luxury Partnership</span></div>
          </div>
        </header>
        <div class="sp-hero">
          <h1>New Partnership with European Luxury Goods Alliance</h1>
          <p>Partnership · February 2026</p>
        </div>
        <div class="sp-body" style="max-width:800px; margin:0 auto; padding-top:40px;">
          <div class="sp-reveal" style="font-size:16px; line-height:1.8; color:#444;">
             <p>Twelve luxury brands across France, Italy, and Germany will transition to custom mycelium gift packaging throughout 2026, eliminating over 400 tonnes of foam annually.</p>
             <p>Luxury packaging is often synonymous with excess. We are redefining luxury by introducing packaging that is grown, velvet-soft to the touch, and completely natural. The European Luxury Goods Alliance chose Mushroom Bio Packaging because of our material's unique aesthetic and our ability to mold complex shapes that snugly fit premium products like perfumes, watches, and jewelry.</p>
             <p>"The tactile experience of mycelium packaging tells a story of care—for the product and for the planet," noted the Alliance's sustainability director. By 2030, the alliance plans to phase out all non-compostable plastics from their secondary packaging.</p>
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
            <div class="sp-breadcrumb">Home / News / <span>Research Study</span></div>
          </div>
        </header>
        <div class="sp-hero">
          <h1>New Study Confirms Superior Compostability vs. Bio-Plastics</h1>
          <p>Research · January 2026</p>
        </div>
        <div class="sp-body" style="max-width:800px; margin:0 auto; padding-top:40px;">
          <div class="sp-reveal" style="font-size:16px; line-height:1.8; color:#444;">
             <p>An independent study from the University of Wageningen confirmed that our mycelium packaging degrades 4× faster than PLA bio-plastics under home-compost conditions.</p>
             <p>Many "bio-plastics" require industrial composting facilities reaching high temperatures to break down properly, often confusing consumers and ending up in landfills where they behave just like regular plastics. The study showed that mycelium breaks down naturally in a standard garden compost bin within 45 to 90 days.</p>
             <p>Furthermore, the researchers discovered that the hemp hurd used in our substrate actually improves soil aeration and moisture retention as it breaks down, making our packaging not just "less bad" for the environment, but actively beneficial for local ecosystems.</p>
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
            <div class="sp-breadcrumb">Home / News / <span>COP30 Event</span></div>
          </div>
        </header>
        <div class="sp-hero">
          <h1>We Spoke at COP30 — Here's What We Said</h1>
          <p>Event · December 2025</p>
        </div>
        <div class="sp-body" style="max-width:800px; margin:0 auto; padding-top:40px;">
          <div class="sp-reveal" style="font-size:16px; line-height:1.8; color:#444;">
             <p>Our CEO presented the case for biological packaging at the UN Climate Conference, calling on global brands to make the switch by 2030.</p>
             <p>During the "Future of Materials" panel at COP30, our team highlighted how transitioning to grown materials can sequester carbon, reduce petroleum dependency, and utilize vast amounts of agricultural waste. "Every year, billions of tons of crop waste are burned or left to rot. We use that waste as food for our fungi, turning a problem into a high-performance packaging solution," our CEO stated.</p>
             <p>The reception from policymakers was overwhelmingly positive, leading to discussions about potential subsidies for bio-manufacturing and stricter regulations on single-use protective plastics across the EU and North America.</p>
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
            <div class="sp-breadcrumb">Home / News / <span>SPC Award</span></div>
          </div>
        </header>
        <div class="sp-hero">
          <h1>Winner: Sustainable Packaging Coalition Innovation Award</h1>
          <p>Award · November 2025</p>
        </div>
        <div class="sp-body" style="max-width:800px; margin:0 auto; padding-top:40px;">
          <div class="sp-reveal" style="font-size:16px; line-height:1.8; color:#444;">
             <p>Mushroom Bio Packaging received the SPC's top honour for breakthrough material innovation in protective packaging.</p>
             <p>The judges praised our Breakaway Corners product line, which provides a drop-in replacement for styrofoam corner blocks. By designing the corners to break apart cleanly at the seams, we improved composting efficiency and reduced shipping volume for end consumers.</p>
             <p>This award validates years of research and development, proving that performance and sustainability are not mutually exclusive. We are honored to be recognized by our peers and remain committed to pushing the boundaries of what mycelium can do.</p>
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
            <div class="sp-breadcrumb">Home / News / <span>GrowKit Launch</span></div>
          </div>
        </header>
        <div class="sp-hero">
          <h1>Introducing GrowKit: A Sample Set for Brands</h1>
          <p>Product · October 2025</p>
        </div>
        <div class="sp-body" style="max-width:800px; margin:0 auto; padding-top:40px;">
          <div class="sp-reveal" style="font-size:16px; line-height:1.8; color:#444;">
             <p>We launched a curated sample kit allowing procurement teams to test mycelium packaging in their own facilities before committing to a custom program.</p>
             <p>The GrowKit includes samples of our standard Breakaway Corners, a cold shipping liner section, and a custom-molded interior piece. It demonstrates the versatility, strength, and feel of mycelium materials.</p>
             <p>Understanding a new material is best done hands-on. By sending these kits to sustainability officers and packaging engineers, we are accelerating the adoption of grown materials. Each kit also includes a timeline for custom tooling and a lifecycle analysis sheet detailing the carbon offset of switching away from foam.</p>
          </div>
        </div>
      </div>
"""

# Insert right before </div><!-- /subpage-overlay -->
content = content.replace('    </div><!-- /subpage-overlay -->', pages_html + '\n    </div><!-- /subpage-overlay -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html")
