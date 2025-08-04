### 解題思路

**錯誤方法** <br>
一開始我打算我把shellcode 放在 path 上面，沒有注意到題目説的realpath 會把 shellcode 破壞掉。因此在我level00.py 正解上有被注解掉的代碼。

**正確方法**<br>
雖然很容易算到在shellcode 之前有156個bytes, 但是在做的過程中不知道爲什麽把 buf_addr 相成32 bytes，導致距離算錯。即使距離算好之後，爲了容錯性，還是給 shellcode 多加了 nop sled。