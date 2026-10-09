#!/usr/bin/env python3
"""Cut the Veyan wordmark and orb icon out of the brand image (background keyed to transparency).

Usage: python3 -I tools/make_brand_assets.py <brand_image> <out_dir>
Writes veyan_logo.png (navy wordmark, transparent), veyan_logo_white.png (for dark backgrounds),
veyan_icon.png (the orb "e", transparent, square) and veyan_hero.png (the light-beam visual, no text).
"""
import sys, numpy as np
from PIL import Image, ImageFilter

src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGB")
S = 3  # upscale factor before keying, for smoother edges

def key(box, orb, force_r=0.55):
    """box: crop in source px; orb: (cx, cy, r) in source px. Returns RGBA array (upscaled)."""
    c = im.crop(box).resize(((box[2]-box[0])*S, (box[3]-box[1])*S), Image.LANCZOS)
    a = np.asarray(c).astype(float); h, w, _ = a.shape
    yy, xx = np.mgrid[0:h, 0:w]
    ocx, ocy, orr = ((orb[0]-box[0])*S, (orb[1]-box[1])*S, orb[2]*S)
    rr = np.hypot(xx-ocx, yy-ocy)
    lum = a.mean(axis=2)
    bgmask = (lum > 175) & (rr > orr*1.05)
    # quadratic background surface per channel
    X = np.stack([np.ones(bgmask.sum()), xx[bgmask], yy[bgmask], xx[bgmask]**2, yy[bgmask]**2, xx[bgmask]*yy[bgmask]], 1)
    Xa = np.stack([np.ones(h*w), xx.ravel(), yy.ravel(), xx.ravel()**2, yy.ravel()**2, (xx*yy).ravel()], 1)
    bg = np.zeros_like(a)
    for ch in range(3):
        coef, *_ = np.linalg.lstsq(X, a[..., ch][bgmask], rcond=None)
        bg[..., ch] = (Xa @ coef).reshape(h, w)
    d = np.linalg.norm(a - bg, axis=2)
    alpha = np.clip((d - 18) / 70, 0, 1)
    alpha[rr < orr*force_r] = 1.0                       # orb core is always solid
    alpha = np.asarray(Image.fromarray((alpha*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.6))).astype(float)/255
    # drop faint specks: keep only pixels connected to clearly opaque regions (dilated core)
    core = Image.fromarray(((alpha > 0.5)*255).astype(np.uint8)).filter(ImageFilter.MaxFilter(9))
    alpha[np.asarray(core) == 0] = 0
    safe = np.maximum(alpha, 1e-3)[..., None]
    fg = np.clip((a - (1-alpha[..., None])*bg) / safe, 0, 255)
    return fg, alpha, rr, orr

def save(fg, alpha, path, trim=True):
    rgba = np.dstack([fg, alpha*255]).astype(np.uint8)
    img = Image.fromarray(rgba, "RGBA")
    if trim: img = img.crop(img.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox())
    img.save(path); return img

ORB = (1050, 441, 56)
fg, al, rr, orr = key((858, 352, 1462, 522), ORB)
logo = save(fg, al, out + "/veyan_logo.png")
# white version: navy letterforms (dark, low saturation) outside the orb become white
lum = fg.mean(axis=2); sat = fg.max(axis=2) - fg.min(axis=2)
navy = (rr > orr*1.02) & (lum < 120) & (sat < 70)
fw = fg.copy(); fw[navy] = 255
save(fw, al, out + "/veyan_logo_white.png")
# icon: the orb "e"
fg, al, rr, orr = key((1050-62, 441-62, 1050+62, 441+62), ORB)
al = al * np.clip((orr*1.04 - rr) / (orr*0.06), 0, 1)   # nothing outside the orb
save(fg, al, out + "/veyan_icon.png", trim=False)
# hero visual: the light beams and sphere, cropped clear of the brand text
im.crop((200, 0, 845, 941)).save(out + "/veyan_hero.png")
print("logo", logo.size)
# narrow strip of the hero for section dividers (4.13 x 7.5 in)
hero = Image.open(out + "/veyan_hero.png"); hw, hh = hero.size; tw = int(hh * 4.13 / 7.5); x0 = (hw - tw) // 2 + 40
hero.crop((x0, 0, x0 + tw, hh)).save(out + "/veyan_hero_strip.png")
im.convert("RGB").save(out + "/veyan_brand_card.jpg", quality=92)
# the visual icon: the golden V of light beams on the glass "eye" sphere (rounded badge; it sits on a photo, so it
# is not keyed) and the full lockups (visual icon + word mark) for light and dark backgrounds
from PIL import ImageDraw
mark = im.crop((212, 152, 832, 772)).resize((800, 800), Image.LANCZOS).convert("RGBA")
m = Image.new("L", (800, 800), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, 799, 799), radius=150, fill=255)
mark.putalpha(m); mark.save(out + "/veyan_mark.png")
for word_file, name in (("veyan_logo.png", "veyan_lockup.png"), ("veyan_logo_white.png", "veyan_lockup_white.png")):
    word = Image.open(out + "/" + word_file); H = 600
    mk = mark.resize((H, H), Image.LANCZOS)
    w = word.resize((int(word.size[0] * H * 0.62 / word.size[1]), int(H * 0.62)), Image.LANCZOS)
    gap = int(H * 0.18); canvas = Image.new("RGBA", (H + gap + w.size[0], H), (0, 0, 0, 0))
    canvas.alpha_composite(mk, (0, 0)); canvas.alpha_composite(w, (H + gap, (H - w.size[1]) // 2 + int(H * 0.04)))
    canvas.save(out + "/" + name)
lk = Image.open(out + "/veyan_lockup.png"); lk.resize((int(lk.size[0] * 160 / lk.size[1]), 160), Image.LANCZOS).save(out + "/veyan_lockup_small.png", optimize=True)
lk = Image.open(out + "/veyan_lockup_white.png"); lk.resize((int(lk.size[0] * 160 / lk.size[1]), 160), Image.LANCZOS).save(out + "/veyan_lockup_white_small.png", optimize=True)
