import pygame
from moviepy.editor import VideoFileClip

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Video Player')

# Load video using moviepy
video_path = ('lor.mp4')
clip = VideoFileClip(video_path)

# Play video using pygame
for frame in clip.iter_frames(fps=24, dtype="uint8"):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            clip.close()
            pygame.quit()
            exit()

    # Convert the frame to pygame surface
    frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
    screen.blit(frame_surface, (0, 0))
    pygame.display.update()

clip.close()
pygame.quit()
