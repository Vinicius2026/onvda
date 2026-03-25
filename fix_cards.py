import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the parent container for mobile carousel
content = content.replace(
    '<div class="bonus-cards mt-2 md:mt-8 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-5 lg:gap-6 w-full max-w-full mx-auto reveal pb-10 sm:pb-8 px-4 md:px-0">',
    '<div class="bonus-cards mt-2 md:mt-8 flex overflow-x-auto sm:grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-5 lg:gap-6 w-full max-w-full mx-auto reveal pb-10 sm:pb-8 px-4 sm:px-0 snap-x snap-mandatory scrollbar-hide py-2">'
)

# 2. Add shrink-0 w-[80vw] sm:w-auto snap-center to cards
content = content.replace(
    '<div class="card-item relative bg-gradient-to-b',
    '<div class="card-item shrink-0 w-[80vw] sm:w-auto snap-center relative bg-gradient-to-b'
)

# 3. Remove group-hover:scale-[1.05] from image parent
content = content.replace(
    'relative z-10 flex justify-center items-center mb-5 transition-transform duration-700 group-hover:scale-[1.05]',
    'relative z-10 flex justify-center items-center mb-5 transition-transform duration-700'
)

# 4. Decrease mobile height from h-[120px] to h-[105px]
content = content.replace('h-[120px] sm:h-[140px]', 'h-[105px] sm:h-[140px]')

# 5. Remove 'transform group-hover:scale-[1.15] group-hover:-translate-y-2 '
content = content.replace('transform group-hover:scale-[1.15] group-hover:-translate-y-2 ', '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Cards fixed.")
