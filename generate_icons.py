#!/usr/bin/env python3
"""
Script pour générer automatiquement toutes les tailles d'icônes
nécessaires pour la PWA مطبخ النكهات

Utilisation :
    python generate_icons.py input_image.png

Nécessite : Pillow (PIL)
Installation : pip install Pillow
"""

import sys
import os
from PIL import Image, ImageDraw, ImageFont

# Tailles d'icônes requises
ICON_SIZES = [72, 96, 128, 144, 152, 192, 384, 512]

def create_default_icon(size):
    """Crée une icône par défaut avec le design مطبخ النكهات"""
    
    # Créer l'image avec dégradé
    img = Image.new('RGB', (size, size))
    draw = ImageDraw.Draw(img)
    
    # Créer un dégradé rouge-orange
    for y in range(size):
        # Interpolation entre rouge (#c84a31) et orange (#e8a05d)
        ratio = y / size
        r = int(200 + (232 - 200) * ratio)
        g = int(74 + (160 - 74) * ratio)
        b = int(49 + (93 - 49) * ratio)
        draw.line([(0, y), (size, y)], fill=(r, g, b))
    
    # Ajouter un cercle blanc au centre
    circle_size = int(size * 0.6)
    circle_pos = (size - circle_size) // 2
    draw.ellipse(
        [circle_pos, circle_pos, circle_pos + circle_size, circle_pos + circle_size],
        fill='white',
        outline=None
    )
    
    # Ajouter emoji (approximatif)
    try:
        # Essayer d'ajouter du texte
        font_size = int(size * 0.4)
        draw.text(
            (size // 2, size // 2),
            '🍽️',
            fill='#c84a31',
            anchor='mm'
        )
    except:
        # Si l'emoji ne fonctionne pas, dessiner un simple cercle coloré
        inner_circle_size = int(size * 0.3)
        inner_circle_pos = (size - inner_circle_size) // 2
        draw.ellipse(
            [inner_circle_pos, inner_circle_pos, 
             inner_circle_pos + inner_circle_size, inner_circle_pos + inner_circle_size],
            fill='#c84a31'
        )
    
    return img

def resize_image(input_path, output_dir='icons'):
    """Redimensionne l'image source vers toutes les tailles requises"""
    
    # Créer le dossier de sortie
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        # Ouvrir l'image source
        img = Image.open(input_path)
        img = img.convert('RGBA')
        
        print(f"✓ Image source chargée : {input_path}")
        print(f"  Taille originale : {img.size}")
        
    except FileNotFoundError:
        print(f"✗ Fichier non trouvé : {input_path}")
        print("  Création d'icônes par défaut...")
        img = None
    
    # Générer toutes les tailles
    for size in ICON_SIZES:
        output_path = os.path.join(output_dir, f'icon-{size}x{size}.png')
        
        if img:
            # Redimensionner l'image source
            resized = img.resize((size, size), Image.Resampling.LANCZOS)
        else:
            # Créer une icône par défaut
            resized = create_default_icon(size)
        
        # Sauvegarder
        resized.save(output_path, 'PNG', optimize=True)
        print(f"✓ Créé : {output_path}")
    
    # Créer aussi favicon.ico
    if img:
        favicon_sizes = [(16, 16), (32, 32), (48, 48)]
        favicon_images = [img.resize(size, Image.Resampling.LANCZOS) for size in favicon_sizes]
    else:
        favicon_images = [create_default_icon(size[0]) for size in [(16, 16), (32, 32), (48, 48)]]
    
    favicon_path = os.path.join(output_dir, 'favicon.ico')
    favicon_images[0].save(
        favicon_path,
        format='ICO',
        sizes=[(16, 16), (32, 32), (48, 48)]
    )
    print(f"✓ Créé : {favicon_path}")
    
    print(f"\n🎉 Terminé ! {len(ICON_SIZES) + 1} icônes générées dans {output_dir}/")

def main():
    print("=" * 60)
    print("  Générateur d'Icônes PWA - مطبخ النكهات")
    print("=" * 60)
    print()
    
    if len(sys.argv) > 1:
        input_path = sys.argv[1]
        resize_image(input_path)
    else:
        print("Aucune image source fournie.")
        print("Création d'icônes par défaut avec le design مطبخ النكهات...")
        print()
        
        # Créer des icônes par défaut
        output_dir = 'icons'
        os.makedirs(output_dir, exist_ok=True)
        
        for size in ICON_SIZES:
            output_path = os.path.join(output_dir, f'icon-{size}x{size}.png')
            icon = create_default_icon(size)
            icon.save(output_path, 'PNG', optimize=True)
            print(f"✓ Créé : {output_path}")
        
        print(f"\n🎉 Terminé ! {len(ICON_SIZES)} icônes par défaut créées dans {output_dir}/")
        print()
        print("💡 Pour utiliser votre propre image :")
        print("   python generate_icons.py votre_image.png")

if __name__ == '__main__':
    main()
