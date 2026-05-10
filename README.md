# pearsonlab.github.io

Lab webpage

### Notes

In order to render publications into page:

1. Download citations from Google Scholar in .bib format.
1. Place in `_publications/publications.bib`
1. `. process_refs`

Everything else should just work.

## Contributing

### Local preview

The site is built by Jekyll. To preview changes locally:

```sh
bundle install
bundle exec jekyll serve --livereload
```

Then open http://localhost:4000.

### Pre-commit hooks

The repo uses [pre-commit](https://pre-commit.com) to compress images and
catch other small issues before they land. One-time setup:

```sh
pip install pre-commit
pre-commit install

# image tooling (one of these per platform):
sudo apt install jpegoptim && cargo install oxipng   # Ubuntu/Debian
brew install jpegoptim oxipng                        # macOS
npm install -g svgo
```

After that, every `git commit` will automatically:

- Compress staged JPEGs to quality 85 with `jpegoptim`
- Losslessly optimize staged PNGs with `oxipng`
- Minify staged SVGs with `svgo`
- Block any image still over 1 MB after compression, and warn on images
  between 500 KB and 1 MB (see "Image size policy" below)

If a hook modifies a file, the commit is aborted; re-stage the modified
file and commit again. To run the hooks manually across the whole repo:

```sh
pre-commit run --all-files
```

The same hooks run in CI on every PR — if you skip the local install,
CI will tell you what would have changed.

### Image size policy

To keep the repo lean, images are subject to:

- **Hard cap:** 1 MB per file (post-compression). Commits with larger
  images are blocked.
- **Soft warning:** 500 KB. Commits succeed but print a warning.

Most properly-sized lab-member photos at q=85 land in 100–300 KB. If a
figure genuinely needs to exceed 1 MB (e.g., a high-resolution research
figure where detail matters), add its repo-relative path to
`.image-size-overrides` and commit that change with a brief justification
in the commit message.
