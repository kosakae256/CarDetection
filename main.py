from detect import detect_car
import glob
import os

os.makedirs("./1.detection_imgs", exist_ok=True)
os.makedirs("./2.correct", exist_ok=True)
os.makedirs("./3.failed", exist_ok=True)
os.makedirs("./4.frame", exist_ok=True)

if __name__ == "__main__":
    # jpgファイルリスト
    readpath = "./1.detection_imgs"
    read_list = sorted(glob.glob(readpath + '/*.jpg'))
    # 判定後正解画像保存先
    correct = "./2.correct"
    # 判定後失敗画像保存先
    failedpath = "./3.failed"
    # 判定後、フレームつき画像保存先
    framepath = "./4.frame"

    n=1
    for filepath in read_list:
        detect_car(filepath,correct,failedpath,framepath,f"car.{n}")
        n+=1