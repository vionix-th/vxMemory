import re, pathlib, sys
p = pathlib.Path('index.html')
s = p.read_text()
# Add options
s = s.replace(
    '          <option value="shapes">Shapes</option>\n',
    '          <option value="shapes">Shapes</option>\n          <option value="thai">Thai</option>\n          <option value="dinosaur">Dinosaur</option>\n'
)
# Add CSS rule for images
s = s.replace(
    '  .front{background:var(--card-face); transform:rotateY(180deg); font-size:clamp(18px,5vmin,48px)}\n',
    '  .front{background:var(--card-face); transform:rotateY(180deg); font-size:clamp(18px,5vmin,48px)}\n  .front img{width:70%; height:70%; object-fit:contain; filter: drop-shadow(0 2px 2px rgba(0,0,0,.35));}\n'
)
# Insert new themes before end of THEMES
m = re.search(r"(const THEMES = \{[\s\S]*?shapes:\s*\[[\s\S]*?\])\s*\}\s*;", s, re.M)
if not m:
    print('Failed to locate THEMES block', file=sys.stderr)
    sys.exit(1)
base = m.group(1)
addon = ",\n    thai: [\n      'img:assets/tiles_png/thai/chili.png','img:assets/tiles_png/thai/boat.png','img:assets/tiles_png/thai/tomyum.png','img:assets/tiles_png/thai/temple.png','img:assets/tiles_png/thai/sala.png','img:assets/tiles_png/thai/elephant.png','img:assets/tiles_png/thai/durian.png','img:assets/tiles_png/thai/krathong.png','img:assets/tiles_png/thai/orchid.png','img:assets/tiles_png/thai/coconut.png','img:assets/tiles_png/thai/padthai.png','img:assets/tiles_png/thai/mango.png','img:assets/tiles_png/thai/padkrapao.png','img:assets/tiles_png/thai/umbrella.png','img:assets/tiles_png/thai/mangostickyrice.png','img:assets/tiles_png/thai/thaitea.png','img:assets/tiles_png/thai/tuktuk.png','img:assets/tiles_png/thai/ricebowl.png','img:assets/tiles_png/thai/palm.png','img:assets/tiles_png/thai/buddha.png','img:assets/tiles_png/thai/naga.png','img:assets/tiles_png/thai/drum.png','img:assets/tiles_png/thai/lotus.png','img:assets/tiles_png/thai/khonmask.png','img:assets/tiles_png/thai/rooster.png','img:assets/tiles_png/thai/bananaleaf.png','img:assets/tiles_png/thai/somtam.png'\n    ],\n    dinosaur: [\n      'img:assets/tiles_png/dinosaur/iguanodon.png','img:assets/tiles_png/dinosaur/footprint.png','img:assets/tiles_png/dinosaur/dilophosaurus.png','img:assets/tiles_png/dinosaur/parasaurolophus.png','img:assets/tiles_png/dinosaur/stegosaurus.png','img:assets/tiles_png/dinosaur/apatosaurus.png','img:assets/tiles_png/dinosaur/archaeopteryx.png','img:assets/tiles_png/dinosaur/ankylosaurus.png','img:assets/tiles_png/dinosaur/spinosaurus.png','img:assets/tiles_png/dinosaur/trex.png','img:assets/tiles_png/dinosaur/pachycephalosaurus.png','img:assets/tiles_png/dinosaur/raptor.png','img:assets/tiles_png/dinosaur/pterodactyl.png','img:assets/tiles_png/dinosaur/mosasaurus.png','img:assets/tiles_png/dinosaur/coelophysis.png','img:assets/tiles_png/dinosaur/ceratosaurus.png','img:assets/tiles_png/dinosaur/therizinosaurus.png','img:assets/tiles_png/dinosaur/allosaurus.png','img:assets/tiles_png/dinosaur/brachiosaurus.png','img:assets/tiles_png/dinosaur/egg.png','img:assets/tiles_png/dinosaur/protoceratops.png','img:assets/tiles_png/dinosaur/carnotaurus.png','img:assets/tiles_png/dinosaur/giganotosaurus.png','img:assets/tiles_png/dinosaur/triceratops.png'\n    ]\n  }"
start, end = m.span()
s = s[:start] + base + addon + s[end-1:]
# Replace card building block with image-aware version
block_re = re.compile(r"card\.dataset\.symbol = sym;\s*card\.dataset\.index = i;\s*card\.innerHTML = `[\s\S]*?<\\/div>\n\s*`;", re.M)
s = block_re.sub(
    "card.dataset.index = i;\n      if(typeof sym === 'string' && sym.startsWith('img:')){\n        const src = sym.slice(4);\n        const base = src.split('/').pop().replace(/\\.[a-zA-Z0-9]+$/, '');\n        card.dataset.symbol = base;\n        card.innerHTML = `\n          <div class=\\\"face back\\\">?</div>\n          <div class=\\\"face front\\\" aria-hidden=\\\"true\\\"><img src=\\\"${src}\\\" alt=\\\"\\\"></div>\n        `;\n      }else{\n        card.dataset.symbol = sym;\n        card.innerHTML = `\n          <div class=\\\"face back\\\">?</div>\n          <div class=\\\"face front\\\" aria-hidden=\\\"true\\\">${sym}</div>\n        `;\n      }",
    s,
    count=1
)
# Improve matched aria-label
s = s.replace(
    "first.setAttribute('aria-label', `Matched ${card.dataset.symbol}`);\n      card.setAttribute('aria-label', `Matched ${card.dataset.symbol}`);",
    "const label = card.dataset.symbol.replace(/[-_]/g,' ');\n      first.setAttribute('aria-label', `Matched ${label}`);\n      card.setAttribute('aria-label', `Matched ${label}`);"
)
p.write_text(s)
print('Patched index.html')
