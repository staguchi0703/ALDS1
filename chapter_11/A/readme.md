# 注意点まとめる

## BFS

### collections.deque
* que で使うときは、popleft()
* queのインスタンスを生成するとき
  * `que = collections.deque([obj])`とすることがみそ
  * iterableなオブジェクトを受け取らないといけないので、queのリストを与えるイメージ
  * `.deque(int)`だとNG
* queにappend()するとき
  * `.append(obj)`とする
  * queがiterableなオブジェクトなので、追加する要素を加える

* 例
  * 親子関係や深さの情報を配列で与える場合

``` python3

que = collections.deque([[0, [1,3], 0]]) #rootであるnode:0が、子の[1, 3]を有し、深さ0である。この要素リストをさらにリストに入れて、dequeメソッドに渡す。
temp_node = que.popleft() # queだからFIFOで取り出す

que.append([1, [2,4], 1]) #node:1の要素リストを渡す。queを生成した時とリストのネストが一個少ないのがポイント

```