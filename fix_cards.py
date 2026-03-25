import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the outer card to look more professional
outer_card_pattern = r'class="card-item relative bg-\[#0A1225\] rounded-\[18px\] md:rounded-2xl p-3 md:p-4 border border-white/10 flex flex-col transition-all duration-500 shadow-\[0_8px_35px_rgba\(0,0,0,0\.35\)\] hover:shadow-\[0_10px_40px_(rgba\([^\)]+\))\] hover:-translate-y-1 transform-gpu group overflow-hidden"'
outer_card_repl = r'class="card-item relative bg-gradient-to-b from-[#111A2C] to-[#0A1225] rounded-[18px] md:rounded-2xl p-4 md:p-5 border border-white/5 flex flex-col transition-all duration-500 shadow-xl hover:shadow-[0_20px_40px_\1] hover:-translate-y-2 transform-gpu group overflow-hidden"'
content = re.sub(outer_card_pattern, outer_card_repl, content)

# 2. Add an inner gradient glow right after the start of the card
def add_inner_glow(match):
    color = match.group(1)
    if 'cyan' in color: color_str = 'cyan-400'
    elif 'blue' in color: color_str = 'blue-400'
    else: color_str = color
    return match.group(0) + f'\n                        <div class="absolute inset-0 bg-gradient-to-b from-{color_str}/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700 z-0 pointer-events-none"></div>'
    
glow_pattern = re.compile(r'(<div\s+class="absolute -top-10 -right-10 w-24 h-24 bg-([^/]+)/10 rounded-full blur-\[40px\] pointer-events-none group-hover:bg-[^/]+/20 transition-colors duration-500">\s*</div>)')
content = glow_pattern.sub(add_inner_glow, content)

# 3. Replace the image container to have the same size and pure images
img_container_pattern = r'<!-- Image Container -->\s*<div\s+class="w-\[78%\] sm:w-\[70%\] mx-auto aspect-\[4/3\] sm:aspect-square bg-\[#0B0F19\]/60 rounded-\[10px\] mb-2 sm:mb-3 relative z-10 flex flex-col items-center justify-center border border-white/5 backdrop-blur-sm p-0\.5 shadow-inner overflow-hidden group-hover:border-([^/]+)/20 transition-colors duration-500">\s*<img src="([^"]+)" alt="([^"]+)"\s+class="w-full h-full object-contain filter drop-shadow-\[0_4px_12px_rgba\(0,0,0,0\.5\)\] transform group-hover:scale-\[1\.10\] transition-transform duration-700 ease-\[cubic-bezier\(0\.19,1,0\.22,1\)\]">\s*</div>'

img_container_repl = r'''<!-- Image Container (Pure, same size) -->
                        <div class="w-full h-[120px] sm:h-[150px] relative z-10 flex justify-center items-center mb-4 transition-transform duration-700 group-hover:scale-[1.05]">
                            <!-- Glowing halo behind pure image -->
                            <div class="absolute inset-0 bg-\1/0 group-hover:bg-\1/20 blur-2xl rounded-full transition-all duration-700 transform scale-50 group-hover:scale-110 opacity-0 group-hover:opacity-100 pointer-events-none"></div>
                            <img src="\2" alt="\3"
                                class="w-full h-full object-contain mix-blend-screen transform group-hover:scale-[1.20] group-hover:-translate-y-2 transition-all duration-700 ease-[cubic-bezier(0.34,1.56,0.64,1)] relative z-10 filter brightness-110 contrast-125 drop-shadow-[0_10px_15px_rgba(0,0,0,0.8)]">
                        </div>'''
content = re.sub(img_container_pattern, img_container_repl, content)

# 4. Enhance typography hover effects
h4_pattern = r'(<h4[^>]+text-slate-100 [^>]+>)([\s\S]*?)(</strong>\s*</h4>)'
h4_repl = r'\1\2 transition-all duration-300 group-hover:drop-shadow-[0_4px_15px_currentColor]\3'
content = re.sub(h4_pattern, h4_repl, content)

# Make the title text transition smoothly
content = content.replace("text-slate-100 tracking-wide", "text-slate-300 group-hover:text-white transition-colors duration-300 tracking-wide")

# Give bottom border a sliding transition effect
bot_border_pattern = r'(class="absolute bottom-0 left-1/2 -translate-x-1/2 w-6 sm:w-10 h-1 bg-([^ ]+) rounded-t-full shadow-\[[^\]]+\] opacity-80 group-hover:opacity-100) group-hover:w-12 sm:group-hover:w-20 transition-all duration-500"'
bot_border_repl = r'class="absolute bottom-0 left-0 w-full h-[2px] bg-gradient-to-r from-transparent via-\2/60 to-transparent transform scale-x-0 group-hover:scale-x-100 transition-transform duration-700 ease-out origin-center opacity-80 group-hover:opacity-100"'
content = re.sub(bot_border_pattern, bot_border_repl, content)

# Enhance description text color gracefully
desc_text_pattern = r'(class="text-slate-400 text-\[9px\] sm:text-\[10px\] relative z-10 pb-1\.5 font-light leading-tight text-center mt-auto w-full drop-shadow-\[[^\]]+\] transition-all duration-300 group-hover:drop-shadow-\[[^\]]+\]) group-hover:text-white"'
desc_text_repl = r'\1 group-hover:text-slate-200"'
content = re.sub(desc_text_pattern, desc_text_repl, content)

# Reduce the inner padding bottom since bottom margin is higher
content = content.replace('pb-1.5', 'pb-0')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Modification complete!")
