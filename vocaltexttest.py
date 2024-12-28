import pyttsx3
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("robotto")

    

# Initialize the TTS engine
engine = pyttsx3.init()

# Get and set the properties
rate = engine.getProperty('rate')   # Get the current speaking rate
engine.setProperty('rate', 100)     # Set the new speaking rate

voices = engine.getProperty('voices')  # Get the available voices
engine.setProperty('voice', voices[2].id)  # Set the voice (0 for male, 1 for female)

# Define a function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Example usage
speak("Hello, how are you doing today?")
def function():
    while True:
        inputo = input("speak:")
        speak(inputo)
function()





# Main loop
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