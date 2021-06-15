## 使い方ぁ

cmdで作業ディレクトリに移動して

git clone https://github.com/kosakae256/CarDetection

cd ./CarDetection/

(必要であればvenv環境を作る)

pip install -m requirements.txt



1.detection_imgsに判定したい画像を入れる

python3 main.py

以上が実行手順です



車があったと判定された画像は2.correctに入ります

なかったと判定されると3.failedに入ります

4.frameはどの範囲が判定されたかがわかります
