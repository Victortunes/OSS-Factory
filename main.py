from storage.fileStorage import FileStorage
from box.boxCollection import BoxCollection

path = './storage/input.txt'

box_collection = BoxCollection()
file_storage = FileStorage(path)

box_collection, unregistered_boxes = file_storage.register_into_box_collection(box_collection)
cheksum = box_collection.checksum

if unregistered_boxes:
    print('Warning somes boxes hasn\'t be imported')
    for unregistered_box in unregistered_boxes:
        print(f'Box id : {unregistered_box["box_id"]} Reason : {unregistered_box["error"]}')

print(f'Total register boxes : {len(box_collection)}')
print(f'Cheksum : {cheksum}')
