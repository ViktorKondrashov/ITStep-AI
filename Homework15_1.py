# file = f.readlines()
# # f1 = open("block.txt", "wt", encoding='utf-8')
#
# count_empty = 2
# flag_write = False
# docs = []
# previos_block = 1
# for line in file:
#
#     if count_empty > 1:
#         count_empty = 0
#         if file.index(line) != 0:
#
#             if previos_block != 1:
#
#                 f1.close()
#                 f1 = open("block" + str(previos_block) + ".txt", "rt", encoding='utf-8')
#                 text = f1.read()
#
#                 doc = Document(
#                     page_content=text,  # вміст документа
#                     metadata={'name': f1.name,
#                               'name_block': text.splitlines()[0]
#                               }
#                 )
#                 docs.append(doc)
#
#         f1 = open("block"+ str(file.index(line) + 1) + ".txt", "wt", encoding='utf-8')
#         previos_block = file.index(line) + 1
#         flag_write = True
#
#     if flag_write:
#         f1.write(line)
#
#     if line.strip() == "":
#         count_empty += 1
#         if count_empty > 1:
#             flag_write = False
#             continue
#     else:
#         count_empty = 0
#
# f.close()
# f1.close()
