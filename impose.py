# requires python 3 and PIL, do 'pip3 install image' in term
# copyright ry

import os, random, os.path, decimal
from PIL import Image

path = "data\\"
save_path = "saved\\"

while True:

    # randomise stuff
    print("let's randomise fam")
    alpha_random1 = decimal.Decimal(random.randrange(100))/100
    alpha_random2 = decimal.Decimal(random.randrange(100))/100

    random_file1 = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x)) and
        x.endswith(('.png','.jpg','.jpeg','.gif','.bmp'))
    ])

    random_file2 = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x)) and
        x.endswith(('.png','.jpg','.jpeg','.gif','.bmp'))
    ])

    # Overlay image script

    # Function to change the image size
    def alterImageSize(maxWidth,
                        maxHeight,
                        image):

        widthRatio  = maxWidth/image.size[0]
        heightRatio = maxHeight/image.size[1]

        newWidth    = int(widthRatio*image.size[0])
        newHeight   = int(heightRatio*image.size[1])

        newImage    = image.resize((newWidth, newHeight))
        return newImage

    # Choose 2 images to blend
    image1 = Image.open("D:\\mia\\machine\\data\\" + str(random_file1))
    image2 = Image.open("D:\\mia\\machine\\data\\" + str(random_file2))

    # Resize images
    image3 = alterImageSize(800, 500, image1)
    image4 = alterImageSize(800, 500, image2)

    # Alpha the images
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")

    # Display the original images
    #image5.show()
    #image6.show()

    # Randomly blend the images
    alphaBlended1 = Image.blend(image5, image6, alpha=alpha_random1)
    alphaBlended2 = Image.blend(image5, image6, alpha=alpha_random2)

    # Display the completed images
    alphaBlended1.show()
    alphaBlended2.show()

# Save the images (not working currently)
#alphaBlended1.save(save_path, 'png')
#alphaBlended2.save(save_path, 'png')

# Potential extra feature?
# Salt and Pepper noise

#def add_salt_and_pepper(image, amount):
#
#    output = np.copy(np.array(image))
#
#    # add salt
#    nb_salt = np.ceil(amount * output.size * 0.5)
#    coords = [np.random.randint(0, i - 1, int(nb_salt)) for i in output.shape]
#    output[coords] = 1
#
#    # add pepper
#    nb_pepper = np.ceil(amount* output.size * 0.5)
#    coords = [np.random.randint(0, i - 1, int(nb_pepper)) for i in output.shape]
#    output[coords] = 0
#
#    return Image.fromarray(output)
