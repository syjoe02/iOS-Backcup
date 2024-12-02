from PIL import Image, ExifTags

def check_exif(file_path):
    img = Image.open(file_path)
    exif_data = img._getexif()

    if exif_data:
        for tag, value in ExifTags.TAGS.items():
            # print(f"tag: {tag} and value: {value}")
            
            if value == "DateTime":
                print(f"Original Date: {exif_data.get(tag)}")
    else:
        print("No EXIF file")

# Enter the pictures
path = "./IMG_2434.JPG"
check_exif(path)
