# Photo booth

## Description
This script was used to simulate the process of the AI Software,
which replaces the cached image, taken with DSLRBooth, with
a new generated image, made by the AI.

First, the script watches a specific folder with "watchdog". If there is any change or an image gets added, the image gets replaced by a new one.

## Setup

- Download and Install DSLRBooth.

- First, you need to define the folder path, where the cached image gets saved, see screenshot below.

![](media/2023-12-08%2013_19_04-Window.png)

- Replace the `folder_to_watch` and `replacement_image_path` variables in the script according to your needs.

- Start the script with `python directory_watchdog.py` (start cmd as admin)

- Important: Deactivate Anti-Virus, otherwise you could get the error "permission denied".

## Developers

- Marin Sekic (marin.sekic@edu.fh-joanneum.at)
- Stefan Jovic (stefan.jovic@edu.fh-joanneum.at)