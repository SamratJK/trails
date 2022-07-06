
# from pdfminer.high_level import extract_pages,extract_text_to_fp
# from pdfminer.layout import LTTextContainer, LTImage, LTFigure,LTTextLineHorizontal


# def get_text_and_image(path):
#   text = []
#   count = 0
#   text_image = dict()
#   text_image["image"] = []
#   for page_layout in extract_pages(path):
#     for element in page_layout:
#       each_case = []
#       b = []
#       if isinstance(element,LTTextContainer):
#         for eli in element:
#           if isinstance(eli,LTTextLineHorizontal):
#             each_case.append(eli.get_text().replace("\n","").replace(' ',''))

#       if isinstance(element, LTFigure):
#         for el in element:
#           if isinstance(el,LTImage):
#             imdata = el.stream.get_data()
#             if imdata.startswith(b'\xff\xd8\xff\xe0'):
#               b.append(el.name)

#       if each_case:
#         print(len(text))
#         if len(each_case) == 1 and count > 0:
#           text[count-2].extend(each_case)
#         else:
#           text.append(each_case)
#           count+=1
#       for i in range(0,len(b)-1):
#         b[i] = b[i] + ".jpg"
#       text_image["image"].extend(b)
#   text.pop(0)
#   text_image["text"]= text

#   with open("temp.csv","w") as file:


# if __name__ == "__main__":
#   get_text_and_image("missing_child.pdf")
    
# # text = extract_text('one.pdf')

# # print(output_string.getvalue())
import fitz
from PIL import Image, ImageTk

doc = fitz.open("missing_child.pdf")
# print(doc.metadata)
page = doc[0]
pix = page.get_text('Dict')
print(pix)
# pix.save("page-%i.png" % page.number)