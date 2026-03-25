import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('w-[80vw] sm:w-auto snap-center', 'w-[42vw] sm:w-auto snap-start')
content = content.replace('p-4 md:p-5', 'p-3 md:p-5')
content = content.replace('text-xs sm:text-sm font-medium mb-4', 'text-[10px] sm:text-sm font-medium mb-3 sm:mb-4')
content = content.replace('text-sm sm:text-lg drop-shadow', 'text-[11px] sm:text-lg drop-shadow')

# Match the image wrapper exactly to be safe
content = content.replace('h-[105px] sm:h-[140px] relative z-10 flex justify-center items-center mb-5', 'h-[75px] sm:h-[140px] relative z-10 flex justify-center items-center mb-3 sm:mb-5')

# Match the paragraph exactly
content = content.replace('<p class="text-slate-400 text-[10px] sm:text-xs relative z-10 pb-0 font-light leading-relaxed text-center mt-auto w-full transition-all duration-300 group-hover:text-slate-200">', '<p class="text-slate-400 text-[9px] sm:text-xs relative z-10 pb-0 font-light leading-[1.3] text-center mt-auto w-full transition-all duration-300 group-hover:text-slate-200">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Cards minified.")
