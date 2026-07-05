#!/bin/bash
# Run this once from your project folder (where index.html lives) in Termux.
# It downloads all site photos into an images/ folder so nothing is hotlinked.
# All photos are free to use under the Unsplash License (no attribution required).

mkdir -p images

curl -L -o images/hero-workspace.jpg   "https://images.unsplash.com/photo-1752223638233-4c9545333f89?fm=jpg&q=80&w=1600&auto=format&fit=crop"
curl -L -o images/ecommerce.jpg        "https://images.unsplash.com/photo-1573164713712-03790a178651?fm=jpg&q=80&w=1200&auto=format&fit=crop"
curl -L -o images/branding-flatlay.jpg "https://images.unsplash.com/photo-1764818958908-d5efcec563d1?fm=jpg&q=80&w=1200&auto=format&fit=crop"
curl -L -o images/mobile-app.jpg       "https://images.unsplash.com/photo-1573164574230-db1d5e960238?fm=jpg&q=80&w=1200&auto=format&fit=crop"
curl -L -o images/ux-sketchbook.jpg    "https://images.unsplash.com/photo-1540612597331-63c67ea382fc?fm=jpg&q=80&w=1600&auto=format&fit=crop"
curl -L -o images/content-writing.jpg  "https://images.unsplash.com/photo-1573164713988-8665fc963095?fm=jpg&q=80&w=1200&auto=format&fit=crop"
curl -L -o images/brand-strategy.jpg   "https://images.unsplash.com/photo-1573164574572-cb89e39749b4?fm=jpg&q=80&w=1200&auto=format&fit=crop"
curl -L -o images/social-media.jpg     "https://images.unsplash.com/photo-1759215524600-7971d6a4dac0?fm=jpg&q=80&w=1200&auto=format&fit=crop"

echo "Done. Check the images/ folder before committing."
