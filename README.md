# sw_test0118

戦闘力測定器
相手の戦闘力を測定し、画像としてファイルに保存します。

操作方法・概要
SimpleCV,time,random,RPi.GPIO as GPIOをインポート。
カメラの設定（顔認識）、ディスプレイ、描画レイヤー、GPIOの設定を行う。
実行すると、カメラが顔認識を行っていないときはbash上に'No face'と表示され、
カメラが顔認識すると2番ピンがHIGHになり、LEDが発光。生成したランダム関数の値を取り込んだ画像にテキスト表示。
そのあとに取り込んだ画像を現在のディレクトリ以下に保存する。