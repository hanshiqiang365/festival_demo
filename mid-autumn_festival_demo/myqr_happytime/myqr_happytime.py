#author:hanshiqiang365

from MyQR import myqr
import os
words='http://weixin.qq.com/r/DkyxqYPE_96ErcfK9xkc'
version, level, qr_name = myqr.run(
    words,
    version=1,
    level='H',
    picture='happytime.gif',
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name='myqr_happytime.gif'
)