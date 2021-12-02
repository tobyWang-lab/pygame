#sprite->遊戲中的元素
import pygame

FPS = 60
WIDTH=500
HEIGHT=600

WHITE=(255,255,255)
GREEN=(0,255,0)

# 遊戲初始化
pygame.init()

# 創建遊戲視窗，pygame.display.set_mode((寬度,高度))
screen=pygame.display.set_mode((WIDTH,HEIGHT))

#編輯遊戲視窗上方名稱
pygame.display.set_caption("第一個遊戲")

# 對時間進行管控
clock=pygame.time.Clock()

# 設定遊戲中的物件
class Player(pygame.sprite.Sprite):
    def __init__(self):
        # call sprite內建初始涵式
        pygame.sprite.Sprite.__init__(self)
        # 定義所需顯示的圖片，下圖為pygame預設的平面 
        self.image=pygame.Surface((50,40))
        self.image.fill(GREEN)
        # 定位圖片位置，將圖片框起來 
        self.rect=self.image.get_rect()
        # 設定圖片位置，下方xy為圖片左上角的座標，整個遊戲框架的左上角為(0,0)
        self.rect.x=200
        self.rect.y=200
        # 將圖片設置在中央
        # self.rect.center=(WIDTH/2,HEIGHT/2)
    
    def update(self):
        self.rect.x +=2
        if self.rect.left>WIDTH:
            self.rect.right=0

# 將遊戲中的物件加入至sprite群組當中
all_sprites=pygame.sprite.Group()
player=Player()
all_sprites.add(player )


running=True

# 遊戲迴圈
while running:
    # 此處代表一秒鐘最多只能執行幾次,也相當於帪數(一秒更新幾次畫面)
    clock.tick(FPS)
    
# 取得輸入，因為可能輸入同時會有多個，故需要用for迴圈全部讀出來
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            # print(type(event))
# 更新遊戲
    #取得sprite群組裡所有物件的update函式
    all_sprites.update()
# 畫面顯示
    # 將畫面填滿，三個參數分別為R、G、B，範圍都是0~255
    # screen.fill((R,G,B))
    screen.fill(WHITE)
    
    # 將sprite群組裡所有遊戲物件放置在螢幕上
    all_sprites.draw(screen)
# 更新畫面
    pygame.display.update()

# 關閉
pygame.quit()