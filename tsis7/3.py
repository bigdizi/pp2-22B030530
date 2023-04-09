import pygame
pygame.init()

W = 745
H = 559
FPS = 20

clock = pygame.time.Clock()

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("I will never lose the love for the arriving, but I'm born to leave")
muller = pygame.image.load(r"C:\Users\Acer\OneDrive\Documents\MyGit\tsis7\muller_heaphones.jpg")
sc.blit(muller, (0, 0))
pygame.display.update()

sweethomePath = r"C:\Users\Acer\OneDrive\Documents\MyGit\tsis7\music\Abigail-Barro-Sweet-home.ogg"
deependPath = r"C:\Users\Acer\OneDrive\Documents\MyGit\tsis7\music\Deep-end.ogg"
boiybulganPath = r"C:\Users\Acer\OneDrive\Documents\MyGit\tsis7\music\dudeontheguitar-MONRO-boiy-bulgan.ogg"
platinaPath = r"C:\Users\Acer\OneDrive\Documents\MyGit\tsis7\music\Jakomo-Platina.ogg"
lovePath = r"C:\Users\Acer\OneDrive\Documents\MyGit\tsis7\music\LOVE.ogg"
musicalfictionPath = r"C:\Users\Acer\OneDrive\Documents\MyGit\tsis7\music\Musical_Fiction-Rudy_Mancuso.ogg"
sonnyboyPath = r"C:\Users\Acer\OneDrive\Documents\MyGit\tsis7\music\Sonny_Boy.ogg"

sweethome = pygame.mixer.music.load(sweethomePath)
musicList = [sweethomePath, deependPath, boiybulganPath, platinaPath, lovePath, musicalfictionPath, sonnyboyPath]
pygame.mixer.music.play(-1)

flPlay = False
index = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flPlay = not flPlay
                if flPlay:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                index += 1
                if index == len(musicList):
                    index = 0
                pygame.mixer.music.load(musicList[index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                index -= 1
                if index == -1:
                    index = len(musicList)-1
                pygame.mixer.music.load(musicList[index])
                pygame.mixer.music.play()

    clock.tick(FPS)