document.addEventListener('DOMContentLoaded', () => {

    // --- Mobile Menu Drawer Logic ---
    const mobileBtn = document.getElementById('mobile-menu-btn');
    const closeBtn = document.getElementById('close-drawer-btn');
    const mobileDrawer = document.getElementById('mobile-drawer');
    const mobileOverlay = document.getElementById('mobile-overlay');
    const mobileLinks = document.querySelectorAll('.mobile-link');
    let isMenuOpen = false;

    const toggleMenu = () => {
        isMenuOpen = !isMenuOpen;

        // Toggle Hamburger lines to 'X' (Premium asymmetrical X for right-aligned)
        const spans = mobileBtn.querySelectorAll('span');
        if (isMenuOpen) {
            spans[0].style.transform = 'rotate(-45deg) translate(-6px, 6px)';
            spans[0].style.width = '24px';
            spans[1].style.opacity = '0';
            spans[1].style.transform = 'translateX(10px)';
            spans[2].style.transform = 'rotate(45deg) translate(-5px, -5px)';
            spans[2].style.width = '24px';

            // Open Drawer
            mobileDrawer.style.transform = 'translateX(0)';

            // Show overlay & disable scroll
            mobileOverlay.style.opacity = '1';
            mobileOverlay.style.pointerEvents = 'auto';
            document.body.style.overflow = 'hidden';

        } else {
            spans[0].style.transform = 'none';
            spans[0].style.width = '24px'; // original class w-6
            spans[1].style.opacity = '1';
            spans[1].style.transform = 'none';
            spans[1].style.width = '32px'; // original class w-8
            spans[2].style.transform = 'none';
            spans[2].style.width = '20px'; // original class w-5

            // Close Drawer
            mobileDrawer.style.transform = 'translateX(-100%)';

            // Hide overlay & enable scroll
            mobileOverlay.style.opacity = '0';
            mobileOverlay.style.pointerEvents = 'none';
            document.body.style.overflow = '';
        }
    };

    if (mobileBtn && mobileDrawer && mobileOverlay) {
        mobileBtn.addEventListener('click', toggleMenu);
        if (closeBtn) closeBtn.addEventListener('click', toggleMenu);
        mobileOverlay.addEventListener('click', toggleMenu);

        // Auto-close menu when a link is clicked
        mobileLinks.forEach(link => {
            link.addEventListener('click', toggleMenu);
        });
    }

    // --- Reveal Animation Logic --- 
    const reveals = document.querySelectorAll('.reveal');

    const revealOnScroll = () => {
        const windowHeight = window.innerHeight;
        const elementVisible = 100;

        reveals.forEach((element) => {
            const elementTop = element.getBoundingClientRect().top;
            if (elementTop < windowHeight - elementVisible) {
                element.classList.add('active');
            }
        });
    };

    window.addEventListener('scroll', revealOnScroll, { passive: true });
    revealOnScroll(); // Trigger once on load

    // --- Hero Canvas Sequence Animation ---
    const canvas = document.getElementById('hero-canvas');
    if (!canvas) return;

    const context = canvas.getContext('2d');
    const heroContainer = document.getElementById('hero-scroll-container');

    // Config: 80 frames (from 000 to 079)
    const frameCount = 40;
    const images = [];

    // Set internal canvas resolution to standard 1080p horizontal layout
    canvas.width = 1920;
    canvas.height = 1080;

    const getFramePath = index => (
        `./banner home vda astronauta 1/Astronaut_standing_in_ocean_delpmaspu__${index.toString().padStart(3, '0')}.webp`
    );

    const preloadImages = () => {
        for (let i = 0; i < frameCount; i++) {
            const img = new Image();
            img.src = getFramePath(i);

            // Draw first frame instantly
            if (i === 0) {
                img.onload = () => {
                    context.drawImage(img, 0, 0, canvas.width, canvas.height);
                };
            }
            images.push(img);
        }
    };

    let activeFrameIndex = 0;
    const drawFrame = (index) => {
        if (!images[index] || activeFrameIndex === index) return;
        // Verify it's actually loaded before painting
        if (images[index].complete && images[index].naturalHeight !== 0) {
            context.drawImage(images[index], 0, 0, canvas.width, canvas.height);
            activeFrameIndex = index;
        }
    };

    const overlay = document.getElementById('hero-overlay');
    const heroBgWrapper = document.getElementById('hero-bg-wrapper');

    // Calculate frame based on vertical scroll
    const updateScrollAnimation = () => {
        if (!heroContainer) return;

        // Prevent negative values from iOS bounce effect
        const scrollTop = Math.max(0, window.scrollY);
        const isMobile = window.innerWidth < 768;

        // Stretch the scroll distance on mobile so a single swipe doesn't rush all 40 frames
        const scrollMultiplier = isMobile ? 1.5 : 0.8;
        const maxScroll = Math.max(window.innerHeight * scrollMultiplier, 600);

        // Progress bounded from 0 to 1
        let scrollFraction = scrollTop / maxScroll;
        scrollFraction = Math.max(0, Math.min(1, scrollFraction));

        // Match fraction to total frames
        const frameIndex = Math.min(
            frameCount - 1,
            Math.floor(scrollFraction * frameCount)
        );

        drawFrame(frameIndex);

        // Darken overlay as the user scrolls (from 40% up to 95%) 
        // to smoothly transition into the next dark section
        if (overlay) {
            const currentOpacity = 0.4 + (scrollFraction * 0.55);
            overlay.style.backgroundColor = `rgba(11, 15, 25, ${currentOpacity})`;
        }

        // Apply smooth parallax effect
        // Disable parallax transform on mobile to prevent extreme GPU repaint lag mixed with Canvas drawing
        if (heroBgWrapper) {
            if (isMobile) {
                heroBgWrapper.style.transform = `translate3d(0, 0, 0)`;
            } else {
                heroBgWrapper.style.transform = `translate3d(0, ${scrollTop * 0.4}px, 0)`;
            }
        }
    };

    // Initialize Video Scrub
    preloadImages();

    // Use requestAnimationFrame on scroll for 60fps performance
    let ticking = false;
    window.addEventListener('scroll', () => {
        if (!ticking) {
            window.requestAnimationFrame(() => {
                updateScrollAnimation();
                ticking = false;
            });
            ticking = true;
        }
    }, { passive: true });

});
