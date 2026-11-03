from __future__ import annotations

import argparse
import html
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
TEMPLATE = ROOT / "shared" / "graphics" / "trial-achievement-template.svg"
SCALE = 2
WIDTH, HEIGHT = 400, 92
FONT_PATH = Path("C:/Windows/Fonts/arialbd.ttf")


def render(number: int, title: str, total: int, svg_output: Path, png_output: Path) -> None:
    if not 1 <= number <= total:
        raise ValueError("number must be between 1 and total")

    subtitle = f"ИСПЫТАНИЕ {number} ИЗ {total}"
    title_size = min(29, int(292 * 29 / ImageFont.truetype(str(FONT_PATH), 29).getlength(title)))
    svg = TEMPLATE.read_text(encoding="utf-8")
    svg = svg.replace("{{NUMBER}}", html.escape(str(number)))
    svg = svg.replace("{{TITLE}}", html.escape(title))
    svg = svg.replace("{{TITLE_SIZE}}", str(title_size))
    svg = svg.replace("{{SUBTITLE}}", html.escape(subtitle))
    svg_output.parent.mkdir(parents=True, exist_ok=True)
    svg_output.write_text(svg, encoding="utf-8")

    s = SCALE
    badge = Image.new("RGBA", (WIDTH * s, HEIGHT * s), (0, 0, 0, 0))
    draw = ImageDraw.Draw(badge)
    draw.rounded_rectangle(
        (1 * s, 1 * s, 399 * s, 91 * s),
        radius=10 * s,
        fill=(31, 29, 17, 220),
        outline=(215, 176, 78, 235),
        width=2 * s,
    )
    draw.ellipse(
        (14 * s, 14 * s, 78 * s, 78 * s),
        fill=(211, 161, 58, 255),
        outline=(255, 224, 131, 255),
        width=3 * s,
    )
    draw.ellipse((20 * s, 20 * s, 72 * s, 72 * s), outline=(124, 85, 25, 255), width=2 * s)
    number_font = ImageFont.truetype(str(FONT_PATH), 36 * s)
    title_font = ImageFont.truetype(str(FONT_PATH), title_size * s)
    subtitle_font = ImageFont.truetype(str(FONT_PATH), 16 * s)
    draw.text((46 * s, 46 * s), str(number), anchor="mm", font=number_font, fill=(75, 47, 14, 255))
    draw.text((95 * s, 12 * s), title, font=title_font, fill=(244, 211, 136, 255))
    draw.text((96 * s, 55 * s), subtitle, font=subtitle_font, fill=(240, 229, 194, 255))
    badge = badge.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
    png_output.parent.mkdir(parents=True, exist_ok=True)
    badge.save(png_output)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--number", type=int, required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--total", type=int, default=4)
    parser.add_argument("--svg-out", type=Path, required=True)
    parser.add_argument("--png-out", type=Path, required=True)
    args = parser.parse_args()
    render(args.number, args.title, args.total, args.svg_out, args.png_out)
    print(f"Rendered badge {args.number}/{args.total}: {args.svg_out} -> {args.png_out}")


if __name__ == "__main__":
    main()
