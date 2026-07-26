/**
 * ==========================================================================
 * REUSABLE WEBSITE INTERACTION & JS LOGIC
 * Includes: Sticky Header, Mobile Navigation, FAQ Accordions, Scroll Animations
 * ==========================================================================
 */

document.addEventListener('DOMContentLoaded', () => {

    // ===== HEADER SCROLL & BACK TO TOP =====
    const header = document.getElementById('site-header');
    const backToTopBtn = document.getElementById('back-to-top');

    function updateScrollState() {
        const scrollY = window.scrollY || window.pageYOffset;
        
        if (header) {
            if (scrollY > 80) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        }

        if (backToTopBtn) {
            if (scrollY > 400) {
                backToTopBtn.classList.add('is-visible');
            } else {
                backToTopBtn.classList.remove('is-visible');
            }
        }
    }

    window.addEventListener('scroll', updateScrollState, { passive: true });
    updateScrollState();

    if (backToTopBtn) {
        backToTopBtn.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // ===== MOBILE MENU DRAWER =====
    const hamburgerBtn = document.getElementById('hamburger-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileClose = document.getElementById('mobile-close');

    if (hamburgerBtn && mobileMenu) {
        hamburgerBtn.addEventListener('click', () => {
            mobileMenu.classList.add('active');
            document.body.style.overflow = 'hidden';
        });
    }

    if (mobileClose && mobileMenu) {
        mobileClose.addEventListener('click', closeMobileMenu);
    }

    function closeMobileMenu() {
        if (mobileMenu) {
            mobileMenu.classList.remove('active');
            document.body.style.overflow = '';
        }
    }

    // ===== MOBILE DROPDOWN TOGGLE =====
    const mobileDropdownToggles = document.querySelectorAll('.mobile-dropdown-toggle');
    mobileDropdownToggles.forEach(toggle => {
        toggle.addEventListener('click', function(e) {
            if (e.target.closest('.mobile-arrow')) {
                e.preventDefault();
                e.stopPropagation();
                const container = this.closest('.mobile-dropdown-container');
                const isOpen = container.classList.contains('open');

                // Close other open containers
                document.querySelectorAll('.mobile-dropdown-container.open').forEach(item => {
                    if (item !== container) item.classList.remove('open');
                });

                container.classList.toggle('open', !isOpen);
            }
        });
    });

    // ===== FAQ ACCORDION LOGIC =====
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        if (question) {
            question.addEventListener('click', () => {
                const isActive = item.classList.contains('active');

                // Close all accordion items
                faqItems.forEach(otherItem => otherItem.classList.remove('active'));

                // Toggle current item if it wasn't active
                if (!isActive) {
                    item.classList.add('active');
                }
            });
        }
    });

    // Open first FAQ by default if available
    if (faqItems.length > 0) {
        faqItems[0].classList.add('active');
    }

    // ===== SCROLL REVEAL ANIMATIONS =====
    const revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right');

    if ('IntersectionObserver' in window) {
        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    revealObserver.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.12,
            rootMargin: '0px 0px -40px 0px'
        });

        revealElements.forEach(el => revealObserver.observe(el));
    } else {
        // Fallback for older browsers
        revealElements.forEach(el => el.classList.add('visible'));
    }

    // ===== SMOOTH ANCHOR SCROLLING =====
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId && targetId !== '#') {
                const target = document.querySelector(targetId);
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                    closeMobileMenu();
                }
            }
        });
    });

});
