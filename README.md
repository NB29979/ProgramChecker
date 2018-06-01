# ProgramChecker
C言語のソースファイルが要求されているものかを判定するスクリプト．
Windows上で動作．
gccおよびPython3が必要．

## 実行方法
 
 1. ProgramChecker/{QuestionName}に判定対象のソースファイルを置く
 2. ProgramChecker/{QuestionName}にプログラムに対する入力ファイルと理想的な出力ファイルを置く
 3. "python ProgramChecker {QuestionName}"で実行可能．
 
{QuestionName}はディレクトリの名前．

## 出力
Windowsのコマンドを利用することでgccなど外部プロセスを通して対象のソースファイルのコンパイル結果を表示する．

また，そのプログラムに対して入力ファイルを通した実行結果も出力ファイルと比較されるため，プログラムが正解の出力を行うものであるかを比較可能．
プログラム自体も画面上に出力される．

最後には，対象のディレクトリ内のソースファイルを一通り確認後，その得点をcsvとして出力する．
