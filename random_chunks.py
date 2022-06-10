# Write functuin that splits given list into random chunks of legnth from 4 to 7
# last chunk has to be from 4 to 7 lenght max
import random

alphabet = [x for x in 'abcdefghijklmnoprstuwxyz']


# for alphabet = [x for x in 'abcdefghijklmnoprstuwxyzzyxwutsrponmlkjihgfedcba123456789123'] and chunk lenght range(17, 23)
# def to_chunks(_list):
#     chunks = []
#     while len(_list) != 0:
#         chunk_lenght = random.randint(17, 23)
#         if len(_list) <= 43:
#             if 17 <= len(_list) - chunk_lenght <= 23:
#                 chunks.append(_list[:chunk_lenght])    
#                 del _list[:chunk_lenght]
#                 print(1, chunks)
#             if 17 <= len(_list) <= 23:
#                 chunks.append(_list)
#                 _list = []
#                 print(2, chunks)
#         else:
#             chunks.append(_list[:chunk_lenght])    
#             del _list[:chunk_lenght]
#             print(3, chunks)
#             print('lenght', len(_list))
#     return chunks


# for lenght range 6-9
# def to_chunks(_list):
#     chunks = []
#     while len(_list) != 0:
#         chunk_lenght = random.randint(6, 9)
#         if len(_list) <= 18:
#             if 6 <= len(_list) - chunk_lenght <= 9:
#                 chunks.append(_list[:chunk_lenght])
#                 del _list[:chunk_lenght]
#             if 6 <= len(_list) <= 9:
#                 chunks.append(_list)
#                 _list = []
#         else:
#             chunks.append(_list[:chunk_lenght])    
#             del _list[:chunk_lenght]
#     return chunks


# for lenght 8
# def to_chunks(_list):
#     chunks = []
#     while len(_list) != 0:
#         chunks.append(_list[:8])
#         _list = _list[8:]
#     return chunks


# for lenght range 4-7
# def to_chunks(_list):
#     chunks = []
#     while len(_list) != 0:
#         chunk_lenght = random.randint(4,7)
#         if len(_list) <= 11:
#             if 4 <= len(_list) - chunk_lenght <= 7:
#                 chunks.append(_list[:chunk_lenght])    
#                 del _list[:chunk_lenght]
#             if 4 <= len(_list) <= 7:
#                 chunks.append(_list)
#                 _list = []
#         else:
#             chunks.append(_list[:chunk_lenght])    
#             del _list[:chunk_lenght]
#     return chunks


chunks = to_chunks(alphabet)
print(chunks)
