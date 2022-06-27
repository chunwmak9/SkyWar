import pygame

class item_list:
    def __init__(self,window,sw,sh):
        self.window = window
        self.x = 40
        self.y = 20
        self.s_x = 100 #200
        self.s_y = 100 #200
        self.gap = 150 #200
        self.pos = [[self.x,self.y,self.s_x,self.s_y],[self.x+self.gap,self.y,self.s_x,self.s_y],[self.x+self.gap*2,self.y,self.s_x,self.s_y],[self.x+self.gap*3,self.y,self.s_x,self.s_y],[self.x+self.gap*4,self.y,self.s_x,self.s_y],[self.x+self.gap*5,self.y,self.s_x,self.s_y],[self.x+self.gap*6,self.y,self.s_x,self.s_y]]#,[self.x+self.gap*7,self.y,self.s_x,self.s_y],[self.x+self.gap*8,self.y,self.s_x,self.s_y],[self.x+self.gap*9,self.y,self.s_x,self.s_y]]
        self.color = (255,255,255)
        self.sw,self.sh = sw,sh
        #self.count = 0 #Represent objects number in item list
        self.image = []
        self.tokens = [] #The NFT retrieved
        self.tokens_storage = [] #The NFT retrieved storage backup
        self.move_y = self.sh 
        
    def show(self):
        obj = pygame.Surface(self.window.get_size(), pygame.SRCALPHA)
        for pos in self.pos:
            pygame.draw.rect(obj,self.color,pygame.Rect(pos[0],pos[1],pos[2],pos[3]))
        pygame.draw.rect(obj, (0,0,0), pygame.Rect(20, 10,self.gap*len(self.pos), self.s_y*1.4),4)
        return obj
    
    def __positions(self):
        return self.pos
    def __size(self):
        return (self.s_x,self.s_y)
    def Append(self,image):
        if len(self.image)<= len(self.pos)-1:
            from NFT_generator import NFT_generator
            NFT_code = NFT_generator.NFT_generator()
            if NFT_code not in self.tokens_storage:
                self.image.append(image)
                self.tokens.append(NFT_code)
                self.tokens_storage.append(NFT_code)    
        
    #Function: Update item into item list   
    def update(self):   
        if len(self.image)>0:
            surf = pygame.Surface(self.window.get_size(), pygame.SRCALPHA)
            for i in range(len(self.image)):
                image = pygame.transform.scale(self.image[i],(self.__size()[0],self.__size()[1]))
                surf.blit(image, (self.__positions()[i][0], self.__positions()[i][1]))
            return surf
    def text_movement(self):
        if self.move_y < self.sh /4:
            self.move_y = self.sh
            del self.tokens[0]
        if len(self.tokens)>0:
            font = pygame.font.SysFont(None, 32)
            text_surface = font.render(f"You got an NFT with code #{len(self.tokens_storage)}: {self.tokens[-1]}.",False,(0,255,0))
            
            return text_surface


        
