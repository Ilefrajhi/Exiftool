import sys
import exiftool
import webbrowser

def extract_metadata(image_path):
    with exiftool.ExifTool() as et:
        metadata = et.get_metadata(image_path)
    return metadata

def open_google_maps(latitude, longitude):
    """
    Open Google Maps with the provided latitude and longitude coordinates.
    
    Args:
        latitude (float): Latitude coordinate.
        longitude (float): Longitude coordinate.
    """
    google_maps_url = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"
    webbrowser.open(google_maps_url)

if __name__ == "__main__":
    if len(sys.argv) != 2:
            
      print("██████╗░██╗░░░██╗███████╗░██████╗██╗░░░██╗███████╗██████╗░░█████╗░██████╗░")
    print("██╔══██╗██║░░░██║██╔════╝██╔════╝██║░░░██║██╔════╝██╔══██╗██╔══██╗██╔══██╗")
    print("██████╦╝██║░░░██║█████╗░░╚█████╗░██║░░░██║█████╗░░██████╔╝██║░░██║██████╔╝")
    print("██╔══██╗██║░░░██║██╔══╝░░░╚═══██╗██║░░░██║██╔══╝░░██╔══██╗██║░░██║██╔═══╝░")
    print("██████╦╝╚██████╔╝███████╗██████╔╝╚██████╔╝███████╗██║░░██║╚█████╔╝██║░░░░░")
    print("╚═════╝░░╚═════╝░╚══════╝╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░░░░")
    print()
    print("Usage: exiftool_wrapper.py <image_path>")
    sys.exit(1)
    
    image_path = sys.argv[1]
    metadata = extract_metadata(image_path)
    
    # Extract latitude and longitude from metadata if available
    latitude = metadata.get("EXIF:GPSLatitude")
    longitude = metadata.get("EXIF:GPSLongitude")
    
    if latitude and longitude:
        print("Location found! Opening in Google Maps...")
        open_google_maps(latitude, longitude)
    else:
        print("Location not found in metadata.")