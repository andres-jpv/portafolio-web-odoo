// Portfolio Website — Dark/Light Mode Toggle
// Uses data-pf-theme attribute on .pf-wrapper element

(function () {
    'use strict';

    const STORAGE_KEY = 'portfolio-theme';
    const ATTR = 'data-pf-theme';

    function getWrapper() {
        return document.querySelector('.pf-wrapper');
    }

    function applyTheme(theme) {
        const wrapper = getWrapper();
        if (wrapper) {
            wrapper.setAttribute(ATTR, theme);
        }
        // Update toggle button icon/label
        const btn = document.getElementById('pf-theme-toggle');
        if (btn) {
            if (theme === 'dark') {
                btn.innerHTML = '&#9728; Modo Claro';
                btn.setAttribute('title', 'Cambiar a modo claro');
            } else {
                btn.innerHTML = '&#9790; Modo Oscuro';
                btn.setAttribute('title', 'Cambiar a modo oscuro');
            }
        }
    }

    function toggleTheme() {
        const wrapper = getWrapper();
        if (!wrapper) return;
        const current = wrapper.getAttribute(ATTR) || 'light';
        const next = current === 'dark' ? 'light' : 'dark';
        localStorage.setItem(STORAGE_KEY, next);
        applyTheme(next);
    }

    function init() {
        // Apply saved theme immediately (before page render)
        const saved = localStorage.getItem(STORAGE_KEY) || 'light';
        applyTheme(saved);

        // Bind toggle button
        const btn = document.getElementById('pf-theme-toggle');
        if (btn) {
            btn.addEventListener('click', toggleTheme);
        }
    }

    // Run on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
