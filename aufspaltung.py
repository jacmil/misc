from PIL import Image


# vertical chop
def vertical_chop(list):

    images = list
    v_chopped_images = []


    for current_image in images:
        height = current_image.height
        width = current_image.width
        v_chops = []

        num_v_chops = int(height/100) * 2

        for chop in range(num_v_chops):
            new_im = current_image.copy()
            upper = (height / num_v_chops) * chop
            lower = (height / num_v_chops) * (chop + 1)
            v_crop = new_im.crop((0, upper, width, lower))
            v_chops.append(v_crop)

        # new images
        v_image1 = Image.new('RGB', (width, int(height/2)), 'white')
        v_image2 = Image.new('RGB', (width, int(height/2)), 'white')
        v_images = [v_image1, v_image2]

        i = 0
        for v_image in v_images:
            paste_location = (0, 0)
            for j in range(i, num_v_chops, 2):
                v_image.paste(v_chops[j], paste_location)
                paste_location = (0, paste_location[1] + int(height/num_v_chops))
            v_chopped_images.append(v_image)
            i += 1

    return v_chopped_images


def horizontal_chop(list):

    images = list
    h_chopped_images = []

    for current_image in images:
        height = current_image.height
        width = current_image.width
        h_chops = []
        num_h_chops = int(width/100) * 2


        for chop in range(num_h_chops):
            new_im = current_image.copy()
            left = (width / num_h_chops) * chop
            right = (width / num_h_chops) * (chop + 1)
            h_crop = new_im.crop((left, 0, right, height))
            h_chops.append(h_crop)

        # new images
        h_image1 = Image.new('RGB', (int(width / 2), height), 'white')
        h_image2 = Image.new('RGB', (int(width / 2), height), 'white')
        h_images = [h_image1, h_image2]

        i = 0
        for h_image in h_images:
            paste_location = (0, 0)
            for j in range(i, num_h_chops, 2):
                h_image.paste(h_chops[j], paste_location)
                paste_location = (paste_location[0] + int(width / num_h_chops), 0)
            h_chopped_images.append(h_image)
            i += 1

    return h_chopped_images




image = [Image.open('  Your File  ')]

if image[0].height > image[0].width:
    first = horizontal_chop(image)
    second = vertical_chop(first)
else:
    first = vertical_chop(image)
    second = horizontal_chop(first)

for i in range(len(second)):
    second[i].show()










