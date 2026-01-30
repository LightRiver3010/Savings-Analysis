from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

buf = BytesIO()
# Pillow & BytesIO Testing

image = Image.open('data/test_image.png')
# image.show()

#Make a new Image

image2 = Image.new('RGB', (1000, 700), color='white')
# image2.show()

#Save an Image
# image.save('first_save.png')

width = 1000
height = 800

draw = ImageDraw.Draw(image2)

#Drawing Text
draw.text((900, 100), "Testing")

title_font = ImageFont.truetype('SourceSans3-Medium.ttf', size=80)
body_font = ImageFont.truetype('SourceSans3-Medium.ttf', size=30)

draw.text((100, 50), 'Testing again', font=title_font, fill='black')
draw.text((100, 150), 'This is a body font', font=body_font, fill='black')

# Save image using buf

image2.save(buf, format='PNG')
buf.seek(0)

data = buf.getvalue()

# with open("testing.png", "wb") as f:
#     f.write(buf.getvalue())


def testing_download(savings_amount, tip_list):
    img = Image.new('RGB', (1920, 1080), color='white')
    draw = ImageDraw.Draw(img)
    draw.text((100, 50), 'Savings Report', font=title_font, fill='black')
    draw.text((100, 175), f'By going through the Savings Simulator at saving-sim.streamlit.app and \ntaking action on with the following tips...', font=body_font, fill='black')
    
    for i, tip in enumerate(tip_list):
        y_pos = 275 + (i * 50)
        if y_pos > 650:
            draw.text((900, y_pos-(650-250)), f'- {tip}', fill='black', font=body_font)
        else:
            draw.text((100, y_pos), f'- {tip}', fill='black', font=body_font)

    draw.text((100, 700), f'...I realized I could save ${savings_amount} each month!', font=body_font, fill='black')
    
    img.save(buf, format='PNG')
    buf.seek(0)
    img_data = buf.getvalue()
    with open("SavingsReport.png", "wb") as f:
        f.write(img_data)
    print("Image Saved!")
    

tips = ['Do this this this htis this', 'no do this this this this thisthi sthis', 'by doing this you can save a ton of money when you shop and all that', 'by doing this you can save a ton of money when you shop and all that', 'by doing this you can save a ton of money when you shop and all that', 'by doing this you can save a ton of money when you shop and all that', 'by doing this you can save a ton of money when you shop and all that', 'by doing this you can save a ton of money when you shop and all that', 'by doing this you can save a ton of money when you shop and all that', 'by doing this you can save a ton of money when you shop and all that', 'by doing this you can save a ton of money when you shop and all that', 'by doing this you can save a ton of money when you shop and all that', 'by doing this you can save a ton of money when you shop and all that', 'by doing this you can save a ton of money when you shop and all that', 'by doing this you can save a ton of money when you shop and all that', 'by doing this you can save a ton of money when you shop and all that', 'by doing this you can save a ton of money when you shop and all that', 'by doing this you can save a ton of money when you shop and all that', 'by doing this you can save a ton of money when you shop and all that', 'by doing this you can save a ton of money when you shop and all that']
    
testing_download(533, tips)