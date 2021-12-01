import os
import random
import sys
from pathlib import Path


def main(wallpapers_folder: Path) -> None:
    images = [
        i
        for i in wallpapers_folder.iterdir()
        if i.is_file() and i.suffix in {".jpg", ".png", ".jpeg"}
    ]
    random_image = random.choice(images)
    os.system(
        f"/usr/bin/gsettings set org.gnome.desktop.background picture-uri {str(random_image.absolute())}"
    )


if __name__ == "__main__":
    main(Path(sys.argv[1]))
