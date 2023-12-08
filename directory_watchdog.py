import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sys

class ImageHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        # Check if the created file is an image
        if event.src_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            print(f"New image created: {event.src_path}")

            # Call your script or function here
            # Example: run_script(event.src_path)

            # Replace the created image with the specified replacement image
            self.replace_image(event.src_path)
            sys.exit()

    # Define the replace_image function inside the ImageHandler class
    def replace_image(self, image_path):
        # Assuming the replacement image is named "aP9eE3.jpg"
        replacement_image_path = "C://Users//itm//Desktop//new_image//aP9eE3.jpg"

        try:
            # Read the contents of the replacement image
            with open(replacement_image_path, 'rb') as replacement_image_file:
                replacement_image_content = replacement_image_file.read()

            # Write the contents of the replacement image to the original image file
            with open(image_path, 'wb') as original_image_file:
                original_image_file.write(replacement_image_content)

            print(f"Image replaced: {image_path}")
        except Exception as e:
            print(f"Error replacing image: {e}")

if __name__ == "__main__":
    folder_to_watch = "D://Fotobox//Bilder"

    event_handler = ImageHandler()
    observer = Observer()
    observer.schedule(event_handler, path=folder_to_watch, recursive=False)

    print(f"Watching for new images in {folder_to_watch}")

    try:
        observer.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()