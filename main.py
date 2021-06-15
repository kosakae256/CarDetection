from detect import detect_car
import glob

if __name__ == "__main__":
    # jpgファイルリスト
    readpath = "C:/Users/kosakae256/Documents/01Develop/CarDetection/1.detection_imgs"
    read_list = sorted(glob.glob(readpath + '/*.jpg'))
    # 判定後正解画像保存先
    correct = "C:/Users/kosakae256/Documents/01Develop/CarDetection/2.correct"
    # 判定後失敗画像保存先
    failedpath = "C:/Users/kosakae256/Documents/01Develop/CarDetection/3.failed"
    # 判定後、フレームつき画像保存先
    framepath = "C:/Users/kosakae256/Documents/01Develop/CarDetection/4.frame"

    n=1
    for filepath in read_list:
        detect_car(filepath,correct,failedpath,framepath,f"car.{n}")
        n+=1