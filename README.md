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

If a hook modifies a file, the commit is aborted; re-stage the modified
file and commit again. To run the hooks manually across the whole repo:

```sh
pre-commit run --all-files
```

The same hooks run in CI on every PR — if you skip the local install,
CI will tell you what would have changed.
