# Photo booth

## Description
This script was used to simulate the process of the AI Software,
which replaces the cached image, taken with DSLRBooth, with
a new generated image, made by the AI.

First, the script watches a specific folder with "watchdog". If there is any change or an image gets added, the image gets replaced by a new one.

DSLRBooth Process:
- Photo gets taken
- Photo is temporarely saved in specified directory (see below)
    - **Important**: Here is the only way to **manipulate the picture externally** (in our case replace with AI image) during the photo taking process! DSLR Booth also allows only 30s to do this, respectively, you have to "block" 30s with a post-processing script. Otherwise DSLR Boot skips and goes on with the process.
- After post-processing, the photo gets automatically moved to final directory (specified by DSLRBooth)

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