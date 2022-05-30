
import os
from GoogleImageScrapper import GoogleImageScraper
from patch import webdriver_executable
import PIL

if __name__ == "__main__":
    #Define file path
    webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', webdriver_executable()))
    image_path = os.path.normpath(os.path.join(os.getcwd(), 'photos'))

    search_keys= ['cradle','trundle bed', 'cellarette', 'court cupboard', 'cupboard', 'sideboard', 'vargueno', 
                  'Barcelona chair', 'basket chair', 'bath chair', 'bench', 'Brewster chair', 'Carver chair',
                  'cathedra', 'chaise longue', 'cockfighting chair', 'confidante', 'couch', 'Cromwellian chair',
                  'curule chair', 'faldstool', 'farthingale chair', 'Gainsborough chair', 'inglenook', 'klismos',
                  'ladder-back chair', 'love seat', 'Morris chair', 'ottoman', 'pew', 'platform rocker', 
                  'settee', 'settle', 'stool', 'taboret', 'throne', 'wainscot chair', 'Windsor chair', 'wing chair',
                  'armoire', 'bureau', 'cassone', 'chest of drawers', 'coffer', 'commode', 'dresser', 'wardrobe',
                  'Act of Parliament clock', 'banjo clock', 'bracket clock', 'grandfather clock', 'ogee clock', 
                  'pillar and scroll shelf clock', 'bonheur du jour', 'carrel', 'davenport', 'lectern', 'prie-dieu',
                  'rolltop desk', 'secretary', 'bookcase', 'Carlton House table', 'dining table', 'dressing table', 
                  'drop-leaf table', 'drum table', 'gateleg table', 'gueridon', 'Parsons table', 'Pembroke table',
                  'tilt-top table','scissors chair']
    #Parameters
    number_of_images = 1
    headless = False
    min_resolution=(0,0)
    max_resolution=(9999,9999)

    #Main program
    for search_key in search_keys:
        image_scrapper = GoogleImageScraper(webdriver_path,image_path,search_key,number_of_images,headless,min_resolution,max_resolution)
        image_urls = image_scrapper.find_image_urls()
        image_scrapper.save_images(image_urls)
    
    #Release resources    
    del image_scrapper