from storage.fileStorage import FileStorage
from utils import common_letters

def run():
    path = './storage/input.txt'

    file_storage = FileStorage(path)

    box_collection, unregistered_boxes = file_storage.register_into_box_collection()
    cheksum = box_collection.checksum

    print('-'*6 + ' Part 1 ' + '-'*6)

    if unregistered_boxes:
        print('Warning somes boxes hasn\'t be imported')
        for unregistered_box in unregistered_boxes:
            print(f'Box id : {unregistered_box["box_id"]} Reason : {unregistered_box["error"]}')

    print(f'Total registered boxes : {len(box_collection)}')
    print(f'Cheksum : {cheksum}')

    print('-'*6 + ' Part 2 ' + '-'*6)
    near_boxes_list = box_collection.get_near_box_ids()
    for near_boxes in near_boxes_list:
        box_id_a = near_boxes[0].id
        box_id_b = near_boxes[1].id
        similiraties = common_letters(box_id_a, box_id_b)
        print(f'Box id a/b : {box_id_a} / {box_id_b} -> {similiraties}')

run()