// Portfolio Website — Dark/Light Mode Toggle
// Uses data-pf-theme attribute on .pf-wrapper element

(function () {
    'use strict';

    const STORAGE_KEY = 'portfolio-theme';
    const ATTR = 'data-pf-theme';
    const DEFAULT_THEME = 'dark';

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
                btn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 18a6 6 0 1 1 0-12 6 6 0 0 1 0 12zm0-2a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM11 1h2v3h-2V1zm0 19h2v3h-2v-3zM3.515 4.929l1.414-1.414L7.05 5.636 5.636 7.05 3.515 4.929zm13.021 13.021l1.414-1.414 2.121 2.121-1.414 1.414-2.121-2.121zM1 11h3v2H1v-2zm19 0h3v2h-3v-2zM4.929 20.485l-1.414-1.414 2.121-2.121 1.414 1.414-2.121 2.121zm13.021-13.021l-1.414-1.414 2.121-2.121 1.414 1.414-2.121 2.121z"/></svg> Modo Claro';
                btn.setAttribute('title', 'Cambiar a modo claro');
            } else {
                btn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 3a9 9 0 1 0 9 9c0-.46-.04-.92-.1-1.36a5.389 5.389 0 0 1-4.4 2.26 5.403 5.403 0 0 1-3.14-9.8c-.44-.06-.9-.1-1.36-.1z"/></svg> Modo Oscuro';
                btn.setAttribute('title', 'Cambiar a modo oscuro');
            }
        }
    }

    function toggleTheme() {
        const wrapper = getWrapper();
        if (!wrapper) return;
        const current = wrapper.getAttribute(ATTR) || DEFAULT_THEME;
        const next = current === 'dark' ? 'light' : 'dark';
        localStorage.setItem(STORAGE_KEY, next);
        applyTheme(next);
    }

    function init() {
        // Apply saved theme (default: dark)
        const saved = localStorage.getItem(STORAGE_KEY) || DEFAULT_THEME;
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
