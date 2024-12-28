import pyttsx3
import pygame
import sys
#every mentioning of pygame in the code was a failed attempt to give the robot a cute fac
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("robotto")

    

engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', 100)

voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[2].id)  

def speak(text):
    engine.say(text)
    engine.runAndWait()


speak("Hello, how are you doing today?")
def function():
    while True:
        inputo = input("speak:")
        speak(inputo)
function()




def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_square()

    pygame.quit()
    sys.exit()

# Run the main loop
main()
