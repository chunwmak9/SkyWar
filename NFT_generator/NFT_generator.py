#NFT generations
from random import randint
from PIL import Image
import hashlib
import os
DIR = os.getcwd()+"/NFT_generator"
def NFT_generator():
    
    #1. File name combination generations
    def file_name_generator(components = 4): #The number of each components
        #bg + face + hat
        component_names = ["bg","face","hat","weapon"] 
        FORMAT = ".png"
        files = []
        for i in range(components):
            file_name = DIR+"/Images/"+component_names[i]+str(randint(1,components))+FORMAT
            files.append(file_name)
        return files
    items = file_name_generator()

    #2. Layers Generation (default:3 layers)
    new_image_height = 600
    new_image_length = 600
    layer1 = Image.open(items[0]).convert('RGBA').resize((new_image_height, new_image_length), Image.ANTIALIAS)
    layer2 = Image.open(items[1]).convert('RGBA').resize((new_image_height, new_image_length), Image.ANTIALIAS)
    layer3 = Image.open(items[2]).convert('RGBA').resize((new_image_height, new_image_length), Image.ANTIALIAS)
    layer4 = Image.open(items[3]).convert('RGBA').resize((new_image_height, new_image_length), Image.ANTIALIAS)
    def remove_background(image):
        data = image.getdata()
        
        newData = []
        for pix in data:
            if (pix[0] == 255 and pix[1] == 255 and pix[2] == 255) or (pix[0] == 0 and pix[1] == 0 and pix[2] == 0):
                #print(pix)
                newData.append((255,255,255,0))
            else:
                newData.append(pix)
        image.putdata(newData)
        return image
    layer1 =  remove_background(layer1)
    layer2 =  remove_background(layer2)
    layer3 =  remove_background(layer3)
    layer4 =  remove_background(layer4)


    #3. Combination of layers
    com1 = Image.alpha_composite(layer1,layer2) #Alpha layer2 over layer1
    com2 = Image.alpha_composite(com1,layer3)
    com3 = Image.alpha_composite(com2,layer4)

    rgb_im = com3.convert('RGB')
    file_name = "result.png"
    image_code = hashlib.sha256(str(items).encode()).hexdigest()
    print("The NFT code: {}".format(image_code))
    rgb_im.save(DIR+'/Images/'+file_name)
    return image_code


if __name__ == "__main__": 
    NFT_generator()

    
