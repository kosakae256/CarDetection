import tensorflow as tf
import copy
import cv2
import numpy as np

model_path = './model/saved_model'
DEFAULT_FUNCTION_KEY = 'serving_default'
loaded_model = tf.saved_model.load(model_path)
inference_func = loaded_model.signatures[DEFAULT_FUNCTION_KEY]

# 推論用関数(Function for inference)
def run_inference_single_image(image, inference_func):
    tensor = tf.convert_to_tensor(image)
    output = inference_func(tensor)

    output['num_detections'] = int(output['num_detections'][0])
    output['detection_classes'] = output['detection_classes'][0].numpy()
    output['detection_boxes'] = output['detection_boxes'][0].numpy()
    output['detection_scores'] = output['detection_scores'][0].numpy()
    return output

def detect_car(readpath,correct,failedpath,framepath,write_filename):
    image = cv2.imread(readpath)

    # 変換する画像
    debug_image = copy.deepcopy(image)

    # 画像の大きさとか必要な情報を取得
    image_width, image_height = image.shape[1], image.shape[0]
    image = image[:, :, [2, 1, 0]]  # BGR2RGB
    image_np_expanded = np.expand_dims(image, axis=0)

    #推論
    output = run_inference_single_image(image_np_expanded, inference_func)

    #推論結果をnum_detectionsに代入
    c = 0
    num_detections = output['num_detections']

    print(num_detections)
    for i in range(num_detections):
        score = output['detection_scores'][i]
        bbox = output['detection_boxes'][i]
        labelclass = output['detection_classes'][i]

        # この数値以上の信頼度なら通る
        if score < 0.7:
            continue
        
        #車なら
        if labelclass == 2:
            c+=1

        print(labelclass)
        x1, y1 = int(bbox[1] * image_width), int(bbox[0] * image_height)
        x2, y2 = int(bbox[3] * image_width), int(bbox[2] * image_height)

        # 推論結果描画(Inference result drawing)
        cv2.rectangle(debug_image, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.putText(debug_image, str('{:.2f}'.format(score)) + "car", (x1, y1-10), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.rectangle(debug_image, (x1, y1), (x2, y2), (0, 0, 255), 5)
        
    #再変換
    image = image[:, :, [2, 1, 0]]

    # 車が見つからなかった
    if c==0:
        cv2.imwrite(f"{failedpath}/{write_filename}.jpg",image)
        cv2.imwrite(f"{framepath}/{write_filename}.jpg",debug_image)
    
    # 車が見つかった
    else:
        cv2.imwrite(f"{correct}/{write_filename}.jpg",image)
        cv2.imwrite(f"{framepath}/{write_filename}.jpg",debug_image)
    

if "__main__" == __name__:
    readpath1 = "C:/Users/kosakae256/Documents/01Develop/CarDetection/1.detection_imgs/test1.jpg"
    readpath2 = "C:/Users/kosakae256/Documents/01Develop/CarDetection/1.detection_imgs/test2.jpg"
    # 判定後正解画像保存先
    correct = "C:/Users/kosakae256/Documents/01Develop/CarDetection/2.correct"
    # 判定後失敗画像保存先
    failedpath = "C:/Users/kosakae256/Documents/01Develop/CarDetection/3.failed"
    # 判定後、フレームつき画像保存先
    framepath = "C:/Users/kosakae256/Documents/01Develop/CarDetection/4.frame"
    # ファイル名
    write_filename = "test2"
    detect_car(readpath1,correct,failedpath,framepath,write_filename)
    detect_car(readpath2,correct,failedpath,framepath,write_filename)