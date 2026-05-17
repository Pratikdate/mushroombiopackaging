import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replacements
replacements = [
    ('<a href="#custom" class="btn-white">Learn More</a>', '<a href="#" onclick="openPage(\'blog-custom\'); return false;" class="btn-white">Learn More</a>'),
    ('<a href="#process" class="btn-white">Learn More</a>', '<a href="#" onclick="openPage(\'blog-process\'); return false;" class="btn-white">Learn More</a>'),
    ('<a href="#custom" class="btn-dark">Learn More</a>', '<a href="#" onclick="openPage(\'blog-custom\'); return false;" class="btn-dark">Learn More</a>'),
    ('<a href="#process" class="btn-outline-white">Learn More</a>', '<a href="#" onclick="openPage(\'blog-process\'); return false;" class="btn-outline-white">Learn More</a>'),
    ('<a href="#custom" class="wc-read">Read More</a>', '<a href="#" onclick="openPage(\'blog-custom\'); return false;" class="wc-read">Read More</a>'),
    ('<a href="#timeline" class="wc-read">Read More</a>', '<a href="#" onclick="openPage(\'blog-timeline\'); return false;" class="wc-read">Read More</a>'),
    ('<a href="#phases" class="wc-read">Read More</a>', '<a href="#" onclick="openPage(\'blog-process\'); return false;" class="wc-read">Read More</a>'),
]

for old, new in replacements:
    content = content.replace(old, new)

pages_html = """
      <!-- ── BLOG PAGE CUSTOM ── -->
      <div class="sp-page" id="sp-blog-custom" style="display:none">
        <header class="sp-header">
          <div class="sp-header-inner">
            <button class="sp-back" onclick="closePage()">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 5l-7 7 7 7" /></svg> Back to Home
            </button>
            <div class="sp-logo-name">Mushroom<br>Bio Packaging<span>Grown, Not Made.</span></div>
            <div class="sp-breadcrumb">Home / Blog / <span>Custom Packaging</span></div>
          </div>
        </header>
        <div class="sp-hero">
          <h1>Custom Packaging: Made by Nature, Designed by You</h1>
          <p>Learn how we engineer bespoke mycelium solutions for unique product shapes.</p>
        </div>
        <div class="sp-body" style="max-width:800px; margin:0 auto; padding-top:40px;">
          <div class="sp-reveal" style="font-size:16px; line-height:1.8; color:#444;">
             <p>Our custom packaging service goes beyond mere protective enclosures. It represents a paradigm shift where packaging is grown specifically to match the contours of your product. By utilizing the root structure of mushrooms—mycelium—and agricultural waste like hemp hurd, we mold completely custom shapes that offer exceptional shock absorption.</p>
             <p>The journey starts with our engineering team designing a 3D model that perfectly cradles your item. From fragile glassware and high-end electronics to heavy mechanical components, we can achieve protective capabilities that rival expanded polystyrene (EPS) foam. After the digital design, we create custom thermoformed molds.</p>
             <p>Once the molds are filled with our organic substrate, nature does the rest. Within a few days, the mycelium binds the hemp fibers together in a solid, resilient structure. We then halt the growth process through a careful drying phase, ensuring the packaging is safe, inert, and ready for transit. This bespoke approach means your customers receive a premium unboxing experience, knowing the packaging will fully compost in their backyard within 45 days.</p>
          </div>
        </div>
      </div>

      <!-- ── BLOG PAGE PROCESS ── -->
      <div class="sp-page" id="sp-blog-process" style="display:none">
        <header class="sp-header">
          <div class="sp-header-inner">
            <button class="sp-back" onclick="closePage()">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 5l-7 7 7 7" /></svg> Back to Home
            </button>
            <div class="sp-logo-name">Mushroom<br>Bio Packaging<span>Grown, Not Made.</span></div>
            <div class="sp-breadcrumb">Home / Blog / <span>Our Growth Process</span></div>
          </div>
        </header>
        <div class="sp-hero">
          <h1>The Growth Process: From Agricultural Waste to Packaging</h1>
          <p>Discover the science and art behind our MycoComposite™ technology.</p>
        </div>
        <div class="sp-body" style="max-width:800px; margin:0 auto; padding-top:40px;">
          <div class="sp-reveal" style="font-size:16px; line-height:1.8; color:#444;">
             <p>At the heart of Mushroom Bio Packaging is a revolutionary but simple biological process. We don't manufacture our materials in traditional factories using heat and petroleum; instead, we grow them in controlled vertical farming environments. Our primary ingredients are agricultural byproducts—often corn stalks or hemp hurd—and a specialized strain of mycelium.</p>
             <p>The process is broken down into several distinct phases. First is the <strong>Mixing Phase</strong>, where the raw agricultural waste is sterilized and inoculated with mycelium spores. The mixture is then allowed to colonize in a bulk state for a few days, creating a dense, white biological network.</p>
             <p>Next comes the <strong>Molding Phase</strong>. The colonized substrate is broken up and packed into precise, 3D-designed molds. Over the next 4 to 6 days, the mycelium continues to grow, acting as a natural glue that binds the loose particles into a solid, durable shape matching the mold exactly.</p>
             <p>Finally, we enter the <strong>Drying Phase</strong>. The grown parts are removed from their molds and baked in an oven. This crucial step deactivates the mycelium, stopping the growth and ensuring the final product is completely biologically inactive, lightweight, and incredibly strong. The result is a high-performance material that requires only a fraction of the energy used to produce synthetic foams.</p>
          </div>
        </div>
      </div>

      <!-- ── BLOG PAGE TIMELINE ── -->
      <div class="sp-page" id="sp-blog-timeline" style="display:none">
        <header class="sp-header">
          <div class="sp-header-inner">
            <button class="sp-back" onclick="closePage()">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 5l-7 7 7 7" /></svg> Back to Home
            </button>
            <div class="sp-logo-name">Mushroom<br>Bio Packaging<span>Grown, Not Made.</span></div>
            <div class="sp-breadcrumb">Home / Blog / <span>Our Journey</span></div>
          </div>
        </header>
        <div class="sp-hero">
          <h1>Our Timeline: Pioneering the Future of Sustainable Materials</h1>
          <p>A look back at how we transitioned from a wild idea to a global manufacturing standard.</p>
        </div>
        <div class="sp-body" style="max-width:800px; margin:0 auto; padding-top:40px;">
          <div class="sp-reveal" style="font-size:16px; line-height:1.8; color:#444;">
             <p>Mushroom Bio Packaging began with a simple observation: nature already knows how to build complex, durable structures without generating waste. Our founders recognized that mycelium, the vegetative part of fungi, is essentially nature's recycling system. Why couldn't we harness it to replace environmentally disastrous single-use plastics?</p>
             <p>In our early years, the challenge was scalability. We spent countless hours in the lab experimenting with different agricultural waste streams and fungal strains. We needed a combination that grew quickly, reliably, and produced a uniform density. After significant breakthroughs, we launched our first commercial product: Breakaway Corners, proving that biological materials could pass standard drop tests.</p>
             <p>As word spread, demand skyrocketed. We rapidly expanded our operations, opening our first large-scale vertical growing facility. We also introduced our global licensing program, allowing partners in Europe, Asia, and South America to grow our patented MycoComposite™ using their own local agricultural waste. Today, our timeline is defined by continuous innovation—from advanced thermal insulators for cold-chain logistics to elegant, velvet-soft luxury packaging.</p>
             <p>Looking ahead, we aim to completely displace EPS foam in high-volume industries by 2030, transforming the packaging industry from a linear waste stream into a circular, regenerative system.</p>
          </div>
        </div>
      </div>
"""

content = content.replace('    </div><!-- /subpage-overlay -->', pages_html + '\n    </div><!-- /subpage-overlay -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated learn more / read more blogs in index.html")
