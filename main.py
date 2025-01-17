import time, os, pygame, sys
import pyautogui, platform
from pygamehelp import Button

def open_folder(path):
    if platform.system() == "Windows":  # For Windows
        os.system(f'start "" "{path}"')
    elif platform.system() == "Darwin":  # For macOS
        os.system(f'open "{path}"')
    else:  # For Linux
        os.system(f'xdg-open "{path}"')

def print_screen():
   global directory_base
   print("Printing screenshot...")
   image = pygame.Surface(pygame.display.get_surface().get_size(), pygame.SRCALPHA)
   image.blit(screen, (0, 0))
   local_time = time.localtime()
   formatted_time = time.strftime("%Y-%m-%d_%H-%M-%S", local_time)


   try:
        file_path = os.path.join(directory_base, f"Screenshot_{formatted_time}.png")
        pyautogui.screenshot(file_path)
   except Exception as e:
       print(f"Error saving screenshot: {e}")
       return
   return formatted_time

def delete_screenshot(time):
   global directory_base
   global time_record
   print("Deleting screenshot...")
   test = time.split('_')
   if len(test) != 2:
       print(f"Invalid time format: {time}")
       return False
   try:
       file = f"Screenshot_{time}.png"
       os.remove(os.path.join(directory_base, file))
       print(f"Deleted screenshot: {file}")
       time_record.remove(time)
       return
   except Exception as e:
       print(f"Error deleting screenshot: {e}")
       return
  
directory_base = "Screenshots"
if not os.path.exists(directory_base):
   print(f"Creating directory: {directory_base}")
   os.makedirs(directory_base)

time_record = []
file_content = []
try:
    screenshot_files = os.listdir(directory_base)
    for file in screenshot_files:
        file_content = file.replace('_', '.').split('.')[1:-1]
        string = (f"{file_content[0]}_" + f"{file_content[1]}")
        time_record.append(string)
    print(time_record)
except Exception as e:
    print(f"Error reading screenshots: {e}")

#Initialize Pygame
pygame.init()

#Screen dimensions
screen_width = 500
screen_height = 50
formatted_time = None
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Better Screen Shot')

#Display the caption
caption_font = pygame.font.SysFont('Arial', 18, bold=True)
caption_text = caption_font.render('Press Space to take a screenshot', True, (0, 0, 0))
snip = Button((5,25), (105,20), text='Screenshot')
delete = Button((115,25), (60,20), text='Delete')
new_screen= Button((180,25), (155,20), text='See Screenshots')


#Main loop
while __name__ == '__main__':
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
       elif event.type == pygame.MOUSEBUTTONDOWN:
           if snip.update(screen):
               formatted_time = print_screen()
               time_record.append(formatted_time)

           elif delete.update(screen):
               if len(time_record) > 0:
                   delete_screenshot(time_record[-1])

           elif new_screen.update(screen):
               print("Opening screenshot folder")
               path = (os.path.dirname(os.path.abspath(__file__)) +"\Screenshots")
               open_folder(path)
               time.sleep(5)
              
   #Set the background color
   screen.fill((250, 250, 255))
   screen.blit(caption_text, (5, 5))
   snip.update(screen)
   delete.update(screen)
   new_screen.update(screen)
   pygame.display.update()



