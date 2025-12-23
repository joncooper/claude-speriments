// Ghostty Explainer - Interactive Features

document.addEventListener('DOMContentLoaded', () => {
    initNavigation();
    initSmoothScrolling();
    initCodeHighlighting();
});

/**
 * Initialize navigation highlighting based on scroll position
 */
function initNavigation() {
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('.section');

    // Create intersection observer for sections
    const observerOptions = {
        root: null,
        rootMargin: '-20% 0px -60% 0px',
        threshold: 0
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                updateActiveNavLink(id);
            }
        });
    }, observerOptions);

    sections.forEach(section => {
        observer.observe(section);
    });

    // Handle click events on nav links
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            const href = link.getAttribute('href');
            if (href.startsWith('#')) {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth' });
                    updateActiveNavLink(href.substring(1));
                }
            }
        });
    });
}

/**
 * Update the active nav link
 */
function updateActiveNavLink(sectionId) {
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === `#${sectionId}`) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
}

/**
 * Initialize smooth scrolling for anchor links
 */
function initSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href.length > 1) {
                const target = document.querySelector(href);
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({ behavior: 'smooth' });

                    // Update URL without jumping
                    history.pushState(null, '', href);
                }
            }
        });
    });
}

/**
 * Simple syntax highlighting for Zig code
 */
function initCodeHighlighting() {
    const codeBlocks = document.querySelectorAll('.code-snippet code, .code-block code');

    codeBlocks.forEach(block => {
        const code = block.innerHTML;
        block.innerHTML = highlightZig(code);
    });
}

/**
 * Basic Zig syntax highlighting
 */
function highlightZig(code) {
    // Keywords
    const keywords = [
        'const', 'var', 'pub', 'fn', 'return', 'if', 'else', 'while', 'for',
        'switch', 'break', 'continue', 'try', 'catch', 'errdefer', 'defer',
        'comptime', 'inline', 'export', 'extern', 'struct', 'enum', 'union',
        'error', 'undefined', 'null', 'true', 'false', 'orelse', 'and', 'or',
        'test', 'unreachable', 'async', 'await', 'suspend', 'resume', 'noasync'
    ];

    // Types
    const types = [
        'void', 'bool', 'u8', 'u16', 'u21', 'u32', 'u64', 'usize',
        'i8', 'i16', 'i32', 'i64', 'isize', 'f32', 'f64',
        'anytype', 'type', 'noreturn', 'anyerror', 'anyframe'
    ];

    // Escape HTML first
    let result = code;

    // Highlight strings (simple approach)
    result = result.replace(/"([^"\\]|\\.)*"/g, '<span style="color: #a5d6ff;">$&</span>');

    // Highlight comments
    result = result.replace(/\/\/[^\n]*/g, '<span style="color: #8b949e; font-style: italic;">$&</span>');

    // Highlight keywords
    keywords.forEach(keyword => {
        const regex = new RegExp(`\\b(${keyword})\\b`, 'g');
        result = result.replace(regex, '<span style="color: #ff7b72;">$1</span>');
    });

    // Highlight types
    types.forEach(type => {
        const regex = new RegExp(`\\b(${type})\\b`, 'g');
        result = result.replace(regex, '<span style="color: #79c0ff;">$1</span>');
    });

    // Highlight builtins (@import, @This, etc.)
    result = result.replace(/@\w+/g, '<span style="color: #d2a8ff;">$&</span>');

    // Highlight numbers
    result = result.replace(/\b(\d+)\b/g, '<span style="color: #79c0ff;">$1</span>');

    return result;
}

/**
 * Handle hash changes for deep linking
 */
window.addEventListener('hashchange', () => {
    const hash = window.location.hash;
    if (hash) {
        const target = document.querySelector(hash);
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
            updateActiveNavLink(hash.substring(1));
        }
    }
});

/**
 * Initialize on page load with hash
 */
if (window.location.hash) {
    const hash = window.location.hash;
    const target = document.querySelector(hash);
    if (target) {
        setTimeout(() => {
            target.scrollIntoView({ behavior: 'smooth' });
            updateActiveNavLink(hash.substring(1));
        }, 100);
    }
}
