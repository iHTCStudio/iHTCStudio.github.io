source "https://rubygems.org"

# This Gemfile mirrors GitHub Pages' bundled gems so we can build the same way locally.
gem "github-pages", group: :jekyll_plugins

# Ruby 3.4+ no longer ships csv as a default gem (Jekyll 3.x still uses it).
gem "csv"
gem "logger"
gem "base64"
gem "bigdecimal"

# Optional plugins explicitly enabled in _config.yml
group :jekyll_plugins do
  gem "jekyll-sitemap"
  gem "jekyll-seo-tag"
end

# Windows / JRuby compatibility — match the GitHub Pages template
gem "tzinfo-data", platforms: [:mingw, :x64_mingw, :mswin, :jruby]
gem "wdm", "~> 0.1.1", platforms: [:mingw, :x64_mingw, :mswin]

# JS runtime fallback for some platforms
gem "http_parser.rb", "~> 0.6.0", platforms: [:jruby]
