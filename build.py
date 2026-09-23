# Copyright (c) 2026 Sayad Md Bayezid Hosan (Smartgen Platform)
import os
import shutil
from smartgen_docs.core import Builder


def remove_multi_style_switcher(output_dir):
    """Keep the configured Book/Writer style as the only site style.

    SmartGenDocs' shared style-switcher exposes every installed theme. This
    learner site intentionally uses only the Book theme, so remove that
    optional UI block from the generated pages while keeping Book's Day/Night
    reading-mode control.
    """
    marker = '<div class="style-switcher" id="style-switcher">'
    end_marker = '</script>\n</body>'
    for root, _, files in os.walk(output_dir):
        for filename in files:
            if not filename.endswith('.html'):
                continue
            path = os.path.join(root, filename)
            with open(path, 'r', encoding='utf-8') as handle:
                html = handle.read()
            start = html.find(marker)
            if start == -1:
                continue
            end = html.find(end_marker, start)
            if end == -1:
                raise RuntimeError(f"Could not locate style switcher ending in {path}")
            updated = html[:start] + html[end + len('</script>'):]
            with open(path, 'w', encoding='utf-8') as handle:
                handle.write(updated)


def fix_mobile_navigation(output_dir):
    """Keep the open Book drawer above the dimmer on touch screens."""
    candidates = (
        os.path.join(output_dir, 'static', 'book', 'css', 'book.css'),
        os.path.join(output_dir, 'static', 'css', 'book.css'),
    )
    css_path = next((path for path in candidates if os.path.exists(path)), None)
    if css_path is None:
        return
    override = """
/* IELTS project override: the drawer must remain above its mobile dimmer. */
@media (max-width: 980px) {
    /* The sidebar is inside .book-shell; raise the parent stacking context,
       otherwise a child z-index cannot escape an overlay sibling. */
    .book-sidebar-overlay { z-index: 900 !important; }
    .book-shell { position: relative; z-index: 1000 !important; }
    .book-sidebar,
    .book-sidebar.open { z-index: 1001 !important; pointer-events: auto !important; }
    .book-sidebar .book-nav,
    .book-sidebar .book-nav-link { pointer-events: auto !important; touch-action: manipulation; }
    .book-shell:has(.book-sidebar.open) .book-main { opacity: .45; pointer-events: none; }
}
"""
    with open(css_path, 'a', encoding='utf-8') as handle:
        handle.write(override)


def fix_day_night_toggle(output_dir):
    """Make the Book toolbar icon a reliable one-tap Day/Night toggle."""
    script = """
<script>
(function () {
    const button = document.getElementById('theme-toggle');
    const menu = document.getElementById('theme-menu');
    if (!button) return;
    button.addEventListener('click', function () {
        const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
        const next = isDark ? 'light' : 'dark';
        if (next === 'light') document.documentElement.removeAttribute('data-theme');
        else document.documentElement.setAttribute('data-theme', 'dark');
        try { localStorage.setItem('smartgen-theme', next); } catch (e) { /* ignore */ }
        if (menu) menu.hidden = true;
        button.setAttribute('aria-label', next === 'dark' ? 'Switch to Day mode' : 'Switch to Night mode');
    });
})();
</script>
"""
    for root, _, files in os.walk(output_dir):
        for filename in files:
            if filename.endswith('.html'):
                path = os.path.join(root, filename)
                with open(path, 'r', encoding='utf-8') as handle:
                    html = handle.read()
                html = html.replace('</body>', script + '</body>')
                with open(path, 'w', encoding='utf-8') as handle:
                    handle.write(html)

def main():
    config_file = "smartgen.yml"
    output_dir = "site"
    
    print(f"Building documentation with Book theme...")
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Configuration file {config_file} not found!")
        
    # Shudhumatro core builder config path diye initialize kora hocche
    builder = Builder(
        config_path=config_file, 
        site_dir=output_dir
    )
    
    builder.build()
    # SmartGen builds Markdown pages but does not copy custom documentation assets.
    # Keep learner-facing diagrams available at the same relative URLs used in Markdown.
    image_source = os.path.join("docs", "images")
    image_target = os.path.join(output_dir, "images")
    if os.path.isdir(image_source):
        shutil.copytree(image_source, image_target, dirs_exist_ok=True)
    fix_mobile_navigation(output_dir)
    remove_multi_style_switcher(output_dir)
    fix_day_night_toggle(output_dir)
    print(f"Build successfully completed with Book theme in '{output_dir}/'!")

if __name__ == "__main__":
    main()
