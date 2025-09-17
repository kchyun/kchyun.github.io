// -----------------------------
// 🖼️ Click-to-zoom Lightbox
// -----------------------------
const lightbox = document.createElement('div');
lightbox.className = 'lightbox-overlay';
lightbox.setAttribute('role', 'dialog');
lightbox.setAttribute('aria-modal', 'true');
lightbox.innerHTML = '<img alt="Expanded image">';
document.body.appendChild(lightbox);
const lightboxImg = lightbox.querySelector('img');

function openLightbox(src, alt) {
    console.log('Opening lightbox with src:', src, 'alt:', alt);
    lightboxImg.src = src;
    lightboxImg.alt = alt || '';
    lightbox.classList.add('active');
    document.body.classList.add('no-scroll');
    console.log('Lightbox should now be visible');
}

function closeLightbox() {
    console.log('Closing lightbox');
    lightbox.classList.remove('active');
    document.body.classList.remove('no-scroll');
    lightboxImg.src = '';
}

lightbox.addEventListener('click', closeLightbox);
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && lightbox.classList.contains('active')) closeLightbox();
});

// Initialize lightbox functionality
function initLightbox() {
    console.log('Initializing lightbox...');
    const images = document.querySelectorAll('.image-container');
    console.log('Found', images.length, 'images with .image-container class');
    
    images.forEach((img, index) => {
        console.log('Setting up image', index, img.src);
        img.classList.add('zoomable');
        // Prevent Magnific Popup from handling these images
        img.style.pointerEvents = 'auto';
        
        // Remove any existing click listeners to avoid duplicates
        img.removeEventListener('click', handleImageClick);
        img.addEventListener('click', handleImageClick);
    });
}

function handleImageClick(e) {
    e.preventDefault();
    e.stopPropagation();
    console.log('Image clicked!');
    const src = e.target.getAttribute('data-fullsrc') || e.target.currentSrc || e.target.src;
    console.log('Opening lightbox with src:', src);
    openLightbox(src, e.target.alt);
}

// Multiple initialization strategies to ensure it works
function tryInit() {
    console.log('Attempting to initialize lightbox...');
    initLightbox();
}

// Strategy 1: Immediate execution if DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', tryInit);
} else {
    // DOM is already ready
    tryInit();
}

// Strategy 2: jQuery ready (if available)
if (typeof $ !== 'undefined') {
    $(document).ready(function() {
        console.log('jQuery ready - initializing lightbox');
        setTimeout(tryInit, 100);
    });
}

// Strategy 3: Window load (fallback)
window.addEventListener('load', function() {
    console.log('Window loaded - trying to initialize lightbox');
    setTimeout(tryInit, 200);
});

// Strategy 4: Periodic check (last resort)
let attempts = 0;
const maxAttempts = 10;
const interval = setInterval(() => {
    attempts++;
    console.log('Periodic check attempt', attempts);
    const images = document.querySelectorAll('.image-container');
    if (images.length > 0) {
        console.log('Found images, initializing lightbox');
        initLightbox();
        clearInterval(interval);
    } else if (attempts >= maxAttempts) {
        console.log('Max attempts reached, stopping periodic checks');
        clearInterval(interval);
    }
}, 500);
