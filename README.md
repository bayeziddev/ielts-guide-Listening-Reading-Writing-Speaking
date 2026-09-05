# ielts-guide-Listening-Reading-Writing-Speaking
A comprehensive, article-based IELTS preparation course built on smartGenDocs. Features complete modules for IELTS Academic &amp; General Training (Listening, Reading, Writing, Speaking) with optimized MDX/Markdown documentation templates
ficial developer documentation and API reference for the Smartgen NexusLeads B2B lead discovery, verification, enrichment, outreach-draft, and Google Sheets export platform.

This documentation is authored in Markdown and built with [SmartGen Docs](https://docs.smartgentools.com/). The site is designed to be deployed as a static GitHub Pages project and can be moved to a custom documentation domain later.

## What is included

The `docs/` directory covers the platform architecture, lead lifecycle, authentication, account and BYOK APIs, discovery, enrichment, export, usage, pricing, security, Google Sheets setup, paid activation, environment bindings, data model, troubleshooting, and contribution rules. `smartgen.yml` defines the branded navigation and theme. `.github/workflows/deploy-docs.yml` builds and deploys the site on pushes to `main` or through a manual workflow run.

## Local build

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install smartgen-docs
smartgen-docs serve
```

Build the static output with:

```bash
smartgen-docs build
```

The generated site is written to `site/`. The source repository deliberately does not contain runtime API keys, service-account JSON, bearer tokens, Cloudflare secrets, or GitHub secret values.

## Deployment

Enable GitHub Pages with the **GitHub Actions** source in repository settings. The included workflow uses the official Pages artifact and deployment actions. It requires no custom repository secret for the documentation build.
