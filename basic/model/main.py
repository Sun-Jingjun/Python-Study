from basic.model.class_utils import Encoder, Decoder
from basic.model.utils.utils import get_sum

print(get_sum(1,2))


decode = Decoder()
encode = Encoder()

print(decode.decode('abcd'))
print(encode.encode('abcd'))